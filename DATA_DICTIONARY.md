# MS Repo Tracker Data Dictionary

This document describes the committed artifacts used for human review and downstream ingestion.

## Artifact Contracts

All machine-readable JSON report artifacts include:

| Field | Meaning |
| --- | --- |
| `schema_version` | Integer schema generation for backward-compatible parsing. Current value is `1`. |
| `artifact_type` | Stable artifact identifier such as `tracker-report`, `tracker-report-index`, `tracker-status`, or `tracker-manifest`. |
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
| `releases` | Release scan summary and recent release items. |
| `lifecycle` | Latest inventory lifecycle summary when it overlaps the digest window. |
| `graphql` | GraphQL enrichment strategy and batch telemetry. |
| `events_prefilter` | Optional Events API candidate telemetry. |
| `events_calibration` | Optional Events-vs-`pushed_at` calibration snapshot. |

## Inventory And State

`msft_repo_inventory.csv` is the durable repository baseline. It intentionally includes `other` repositories so the tracker can preserve Microsoft ecosystem coverage even when reports default to focused categories.

`msft_repo_inventory_watchfeeds.csv` exposes commit and release Atom feed URLs for each inventory repo.

`msft_repo_tracker_state.json` stores per-org scan metadata, conditional request cache data, digest continuity metadata, and lifecycle summaries. It is committed so GitHub Actions and local runs share the same baseline.
