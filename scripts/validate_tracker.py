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
    "default_branch",
    "commit_count_24h",
    "newest_commit_date",
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

    return rows


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inventory", default="msft_repo_inventory.csv")
    parser.add_argument("--watchfeeds", default="msft_repo_inventory_watchfeeds.csv")
    parser.add_argument("--state", default="msft_repo_tracker_state.json")
    parser.add_argument("--digest-csv", default="changes_last24h.csv")
    parser.add_argument("--digest-md", default="changes_last24h.md")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    inventory_rows = validate_inventory(Path(args.inventory))
    watchfeed_rows = validate_watchfeeds(Path(args.watchfeeds), inventory_rows)
    validate_state(Path(args.state), inventory_rows)
    digest_rows = validate_digest(Path(args.digest_csv), Path(args.digest_md))

    print(
        f"Validated {len(inventory_rows)} inventory rows and "
        f"{len(watchfeed_rows)} watchfeed rows. "
        f"Digest rows: {len(digest_rows)}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
