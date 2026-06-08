# MS Repo Tracker Data Dictionary

This document describes the committed artifacts used for human review and downstream ingestion.

## Artifact Contracts

All machine-readable JSON report artifacts include:

| Field | Meaning |
| --- | --- |
| `schema_version` | Integer schema generation for backward-compatible parsing. Current value is `1`. |
| `artifact_type` | Stable artifact identifier such as `tracker-report`, `tracker-summary`, `tracker-report-index`, `tracker-status`, or `tracker-manifest`. |
| `artifact_version` | Producer contract version. Current value is `1.0.0`. |
| `schema_url` | Repository-relative path to the artifact schema under `schemas/`. |
| `generated_at` | UTC timestamp when the artifact was generated. |
| `source` | Best-effort GitHub repository, commit, workflow, run ID, and run URL metadata. Local runs may leave workflow fields blank. |

## Manifest And Status

`reports/manifest.json` is the artifact catalog for ingestion systems.

| Field | Meaning |
| --- | --- |
| `status` | Summary of the most recent digest attempt and the latest successful report freshness. |
| `freshness` | Fresh/stale/unknown state using the configured freshness threshold. |
| `artifacts` | List of generated artifact names, types, paths, optional schemas, and whether each path is required. |

`reports/status.json` records the last digest attempt.

| Field | Meaning |
| --- | --- |
| `status` | `complete`, `deferred`, or `failed`. Current script writes `complete` after a successful digest and `deferred` when API budget is too low. |
| `reason` | Short machine-friendly reason such as `success`, `rest_budget_too_low`, `graphql_budget_too_low`, or `github_rate_limit`. |
| `last_attempt_at` | UTC time of the latest attempted digest run. |
| `last_success_at` | UTC time of the latest successful report known to the tracker. |
| `latest_report_generated_at` | `generated_at` from `reports/latest.json`, when available. |
| `latest_report_stale` | Boolean freshness flag. The current threshold is 30 hours. |

## Digest CSV

`changes_last24h.csv` is the row-level digest export. The filename is retained for compatibility, but rows now carry explicit window fields.

| Field | Meaning |
| --- | --- |
| `full_name` | Repository name in `owner/repo` form. |
| `org` | GitHub organization owner from the inventory. |
| `name` | Repository short name. |
| `category` | Local classification: `docs`, `reference`, `training`, `samples`, or `other`. |
| `repo_type` | Explainable taxonomy type such as `docs`, `reference`, `training`, `samples`, `sdk`, `tool`, `service`, `infra`, or `other`. |
| `product_area` | Best-effort product area such as `Azure`, `.NET`, `Microsoft Graph`, `PowerShell`, or `Unknown`. |
| `audience` | Best-effort intended audience such as `developer`, `admin`, `architect`, `learner`, `operator`, or `unknown`. |
| `default_branch` | Branch used for commit movement checks. |
| `commit_count_window` | Canonical commit count for the actual report window. |
| `commit_count_24h` | Deprecated compatibility alias for `commit_count_window`. Do not use for new ingestion. |
| `window_since` | Inclusive UTC lower bound used for commit movement checks. |
| `window_until` | UTC upper bound for the digest run. |
| `hours_requested` | CLI `--hours` value requested for the run before state-window extension. |
| `state_window_enabled` | Whether `--use-state-window` was enabled. |
| `newest_commit_date` | Most recent default-branch commit timestamp returned for the repo. |
| `signal_score` | Local report score for human triage priority. |
| `signal_tags` | Semicolon-separated signal tags. |
| `release_count` | Number of recent releases attached to the repo in this digest. |
| `commitN_*` | Commit detail columns for up to `--max-commits` commits. |

## Report JSON

`reports/latest.json` and `reports/YYYY-MM-DD.json` are structured daily briefs.

| Field | Meaning |
| --- | --- |
| `window.since` | UTC lower bound used for movement checks. |
| `window.until` | UTC upper bound for the digest run. |
| `window.hours_requested` | CLI `--hours` value. |
| `window.state_window_enabled` | Whether the state-aware catch-up window was enabled. |
| `filters` | Category, archived, fork, and Events API prefilter settings. |
| `totals` | Inventory, candidate, movement, commit, and release counts. |
| `summaries` | Rollups by category, org, and signal grouping. |
| `top_repos` | Highest-scoring movement items for the daily brief. |
| `activities` | Row-level repository movement details. |
| `event_stream` | Paths and counts for the flat NDJSON event stream generated from already-collected commit and release data. |
| `notable_changes` | Top event-level changes selected from the event stream by notability score while filtering high-noise events. |
| `product_area_summary` | Human-oriented product-area rollup with event, release, security, repo, noisy-event, and top-link counts. Unknown product areas are grouped as `Unmapped Activity`. |
| `top_links` | Compact prioritized links to the most important changes in the brief. Intended for quick reading, dashboards, and notification summaries. |
| `noise_summary` | Automation/noise rollup covering medium/high-noise events, bot or automation actors, bulk automation, and dependency maintenance clusters. |
| `releases` | Release scan summary and recent release items. |
| `lifecycle` | Latest inventory lifecycle summary when it overlaps the digest window. |
| `graphql` | GraphQL enrichment strategy and batch telemetry. |
| `events_prefilter` | Optional Events API candidate telemetry. |
| `events_calibration` | Optional Events-vs-`pushed_at` calibration snapshot. |

## Compact Summary JSON

`reports/latest.summary.json` and `reports/YYYY-MM-DD.summary.json` are compact broker summaries for dashboards, notifications, and AI prompt context. They intentionally avoid the full nested activity list.

| Field | Meaning |
| --- | --- |
| `freshness` | Fresh/stale/unknown state for the latest successful report at generation time. |
| `window` | Effective report window copied from the full report. |
| `filters` | Category, archived, fork, and Events API prefilter settings copied from the full report. |
| `totals` | Inventory, candidate, movement, commit, and release counts copied from the full report. |
| `event_stream` | Latest event-stream paths and commit/release event counts. |
| `plain_english_summary` | Short human-readable bullet list used by the Markdown brief. |
| `top_links` | Diverse prioritized links for quick triage. |
| `product_area_summary` | Product-area event, repo, release, security, and top-link rollup. |
| `noise_summary` | Automation/noise rollup. |
| `artifact_links` | Stable pointers to latest and dated Markdown, JSON, summary, and event stream artifacts. |

## Report Index

`reports/index.md` is the human landing page for daily briefs. `reports/index.json` is the machine-readable index for dashboards and recurring trend views.

| Field | Meaning |
| --- | --- |
| `latest` | Pointer block for the current brief, including latest Markdown, JSON, event stream paths, headline counts, and latest product-area summary. |
| `daily` | Dated report history with per-day movement, commit, release, and high-signal counts. |
| `trends.last_7_days` | Seven-report rollup. When fewer than seven reports exist, this covers all available reports. |
| `trends.last_30_days` | Thirty-report rollup. When fewer than thirty reports exist, this covers all available reports. |
| `top_repositories` | Repositories recurring most often across available report history. |
| `top_products` | Product areas recurring most often across available report history, including watchlist product matches and report product-area summaries. |

## Inventory And State

`msft_repo_inventory.csv` is the durable repository baseline. It intentionally includes `other` repositories so the tracker can preserve Microsoft ecosystem coverage even when reports default to focused categories.

Inventory taxonomy fields:

| Field | Meaning |
| --- | --- |
| `repo_type` | Config-driven repository type used for explainable grouping. |
| `product_area` | Config-driven product area. |
| `audience` | Config-driven intended audience. |
| `classification_confidence` | 0-1 heuristic confidence score. |
| `classification_reason` | Semicolon-separated reasons such as org, keyword, category, or override matches. |
| `classification_version` | Version string for the classification rules used. |

`msft_repo_inventory_watchfeeds.csv` exposes commit and release Atom feed URLs for each inventory repo.

`msft_repo_tracker_state.json` stores per-org scan metadata, conditional request cache data, digest continuity metadata, and lifecycle summaries. It is committed so GitHub Actions and local runs share the same baseline.

## Event Stream

`reports/latest.events.ndjson` and `reports/YYYY-MM-DD.events.ndjson` are line-delimited JSON files for AI, search, and BI ingestion. Each line is one commit or release event generated from already-collected report data. Repeated state-window runs can overlap; consumers should deduplicate with `dedupe_key`.

| Field | Meaning |
| --- | --- |
| `event_id` | Stable event ID in provider/type/repo/object form. |
| `event_type` | `commit` or `release`. |
| `dedupe_key` | Stable key for overlap-safe deduplication. Commit events use `commit:<oid>`; release events use `release:<repo>:<tag-or-url>`. |
| `repo`, `org`, `repo_name` | Repository identifiers. |
| `category` | Local inventory category. |
| `repo_type`, `product_area`, `audience` | Inventory taxonomy fields copied onto the event when available. |
| `default_branch` | Branch used for movement checks. |
| `committed_at` | Commit timestamp from GitHub GraphQL, or release publish timestamp for release events. |
| `headline` | Commit headline. |
| `author` | Commit author display string. |
| `actor_type` | `human`, `bot`, `automation`, or `unknown`. |
| `commit_oid`, `commit_url` | Commit identity and source URL. For release events, these carry the release tag/identity and release URL for backward-compatible consumers. |
| `published_at`, `release_tag`, `release_name`, `release_url`, `prerelease`, `draft` | Release-specific fields present on `event_type=release` records. |
| `pr_number`, `pr_title`, `pr_url` | Associated pull request metadata when GraphQL returns it. |
| `change_type` | First-pass change classification such as `docs_update`, `dependency_update`, `security_fix`, `bulk_automation`, `ci_infra`, or `feature`. |
| `noise_level` | `low`, `medium`, `high`, or `unknown`, intended to keep bot/bulk activity visible without over-ranking it. |
| `customer_visible` | `true`, `false`, or `unknown`; conservative until deeper enrichment is added. |
| `notability_score` | 0-100 first-pass event score derived from repo signal, actor type, change type, and noise level. |
| `notability_reason` | Machine-friendly explanation tags for the score. |
| `labels` | Current signal tags from the repo activity. |
| `window_since`, `window_until` | Effective report window for the event. |
| `retrieved_at` | Report generation timestamp. |
| `source` | Provider/API and source URL metadata. |
