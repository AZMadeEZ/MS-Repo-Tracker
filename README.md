# MS-Repo-Tracker

A lightweight Python toolkit for tracking activity across Microsoft GitHub repositories.

This repo includes two scripts:

- `msft_docs_inventory.py` - builds an inventory of public repos across one or more orgs, classifies them as docs/reference/training/samples/other, and generates watch-feed URLs.
- `msft_changes_last24h.py` - summarizes recent default-branch commits for repos in the inventory and outputs both CSV and Markdown digests.

## What gets generated

Running the scripts creates these output files:

- `msft_repo_inventory.csv` - categorized inventory of repositories.
- `msft_repo_inventory_watchfeeds.csv` - Atom feed URLs for commit/release monitoring.
- `msft_repo_tracker_state.json` - durable scan state, rate-budget metadata, and conditional request cache metadata.
- `changes_last24h.csv` - machine-friendly snapshot of recent repo activity.
- `changes_last24h.md` - human-readable activity digest.

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

Outputs:

- `changes_last24h.csv`
- `changes_last24h.md`

## Typical Workflow

1. Update `orgs.txt` when the tracked organizations change.
2. Refresh inventory incrementally each day through `msft-docs-changes-last24h.yml`.
3. Run full inventory reconciliation weekly through `ms-docs-inventory.yml` or manually with `workflow_dispatch`.
4. Generate the changes digest daily through `msft-docs-changes-last24h.yml`.
5. Review `changes_last24h.md` for a quick daily summary and use CSV outputs for automation/reporting.

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
- Inventory refreshes defer cleanly when GitHub API budget is too low instead of exhausting the rate limit.
- The daily digest workflow uses the tracker state to avoid fixed 24-hour gaps after missed or failed runs.
