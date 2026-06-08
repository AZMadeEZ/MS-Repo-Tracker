# Data Contract

The generated data is treated as a versioned artifact set.

## Discovery

Consumers should start with `reports/manifest.json`. It lists current artifacts, paths, schemas, and whether each artifact is required.

## Freshness

Consumers should read `reports/status.json` before trusting report recency. The important fields are:

- `status`
- `reason`
- `last_attempt_at`
- `last_success_at`
- `latest_report_generated_at`
- `latest_report_stale`
- `freshness`

## Schemas

Schemas live under `schemas/` and use schema version `1`.

Current schemas include:

- `schemas/inventory.v1.schema.json`
- `schemas/watchfeeds.v1.schema.json`
- `schemas/digest-csv.v1.schema.json`
- `schemas/report.v1.schema.json`
- `schemas/report-index.v1.schema.json`
- `schemas/manifest.v1.schema.json`
- `schemas/status.v1.schema.json`
- `schemas/event.v1.schema.json`
- `schemas/events-calibration.v1.schema.json`
- `schemas/state.v1.schema.json`

## Event Stream

`reports/latest.events.ndjson` is the preferred machine-ingestion artifact for individual changes. Each line is a JSON object. Use `dedupe_key` to deduplicate across overlapping windows.

The event stream is generated from `reports/latest.json` activity commit records and validated offline by `scripts/validate_tracker.py`.

## Backward Compatibility

`changes_last24h.csv` keeps `commit_count_24h` as a deprecated compatibility alias. New consumers should use:

- `commit_count_window`
- `window_since`
- `window_until`
- `hours_requested`
- `state_window_enabled`

See `DATA_DICTIONARY.md` for field-level details.
