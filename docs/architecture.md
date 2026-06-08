# Architecture

MS-Repo-Tracker has three main layers: inventory, digest, and published artifacts.

## Inventory Layer

`msft_docs_inventory.py` reads `orgs.txt`, lists public repositories from configured organizations, classifies each repository, and writes:

- `msft_repo_inventory.csv`
- `msft_repo_inventory_watchfeeds.csv`
- `msft_repo_tracker_state.json`

The inventory can run in full or incremental mode. Incremental mode reads repositories sorted by recent pushes and stops after the overlap window. Full mode is the reconciliation safety net.

## Digest Layer

`msft_changes_last24h.py` reads the inventory, filters repositories by category/archive/fork settings, prefilters candidates by inventory `pushed_at`, and enriches recent default-branch movement with GitHub GraphQL.

The digest also performs capped release checks and local signal scoring. It writes raw CSV/Markdown outputs and structured report artifacts under `reports/`.

## Artifact Layer

Generated artifacts are committed so GitHub Actions, local runs, humans, and downstream systems share the same baseline.

Primary artifacts:

- `reports/manifest.json`: discovery entry point.
- `reports/status.json`: latest attempt and freshness state.
- `reports/latest.events.ndjson`: flat event stream.
- `reports/latest.json`: structured report.
- `reports/latest.md`: human daily brief.

## API Efficiency

The tracker reduces API calls by:

- using incremental inventory refreshes
- using conditional REST requests where supported
- deferring cleanly on low API budget
- prefiltering digest candidates by `pushed_at`
- using two-stage GraphQL enrichment
- capping release endpoint checks
- generating signal/event/report improvements locally without more API calls
