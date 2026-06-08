# Operations

## Scheduled Workflows

The repository uses GitHub Actions for routine updates:

- `Microsoft Repo Change Digest`: daily digest and report generation.
- `MS Repo Inventory Reconciliation`: weekly full inventory reconciliation or manual inventory refresh.
- `Microsoft Repo Events Calibration`: weekly Events API candidate calibration.
- `Validate Tracker`: no-network artifact and unit validation on push, pull request, and manual dispatch.

## Local Validation

Run:

```bash
python -m py_compile github_api.py msft_docs_inventory.py msft_changes_last24h.py msft_events_calibration.py scripts/validate_tracker.py
python scripts/validate_tracker.py
python -m unittest discover -s tests
```

## Deferrals

API-heavy work should defer instead of exhausting GitHub API limits. A deferred digest writes `reports/status.json` when possible and preserves the last successful report artifacts.

Common reasons:

- `rest_budget_too_low`
- `graphql_budget_too_low`
- `github_rate_limit`

## Interpreting Freshness

`reports/status.json` is authoritative for freshness. The current policy marks the latest report stale when it is older than the expected schedule window.

## Manual Digest

Example:

```bash
python msft_changes_last24h.py --input msft_repo_inventory.csv --hours 24 --max-commits 5 --state msft_repo_tracker_state.json --use-state-window --watchlist watchlist.yml --reports-dir reports
```

Use a `GITHUB_TOKEN` for reliable local runs.
