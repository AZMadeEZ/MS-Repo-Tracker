# MS-Repo-Tracker

A lightweight Python toolkit for tracking activity across Microsoft GitHub repositories.

This repo includes two scripts:

- `msft_docs_inventory.py` - builds an inventory of public repos across one or more orgs, classifies them as docs/reference/training/samples/other, and generates watch-feed URLs.
- `msft_changes_last24h.py` - summarizes recent default-branch commits for repos in the inventory and outputs both CSV and Markdown digests.
- `msft_events_calibration.py` - compares GitHub Events API candidates with inventory `pushed_at` candidates without spending GraphQL enrichment budget.

## What gets generated

Running the scripts creates these output files:

- `msft_repo_inventory.csv` - categorized inventory of repositories.
- `msft_repo_inventory_watchfeeds.csv` - Atom feed URLs for commit/release monitoring.
- `msft_repo_tracker_state.json` - durable scan state, rate-budget metadata, and conditional request cache metadata.
- `changes_last24h.csv` - machine-friendly snapshot of recent repo activity.
- `changes_last24h.md` - human-readable activity digest.
- `reports/latest.md` and `reports/latest.json` - current daily brief for human review and downstream ingestion.
- `reports/YYYY-MM-DD.md` and `reports/YYYY-MM-DD.json` - dated report history.
- `reports/index.md` and `reports/index.json` - rolling report index with 7/30-day trend totals.
- `reports/manifest.json` - artifact catalog for downstream ingestion.
- `reports/status.json` - latest digest attempt status and report freshness metadata.
- `reports/events-calibration/latest.md` and `.json` - Events API calibration report.
- `schemas/*.schema.json` - lightweight data contracts for generated machine-readable artifacts.
- `DATA_DICTIONARY.md` - field-level notes for report, manifest, status, inventory, and CSV outputs.

## Requirements

- Python 3.9+
- `requests` Python package (see `requirements.txt`)
- Recommended for local runs and expected for scheduled runs: `GITHUB_TOKEN` for higher GitHub API rate limits.

Install dependencies:

```bash
pip install -r requirements.txt
```

Set your token:

```bash
export GITHUB_TOKEN="<your_token>"
```

For GitHub Actions, create a repository secret named `MS_REPO_TRACKER_GITHUB_TOKEN` when you want a higher API budget than the built-in workflow token. The workflows fall back to `github.token` when that secret is not present.

## Configuration

`orgs.txt` controls which GitHub orgs are scanned by `msft_docs_inventory.py`.

- One org per line
- Empty lines and `#` comments are ignored

Example:

```txt
MicrosoftDocs
MicrosoftLearning
Azure-Samples
```

`watchlist.yml` controls which repos, orgs, keywords, and products are elevated in the daily signal report. Watchlist matches do not add GitHub API calls; they only affect report scoring and grouping.

## Usage

### 1. Build Inventory

Full reconciliation:

```bash
python msft_docs_inventory.py --mode full --state msft_repo_tracker_state.json
```

Daily incremental refresh:

```bash
python msft_docs_inventory.py --mode incremental --overlap-hours 48 --state msft_repo_tracker_state.json
```

This reads `orgs.txt` and writes:

- `msft_repo_inventory.csv`
- `msft_repo_inventory_watchfeeds.csv`
- `msft_repo_tracker_state.json`

Inventory modes:

- `full`: complete reconciliation across all public repos in configured orgs.
- `incremental`: scan org repo pages sorted by recent pushes and stop once the overlap window is passed.

The durable inventory baseline keeps all public repos, including `other`; digest commands filter categories by default.

### 2. Build Recent Changes Digest

```bash
python msft_changes_last24h.py --input msft_repo_inventory.csv --hours 24 --max-commits 5
```

Common options:

- `--input` (required): inventory CSV path
- `--hours` (default `24`): lookback window
- `--max-commits` (default `5`): max commit headlines per repo
- `--include-archived`: include archived repos
- `--include-forks`: include forked repos
- `--categories docs,reference,...`: filter inventory categories
- `--categories all`: include every category in the inventory
- `--include-other`: include `other` repositories alongside the default docs/reference/training/samples set
- `--state msft_repo_tracker_state.json --use-state-window`: extend the lookback to the last successful digest timestamp, with overlap
- `--digest-overlap-hours` (default `2`): overlap before the last successful digest timestamp when using state
- `--max-lookback-hours` (default `168`): cap for state-extended digest windows
- `--events-prefilter-mode off|union|intersect`: optionally use GitHub organization Events API pages as a candidate hint
- `--events-calibration`: include Events-vs-`pushed_at` comparison metadata in the report
- `--enrichment-mode one-stage|two-stage`: choose GraphQL enrichment strategy; `two-stage` is the default
- `--graphql-batch-size 0`: use adaptive GraphQL batch sizing; pass a positive number to force a batch size
- `--release-mode off|candidates|watched|candidates-and-watched`: control release detection scope
- `--max-release-repos` (default `150`): cap release endpoint checks
- `--watchlist watchlist.yml`: load signal-scoring watchlist configuration
- `--reports-dir reports`: write the current and dated daily brief artifacts
- `--no-reports`: skip report artifact generation

Outputs:

- `changes_last24h.csv`
- `changes_last24h.md`
- `reports/latest.md`
- `reports/latest.json`
- `reports/YYYY-MM-DD.md`
- `reports/YYYY-MM-DD.json`
- `reports/index.md`
- `reports/index.json`
- `reports/manifest.json`
- `reports/status.json`

`changes_last24h.csv` keeps the legacy `commit_count_24h` column for compatibility. New ingestion should use `commit_count_window` with `window_since`, `window_until`, `hours_requested`, and `state_window_enabled` so state-extended runs are interpreted correctly.

Events prefilter modes:

- `off`: default. Use inventory `pushed_at` as the digest prefilter.
- `union`: include repos found by either inventory `pushed_at` or the organization Events API.
- `intersect`: only enrich repos found by both inventory `pushed_at` and Events API when Events API returns candidates. If Events API returns no candidates, the script keeps the `pushed_at` candidates to avoid an accidental blank run.

GitHub's Events API is optimized for polling with conditional requests and exposes `X-Poll-Interval`, but organization event feeds can have latency. Keep `off` for the safest scheduled default; use `union` or `intersect` when tuning collection efficiency.

Signal reporting:

- High-signal items are scored from human-authored commits, watchlist hits, release activity, security language, and category.
- Bot-only dependency churn is tagged separately so it can be scanned or filtered without hiding it.
- Recent releases are fetched through capped, conditional REST calls and recorded under `releases` in the JSON report.
- Repository lifecycle changes are recorded during inventory refresh and surfaced in the next digest report.
- `reports/status.json` is updated on successful runs and clean API-budget deferrals so reviewers can distinguish a stale report from a failed collection.

### 3. Calibrate Events API Candidate Coverage

```bash
python msft_events_calibration.py --input msft_repo_inventory.csv --state msft_repo_tracker_state.json --orgs orgs.txt
```

This writes:

- `reports/events-calibration/latest.md`
- `reports/events-calibration/latest.json`
- dated calibration history files

Use this report to decide whether `--events-prefilter-mode intersect` is safe enough to enable for a particular workflow. If the potential miss count is high, keep the default `off`.

## Typical Workflow

1. Update `orgs.txt` when the tracked organizations change.
2. Refresh inventory incrementally each day through `msft-docs-changes-last24h.yml`.
3. Run full inventory reconciliation weekly through `ms-docs-inventory.yml` or manually with `workflow_dispatch`.
4. Generate the changes digest daily through `msft-docs-changes-last24h.yml`.
5. Run weekly Events calibration through `msft-events-calibration.yml`.
6. Review `reports/latest.md` for the daily brief, `reports/index.md` for trends, `changes_last24h.md` for the raw grouped digest, and CSV/JSON outputs for automation/reporting.

## Validation

Run the no-network validation checks locally:

```bash
python scripts/validate_tracker.py
python -m unittest discover -s tests
```

GitHub Actions also runs these checks through `validate.yml` on push, pull request, and manual dispatch.

## Notes

- Inventory classification uses org + keyword heuristics and intentionally avoids expensive per-repo deep scans.
- Changes are measured on each repository's default branch.
- `pushed_at` from the inventory is used as a prefilter to reduce API calls.
- GraphQL enrichment defaults to a two-stage flow that counts changed repos first, then fetches commit/PR details only for repos with movement.
- Release detection is capped and conditional so it improves reporting without taking over the REST budget.
- Inventory refreshes defer cleanly when GitHub API budget is too low instead of exhausting the rate limit.
- The daily digest workflow uses the tracker state to avoid fixed 24-hour gaps after missed or failed runs.
- Data contracts live under `schemas/`, with field guidance in `DATA_DICTIONARY.md`.
