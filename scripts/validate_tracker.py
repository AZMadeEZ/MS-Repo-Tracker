#!/usr/bin/env python3
"""Validate committed tracker artifacts without making network calls."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any, Dict, List


REQUIRED_INVENTORY_COLUMNS = {
    "org",
    "name",
    "full_name",
    "html_url",
    "archived",
    "fork",
    "pushed_at",
    "default_branch",
    "category",
    "score",
    "repo_type",
    "product_area",
    "audience",
    "classification_confidence",
    "classification_reason",
    "classification_version",
}

REQUIRED_WATCHFEED_COLUMNS = {
    "full_name",
    "category",
    "default_branch",
    "commits_atom",
    "releases_atom",
}

REQUIRED_DIGEST_COLUMNS = {
    "full_name",
    "org",
    "name",
    "category",
    "repo_type",
    "product_area",
    "audience",
    "default_branch",
    "commit_count_24h",
    "commit_count_window",
    "window_since",
    "window_until",
    "hours_requested",
    "state_window_enabled",
    "newest_commit_date",
}

VALID_STATUS_VALUES = {"complete", "deferred", "failed"}
VALID_EVENT_TYPES = {"commit", "release"}
VALID_ACTOR_TYPES = {"human", "bot", "automation", "unknown"}
VALID_NOISE_LEVELS = {"low", "medium", "high", "unknown"}
VALID_CUSTOMER_VISIBLE = {"true", "false", "unknown"}
REQUIRED_EVENT_FIELDS = {
    "schema_version",
    "artifact_type",
    "artifact_version",
    "schema_url",
    "event_id",
    "event_type",
    "dedupe_key",
    "repo",
    "org",
    "repo_name",
    "category",
    "repo_type",
    "product_area",
    "audience",
    "default_branch",
    "committed_at",
    "headline",
    "actor_type",
    "commit_oid",
    "commit_url",
    "change_type",
    "noise_level",
    "customer_visible",
    "notability_score",
    "window_since",
    "window_until",
    "retrieved_at",
    "source",
}


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    if not path.exists():
        raise RuntimeError(f"Missing required file: {path}")
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        return list(reader.fieldnames or []), rows


def validate_columns(path: Path, actual: List[str], required: set[str]) -> None:
    missing = sorted(required - set(actual))
    if missing:
        raise RuntimeError(f"{path} is missing required column(s): {', '.join(missing)}")


def validate_inventory(path: Path) -> list[dict[str, str]]:
    fields, rows = read_csv(path)
    validate_columns(path, fields, REQUIRED_INVENTORY_COLUMNS)
    if not rows:
        raise RuntimeError("Inventory is empty.")

    full_names = [row.get("full_name", "").strip() for row in rows]
    if any(not value or "/" not in value for value in full_names):
        raise RuntimeError("Inventory contains invalid full_name values.")
    if len(full_names) != len(set(full_names)):
        raise RuntimeError("Inventory contains duplicate full_name values.")

    categories = {row.get("category", "").strip() for row in rows}
    if "other" not in categories:
        raise RuntimeError("Inventory baseline should include other-category repositories.")

    for row in rows:
        full_name = row.get("full_name", "").strip()
        for field in ("repo_type", "product_area", "audience", "classification_version"):
            if not row.get(field, "").strip():
                raise RuntimeError(f"Inventory row {full_name} is missing {field}.")
        confidence = float(row.get("classification_confidence") or 0)
        if confidence < 0 or confidence > 1:
            raise RuntimeError(f"Inventory row {full_name} has invalid classification_confidence.")
        if not row.get("classification_reason", "").strip():
            raise RuntimeError(f"Inventory row {full_name} is missing classification_reason.")

    return rows


def validate_watchfeeds(path: Path, inventory_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    fields, rows = read_csv(path)
    validate_columns(path, fields, REQUIRED_WATCHFEED_COLUMNS)
    if not rows:
        raise RuntimeError("Watchfeed inventory is empty.")

    inventory_names = {row.get("full_name", "").strip() for row in inventory_rows}
    watchfeed_names = [row.get("full_name", "").strip() for row in rows]
    unknown = sorted(set(watchfeed_names) - inventory_names)
    if unknown:
        sample = ", ".join(unknown[:5])
        raise RuntimeError(f"Watchfeed contains repos missing from inventory: {sample}")

    for row in rows:
        full_name = row.get("full_name", "").strip()
        commits_atom = row.get("commits_atom", "").strip()
        releases_atom = row.get("releases_atom", "").strip()
        if full_name and not commits_atom.startswith(f"https://github.com/{full_name}/commits/"):
            raise RuntimeError(f"Invalid commits_atom for {full_name}")
        if full_name and releases_atom != f"https://github.com/{full_name}/releases.atom":
            raise RuntimeError(f"Invalid releases_atom for {full_name}")

    return rows


def validate_state(path: Path, inventory_rows: list[dict[str, str]]) -> Dict[str, Any]:
    if not path.exists():
        raise RuntimeError(f"Missing required file: {path}")
    with path.open("r", encoding="utf-8-sig") as f:
        state = json.load(f)

    if state.get("schema_version") != 1:
        raise RuntimeError("Unexpected state schema_version.")
    org_state = state.get("orgs")
    if not isinstance(org_state, dict) or not org_state:
        raise RuntimeError("State is missing per-org scan metadata.")

    inventory_orgs = {row.get("org", "").strip() for row in inventory_rows if row.get("org", "").strip()}
    missing_orgs = sorted(inventory_orgs - set(org_state))
    if missing_orgs:
        sample = ", ".join(missing_orgs[:5])
        raise RuntimeError(f"State is missing org metadata for: {sample}")

    last_run = state.get("last_run") or {}
    repos_written = last_run.get("repos_written")
    if repos_written is not None and int(repos_written) != len(inventory_rows):
        raise RuntimeError(
            f"State last_run.repos_written={repos_written} does not match inventory rows={len(inventory_rows)}."
        )

    return state


def validate_digest(csv_path: Path, md_path: Path) -> list[dict[str, str]]:
    fields, rows = read_csv(csv_path)
    validate_columns(csv_path, fields, REQUIRED_DIGEST_COLUMNS)

    if not md_path.exists():
        raise RuntimeError(f"Missing required file: {md_path}")
    md_text = md_path.read_text(encoding="utf-8")
    if not md_text.startswith("# Changes on default branch since "):
        raise RuntimeError(f"{md_path} does not look like a tracker digest.")

    for row in rows:
        full_name = row.get("full_name", "").strip()
        if full_name and "/" not in full_name:
            raise RuntimeError(f"Digest contains invalid full_name value: {full_name}")
        count = row.get("commit_count_24h", "").strip()
        if count:
            int(count)
        window_count = row.get("commit_count_window", "").strip()
        if window_count:
            int(window_count)
        if count and window_count and int(count) != int(window_count):
            raise RuntimeError("Digest commit_count_24h and commit_count_window differ.")
        if not row.get("window_since", "").strip():
            raise RuntimeError("Digest row is missing window_since.")
        if not row.get("window_until", "").strip():
            raise RuntimeError("Digest row is missing window_until.")
        int(row.get("hours_requested", "0") or 0)
        if row.get("state_window_enabled", "").strip() not in {"True", "False", "true", "false"}:
            raise RuntimeError("Digest row has invalid state_window_enabled value.")

    return rows


def validate_artifact_identity(payload: Dict[str, Any], expected_type: str) -> None:
    if payload.get("schema_version") != 1:
        raise RuntimeError(f"Unexpected {expected_type} schema_version.")
    if payload.get("artifact_type") != expected_type:
        raise RuntimeError(f"Unexpected artifact_type for {expected_type}.")
    if not payload.get("artifact_version"):
        raise RuntimeError(f"{expected_type} is missing artifact_version.")
    schema_url = str(payload.get("schema_url") or "")
    if schema_url and not Path(schema_url).exists():
        raise RuntimeError(f"{expected_type} schema_url does not exist: {schema_url}")


def validate_reports(report_dir: Path, digest_rows: list[dict[str, str]]) -> Dict[str, Any]:
    latest_json = report_dir / "latest.json"
    latest_md = report_dir / "latest.md"
    if not latest_json.exists():
        raise RuntimeError(f"Missing required report file: {latest_json}")
    if not latest_md.exists():
        raise RuntimeError(f"Missing required report file: {latest_md}")

    with latest_json.open("r", encoding="utf-8") as f:
        payload = json.load(f)

    validate_artifact_identity(payload, "tracker-report")
    if not payload.get("generated_at"):
        raise RuntimeError("Report is missing generated_at.")
    for key in ("summaries", "top_repos", "activities", "graphql", "releases"):
        if key not in payload:
            raise RuntimeError(f"Report is missing required key: {key}")
    event_stream = payload.get("event_stream")
    if not isinstance(event_stream, dict):
        raise RuntimeError("Report is missing event_stream metadata.")
    window = payload.get("window") or {}
    for key in ("since", "until", "hours_requested", "state_window_enabled"):
        if key not in window:
            raise RuntimeError(f"Report window is missing required key: {key}")

    totals = payload.get("totals") or {}
    repos_with_movement = int(totals.get("repos_with_movement") or 0)
    if repos_with_movement != len(digest_rows):
        raise RuntimeError(
            "Report totals.repos_with_movement does not match digest CSV rows."
        )

    activities = payload.get("activities")
    if not isinstance(activities, list) or len(activities) != len(digest_rows):
        raise RuntimeError("Report activities do not match digest CSV rows.")
    for activity in activities:
        if not isinstance(activity, dict):
            raise RuntimeError("Report activity entries must be objects.")
        if "signal" not in activity:
            raise RuntimeError("Report activity is missing signal metadata.")
        if "releases" not in activity:
            raise RuntimeError("Report activity is missing release metadata.")

    generated_date = str(payload.get("generated_at"))[:10]
    dated_json = report_dir / f"{generated_date}.json"
    dated_md = report_dir / f"{generated_date}.md"
    if generated_date and (not dated_json.exists() or not dated_md.exists()):
        raise RuntimeError("Report history is missing the generated-date files.")

    md_text = latest_md.read_text(encoding="utf-8")
    if not md_text.startswith("# Microsoft Repo Change Brief - "):
        raise RuntimeError(f"{latest_md} does not look like a tracker report.")

    index_json = report_dir / "index.json"
    index_md = report_dir / "index.md"
    if not index_json.exists() or not index_md.exists():
        raise RuntimeError("Report index files are missing.")
    with index_json.open("r", encoding="utf-8") as f:
        index_payload = json.load(f)
    validate_artifact_identity(index_payload, "tracker-report-index")
    if not isinstance(index_payload.get("daily"), list):
        raise RuntimeError("Report index is missing daily report entries.")

    return payload


def read_ndjson(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        raise RuntimeError(f"Missing required event stream file: {path}")
    records: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as f:
        for line_number, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                raise RuntimeError(f"{path}:{line_number} is not valid JSON: {exc}") from exc
            if not isinstance(record, dict):
                raise RuntimeError(f"{path}:{line_number} must be a JSON object.")
            records.append(record)
    return records


def expected_commit_event_count(report_payload: Dict[str, Any]) -> int:
    count = 0
    for activity in report_payload.get("activities") or []:
        if isinstance(activity, dict):
            commits = activity.get("commits") or []
            if isinstance(commits, list):
                count += len(commits)
    return count


def validate_event_record(path: Path, record: dict[str, Any]) -> None:
    missing = sorted(REQUIRED_EVENT_FIELDS - set(record))
    if missing:
        raise RuntimeError(f"{path} event is missing required field(s): {', '.join(missing)}")
    if record.get("schema_version") != 1:
        raise RuntimeError(f"{path} event has unexpected schema_version.")
    if record.get("artifact_type") != "tracker-event":
        raise RuntimeError(f"{path} event has unexpected artifact_type.")
    if record.get("schema_url") != "schemas/event.v1.schema.json":
        raise RuntimeError(f"{path} event has unexpected schema_url.")
    if record.get("event_type") not in VALID_EVENT_TYPES:
        raise RuntimeError(f"{path} event has unexpected event_type.")
    if record.get("actor_type") not in VALID_ACTOR_TYPES:
        raise RuntimeError(f"{path} event has unexpected actor_type.")
    if record.get("noise_level") not in VALID_NOISE_LEVELS:
        raise RuntimeError(f"{path} event has unexpected noise_level.")
    if record.get("customer_visible") not in VALID_CUSTOMER_VISIBLE:
        raise RuntimeError(f"{path} event has unexpected customer_visible value.")
    for key in ("event_id", "dedupe_key", "repo", "commit_oid", "commit_url", "window_since", "window_until"):
        if not str(record.get(key) or "").strip():
            raise RuntimeError(f"{path} event has empty {key}.")
    score = int(record.get("notability_score"))
    if score < 0 or score > 100:
        raise RuntimeError(f"{path} event notability_score is out of range.")
    if not isinstance(record.get("source"), dict):
        raise RuntimeError(f"{path} event source must be an object.")


def validate_event_stream(report_dir: Path, report_payload: Dict[str, Any]) -> list[dict[str, Any]]:
    latest_path = report_dir / "latest.events.ndjson"
    generated_date = str(report_payload.get("generated_at") or "")[:10]
    dated_path = report_dir / f"{generated_date}.events.ndjson"
    latest_records = read_ndjson(latest_path)
    dated_records = read_ndjson(dated_path)
    if latest_path.read_text(encoding="utf-8") != dated_path.read_text(encoding="utf-8"):
        raise RuntimeError("Latest and dated event streams differ.")

    expected_count = expected_commit_event_count(report_payload)
    if len(latest_records) != expected_count:
        raise RuntimeError(
            f"Event stream has {len(latest_records)} events, expected {expected_count} commit events."
        )

    event_stream = report_payload.get("event_stream") or {}
    if int(event_stream.get("commit_event_count") or -1) != expected_count:
        raise RuntimeError("Report event_stream.commit_event_count does not match activities.")
    if int(event_stream.get("event_count") or -1) != len(latest_records):
        raise RuntimeError("Report event_stream.event_count does not match latest event stream.")

    event_ids = set()
    dedupe_keys = set()
    for record in latest_records:
        validate_event_record(latest_path, record)
        event_id = str(record.get("event_id") or "")
        dedupe_key = str(record.get("dedupe_key") or "")
        if event_id in event_ids:
            raise RuntimeError(f"Duplicate event_id in event stream: {event_id}")
        if dedupe_key in dedupe_keys:
            raise RuntimeError(f"Duplicate dedupe_key in event stream: {dedupe_key}")
        event_ids.add(event_id)
        dedupe_keys.add(dedupe_key)

    return latest_records


def resolve_manifest_path(path_value: str) -> Path:
    path = Path(path_value)
    return path if path.is_absolute() else Path.cwd() / path


def validate_manifest_status(report_dir: Path) -> None:
    manifest_path = report_dir / "manifest.json"
    status_path = report_dir / "status.json"
    if not manifest_path.exists():
        raise RuntimeError(f"Missing required report file: {manifest_path}")
    if not status_path.exists():
        raise RuntimeError(f"Missing required report file: {status_path}")

    with status_path.open("r", encoding="utf-8") as f:
        status = json.load(f)
    validate_artifact_identity(status, "tracker-status")
    if status.get("status") not in VALID_STATUS_VALUES:
        raise RuntimeError("Tracker status has an unexpected status value.")
    if not status.get("last_attempt_at"):
        raise RuntimeError("Tracker status is missing last_attempt_at.")
    freshness = status.get("freshness")
    if not isinstance(freshness, dict) or "latest_report_stale" not in freshness:
        raise RuntimeError("Tracker status is missing freshness metadata.")

    with manifest_path.open("r", encoding="utf-8") as f:
        manifest = json.load(f)
    validate_artifact_identity(manifest, "tracker-manifest")
    artifacts = manifest.get("artifacts")
    if not isinstance(artifacts, list) or not artifacts:
        raise RuntimeError("Tracker manifest is missing artifacts.")
    artifact_names = {str(item.get("name") or "") for item in artifacts if isinstance(item, dict)}
    for required_name in {"latest_machine_report", "latest_human_report", "latest_event_stream", "tracker_status"}:
        if required_name not in artifact_names:
            raise RuntimeError(f"Tracker manifest is missing artifact: {required_name}")

    for item in artifacts:
        if not isinstance(item, dict):
            raise RuntimeError("Tracker manifest artifact entries must be objects.")
        path_value = str(item.get("path") or "")
        if not path_value:
            raise RuntimeError("Tracker manifest artifact is missing path.")
        if item.get("required", True) and not resolve_manifest_path(path_value).exists():
            raise RuntimeError(f"Tracker manifest references missing artifact: {path_value}")
        schema_url = str(item.get("schema_url") or "")
        if schema_url and not Path(schema_url).exists():
            raise RuntimeError(f"Tracker manifest references missing schema: {schema_url}")


def validate_events_calibration(report_dir: Path) -> None:
    latest_json = report_dir / "latest.json"
    latest_md = report_dir / "latest.md"
    if not latest_json.exists() and not latest_md.exists():
        return
    if not latest_json.exists() or not latest_md.exists():
        raise RuntimeError("Events calibration latest files are incomplete.")
    with latest_json.open("r", encoding="utf-8") as f:
        payload = json.load(f)
    if payload.get("schema_version") != 1:
        raise RuntimeError("Unexpected Events calibration schema_version.")
    calibration = payload.get("calibration")
    if not isinstance(calibration, dict) or not calibration.get("enabled"):
        raise RuntimeError("Events calibration payload is missing calibration data.")
    md_text = latest_md.read_text(encoding="utf-8")
    if not md_text.startswith("# Events API Calibration - "):
        raise RuntimeError(f"{latest_md} does not look like an Events calibration report.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inventory", default="msft_repo_inventory.csv")
    parser.add_argument("--watchfeeds", default="msft_repo_inventory_watchfeeds.csv")
    parser.add_argument("--state", default="msft_repo_tracker_state.json")
    parser.add_argument("--digest-csv", default="changes_last24h.csv")
    parser.add_argument("--digest-md", default="changes_last24h.md")
    parser.add_argument("--reports-dir", default="reports")
    parser.add_argument("--skip-reports", action="store_true")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    inventory_rows = validate_inventory(Path(args.inventory))
    watchfeed_rows = validate_watchfeeds(Path(args.watchfeeds), inventory_rows)
    validate_state(Path(args.state), inventory_rows)
    digest_rows = validate_digest(Path(args.digest_csv), Path(args.digest_md))
    if not args.skip_reports:
        reports_dir = Path(args.reports_dir)
        report_payload = validate_reports(reports_dir, digest_rows)
        validate_event_stream(reports_dir, report_payload)
        validate_manifest_status(reports_dir)
        validate_events_calibration(reports_dir / "events-calibration")

    print(
        f"Validated {len(inventory_rows)} inventory rows and "
        f"{len(watchfeed_rows)} watchfeed rows. "
        f"Digest rows: {len(digest_rows)}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
