#!/usr/bin/env python3
"""Compare GitHub Events API candidates with inventory pushed_at candidates."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
from typing import Any, Dict, List

from github_api import DEFERRED_EXIT_CODE, GitHubClient, RateLimitDeferred, iso_utc
from msft_changes_last24h import (
    RepoInput,
    build_events_calibration,
    category_filter,
    compute_since_dt,
    fetch_event_candidates,
    load_state,
    parse_iso,
    read_inventory,
    read_orgs,
    save_state,
)


def filter_repos(
    repos: List[RepoInput],
    categories: str,
    include_other: bool,
    include_archived: bool,
    include_forks: bool,
) -> List[RepoInput]:
    selected_categories = category_filter(categories, include_other)
    filtered: List[RepoInput] = []
    for repo in repos:
        if selected_categories is not None and repo.category.strip() not in selected_categories:
            continue
        if not include_archived and repo.archived is True:
            continue
        if not include_forks and repo.fork is True:
            continue
        filtered.append(repo)
    return filtered


def pushed_candidates(repos: List[RepoInput], since_dt: dt.datetime) -> List[RepoInput]:
    if any(repo.pushed_at for repo in repos):
        selected = []
        for repo in repos:
            pushed_at = parse_iso(repo.pushed_at)
            if pushed_at is None or pushed_at >= since_dt:
                selected.append(repo)
        return selected
    return repos


def write_calibration_reports(report_dir: str, payload: Dict[str, Any]) -> List[str]:
    os.makedirs(report_dir, exist_ok=True)
    date_slug = str(payload.get("generated_at") or "latest")[:10]
    paths = [
        os.path.join(report_dir, "latest.json"),
        os.path.join(report_dir, f"{date_slug}.json"),
        os.path.join(report_dir, "latest.md"),
        os.path.join(report_dir, f"{date_slug}.md"),
    ]

    for path in paths[:2]:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2, sort_keys=True)
            f.write("\n")

    for path in paths[2:]:
        calibration = payload.get("calibration") or {}
        samples = calibration.get("samples") or {}
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"# Events API Calibration - {date_slug}\n\n")
            f.write(f"Generated: `{payload.get('generated_at', '')}`\n\n")
            f.write(f"Window since: `{payload.get('since', '')}`\n\n")
            f.write("## Summary\n\n")
            f.write("| Metric | Value |\n")
            f.write("| --- | ---: |\n")
            f.write(f"| Inventory repositories | {payload.get('inventory_repos', 0)} |\n")
            f.write(f"| Filtered repositories | {payload.get('filtered_repos', 0)} |\n")
            f.write(f"| `pushed_at` candidates | {calibration.get('pushed_at_candidates', 0)} |\n")
            f.write(f"| Events candidates in report scope | {calibration.get('event_candidates_in_scope', 0)} |\n")
            f.write(f"| Events candidates outside report scope | {calibration.get('event_candidates_outside_scope', 0)} |\n")
            f.write(f"| Intersection candidates | {calibration.get('intersection_candidates', 0)} |\n")
            f.write(f"| Union candidates | {calibration.get('union_candidates', 0)} |\n")
            f.write(f"| Intersect candidate savings | {calibration.get('intersect_candidate_savings', 0)} |\n")
            f.write(f"| Intersect potential misses | {calibration.get('intersect_potential_miss_count', 0)} |\n\n")

            for title, key in (
                ("Pushed-Only Sample", "pushed_only"),
                ("Events-Only Sample", "events_only"),
                ("Events Outside Report Scope Sample", "events_outside_scope"),
            ):
                values = samples.get(key) or []
                if not values:
                    continue
                f.write(f"## {title}\n\n")
                for value in values:
                    f.write(f"- [{value}](https://github.com/{value})\n")
                f.write("\n")

    return paths


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="msft_repo_inventory.csv")
    parser.add_argument("--orgs", default="orgs.txt")
    parser.add_argument("--state", default="msft_repo_tracker_state.json")
    parser.add_argument("--hours", type=int, default=24)
    parser.add_argument("--categories", default="")
    parser.add_argument("--include-other", action="store_true")
    parser.add_argument("--include-archived", action="store_true")
    parser.add_argument("--include-forks", action="store_true")
    parser.add_argument("--events-max-pages", type=int, default=2)
    parser.add_argument("--min-rest-remaining", type=int, default=100)
    parser.add_argument("--no-budget-check", action="store_true")
    parser.add_argument("--reports-dir", default=os.path.join("reports", "events-calibration"))
    return parser


def main() -> int:
    args = build_parser().parse_args()
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        sys.stderr.write("[WARN] GITHUB_TOKEN not set. API budget will be very low.\n")

    try:
        repos = read_inventory(args.input)
        filtered = filter_repos(
            repos,
            args.categories,
            args.include_other,
            args.include_archived,
            args.include_forks,
        )
        state = load_state(args.state)
        now = dt.datetime.now(dt.timezone.utc)
        since_dt = compute_since_dt(
            now,
            args.hours,
            state=state,
            use_state_window=False,
            overlap_hours=0,
            max_lookback_hours=args.hours,
        )
        since_iso = iso_utc(since_dt)
        pushed = pushed_candidates(filtered, since_dt)

        client = GitHubClient(token=token, user_agent="msft-events-calibration")
        if not args.no_budget_check:
            client.ensure_budget("core", args.min_rest_remaining)
        event_names, events_summary = fetch_event_candidates(
            client=client,
            orgs=read_orgs(args.orgs),
            state=state,
            max_pages_per_org=args.events_max_pages,
        )
        calibration = build_events_calibration(
            filtered=filtered,
            pushed_candidates=pushed,
            event_candidate_names=event_names,
            events_summary=events_summary,
        )
        payload = {
            "schema_version": 1,
            "generated_at": iso_utc(now),
            "since": since_iso,
            "hours_requested": args.hours,
            "inventory_repos": len(repos),
            "filtered_repos": len(filtered),
            "calibration": calibration,
        }
        paths = write_calibration_reports(args.reports_dir, payload)
        state["last_events_calibration"] = {
            **calibration,
            "completed_at": iso_utc(now),
            "report_paths": paths,
        }
        save_state(args.state, state)

    except RateLimitDeferred as exc:
        print(f"[DEFERRED] {exc}", file=sys.stderr)
        return DEFERRED_EXIT_CODE

    print(f"Wrote {len(paths)} Events calibration report file(s) to {args.reports_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
