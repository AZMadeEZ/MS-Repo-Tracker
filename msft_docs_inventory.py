#!/usr/bin/env python3
"""
Microsoft public repository inventory.

- Reads orgs from orgs.txt (one org per line)
- Lists public repos in each org
- Classifies repos into docs/reference/training/samples/other
- Writes:
    msft_repo_inventory.csv
    msft_repo_inventory_watchfeeds.csv
    msft_repo_tracker_state.json

The default inventory baseline includes all public repositories. Digest/report
commands can still filter to docs/reference/training/samples.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import os
import re
import sys
import datetime as dt
from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple

from github_api import (
    DEFERRED_EXIT_CODE,
    GitHubClient,
    RateLimitDeferred,
    iso_utc,
    update_conditional_cache,
    utc_now,
)


STATE_SCHEMA_VERSION = 1
DEFAULT_STATE_PATH = "msft_repo_tracker_state.json"


# --- Classification rules (tune freely) ---
DOC_ORGS = {"MicrosoftDocs"}
TRAINING_ORGS = {"MicrosoftLearning"}
SAMPLES_ORGS = {"Azure-Samples"}

DOC_KEYWORDS = re.compile(
    r"\b(docs?|documentation|learn\.microsoft\.com|docs\.microsoft\.com|docfx|openpublishing|reference)\b",
    re.IGNORECASE,
)
TRAINING_KEYWORDS = re.compile(
    r"\b(mslearn|microsoft learn|workshop|lab|hands-on)\b",
    re.IGNORECASE,
)
SAMPLES_KEYWORDS = re.compile(
    r"\b(sample|samples|quickstart|tutorial|demo|accelerator|reference architecture|azd)\b",
    re.IGNORECASE,
)
REFERENCE_KEYWORDS = re.compile(
    r"\b(api reference|reference|sdk[- ]?api|cmdlet|powershell[- ]?ref)\b",
    re.IGNORECASE,
)


CSV_FIELDS = [
    "org",
    "name",
    "full_name",
    "html_url",
    "description",
    "homepage",
    "archived",
    "fork",
    "created_at",
    "updated_at",
    "pushed_at",
    "default_branch",
    "language",
    "license_spdx",
    "stars",
    "forks",
    "open_issues",
    "category",
    "score",
]


@dataclass
class RepoRow:
    org: str
    name: str
    full_name: str
    html_url: str
    description: str
    homepage: str
    archived: bool
    fork: bool
    created_at: str
    updated_at: str
    pushed_at: str
    default_branch: str
    language: str
    license_spdx: str
    stars: int
    forks: int
    open_issues: int
    category: str
    score: int


def parse_bool(value: Any) -> bool:
    return str(value).strip().lower() in ("true", "1", "yes", "y")


def parse_int(value: Any) -> int:
    try:
        return int(value or 0)
    except (TypeError, ValueError):
        return 0


def parse_iso(value: str) -> Optional[dt.datetime]:
    if not value:
        return None
    try:
        if value.endswith("Z"):
            value = value[:-1] + "+00:00"
        return dt.datetime.fromisoformat(value)
    except ValueError:
        return None


def max_timestamp(values: Iterable[str]) -> str:
    timestamps = [value for value in values if value]
    return max(timestamps) if timestamps else ""


def classify(org: str, name: str, description: str, homepage: str) -> Tuple[str, int]:
    text = f"{name} {description} {homepage}".strip()
    scores = {
        "docs": 0,
        "reference": 0,
        "training": 0,
        "samples": 0,
    }

    if org in DOC_ORGS:
        scores["docs"] += 100
    if org in TRAINING_ORGS:
        scores["training"] += 100
    if org in SAMPLES_ORGS:
        scores["samples"] += 100

    if DOC_KEYWORDS.search(text):
        scores["docs"] += 40
    if REFERENCE_KEYWORDS.search(text):
        scores["reference"] += 35
    if TRAINING_KEYWORDS.search(text):
        scores["training"] += 30
    if SAMPLES_KEYWORDS.search(text):
        scores["samples"] += 25

    lname = name.lower()
    if "docs" in lname or lname.endswith("-docs") or lname.startswith("docs-"):
        scores["docs"] += 20
    if "reference" in lname or ("api" in lname and "docs" in lname):
        scores["reference"] += 15
    if "sample" in lname or "quickstart" in lname:
        scores["samples"] += 15
    if lname.startswith("mslearn-"):
        scores["training"] += 20

    tie_breaker = ["docs", "reference", "training", "samples"]
    winner = max(tie_breaker, key=lambda category: (scores[category], -tie_breaker.index(category)))
    winning_score = scores[winner]

    if winning_score == 0:
        return "other", 0

    return winner, winning_score


def make_row(org: str, repo: Dict[str, Any]) -> RepoRow:
    license_info = repo.get("license") or {}
    category, score = classify(
        org=org,
        name=repo.get("name") or "",
        description=repo.get("description") or "",
        homepage=repo.get("homepage") or "",
    )
    return RepoRow(
        org=org,
        name=repo.get("name") or "",
        full_name=repo.get("full_name") or "",
        html_url=repo.get("html_url") or "",
        description=(repo.get("description") or "").strip(),
        homepage=(repo.get("homepage") or "").strip(),
        archived=bool(repo.get("archived")),
        fork=bool(repo.get("fork")),
        created_at=repo.get("created_at") or "",
        updated_at=repo.get("updated_at") or "",
        pushed_at=repo.get("pushed_at") or "",
        default_branch=repo.get("default_branch") or "",
        language=repo.get("language") or "",
        license_spdx=license_info.get("spdx_id") or "",
        stars=parse_int(repo.get("stargazers_count")),
        forks=parse_int(repo.get("forks_count")),
        open_issues=parse_int(repo.get("open_issues_count")),
        category=category,
        score=score,
    )


def row_to_dict(row: RepoRow) -> Dict[str, Any]:
    return {field: getattr(row, field) for field in CSV_FIELDS}


def row_from_csv(row: Dict[str, str]) -> RepoRow:
    return RepoRow(
        org=(row.get("org") or "").strip(),
        name=(row.get("name") or "").strip(),
        full_name=(row.get("full_name") or "").strip(),
        html_url=(row.get("html_url") or "").strip(),
        description=(row.get("description") or "").strip(),
        homepage=(row.get("homepage") or "").strip(),
        archived=parse_bool(row.get("archived")),
        fork=parse_bool(row.get("fork")),
        created_at=(row.get("created_at") or "").strip(),
        updated_at=(row.get("updated_at") or "").strip(),
        pushed_at=(row.get("pushed_at") or "").strip(),
        default_branch=(row.get("default_branch") or "").strip(),
        language=(row.get("language") or "").strip(),
        license_spdx=(row.get("license_spdx") or "").strip(),
        stars=parse_int(row.get("stars")),
        forks=parse_int(row.get("forks")),
        open_issues=parse_int(row.get("open_issues")),
        category=(row.get("category") or "other").strip() or "other",
        score=parse_int(row.get("score")),
    )


def read_inventory(path: str) -> List[RepoRow]:
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        rows = []
        for row in reader:
            repo = row_from_csv(row)
            if repo.full_name:
                rows.append(repo)
        return rows


def write_csv(path: str, rows: List[RepoRow]) -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow(row_to_dict(row))


def write_watchfeeds(path: str, rows: List[RepoRow]) -> None:
    fields = [
        "full_name",
        "category",
        "default_branch",
        "commits_atom",
        "releases_atom",
    ]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            if not row.full_name or not row.default_branch:
                continue
            writer.writerow(
                {
                    "full_name": row.full_name,
                    "category": row.category,
                    "default_branch": row.default_branch,
                    "commits_atom": f"https://github.com/{row.full_name}/commits/{row.default_branch}.atom",
                    "releases_atom": f"https://github.com/{row.full_name}/releases.atom",
                }
            )


def default_state() -> Dict[str, Any]:
    return {
        "schema_version": STATE_SCHEMA_VERSION,
        "updated_at": "",
        "orgs": {},
        "request_cache": {},
        "last_run": {},
    }


def normalize_state(state: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(state, dict):
        state = {}
    state.setdefault("schema_version", STATE_SCHEMA_VERSION)
    state.setdefault("updated_at", "")
    state.setdefault("orgs", {})
    state.setdefault("request_cache", {})
    state.setdefault("last_run", {})
    if not isinstance(state["orgs"], dict):
        state["orgs"] = {}
    if not isinstance(state["request_cache"], dict):
        state["request_cache"] = {}
    if not isinstance(state["last_run"], dict):
        state["last_run"] = {}
    return state


def load_state(path: str) -> Dict[str, Any]:
    if not os.path.exists(path):
        return default_state()
    with open(path, "r", encoding="utf-8-sig") as f:
        return normalize_state(json.load(f))


def save_state(path: str, state: Dict[str, Any]) -> None:
    tmp_path = f"{path}.tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, sort_keys=True)
        f.write("\n")
    os.replace(tmp_path, path)


def read_orgs(path: str) -> List[str]:
    if not os.path.exists(path):
        raise RuntimeError(f"Missing {path} (one org per line).")
    with open(path, "r", encoding="utf-8") as f:
        orgs = []
        for line in f:
            value = line.strip().lstrip("\ufeff")
            if value and not value.startswith("#"):
                orgs.append(value)
        return orgs


def response_has_next(headers: Mapping[str, str]) -> bool:
    return 'rel="next"' in (headers.get("Link") or headers.get("link") or "")


def cached_item_count(entry: Dict[str, Any]) -> int:
    return parse_int(entry.get("item_count"))


def page_overlaps_cutoff(rows: List[RepoRow], cutoff_dt: dt.datetime) -> bool:
    for row in rows:
        pushed_at = parse_iso(row.pushed_at)
        if pushed_at and pushed_at >= cutoff_dt:
            return True
    return False


def fallback_repo_count(org: str, existing_rows: List[RepoRow], state: Dict[str, Any]) -> int:
    count = sum(1 for row in existing_rows if row.org == org)
    org_state = (state.get("orgs") or {}).get(org) or {}
    return max(count, parse_int(org_state.get("last_repo_count")))


def estimate_full_scan_pages(
    client: GitHubClient,
    orgs: List[str],
    existing_rows: List[RepoRow],
    state: Dict[str, Any],
) -> Tuple[int, Dict[str, int]]:
    counts: Dict[str, int] = {}
    for org in orgs:
        try:
            response = client.get_json(f"/orgs/{org}", use_conditional=False)
            counts[org] = parse_int((response.data or {}).get("public_repos"))
        except RateLimitDeferred:
            raise
        except Exception as exc:
            fallback = fallback_repo_count(org, existing_rows, state)
            counts[org] = fallback
            sys.stderr.write(
                f"[WARN] Could not read public repo count for {org}: {exc}. "
                f"Using fallback estimate {fallback}.\n"
            )

    pages = sum(max(1, math.ceil(count / 100)) for count in counts.values())
    return pages, counts


def ensure_rest_budget(
    client: GitHubClient,
    mode: str,
    orgs: List[str],
    existing_rows: List[RepoRow],
    state: Dict[str, Any],
    buffer_ratio: float,
    minimum_override: Optional[int],
) -> None:
    if mode == "full":
        estimated_pages, counts = estimate_full_scan_pages(client, orgs, existing_rows, state)
        minimum = minimum_override
        if minimum is None:
            minimum = math.ceil(estimated_pages * (1 + buffer_ratio))
        sys.stderr.write(
            f"[INFO] Full scan estimate: {estimated_pages} repo-list request(s), "
            f"minimum remaining REST budget {minimum}. Counts: {counts}\n"
        )
        client.ensure_budget("core", minimum)
        return

    estimated_pages = max(1, len(orgs))
    minimum = minimum_override
    if minimum is None:
        minimum = math.ceil(estimated_pages * (1 + buffer_ratio))
    sys.stderr.write(
        f"[INFO] Incremental scan estimate: at least {estimated_pages} repo-list request(s), "
        f"minimum remaining REST budget {minimum}.\n"
    )
    client.ensure_budget("core", minimum)


def list_org_repos(
    client: GitHubClient,
    org: str,
    state: Dict[str, Any],
    *,
    mode: str,
    cutoff_dt: dt.datetime,
    ignore_cache: bool,
) -> Tuple[List[RepoRow], Set[str], int]:
    cache = state.setdefault("request_cache", {})
    sort = "pushed" if mode == "incremental" else "full_name"
    direction = "desc" if mode == "incremental" else "asc"
    page = 1
    rows: List[RepoRow] = []
    seen: Set[str] = set()
    pages_scanned = 0

    while True:
        response = client.get_json(
            f"/orgs/{org}/repos",
            params={
                "type": "public",
                "per_page": 100,
                "page": page,
                "sort": sort,
                "direction": direction,
            },
            cache=cache,
            use_conditional=not ignore_cache,
        )
        pages_scanned += 1

        if response.not_modified:
            entry = cache.get(response.url, {}) or {}
            cached_names = [str(name) for name in (entry.get("repo_full_names") or [])]
            seen.update(cached_names)
            item_count = cached_item_count(entry)
            has_next = bool(entry.get("has_next"))
            sys.stderr.write(f"[INFO] {org} page {page}: not modified.\n")

            if mode == "incremental":
                break
            if item_count == 0 or not has_next:
                break
            page += 1
            continue

        batch = response.data or []
        if not isinstance(batch, list):
            raise RuntimeError(f"Unexpected repository list response for {org} page {page}.")

        page_rows = [make_row(org, repo) for repo in batch]
        page_names = [row.full_name for row in page_rows if row.full_name]
        rows.extend(page_rows)
        seen.update(page_names)

        has_next = response_has_next(response.headers)
        update_conditional_cache(
            cache,
            response,
            item_count=len(page_rows),
            repo_full_names=page_names,
            has_next=has_next,
        )

        sys.stderr.write(f"[INFO] {org} page {page}: {len(page_rows)} repo(s).\n")

        if not page_rows:
            break

        if mode == "incremental" and not page_overlaps_cutoff(page_rows, cutoff_dt):
            sys.stderr.write(
                f"[INFO] {org} page {page}: older than overlap window; stopping.\n"
            )
            break

        if not has_next:
            break
        page += 1

    return rows, seen, pages_scanned


def update_org_state(
    state: Dict[str, Any],
    org: str,
    *,
    mode: str,
    completed_at: str,
    pages_scanned: int,
    repo_count: int,
    last_seen_pushed_at: str,
) -> None:
    org_state = state.setdefault("orgs", {}).setdefault(org, {})
    org_state["last_successful_scan_at"] = completed_at
    org_state["last_scan_mode"] = mode
    org_state["last_pages_scanned"] = pages_scanned
    org_state["last_repo_count"] = repo_count
    org_state["last_seen_pushed_at"] = last_seen_pushed_at
    if mode == "full":
        org_state["last_full_scan_at"] = completed_at
    else:
        org_state["last_incremental_scan_at"] = completed_at


def lifecycle_row(row: RepoRow) -> Dict[str, Any]:
    return {
        "full_name": row.full_name,
        "org": row.org,
        "name": row.name,
        "html_url": row.html_url,
        "category": row.category,
        "created_at": row.created_at,
        "pushed_at": row.pushed_at,
        "archived": row.archived,
        "fork": row.fork,
        "default_branch": row.default_branch,
    }


def limited_lifecycle_items(items: List[Dict[str, Any]], limit: int = 100) -> List[Dict[str, Any]]:
    return items[:limit]


def build_lifecycle_summary(
    before_rows: List[RepoRow],
    after_rows: List[RepoRow],
    completed_orgs: Set[str],
    mode: str,
    completed_at: str,
) -> Dict[str, Any]:
    before = {
        row.full_name: row
        for row in before_rows
        if row.full_name and row.org in completed_orgs
    }
    after = {
        row.full_name: row
        for row in after_rows
        if row.full_name and row.org in completed_orgs
    }

    new_repos = [lifecycle_row(after[name]) for name in sorted(set(after) - set(before))]
    removed_repos = []
    if mode == "full":
        removed_repos = [lifecycle_row(before[name]) for name in sorted(set(before) - set(after))]

    archived_changed: List[Dict[str, Any]] = []
    default_branch_changed: List[Dict[str, Any]] = []
    category_changed: List[Dict[str, Any]] = []
    fork_changed: List[Dict[str, Any]] = []

    for name in sorted(set(before) & set(after)):
        old = before[name]
        new = after[name]
        if old.archived != new.archived:
            archived_changed.append(
                {
                    **lifecycle_row(new),
                    "previous_archived": old.archived,
                    "current_archived": new.archived,
                }
            )
        if old.default_branch != new.default_branch:
            default_branch_changed.append(
                {
                    **lifecycle_row(new),
                    "previous_default_branch": old.default_branch,
                    "current_default_branch": new.default_branch,
                }
            )
        if old.category != new.category:
            category_changed.append(
                {
                    **lifecycle_row(new),
                    "previous_category": old.category,
                    "current_category": new.category,
                }
            )
        if old.fork != new.fork:
            fork_changed.append(
                {
                    **lifecycle_row(new),
                    "previous_fork": old.fork,
                    "current_fork": new.fork,
                }
            )

    return {
        "available": True,
        "completed_at": completed_at,
        "mode": mode,
        "orgs_completed": sorted(completed_orgs),
        "counts": {
            "new_repos": len(new_repos),
            "removed_repos": len(removed_repos),
            "archived_changed": len(archived_changed),
            "default_branch_changed": len(default_branch_changed),
            "category_changed": len(category_changed),
            "fork_changed": len(fork_changed),
        },
        "new_repos": limited_lifecycle_items(new_repos),
        "removed_repos": limited_lifecycle_items(removed_repos),
        "archived_changed": limited_lifecycle_items(archived_changed),
        "default_branch_changed": limited_lifecycle_items(default_branch_changed),
        "category_changed": limited_lifecycle_items(category_changed),
        "fork_changed": limited_lifecycle_items(fork_changed),
    }


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("incremental", "full"), default="full")
    parser.add_argument("--orgs", default="orgs.txt", help="Org list file.")
    parser.add_argument("--output", default="msft_repo_inventory.csv")
    parser.add_argument("--watchfeeds", default="msft_repo_inventory_watchfeeds.csv")
    parser.add_argument("--state", default=DEFAULT_STATE_PATH)
    parser.add_argument("--overlap-hours", type=int, default=48)
    parser.add_argument(
        "--include-other-baseline",
        dest="include_other_baseline",
        action="store_true",
        default=True,
        help="Include other-category repos in the inventory baseline (default).",
    )
    parser.add_argument(
        "--exclude-other-baseline",
        dest="include_other_baseline",
        action="store_false",
        help="Legacy behavior: omit other-category repos from the inventory CSV.",
    )
    parser.add_argument("--ignore-cache", action="store_true")
    parser.add_argument("--no-budget-check", action="store_true")
    parser.add_argument("--budget-buffer", type=float, default=0.25)
    parser.add_argument("--min-rest-remaining", type=int, default=None)
    return parser


def main() -> int:
    args = build_arg_parser().parse_args()
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        sys.stderr.write("[WARN] GITHUB_TOKEN not set. API budget will be very low.\n")

    try:
        orgs = read_orgs(args.orgs)
    except Exception as exc:
        print(exc, file=sys.stderr)
        return 2

    existing_rows = read_inventory(args.output)
    inventory_by_full_name = {row.full_name: row for row in existing_rows if row.full_name}
    state = load_state(args.state)
    client = GitHubClient(token=token, user_agent="msft-docs-inventory")
    now = utc_now()
    completed_at = iso_utc(now)
    cutoff_dt = now - dt.timedelta(hours=args.overlap_hours)

    try:
        if not args.no_budget_check:
            ensure_rest_budget(
                client=client,
                mode=args.mode,
                orgs=orgs,
                existing_rows=existing_rows,
                state=state,
                buffer_ratio=args.budget_buffer,
                minimum_override=args.min_rest_remaining,
            )

        seen_by_org: Dict[str, Set[str]] = {}
        completed_orgs: Set[str] = set()

        for org in orgs:
            try:
                rows, seen, pages_scanned = list_org_repos(
                    client,
                    org,
                    state,
                    mode=args.mode,
                    cutoff_dt=cutoff_dt,
                    ignore_cache=args.ignore_cache,
                )
            except RateLimitDeferred:
                raise
            except Exception as exc:
                sys.stderr.write(f"[WARN] Skipping org '{org}': {exc}\n")
                continue

            for row in rows:
                if row.full_name:
                    inventory_by_full_name[row.full_name] = row

            seen_by_org[org] = seen
            completed_orgs.add(org)
            org_rows = [row for row in inventory_by_full_name.values() if row.org == org]
            if args.mode == "full":
                pushed_values = [
                    inventory_by_full_name[name].pushed_at
                    for name in seen
                    if name in inventory_by_full_name
                ]
                repo_count = len(seen)
            else:
                pushed_values = [row.pushed_at for row in org_rows]
                repo_count = len(org_rows)

            update_org_state(
                state,
                org,
                mode=args.mode,
                completed_at=completed_at,
                pages_scanned=pages_scanned,
                repo_count=repo_count,
                last_seen_pushed_at=max_timestamp(pushed_values),
            )

        if args.mode == "full":
            for full_name, row in list(inventory_by_full_name.items()):
                if row.org in completed_orgs and full_name not in seen_by_org.get(row.org, set()):
                    del inventory_by_full_name[full_name]

        output_rows = list(inventory_by_full_name.values())
        if not args.include_other_baseline:
            output_rows = [row for row in output_rows if row.category != "other"]

        output_rows.sort(key=lambda row: (row.pushed_at or "", row.full_name), reverse=True)
        lifecycle_summary = build_lifecycle_summary(
            before_rows=existing_rows,
            after_rows=output_rows,
            completed_orgs=completed_orgs,
            mode=args.mode,
            completed_at=completed_at,
        )
        write_csv(args.output, output_rows)
        write_watchfeeds(args.watchfeeds, output_rows)

        state["schema_version"] = STATE_SCHEMA_VERSION
        state["updated_at"] = completed_at
        state["last_run"] = {
            "mode": args.mode,
            "completed_at": completed_at,
            "orgs_requested": orgs,
            "orgs_completed": sorted(completed_orgs),
            "repos_written": len(output_rows),
            "include_other_baseline": args.include_other_baseline,
        }
        state["last_inventory_lifecycle"] = lifecycle_summary
        save_state(args.state, state)

    except RateLimitDeferred as exc:
        print(f"[DEFERRED] {exc}", file=sys.stderr)
        return DEFERRED_EXIT_CODE

    print(f"Wrote {len(output_rows)} repos to {args.output}")
    print(f"Wrote watch feeds to {args.watchfeeds}")
    print(f"Wrote tracker state to {args.state}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
