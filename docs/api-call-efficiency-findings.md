# API Call Efficiency Findings

Date: 2026-06-08

This note captures the current rate-limit findings for MS-Repo-Tracker and records the starting point for remediation planning.

Implementation status: the first remediation pass has been implemented with `github_api.py`, `msft_repo_tracker_state.json`, `msft_docs_inventory.py --mode incremental|full`, digest `--include-other` / `--categories all`, state-aware digest windows, seeded all-repo inventory, report artifacts under `reports/`, optional Events API candidate modes, and updated GitHub Actions workflows.

## Current Hot Spots

1. Daily full inventory refresh is the largest avoidable REST cost.
   - `msft_docs_inventory.py` walks every page for every org in `orgs.txt`.
   - With the current org list, a full scan is about 171 REST requests before retries or future org growth.
   - `.github/workflows/ms-docs-inventory.yml` schedules this full scan daily.

2. Inventory REST calls do not use conditional requests.
   - `gh_get()` always performs a normal `GET`.
   - It does not store `ETag` or `Last-Modified` headers.
   - It does not send `If-None-Match` or `If-Modified-Since` on later runs.
   - GitHub documents that authenticated conditional `GET` requests returning `304 Not Modified` do not count against the primary REST rate limit.

3. The digest prefilter is useful but depends on inventory freshness.
   - `msft_changes_last24h.py` filters repositories using `pushed_at` before making GraphQL calls.
   - In the current inventory, only 63 of 6,788 repositories were candidates for a 24-hour digest.
   - If inventory is stale, missing `pushed_at`, or a longer window is requested, GraphQL usage can rise quickly.

4. The digest GraphQL query fetches rich commit and PR metadata in one pass.
   - Each candidate repo query includes commit history and associated pull request metadata.
   - This is convenient for output quality, but GraphQL cost and node count grow with candidate count and `--max-commits`.
   - The digest now has an optional Events API prefilter mode that can be tested manually. It is not the scheduled default because organization events can be delayed.

5. Scheduled workflows use `GITHUB_TOKEN`.
   - GitHub Actions `GITHUB_TOKEN` has a smaller per-repository automation budget than a normal authenticated user/PAT budget.
   - The project should assume authenticated API access for reliable scheduled runs.

## Request-Cost Snapshot

Current org list estimated minimum pages for a full inventory run:

| Org | Public repos | Minimum pages |
| --- | ---: | ---: |
| microsoft | 8,016 | 81 |
| Azure-Samples | 3,292 | 33 |
| Azure | 2,713 | 28 |
| MicrosoftDocs | 810 | 9 |
| OfficeDev | 451 | 5 |
| MicrosoftLearning | 372 | 4 |
| dotnet | 278 | 3 |
| microsoftgraph | 235 | 3 |
| aspnet | 112 | 2 |
| PowerShell | 105 | 2 |
| SharePoint | 29 | 1 |

Total: about 171 REST requests for a complete page walk.

Current committed inventory:

| Category | Repos |
| --- | ---: |
| samples | 4,688 |
| docs | 1,435 |
| training | 647 |
| reference | 18 |

Total: 6,788 tracked repositories.

## Remediation Direction

The first remediation target should be the daily full inventory refresh.

Recommended direction:

1. Keep a complete inventory so the tracker does not intentionally ignore any known Microsoft ecosystem repository.
2. Add a cheaper incremental inventory mode for daily runs.
3. Use a periodic full reconciliation as a safety net.
4. Store per-org/page request cache metadata so unchanged pages can use GitHub conditional requests.
5. Keep the digest step based on `pushed_at` prefiltering, but make the inventory refresh more reliable and less expensive.

## Tracking All Repositories

Yes, the tracker can keep coverage across all known repositories without querying every repository individually on every run.

The likely design is stateful org-level polling:

1. Keep `msft_repo_inventory.csv` as the full known repository set.
2. On daily runs, list each org's repositories sorted by `pushed` descending.
3. Stop reading pages for an org once the page is older than the last successful scan minus a safety overlap window.
4. Merge any seen repositories into the inventory and pass changed repositories to the digest step.
5. Run a full reconciliation on a slower cadence to catch renames, archived/deleted repos, metadata-only changes, and any edge cases the incremental scan does not surface.

This is not the same as a perfect webhook guarantee. A strict "never miss anything ever" guarantee would require either a full reconciliation every run or webhook coverage across the relevant Microsoft organizations and repositories. For public Microsoft ecosystem tracking, the practical target is a bounded-delay, low-miss design: daily incremental scans for normal pushes plus scheduled full reconciliation as the safety net.

## Planning Decisions

1. Completeness contract: optimize for bounded no-miss tracking of normal pushed updates.
   - Daily incremental scans should catch normal repository pushes promptly.
   - Use a 48-hour overlap window so late workflow runs, clock drift, or interrupted runs do not create a gap.
   - Keep a weekly full reconciliation as the safety net for renames, deleted repositories, archived state changes, metadata-only changes, and other ecosystem drift.

2. Durable scan state: store the shared tracker baseline in a committed JSON state file.
   - Use a file such as `msft_repo_tracker_state.json`.
   - Include a schema version, per-org `last_successful_scan_at`, per-org `last_seen_pushed_at`, and request cache metadata.
   - Keep the file in the repository so GitHub Actions, local runs, and future debugging all use the same tracking baseline.

3. Shared API helper: centralize GitHub API behavior in a small shared module.
   - Add a module such as `github_api.py`.
   - Use it from both inventory and digest scripts.
   - Put authentication headers, API version headers, rate-limit logging, retry/backoff, and REST conditional-request support in one place.

4. Durable baseline scope: track all public repositories from configured orgs.
   - Do not limit the durable inventory baseline to docs/reference/training/samples.
   - Keep category classification as metadata on each repository.
   - Keep category filters for digest and report output.
   - This preserves full Microsoft ecosystem coverage while still allowing focused docs/samples/training views.

5. `other` category handling: retain `other` repositories in the durable baseline but exclude them from the default digest.
   - Daily incremental runs should update all seen repositories, including `other`.
   - Default digest output should keep the current focused category behavior.
   - Add an explicit option such as `--include-other` or `--categories all` when a user wants ecosystem-wide digest output.

6. Full reconciliation cadence: run weekly by default, with manual dispatch support.
   - Weekly full reconciliation should catch repo renames, deletions, archived state changes, classification drift, and incremental-scan edge cases.
   - Full reconciliation must use conditional REST requests where possible.
   - Full reconciliation should check remaining GitHub rate budget before and during execution.
   - If the available budget is too low, the job should stop cleanly, preserve existing inventory/state, and report that reconciliation was deferred instead of exhausting the limit.

7. Low-budget behavior: defer non-urgent API work instead of failing the whole workflow.
   - Daily digest should still run from the last good inventory/state when possible.
   - Full reconciliation should exit cleanly with a clear deferred status when rate budget is too low.
   - The workflow summary should explain that reconciliation was deferred because of low GitHub API budget.

8. Initial rate-budget threshold: use estimated request count plus a buffer.
   - Before full reconciliation, estimate the REST requests needed from current org public repo counts or known page counts.
   - Require estimated REST requests plus a 25% buffer before starting.
   - With the current org list estimate of about 171 REST requests, require about 215 REST requests available before starting.
   - Require at least 100 remaining GraphQL points before digest enrichment.
   - Log actual usage so these thresholds can be tuned after real workflow runs.

9. User-facing command shape: extend the existing scripts rather than replacing them.
   - Add inventory options such as `--mode incremental|full`, `--overlap-hours 48`, `--state msft_repo_tracker_state.json`, and `--include-other-baseline`.
   - Keep `msft_changes_last24h.py` focused on digest generation.
   - Add digest widening through an option such as `--include-other` or `--categories all`.
   - Preserve the current default digest behavior for docs/reference/training/samples.

10. Digest continuity: use tracker state to avoid fixed-window gaps after missed runs.
   - Daily digest runs can pass `--state msft_repo_tracker_state.json --use-state-window`.
   - The digest window extends back to the last successful digest timestamp minus a small overlap.
   - A maximum lookback cap protects GraphQL budget after long outages.

11. GitHub Actions hardening: keep working local paths represented in automation.
   - Daily workflow runs incremental inventory refresh plus digest.
   - Weekly workflow runs full reconciliation.
   - Validation workflow runs no-network compile, CLI, artifact, and unit-test checks on push, pull request, and manual dispatch.
   - Writer workflows share one concurrency group and rebase before pushing generated commits.

12. Human-ingestion reporting: publish concise daily brief artifacts alongside raw outputs.
   - `reports/latest.md` is the easiest daily read for a human reviewer.
   - `reports/latest.json` exposes the same metrics and activity list for downstream ingestion.
   - Dated `reports/YYYY-MM-DD.*` files preserve a lightweight report history in the repository.
   - The daily digest workflow stages `reports/` so successful scheduled runs keep these artifacts current.

13. Events API candidate prefilter: keep it optional and budget-aware.
   - `--events-prefilter-mode off` is the safest default and uses inventory `pushed_at`.
   - `--events-prefilter-mode union` adds repos seen in organization events to the enrichment candidate list.
   - `--events-prefilter-mode intersect` reduces GraphQL enrichment to repos seen by both `pushed_at` and organization events when event candidates are available.
   - The script checks REST budget before optional Events API work and uses conditional request cache metadata for event pages.
   - This mode should be tuned through manual workflow dispatch before becoming a scheduled default.

## Open Planning Question

The key design decision is how strong the completeness guarantee needs to be:

- "Near-real-time incremental" can check recently changed pages cheaply and rely on a scheduled full reconciliation.
- "Strict full reconciliation every run" can be made cheaper with conditional requests, but still touches every org page each run.
- "Webhook-first" could reduce polling but requires control over every relevant org/repo webhook, which is unlikely across the public Microsoft ecosystem.

## References

- GitHub REST "List organization repositories" supports `sort=created`, `sort=updated`, `sort=pushed`, and `sort=full_name`: https://docs.github.com/en/rest/repos/repos#list-organization-repositories
- GitHub REST conditional requests can use `ETag` / `Last-Modified`; authenticated `304 Not Modified` responses do not count against primary REST rate limits: https://docs.github.com/en/rest/using-the-rest-api/best-practices-for-using-the-rest-api#use-conditional-requests-if-appropriate
- GitHub REST rate limits differ by authentication method, and `GITHUB_TOKEN` in Actions has its own per-repository limit: https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api
- GitHub GraphQL has separate point, node, timeout, and secondary-limit constraints: https://docs.github.com/en/graphql/overview/rate-limits-and-query-limits-for-the-graphql-api
- GitHub REST Events endpoints are poll-oriented, support conditional requests, and expose `X-Poll-Interval`; organization events can be delayed: https://docs.github.com/en/rest/activity/events
