# MS-Repo-Tracker

A lightweight Python toolkit for tracking activity across Microsoft GitHub repositories.

This repo includes two scripts:

- `msft_docs_inventory.py` — builds an inventory of public repos across one or more orgs, classifies them (docs/reference/training/samples), and generates watch-feed URLs.
- `msft_changes_last24h.py` — summarizes recent default-branch commits for repos in the inventory and outputs both CSV and Markdown digests.

## What gets generated

Running the scripts creates these output files:

- `msft_repo_inventory.csv` — categorized inventory of repositories.
- `msft_repo_inventory_watchfeeds.csv` — Atom feed URLs for commit/release monitoring.
- `changes_last24h.csv` — machine-friendly snapshot of recent repo activity.
- `changes_last24h.md` — human-readable activity digest.

## Requirements

- Python 3.9+
- `requests` Python package (see `requirements.txt`)
- Optional but recommended: `GITHUB_TOKEN` for higher GitHub API rate limits

Install dependencies:

```bash
pip install -r requirements.txt
```

Set your token (recommended):

```bash
export GITHUB_TOKEN="<your_token>"
```

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

### 1) Build inventory

```bash
python msft_docs_inventory.py
```

This reads `orgs.txt` and writes:

- `msft_repo_inventory.csv`
- `msft_repo_inventory_watchfeeds.csv`

### 2) Build recent changes digest

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

Outputs:

- `changes_last24h.csv`
- `changes_last24h.md`

## Typical workflow

1. Update `orgs.txt`.
2. Run inventory script.
3. Run changes script.
4. Review `changes_last24h.md` for a quick daily summary.
5. Use CSV outputs for automation/reporting.

## Notes

- Inventory classification uses org + keyword heuristics and intentionally avoids expensive per-repo deep scans.
- Changes are measured on each repository's default branch.
- `pushed_at` from the inventory is used as a prefilter to reduce API calls.
