#!/usr/bin/env python3
"""
Summarize changes on the default branch in the last N hours for repos listed in
an inventory CSV.

By default, the digest includes docs/reference/training/samples repositories.
Use --include-other or --categories all to widen the report to the full
inventory baseline.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import os
import re
import subprocess
import sys
from collections import Counter
from dataclasses import dataclass
from typing import Any, Dict, List, Mapping, Optional, Set, Tuple

import yaml

from github_api import (
    DEFERRED_EXIT_CODE,
    GitHubClient,
    RateLimitDeferred,
    iso_utc,
    update_conditional_cache,
)


DEFAULT_DIGEST_CATEGORIES = {"docs", "reference", "training", "samples"}
DEFAULT_STATE_PATH = "msft_repo_tracker_state.json"
DEFAULT_WATCHLIST_PATH = "watchlist.yml"
ARTIFACT_VERSION = "1.0.0"
REPORT_SCHEMA_URL = "schemas/report.v1.schema.json"
REPORT_INDEX_SCHEMA_URL = "schemas/report-index.v1.schema.json"
SUMMARY_SCHEMA_URL = "schemas/summary.v1.schema.json"
MANIFEST_SCHEMA_URL = "schemas/manifest.v1.schema.json"
STATUS_SCHEMA_URL = "schemas/status.v1.schema.json"
DIGEST_CSV_SCHEMA_URL = "schemas/digest-csv.v1.schema.json"
INVENTORY_SCHEMA_URL = "schemas/inventory.v1.schema.json"
WATCHFEEDS_SCHEMA_URL = "schemas/watchfeeds.v1.schema.json"
STATE_SCHEMA_URL = "schemas/state.v1.schema.json"
EVENTS_CALIBRATION_SCHEMA_URL = "schemas/events-calibration.v1.schema.json"
EVENT_SCHEMA_URL = "schemas/event.v1.schema.json"
REPORT_FRESHNESS_HOURS = 30
BOT_MARKERS = ("[bot]", "dependabot", "renovate", "github-actions", "learn-build-service")
DEPENDENCY_MARKERS = ("bump ", "dependabot", "renovate", "dependency", "dependencies")
RELEASE_MARKERS = ("release", "version", "ga ", "generally available", "preview")
SECURITY_MARKERS = ("security", "cve-", "vulnerab", "credential", "secret")
BULK_MARKERS = ("[bulk]", "bulk ", "scheduled execution", "mass update")
CI_MARKERS = ("workflow", "pipeline", "test automation", "github action")
SDK_MARKERS = ("sdk generation", "generated-from-sdk", "generated from sdk", "autorest", "kiota", "unbrandedgenerator", "autopr")


@dataclass
class RepoInput:
    full_name: str
    org: str = ""
    name: str = ""
    html_url: str = ""
    category: str = ""
    created_at: str = ""
    updated_at: str = ""
    pushed_at: str = ""
    default_branch: str = ""
    language: str = ""
    stars: int = 0
    archived: Optional[bool] = None
    fork: Optional[bool] = None
    repo_type: str = ""
    product_area: str = ""
    audience: str = ""
    classification_confidence: str = ""
    classification_reason: str = ""
    classification_version: str = ""


@dataclass
class CommitInfo:
    oid: str
    committed_date: str
    headline: str
    url: str
    author: str
    pr_number: Optional[int] = None
    pr_title: Optional[str] = None
    pr_url: Optional[str] = None


@dataclass
class ReleaseInfo:
    repo_full_name: str
    tag_name: str
    name: str
    published_at: str
    html_url: str
    prerelease: bool = False
    draft: bool = False


@dataclass
class RepoCount:
    repo: RepoInput
    default_branch: str
    commit_count: int


@dataclass
class RepoActivity:
    full_name: str
    org: str
    name: str
    category: str
    default_branch: str
    commit_count: int
    newest_commit_date: str
    commits: List[CommitInfo]
    repo_type: str = ""
    product_area: str = ""
    audience: str = ""
    classification_confidence: str = ""
    classification_reason: str = ""
    classification_version: str = ""


def parse_bool(val: Any) -> Optional[bool]:
    if val is None:
        return None
    value = str(val).strip().lower()
    if value in ("true", "1", "yes", "y"):
        return True
    if value in ("false", "0", "no", "n"):
        return False
    return None


def parse_int(value: Any) -> int:
    try:
        return int(value or 0)
    except (TypeError, ValueError):
        return 0


def read_inventory(path: str) -> List[RepoInput]:
    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        cols = {col.strip() for col in (reader.fieldnames or [])}
        if "full_name" not in cols:
            raise RuntimeError(f"{path} is missing required column: full_name")

        repos: List[RepoInput] = []
        for row in reader:
            full_name = (row.get("full_name") or "").strip()
            if not full_name or "/" not in full_name:
                continue

            org = (row.get("org") or "").strip()
            name = (row.get("name") or "").strip()
            if not org or not name:
                owner, repo_name = full_name.split("/", 1)
                org = org or owner
                name = name or repo_name

            repos.append(
                RepoInput(
                    full_name=full_name,
                    org=org,
                    name=name,
                    html_url=(row.get("html_url") or f"https://github.com/{full_name}").strip(),
                    category=(row.get("category") or "other").strip() or "other",
                    created_at=(row.get("created_at") or "").strip(),
                    updated_at=(row.get("updated_at") or "").strip(),
                    pushed_at=(row.get("pushed_at") or "").strip(),
                    default_branch=(row.get("default_branch") or "").strip(),
                    language=(row.get("language") or "").strip(),
                    stars=parse_int(row.get("stars")),
                    archived=parse_bool(row.get("archived")),
                    fork=parse_bool(row.get("fork")),
                    repo_type=(row.get("repo_type") or "").strip(),
                    product_area=(row.get("product_area") or "").strip(),
                    audience=(row.get("audience") or "").strip(),
                    classification_confidence=(row.get("classification_confidence") or "").strip(),
                    classification_reason=(row.get("classification_reason") or "").strip(),
                    classification_version=(row.get("classification_version") or "").strip(),
                )
            )
        return repos


def read_orgs(path: str) -> List[str]:
    with open(path, "r", encoding="utf-8-sig") as f:
        orgs: List[str] = []
        for line in f:
            value = line.strip()
            if not value or value.startswith("#"):
                continue
            orgs.append(value)
        return orgs


def parse_iso(value: str) -> Optional[dt.datetime]:
    if not value:
        return None
    try:
        if value.endswith("Z"):
            value = value[:-1] + "+00:00"
        return dt.datetime.fromisoformat(value)
    except ValueError:
        return None


def load_state(path: str) -> Dict[str, Any]:
    if not path or not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8-sig") as f:
        state = json.load(f)
    return state if isinstance(state, dict) else {}


def save_state(path: str, state: Dict[str, Any]) -> None:
    if not path:
        return
    tmp_path = f"{path}.tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, sort_keys=True)
        f.write("\n")
    os.replace(tmp_path, path)


def source_commit() -> str:
    value = os.environ.get("GITHUB_SHA", "").strip()
    if value:
        return value
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
            timeout=5,
        )
        return result.stdout.strip()
    except Exception:
        return ""


def workflow_run_url() -> str:
    repository = os.environ.get("GITHUB_REPOSITORY", "").strip()
    run_id = os.environ.get("GITHUB_RUN_ID", "").strip()
    if not repository or not run_id:
        return ""
    server_url = os.environ.get("GITHUB_SERVER_URL", "https://github.com").rstrip("/")
    return f"{server_url}/{repository}/actions/runs/{run_id}"


def source_metadata() -> Dict[str, str]:
    return {
        "repository": os.environ.get("GITHUB_REPOSITORY", "").strip(),
        "commit": source_commit(),
        "workflow": os.environ.get("GITHUB_WORKFLOW", "").strip(),
        "workflow_run_id": os.environ.get("GITHUB_RUN_ID", "").strip(),
        "workflow_run_url": workflow_run_url(),
    }


def normalize_artifact_path(path: str) -> str:
    return os.path.normpath(path).replace("\\", "/")


def latest_report_generated_at(report_dir: str) -> str:
    path = os.path.join(report_dir, "latest.json")
    if not os.path.exists(path):
        return ""
    try:
        with open(path, "r", encoding="utf-8") as f:
            payload = json.load(f)
        return str((payload or {}).get("generated_at") or "")
    except Exception:
        return ""


def freshness_payload(latest_generated_at: str, now_utc: dt.datetime) -> Dict[str, Any]:
    latest_dt = parse_iso(latest_generated_at)
    if latest_dt is None:
        return {
            "max_age_hours": REPORT_FRESHNESS_HOURS,
            "age_hours": None,
            "latest_report_stale": True,
            "state": "unknown",
        }

    age = now_utc - latest_dt.astimezone(dt.timezone.utc)
    age_hours = max(0.0, round(age.total_seconds() / 3600, 2))
    stale = age > dt.timedelta(hours=REPORT_FRESHNESS_HOURS)
    return {
        "max_age_hours": REPORT_FRESHNESS_HOURS,
        "age_hours": age_hours,
        "latest_report_stale": stale,
        "state": "stale" if stale else "fresh",
    }


def infer_deferred_reason(message: str) -> str:
    lowered = message.lower()
    if "graphql" in lowered:
        return "graphql_budget_too_low"
    if "core" in lowered or "rest" in lowered:
        return "rest_budget_too_low"
    if "rate limit" in lowered or "budget exhausted" in lowered or "secondary rate" in lowered:
        return "github_rate_limit"
    return "deferred"


def compute_since_dt(
    now_utc: dt.datetime,
    hours: int,
    *,
    state: Dict[str, Any],
    use_state_window: bool,
    overlap_hours: int,
    max_lookback_hours: int,
) -> dt.datetime:
    requested_since = now_utc - dt.timedelta(hours=hours)
    if not use_state_window:
        return requested_since

    digest_state = state.get("last_digest") or {}
    last_success = parse_iso(str(digest_state.get("completed_at") or ""))
    if last_success is None:
        return requested_since

    state_since = last_success - dt.timedelta(hours=overlap_hours)
    since_dt = min(requested_since, state_since)
    oldest_allowed = now_utc - dt.timedelta(hours=max_lookback_hours)
    if since_dt < oldest_allowed:
        sys.stderr.write(
            f"[WARN] State-based digest window capped at {max_lookback_hours} hours.\n"
        )
        return oldest_allowed
    return since_dt


def chunked(values: List[Any], size: int) -> List[List[Any]]:
    return [values[i : i + size] for i in range(0, len(values), size)]


def category_filter(categories_arg: str, include_other: bool) -> Optional[Set[str]]:
    raw = (categories_arg or "").strip()
    if raw.lower() == "all":
        return None

    if raw:
        selected = {value.strip() for value in raw.split(",") if value.strip()}
    else:
        selected = set(DEFAULT_DIGEST_CATEGORIES)

    if include_other:
        selected.add("other")

    return selected


def normalize_full_name(value: str) -> str:
    return value.strip().lower()


def normalize_keyword(value: str) -> str:
    return value.strip().lower()


def as_string_list(value: Any) -> List[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    return []


def load_watchlist(path: str) -> Dict[str, Any]:
    if not path or not os.path.exists(path):
        return {
            "repos": set(),
            "orgs": set(),
            "keywords": set(),
            "products": [],
        }

    with open(path, "r", encoding="utf-8-sig") as f:
        raw = yaml.safe_load(f) or {}
    if not isinstance(raw, dict):
        raise RuntimeError(f"{path} must contain a YAML mapping.")

    repos = {normalize_full_name(value) for value in as_string_list(raw.get("repos"))}
    orgs = {value.strip().lower() for value in as_string_list(raw.get("orgs"))}
    keywords = {normalize_keyword(value) for value in as_string_list(raw.get("keywords"))}
    products: List[Dict[str, Any]] = []

    for product in raw.get("products") or []:
        if not isinstance(product, dict):
            continue
        name = str(product.get("name") or "").strip()
        if not name:
            continue
        product_repos = {
            normalize_full_name(value) for value in as_string_list(product.get("repos"))
        }
        product_keywords = {
            normalize_keyword(value) for value in as_string_list(product.get("keywords"))
        }
        products.append(
            {
                "name": name,
                "repos": product_repos,
                "keywords": product_keywords,
            }
        )
        repos.update(product_repos)
        keywords.update(product_keywords)

    return {
        "repos": repos,
        "orgs": orgs,
        "keywords": keywords,
        "products": products,
    }


def activity_text(activity: RepoActivity) -> str:
    parts = [activity.full_name, activity.name, activity.category, activity.repo_type, activity.product_area, activity.audience]
    for commit in activity.commits:
        parts.extend([commit.headline, commit.pr_title or "", commit.author])
    return " ".join(part for part in parts if part).lower()


def is_bot_author(author: str) -> bool:
    lowered = (author or "").lower()
    return any(marker in lowered for marker in BOT_MARKERS)


def is_dependency_text(text: str) -> bool:
    lowered = text.lower()
    return any(marker in lowered for marker in DEPENDENCY_MARKERS)


def is_security_text(text: str) -> bool:
    lowered = text.lower()
    return any(marker in lowered for marker in SECURITY_MARKERS)


def is_release_text(text: str) -> bool:
    lowered = text.lower()
    return any(marker in lowered for marker in RELEASE_MARKERS)


def watchlist_matches(activity: RepoActivity, watchlist: Dict[str, Any]) -> Dict[str, List[str]]:
    full_name = normalize_full_name(activity.full_name)
    org = activity.org.lower()
    text = activity_text(activity)
    matches = {
        "repos": [],
        "orgs": [],
        "keywords": [],
        "products": [],
    }

    if full_name in watchlist.get("repos", set()):
        matches["repos"].append(activity.full_name)
    if org in watchlist.get("orgs", set()):
        matches["orgs"].append(activity.org)

    for keyword in sorted(watchlist.get("keywords", set())):
        if keyword and keyword in text:
            matches["keywords"].append(keyword)

    for product in watchlist.get("products", []):
        product_hit = full_name in product.get("repos", set())
        if not product_hit:
            product_hit = any(keyword in text for keyword in product.get("keywords", set()))
        if product_hit:
            matches["products"].append(product.get("name", ""))

    return {key: values for key, values in matches.items() if values}


def score_activity(
    activity: RepoActivity,
    releases: List[ReleaseInfo],
    watchlist: Dict[str, Any],
) -> Dict[str, Any]:
    text = activity_text(activity)
    matches = watchlist_matches(activity, watchlist)
    bot_commits = sum(1 for commit in activity.commits if is_bot_author(commit.author))
    human_commits = max(0, len(activity.commits) - bot_commits)
    bot_only = bool(activity.commits) and human_commits == 0
    dependency_only = bot_only and all(
        is_dependency_text(" ".join([commit.headline, commit.pr_title or "", commit.author]))
        for commit in activity.commits
    )

    tags: Set[str] = set()
    score = min(activity.commit_count, 25)

    if human_commits:
        score += 35
        tags.add("human-authored")
    if bot_only:
        score -= 15
        tags.add("bot-only")
    if dependency_only:
        score -= 10
        tags.add("dependency-noise")
    if releases:
        score += 40
        tags.add("release")
    if is_release_text(text):
        score += 10
        tags.add("release-language")
    if is_security_text(text):
        score += 25
        tags.add("security")
    if matches:
        score += 35
        tags.add("watchlist")
    if activity.category in ("docs", "reference", "training", "samples"):
        score += 5
        tags.add(activity.category)

    if matches.get("products"):
        tags.update(f"product:{name}" for name in matches["products"])

    score = max(0, score)
    return {
        "score": score,
        "tags": sorted(tags),
        "bot_commit_count": bot_commits,
        "human_commit_count": human_commits,
        "watchlist_matches": matches,
    }


def response_has_next(headers: Mapping[str, str]) -> bool:
    return 'rel="next"' in (headers.get("Link") or headers.get("link") or "")


def extract_event_repo_names(events: Any) -> Set[str]:
    names: Set[str] = set()
    if not isinstance(events, list):
        return names

    for event in events:
        if not isinstance(event, dict):
            continue
        repo = event.get("repo") or {}
        full_name = str(repo.get("name") or "").strip()
        if "/" in full_name:
            names.add(full_name)

    return names


def fetch_event_candidates(
    client: GitHubClient,
    orgs: List[str],
    state: Dict[str, Any],
    max_pages_per_org: int,
) -> Tuple[Set[str], Dict[str, Any]]:
    cache = state.get("events_request_cache")
    if not isinstance(cache, dict):
        cache = {}
        state["events_request_cache"] = cache

    candidates: Set[str] = set()
    org_summaries: List[Dict[str, Any]] = []
    pages_checked = 0
    pages_changed = 0
    pages_not_modified = 0

    for org in orgs:
        org_candidates: Set[str] = set()
        org_pages_checked = 0
        org_pages_changed = 0
        org_pages_not_modified = 0
        poll_interval = ""

        for page in range(1, max(1, max_pages_per_org) + 1):
            response = client.get_json(
                f"/orgs/{org}/events",
                params={"per_page": 100, "page": page},
                cache=cache,
                use_conditional=True,
            )
            pages_checked += 1
            org_pages_checked += 1

            poll_interval = (
                response.headers.get("x-poll-interval")
                or response.headers.get("X-Poll-Interval")
                or poll_interval
            )

            if response.not_modified:
                pages_not_modified += 1
                org_pages_not_modified += 1
                entry = cache.get(response.url, {}) or {}
                cached_names = {
                    str(name)
                    for name in (entry.get("repo_full_names") or [])
                    if isinstance(name, str)
                }
                org_candidates.update(cached_names)
                break

            events = response.data if isinstance(response.data, list) else []
            page_candidates = extract_event_repo_names(events)
            org_candidates.update(page_candidates)
            pages_changed += 1
            org_pages_changed += 1
            has_next = response_has_next(response.headers)
            update_conditional_cache(
                cache,
                response,
                item_count=len(events),
                repo_full_names=sorted(page_candidates),
                has_next=has_next,
            )

            if not has_next or not events:
                break

        candidates.update(org_candidates)
        org_summaries.append(
            {
                "org": org,
                "candidate_repos": len(org_candidates),
                "pages_checked": org_pages_checked,
                "pages_changed": org_pages_changed,
                "pages_not_modified": org_pages_not_modified,
                "poll_interval_seconds": poll_interval,
            }
        )

    summary = {
        "enabled": True,
        "orgs_checked": len(orgs),
        "candidate_repos": len(candidates),
        "max_pages_per_org": max_pages_per_org,
        "pages_checked": pages_checked,
        "pages_changed": pages_changed,
        "pages_not_modified": pages_not_modified,
        "orgs": org_summaries,
    }
    state["last_events_prefilter"] = {
        **summary,
        "completed_at": iso_utc(),
    }
    return candidates, summary


def apply_events_prefilter(
    mode: str,
    filtered: List[RepoInput],
    pushed_candidates: List[RepoInput],
    event_candidate_names: Set[str],
) -> List[RepoInput]:
    if mode == "off":
        return pushed_candidates

    filtered_by_name = {repo.full_name: repo for repo in filtered}
    pushed_names = {repo.full_name for repo in pushed_candidates}
    event_names = event_candidate_names & set(filtered_by_name)

    if mode == "union":
        selected_names = pushed_names | event_names
    elif mode == "intersect":
        if not event_names:
            sys.stderr.write(
                "[WARN] Events prefilter produced no repository candidates; "
                "keeping pushed_at candidates.\n"
            )
            selected_names = pushed_names
        else:
            selected_names = pushed_names & event_names
    else:
        raise RuntimeError(f"Unsupported events prefilter mode: {mode}")

    return [repo for repo in filtered if repo.full_name in selected_names]


def build_events_calibration(
    filtered: List[RepoInput],
    pushed_candidates: List[RepoInput],
    event_candidate_names: Set[str],
    events_summary: Dict[str, Any],
    sample_limit: int = 25,
) -> Dict[str, Any]:
    scope_names = {repo.full_name for repo in filtered}
    pushed_names = {repo.full_name for repo in pushed_candidates}
    event_names = event_candidate_names & scope_names
    events_outside_scope = event_candidate_names - scope_names
    intersection = pushed_names & event_names
    pushed_only = pushed_names - event_names
    events_only = event_names - pushed_names

    pushed_count = len(pushed_names)
    intersection_count = len(intersection)
    intersect_savings = pushed_count - intersection_count if event_names else 0
    intersect_risk_count = len(pushed_only) if event_names else 0

    return {
        "enabled": True,
        "pushed_at_candidates": pushed_count,
        "event_candidates_in_inventory": len(event_names),
        "event_candidates_in_scope": len(event_names),
        "event_candidates_not_in_inventory": len(events_outside_scope),
        "event_candidates_outside_scope": len(events_outside_scope),
        "intersection_candidates": intersection_count,
        "union_candidates": len(pushed_names | event_names),
        "pushed_only_candidates": len(pushed_only),
        "events_only_candidates": len(events_only),
        "intersect_candidate_savings": intersect_savings,
        "intersect_potential_miss_count": intersect_risk_count,
        "intersect_potential_miss_ratio": (
            round(intersect_risk_count / pushed_count, 4) if pushed_count else 0
        ),
        "samples": {
            "pushed_only": sorted(pushed_only)[:sample_limit],
            "events_only": sorted(events_only)[:sample_limit],
            "events_not_in_inventory": sorted(events_outside_scope)[:sample_limit],
            "events_outside_scope": sorted(events_outside_scope)[:sample_limit],
        },
        "events_summary": events_summary,
    }


def release_from_api(repo_full_name: str, raw: Dict[str, Any]) -> ReleaseInfo:
    return ReleaseInfo(
        repo_full_name=repo_full_name,
        tag_name=str(raw.get("tag_name") or "").strip(),
        name=str(raw.get("name") or "").strip(),
        published_at=str(raw.get("published_at") or "").strip(),
        html_url=str(raw.get("html_url") or "").strip(),
        prerelease=bool(raw.get("prerelease")),
        draft=bool(raw.get("draft")),
    )


def release_to_dict(release: ReleaseInfo) -> Dict[str, Any]:
    return {
        "repo_full_name": release.repo_full_name,
        "tag_name": release.tag_name,
        "name": release.name,
        "published_at": release.published_at,
        "html_url": release.html_url,
        "prerelease": release.prerelease,
        "draft": release.draft,
    }


def release_cache_payload(releases: List[ReleaseInfo]) -> List[Dict[str, Any]]:
    return [release_to_dict(release) for release in releases]


def releases_from_cache(items: Any) -> List[ReleaseInfo]:
    releases: List[ReleaseInfo] = []
    if not isinstance(items, list):
        return releases
    for item in items:
        if not isinstance(item, dict):
            continue
        releases.append(
            ReleaseInfo(
                repo_full_name=str(item.get("repo_full_name") or ""),
                tag_name=str(item.get("tag_name") or ""),
                name=str(item.get("name") or ""),
                published_at=str(item.get("published_at") or ""),
                html_url=str(item.get("html_url") or ""),
                prerelease=bool(item.get("prerelease")),
                draft=bool(item.get("draft")),
            )
        )
    return releases


def filter_recent_releases(releases: List[ReleaseInfo], since_dt: dt.datetime) -> List[ReleaseInfo]:
    recent: List[ReleaseInfo] = []
    for release in releases:
        if release.draft:
            continue
        published_at = parse_iso(release.published_at)
        if published_at is None or published_at >= since_dt:
            recent.append(release)
    recent.sort(key=lambda item: item.published_at, reverse=True)
    return recent


def select_release_repos(
    mode: str,
    filtered: List[RepoInput],
    candidates: List[RepoInput],
    watchlist: Dict[str, Any],
    max_repos: int,
) -> List[RepoInput]:
    if mode == "off" or max_repos <= 0:
        return []

    selected: Dict[str, RepoInput] = {}
    if mode in ("candidates", "candidates-and-watched"):
        selected.update({repo.full_name: repo for repo in candidates})

    if mode in ("watched", "candidates-and-watched"):
        watched_repos = watchlist.get("repos", set())
        watched_orgs = watchlist.get("orgs", set())
        for repo in filtered:
            if (
                normalize_full_name(repo.full_name) in watched_repos
                or repo.org.lower() in watched_orgs
            ):
                selected.setdefault(repo.full_name, repo)

    return list(selected.values())[:max_repos]


def fetch_recent_releases(
    client: GitHubClient,
    repos: List[RepoInput],
    since_dt: dt.datetime,
    state: Dict[str, Any],
    max_releases_per_repo: int,
) -> Tuple[Dict[str, List[ReleaseInfo]], Dict[str, Any]]:
    cache = state.get("release_request_cache")
    if not isinstance(cache, dict):
        cache = {}
        state["release_request_cache"] = cache

    releases_by_repo: Dict[str, List[ReleaseInfo]] = {}
    requests_checked = 0
    requests_changed = 0
    requests_not_modified = 0
    errors: List[Dict[str, str]] = []

    for repo in repos:
        owner, name = repo.full_name.split("/", 1)
        try:
            response = client.get_json(
                f"/repos/{owner}/{name}/releases",
                params={"per_page": max(1, max_releases_per_repo)},
                cache=cache,
                use_conditional=True,
            )
        except RateLimitDeferred:
            raise
        except Exception as exc:
            errors.append({"repo": repo.full_name, "error": str(exc)[:200]})
            sys.stderr.write(f"[WARN] Skipping release scan for {repo.full_name}: {exc}\n")
            continue
        requests_checked += 1

        if response.not_modified:
            requests_not_modified += 1
            cached = releases_from_cache((cache.get(response.url, {}) or {}).get("releases"))
            recent = filter_recent_releases(cached, since_dt)
            if recent:
                releases_by_repo[repo.full_name] = recent
            continue

        raw_releases = response.data if isinstance(response.data, list) else []
        releases = [
            release_from_api(repo.full_name, item)
            for item in raw_releases
            if isinstance(item, dict)
        ]
        recent = filter_recent_releases(releases, since_dt)
        if recent:
            releases_by_repo[repo.full_name] = recent

        entry = dict(cache.get(response.url, {}) or {})
        update_conditional_cache(
            cache,
            response,
            item_count=len(releases),
            has_next=response_has_next(response.headers),
        )
        entry = dict(cache.get(response.url, {}) or entry)
        entry["releases"] = release_cache_payload(releases)
        entry["cached_at"] = iso_utc()
        cache[response.url] = entry
        requests_changed += 1

    summary = {
        "enabled": True,
        "repos_checked": len(repos),
        "repos_with_releases": len(releases_by_repo),
        "requests_checked": requests_checked,
        "requests_changed": requests_changed,
        "requests_not_modified": requests_not_modified,
        "max_releases_per_repo": max_releases_per_repo,
        "error_count": len(errors),
        "errors": errors[:20],
    }
    state["last_release_scan"] = {
        **summary,
        "completed_at": iso_utc(),
    }
    return releases_by_repo, summary


def build_count_query(repos: List[RepoInput]) -> str:
    parts = ["query($since: GitTimestamp!) {"]
    for idx, repo in enumerate(repos):
        owner, name = repo.full_name.split("/", 1)
        alias = f"r{idx}"
        parts.append(
            f'''
  {alias}: repository(owner: "{owner}", name: "{name}") {{
    nameWithOwner
    isArchived
    isFork
    defaultBranchRef {{
      name
      target {{
        ... on Commit {{
          history(first: 1, since: $since) {{
            totalCount
          }}
        }}
      }}
    }}
  }}
'''
        )
    parts.append("}")
    return "\n".join(parts)


def build_detail_query(repos: List[RepoInput]) -> str:
    parts = ["query($since: GitTimestamp!, $maxCommits: Int!) {"]
    for idx, repo in enumerate(repos):
        owner, name = repo.full_name.split("/", 1)
        alias = f"r{idx}"
        parts.append(
            f'''
  {alias}: repository(owner: "{owner}", name: "{name}") {{
    nameWithOwner
    isArchived
    isFork
    defaultBranchRef {{
      name
      target {{
        ... on Commit {{
          history(first: $maxCommits, since: $since) {{
            totalCount
            nodes {{
              oid
              committedDate
              messageHeadline
              url
              author {{
                name
                user {{ login }}
              }}
              associatedPullRequests(first: 1) {{
                nodes {{
                  number
                  title
                  url
                }}
              }}
            }}
          }}
        }}
      }}
    }}
  }}
'''
        )
    parts.append("}")
    return "\n".join(parts)


def build_query(repos: List[RepoInput]) -> str:
    return build_detail_query(repos)


def gql_request(
    client: GitHubClient,
    query: str,
    variables: Dict[str, Any],
) -> Dict[str, Any]:
    payload = client.graphql(query, variables)
    errors = payload.get("errors") or []
    if errors:
        first = errors[0] or {}
        message = str(first.get("message") or "GraphQL error")
        if "rate limit" in message.lower():
            raise RateLimitDeferred(message)
        sys.stderr.write(f"[WARN] GraphQL returned errors: {message}\n")
    return payload.get("data") or {}


def summarize_author(author_obj: Dict[str, Any]) -> str:
    name = (author_obj.get("name") or "").strip()
    user = author_obj.get("user") or {}
    login = (user.get("login") or "").strip()
    if name and login:
        return f"{name} (@{login})"
    if login:
        return f"@{login}"
    return name or ""


def resolve_graphql_batch_size(
    requested: int,
    repo_count: int,
    max_commits: int,
    remaining: Optional[int],
) -> Tuple[int, Dict[str, Any]]:
    if requested > 0:
        return requested, {
            "strategy": "manual",
            "requested_batch_size": requested,
            "remaining_at_start": remaining,
        }

    batch_size = 35
    strategy = "balanced"
    if max_commits <= 3 and repo_count <= 100:
        batch_size = 45
        strategy = "small-window"
    if repo_count > 500 or max_commits > 5:
        batch_size = 20
        strategy = "large-window"
    if remaining is not None and remaining < 500:
        batch_size = min(batch_size, 15)
        strategy = "low-budget"
    if remaining is not None and remaining < 200:
        batch_size = min(batch_size, 8)
        strategy = "very-low-budget"

    return max(1, batch_size), {
        "strategy": strategy,
        "requested_batch_size": requested,
        "remaining_at_start": remaining,
    }


def parse_repo_count(
    repo: RepoInput,
    node: Dict[str, Any],
    include_archived: bool,
    include_forks: bool,
) -> Optional[RepoCount]:
    if not node:
        return None
    if (not include_archived and node.get("isArchived") is True) or (
        not include_forks and node.get("isFork") is True
    ):
        return None

    default_branch = node.get("defaultBranchRef") or {}
    branch_name = (default_branch.get("name") or "").strip()
    target = default_branch.get("target") or {}
    history = target.get("history") or {}
    total = int(history.get("totalCount") or 0)
    if total <= 0:
        return None
    return RepoCount(repo=repo, default_branch=branch_name, commit_count=total)


def fetch_changed_repo_counts(
    client: GitHubClient,
    repos: List[RepoInput],
    since_iso: str,
    include_archived: bool,
    include_forks: bool,
    batch_size: int,
) -> Tuple[List[RepoCount], Dict[str, Any]]:
    changed: List[RepoCount] = []
    batches = 0
    for batch in chunked(repos, batch_size):
        batches += 1
        data = gql_request(client, build_count_query(batch), {"since": since_iso})
        for idx, repo in enumerate(batch):
            repo_count = parse_repo_count(
                repo=repo,
                node=data.get(f"r{idx}") or {},
                include_archived=include_archived,
                include_forks=include_forks,
            )
            if repo_count:
                changed.append(repo_count)

    return changed, {
        "count_batches": batches,
        "repos_counted": len(repos),
        "repos_with_count": len(changed),
    }


def fetch_activity(
    client: GitHubClient,
    repos: List[RepoInput],
    since_iso: str,
    max_commits: int,
    include_archived: bool,
    include_forks: bool,
    batch_size: int,
    enrichment_mode: str,
) -> Tuple[List[RepoActivity], Dict[str, Any]]:
    activities: List[RepoActivity] = []
    telemetry: Dict[str, Any] = {
        "mode": enrichment_mode,
        "batch_size": batch_size,
        "candidate_repos": len(repos),
        "max_commits": max_commits,
        "count_batches": 0,
        "detail_batches": 0,
        "repos_counted": 0,
        "repos_enriched": 0,
    }

    detail_repos = repos
    count_by_repo: Dict[str, RepoCount] = {}
    if enrichment_mode == "two-stage":
        counts, count_telemetry = fetch_changed_repo_counts(
            client=client,
            repos=repos,
            since_iso=since_iso,
            include_archived=include_archived,
            include_forks=include_forks,
            batch_size=batch_size,
        )
        telemetry.update(count_telemetry)
        count_by_repo = {item.repo.full_name: item for item in counts}
        detail_repos = [item.repo for item in counts]
    elif enrichment_mode != "one-stage":
        raise RuntimeError(f"Unsupported enrichment mode: {enrichment_mode}")

    for batch in chunked(detail_repos, batch_size):
        telemetry["detail_batches"] += 1
        query = build_detail_query(batch)
        data = gql_request(client, query, {"since": since_iso, "maxCommits": max_commits})

        for idx, repo in enumerate(batch):
            node = data.get(f"r{idx}")
            if not node:
                continue

            if (not include_archived and node.get("isArchived") is True) or (
                not include_forks and node.get("isFork") is True
            ):
                continue

            default_branch = node.get("defaultBranchRef") or {}
            branch_name = (default_branch.get("name") or "").strip()
            target = default_branch.get("target") or {}
            history = target.get("history") or {}
            total = int(history.get("totalCount") or 0)
            if total <= 0:
                continue

            commits: List[CommitInfo] = []
            newest_date = ""
            for commit in history.get("nodes") or []:
                prs = ((commit.get("associatedPullRequests") or {}).get("nodes") or [])
                pr = prs[0] if prs else None
                committed_date = commit.get("committedDate") or ""
                if committed_date and (not newest_date or committed_date > newest_date):
                    newest_date = committed_date

                commits.append(
                    CommitInfo(
                        oid=commit.get("oid") or "",
                        committed_date=committed_date,
                        headline=(commit.get("messageHeadline") or "").strip(),
                        url=commit.get("url") or "",
                        author=summarize_author(commit.get("author") or {}),
                        pr_number=(pr.get("number") if pr else None),
                        pr_title=((pr.get("title") or "").strip() if pr else None),
                        pr_url=(pr.get("url") if pr else None),
                    )
                )

            activities.append(
                RepoActivity(
                    full_name=node.get("nameWithOwner") or repo.full_name,
                    org=repo.org,
                    name=repo.name,
                    category=repo.category,
                    default_branch=branch_name,
                    commit_count=total,
                    newest_commit_date=newest_date,
                    commits=commits,
                    repo_type=repo.repo_type,
                    product_area=repo.product_area,
                    audience=repo.audience,
                    classification_confidence=repo.classification_confidence,
                    classification_reason=repo.classification_reason,
                    classification_version=repo.classification_version,
                )
            )

    activities.sort(key=lambda activity: (activity.commit_count, activity.newest_commit_date), reverse=True)
    telemetry["repos_enriched"] = len(detail_repos)
    telemetry["repos_with_movement"] = len(activities)
    if count_by_repo:
        telemetry["stage_one_total_commits"] = sum(item.commit_count for item in count_by_repo.values())
    return activities, telemetry


def write_csv(
    path: str,
    activities: List[RepoActivity],
    max_commits: int,
    since_iso: str,
    until_iso: str,
    hours_requested: int,
    state_window_enabled: bool,
    signals_by_repo: Optional[Dict[str, Dict[str, Any]]] = None,
    releases_by_repo: Optional[Dict[str, List[ReleaseInfo]]] = None,
) -> None:
    signals_by_repo = signals_by_repo or {}
    releases_by_repo = releases_by_repo or {}
    fields = [
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
        "signal_score",
        "signal_tags",
        "release_count",
    ]
    for idx in range(1, max_commits + 1):
        fields += [
            f"commit{idx}_date",
            f"commit{idx}_headline",
            f"commit{idx}_url",
            f"commit{idx}_author",
            f"commit{idx}_pr_number",
            f"commit{idx}_pr_title",
            f"commit{idx}_pr_url",
        ]

    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for activity in activities:
            row: Dict[str, Any] = {
                "full_name": activity.full_name,
                "org": activity.org,
                "name": activity.name,
                "category": activity.category,
                "repo_type": activity.repo_type,
                "product_area": activity.product_area,
                "audience": activity.audience,
                "default_branch": activity.default_branch,
                "commit_count_24h": activity.commit_count,
                "commit_count_window": activity.commit_count,
                "window_since": since_iso,
                "window_until": until_iso,
                "hours_requested": hours_requested,
                "state_window_enabled": state_window_enabled,
                "newest_commit_date": activity.newest_commit_date,
                "signal_score": (signals_by_repo.get(activity.full_name) or {}).get("score", ""),
                "signal_tags": ";".join((signals_by_repo.get(activity.full_name) or {}).get("tags", [])),
                "release_count": len(releases_by_repo.get(activity.full_name, [])),
            }
            for idx in range(max_commits):
                if idx < len(activity.commits):
                    commit = activity.commits[idx]
                    row.update(
                        {
                            f"commit{idx+1}_date": commit.committed_date,
                            f"commit{idx+1}_headline": commit.headline,
                            f"commit{idx+1}_url": commit.url,
                            f"commit{idx+1}_author": commit.author,
                            f"commit{idx+1}_pr_number": commit.pr_number or "",
                            f"commit{idx+1}_pr_title": commit.pr_title or "",
                            f"commit{idx+1}_pr_url": commit.pr_url or "",
                        }
                    )
                else:
                    row.update(
                        {
                            f"commit{idx+1}_date": "",
                            f"commit{idx+1}_headline": "",
                            f"commit{idx+1}_url": "",
                            f"commit{idx+1}_author": "",
                            f"commit{idx+1}_pr_number": "",
                            f"commit{idx+1}_pr_title": "",
                            f"commit{idx+1}_pr_url": "",
                        }
                    )
            writer.writerow(row)


def write_md(path: str, activities: List[RepoActivity], since_iso: str) -> None:
    grouped: Dict[str, Dict[str, List[RepoActivity]]] = {}
    for activity in activities:
        category = activity.category.strip() or "uncategorized"
        org = activity.org or activity.full_name.split("/")[0]
        grouped.setdefault(category, {})
        grouped[category].setdefault(org, [])
        grouped[category][org].append(activity)

    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# Changes on default branch since {since_iso}\n\n")
        f.write(f"Repos with movement: **{len(activities)}**\n\n")

        for category in sorted(grouped.keys()):
            f.write(f"## {category}\n\n")
            for org in sorted(grouped[category].keys()):
                f.write(f"### {org}\n\n")
                org_items = sorted(
                    grouped[category][org],
                    key=lambda activity: (activity.commit_count, activity.newest_commit_date),
                    reverse=True,
                )
                for activity in org_items:
                    f.write(
                        f"- **{activity.full_name}** (`{activity.default_branch}`) - "
                        f"**{activity.commit_count}** commit(s)\n"
                    )
                    for commit in activity.commits:
                        headline = commit.headline or commit.oid[:12] or "Commit"
                        pr_part = ""
                        if commit.pr_url and commit.pr_title:
                            pr_part = f" - PR: [{commit.pr_title} #{commit.pr_number}]({commit.pr_url})"
                        author_part = f" - {commit.author}" if commit.author else ""
                        f.write(
                            f"  - [{headline}]({commit.url}) - "
                            f"{commit.committed_date}{author_part}{pr_part}\n"
                        )
                    f.write("\n")


def commit_to_dict(commit: CommitInfo) -> Dict[str, Any]:
    return {
        "oid": commit.oid,
        "committed_date": commit.committed_date,
        "headline": commit.headline,
        "url": commit.url,
        "author": commit.author,
        "pr_number": commit.pr_number,
        "pr_title": commit.pr_title,
        "pr_url": commit.pr_url,
    }


def activity_to_dict(
    activity: RepoActivity,
    signal: Optional[Dict[str, Any]] = None,
    releases: Optional[List[ReleaseInfo]] = None,
) -> Dict[str, Any]:
    return {
        "full_name": activity.full_name,
        "org": activity.org,
        "name": activity.name,
        "category": activity.category,
        "repo_type": activity.repo_type,
        "product_area": activity.product_area,
        "audience": activity.audience,
        "classification_confidence": activity.classification_confidence,
        "classification_reason": activity.classification_reason,
        "classification_version": activity.classification_version,
        "default_branch": activity.default_branch,
        "commit_count": activity.commit_count,
        "newest_commit_date": activity.newest_commit_date,
        "commits": [commit_to_dict(commit) for commit in activity.commits],
        "signal": signal or {},
        "releases": [release_to_dict(release) for release in (releases or [])],
    }


def recent_repo_creations(repos: List[RepoInput], since_dt: dt.datetime, limit: int = 50) -> List[Dict[str, Any]]:
    created: List[RepoInput] = []
    for repo in repos:
        created_at = parse_iso(repo.created_at)
        if created_at and created_at >= since_dt:
            created.append(repo)
    created.sort(key=lambda repo: repo.created_at, reverse=True)
    return [
        {
            "full_name": repo.full_name,
            "org": repo.org,
            "name": repo.name,
            "category": repo.category,
            "repo_type": repo.repo_type,
            "product_area": repo.product_area,
            "audience": repo.audience,
            "created_at": repo.created_at,
            "html_url": repo.html_url or f"https://github.com/{repo.full_name}",
        }
        for repo in created[:limit]
    ]


def build_signal_summary(signals_by_repo: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    tag_counts: Counter[str] = Counter()
    high_signal = []
    bot_noise = []
    watched = []
    for full_name, signal in signals_by_repo.items():
        tags = set(signal.get("tags") or [])
        tag_counts.update(tags)
        item = {
            "full_name": full_name,
            "score": signal.get("score", 0),
            "tags": sorted(tags),
            "watchlist_matches": signal.get("watchlist_matches", {}),
        }
        if int(signal.get("score") or 0) >= 50 and "dependency-noise" not in tags:
            high_signal.append(item)
        if "dependency-noise" in tags or "bot-only" in tags:
            bot_noise.append(item)
        if "watchlist" in tags:
            watched.append(item)

    high_signal.sort(key=lambda item: (item["score"], item["full_name"]), reverse=True)
    watched.sort(key=lambda item: (item["score"], item["full_name"]), reverse=True)
    bot_noise.sort(key=lambda item: (item["score"], item["full_name"]), reverse=True)

    return {
        "tag_counts": dict(sorted(tag_counts.items())),
        "high_signal": high_signal[:25],
        "watched": watched[:25],
        "bot_or_dependency_noise": bot_noise[:25],
    }


def build_watchlist_summary(watchlist: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "repo_count": len(watchlist.get("repos", set())),
        "org_count": len(watchlist.get("orgs", set())),
        "keyword_count": len(watchlist.get("keywords", set())),
        "products": [product.get("name", "") for product in watchlist.get("products", [])],
    }


def lifecycle_for_report(state: Dict[str, Any], since_dt: dt.datetime) -> Dict[str, Any]:
    lifecycle = state.get("last_inventory_lifecycle") or {}
    completed_at = parse_iso(str(lifecycle.get("completed_at") or ""))
    if completed_at is not None and completed_at < since_dt:
        return {
            "available": False,
            "reason": "latest inventory lifecycle snapshot predates the report window",
            "completed_at": lifecycle.get("completed_at", ""),
        }
    return lifecycle if isinstance(lifecycle, dict) else {}


def build_report_payload(
    *,
    activities: List[RepoActivity],
    filtered_repos: List[RepoInput],
    inventory_repo_count: int,
    filtered_repo_count: int,
    pushed_candidate_count: int,
    candidate_repo_count: int,
    since_iso: str,
    since_dt: dt.datetime,
    generated_at: dt.datetime,
    until_iso: str,
    hours_requested: int,
    selected_categories: Optional[Set[str]],
    include_other: bool,
    include_archived: bool,
    include_forks: bool,
    use_state_window: bool,
    events_prefilter_mode: str,
    events_summary: Optional[Dict[str, Any]],
    events_calibration: Optional[Dict[str, Any]],
    releases_by_repo: Optional[Dict[str, List[ReleaseInfo]]],
    release_summary: Optional[Dict[str, Any]],
    signals_by_repo: Optional[Dict[str, Dict[str, Any]]],
    watchlist_summary: Optional[Dict[str, Any]],
    lifecycle_summary: Optional[Dict[str, Any]],
    graphql_telemetry: Optional[Dict[str, Any]],
) -> Dict[str, Any]:
    category_counts = Counter(activity.category or "uncategorized" for activity in activities)
    org_counts = Counter(activity.org or activity.full_name.split("/")[0] for activity in activities)
    total_commits = sum(activity.commit_count for activity in activities)
    releases_by_repo = releases_by_repo or {}
    signals_by_repo = signals_by_repo or {}
    signal_summary = build_signal_summary(signals_by_repo)

    return {
        "schema_version": 1,
        "artifact_type": "tracker-report",
        "artifact_version": ARTIFACT_VERSION,
        "schema_url": REPORT_SCHEMA_URL,
        "generated_at": iso_utc(generated_at),
        "source": source_metadata(),
        "window": {
            "since": since_iso,
            "until": until_iso,
            "hours_requested": hours_requested,
            "state_window_enabled": use_state_window,
        },
        "filters": {
            "categories": "all" if selected_categories is None else sorted(selected_categories),
            "include_other": include_other,
            "include_archived": include_archived,
            "include_forks": include_forks,
            "events_prefilter_mode": events_prefilter_mode,
        },
        "totals": {
            "inventory_repos": inventory_repo_count,
            "filtered_repos": filtered_repo_count,
            "pushed_at_candidate_repos": pushed_candidate_count,
            "candidate_repos": candidate_repo_count,
            "repos_with_movement": len(activities),
            "default_branch_commits": total_commits,
            "repos_with_releases": len(releases_by_repo),
            "release_count": sum(len(items) for items in releases_by_repo.values()),
        },
        "summaries": {
            "by_category": dict(sorted(category_counts.items())),
            "by_org": dict(sorted(org_counts.items())),
            "signals": signal_summary,
        },
        "watchlist": watchlist_summary or {},
        "top_repos": [
            activity_to_dict(
                activity,
                signals_by_repo.get(activity.full_name),
                releases_by_repo.get(activity.full_name, []),
            )
            for activity in sorted(
                activities,
                key=lambda item: (
                    (signals_by_repo.get(item.full_name) or {}).get("score", 0),
                    item.commit_count,
                    item.newest_commit_date,
                ),
                reverse=True,
            )[:20]
        ],
        "activities": [
            activity_to_dict(
                activity,
                signals_by_repo.get(activity.full_name),
                releases_by_repo.get(activity.full_name, []),
            )
            for activity in activities
        ],
        "releases": {
            "summary": release_summary
            or {
                "enabled": False,
            },
            "items": [
                release_to_dict(release)
                for releases in releases_by_repo.values()
                for release in releases
            ],
        },
        "lifecycle": lifecycle_summary or {},
        "recent_repo_creations": recent_repo_creations(filtered_repos, since_dt),
        "graphql": graphql_telemetry or {},
        "events_prefilter": events_summary
        or {
            "enabled": False,
            "mode": events_prefilter_mode,
        },
        "events_calibration": events_calibration or {},
    }


def md_escape(value: Any) -> str:
    return str(value if value is not None else "").replace("|", "\\|").replace("\n", " ")


def count_phrase(count: Any, singular: str, plural: Optional[str] = None) -> str:
    value = int(count or 0)
    label = singular if value == 1 else (plural or f"{singular}s")
    return f"{value} {label}"


def human_utc(value: Any) -> str:
    parsed = parse_iso(str(value or ""))
    if parsed is None:
        return str(value or "")
    return parsed.astimezone(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def effective_window_hours(window: Mapping[str, Any]) -> float:
    since = parse_iso(str(window.get("since") or ""))
    until = parse_iso(str(window.get("until") or ""))
    if since is None or until is None:
        return 0.0
    return max(0.0, round((until - since).total_seconds() / 3600, 1))


def friendly_change_type(value: Any) -> str:
    labels = {
        "security_fix": "Security",
        "release": "Release",
        "feature": "Feature",
        "bug_fix": "Fix",
        "docs_update": "Docs",
        "reference_update": "Reference",
        "training_update": "Training",
        "sample_update": "Sample",
        "dependency_update": "Dependency",
        "bulk_automation": "Automation",
        "sdk_generation": "SDK",
        "ci_infra": "CI/Infra",
        "unknown": "Other",
    }
    return labels.get(str(value or "unknown"), str(value or "Other").replace("_", " ").title())


def change_type_priority(value: Any) -> int:
    priorities = {
        "security_fix": 50,
        "release": 40,
        "feature": 30,
        "bug_fix": 25,
        "docs_update": 20,
        "reference_update": 20,
        "training_update": 20,
        "sample_update": 20,
        "ci_infra": 10,
        "sdk_generation": 5,
        "dependency_update": 0,
        "bulk_automation": 0,
    }
    return priorities.get(str(value or "unknown"), 10)


def event_repo(event: Mapping[str, Any]) -> str:
    return str(event.get("repo") or event.get("full_name") or "")


def event_url(event: Mapping[str, Any]) -> str:
    repo = event_repo(event)
    return str(
        event.get("url")
        or event.get("pr_url")
        or event.get("commit_url")
        or (f"https://github.com/{repo}" if repo else "")
    )


def event_headline(event: Mapping[str, Any]) -> str:
    return str(event.get("pr_title") or event.get("headline") or "Change")


def why_event_matters(event: Mapping[str, Any]) -> str:
    change_type = str(event.get("change_type") or "unknown")
    headline = event_headline(event)
    if change_type == "security_fix":
        return f"Security-related change: {headline}"
    if change_type == "release":
        return f"Release activity: {headline}"
    if change_type == "dependency_update":
        return f"Dependency maintenance: {headline}"
    if change_type == "bulk_automation":
        return f"Bulk automation: {headline}"
    if change_type == "sdk_generation":
        return f"SDK-generation signal: {headline}"
    if change_type == "feature":
        return f"Feature or capability signal: {headline}"
    if change_type == "bug_fix":
        return f"Fix signal: {headline}"
    if change_type.endswith("_update"):
        return f"{friendly_change_type(change_type)} update: {headline}"
    return headline


def event_change_key(event: Mapping[str, Any]) -> str:
    return str(
        event.get("url")
        or event.get("pr_url")
        or event.get("commit_url")
        or event.get("dedupe_key")
        or event.get("event_id")
        or ""
    )


def unique_by_change(events: List[Dict[str, Any]], limit: int) -> List[Dict[str, Any]]:
    seen: Set[str] = set()
    results: List[Dict[str, Any]] = []
    for event in events:
        key = event_change_key(event)
        if not key or key in seen:
            continue
        seen.add(key)
        results.append(event)
        if len(results) >= limit:
            break
    return results


def compact_event_link(event: Mapping[str, Any]) -> Dict[str, Any]:
    return {
        "repo": event_repo(event),
        "headline": event_headline(event),
        "url": event_url(event),
        "change_type": str(event.get("change_type") or "unknown"),
        "notability_score": int(event.get("notability_score") or 0),
        "committed_at": str(event.get("committed_at") or ""),
    }


def product_area_for_event(event: Mapping[str, Any]) -> str:
    value = str(event.get("product_area") or "").strip()
    return value if value and value.lower() != "unknown" else "Unmapped Activity"


def build_product_area_summary(records: List[Dict[str, Any]], payload: Mapping[str, Any], limit: int = 8) -> List[Dict[str, Any]]:
    release_repos = Counter(
        str(item.get("repo_full_name") or "")
        for item in ((payload.get("releases") or {}).get("items") or [])
        if isinstance(item, dict)
    )
    by_area: Dict[str, Dict[str, Any]] = {}
    for event in records:
        area = product_area_for_event(event)
        item = by_area.setdefault(
            area,
            {
                "product_area": area,
                "event_count": 0,
                "notable_event_count": 0,
                "release_count": 0,
                "security_event_count": 0,
                "noisy_event_count": 0,
                "repos": Counter(),
                "top_events": [],
            },
        )
        repo = event_repo(event)
        item["event_count"] += 1
        item["repos"][repo] += 1
        if int(event.get("notability_score") or 0) >= 70 and event.get("noise_level") != "high":
            item["notable_event_count"] += 1
            item["top_events"].append(event)
        if event.get("change_type") == "security_fix":
            item["security_event_count"] += 1
        if event.get("noise_level") in {"medium", "high"}:
            item["noisy_event_count"] += 1

    for item in by_area.values():
        item["release_count"] = sum(release_repos.get(repo, 0) for repo in item["repos"])
        item["repo_count"] = len([repo for repo in item["repos"] if repo])
        item["top_repos"] = [
            {"repo": repo, "event_count": count}
            for repo, count in item["repos"].most_common(5)
            if repo
        ]
        top_events = sorted(
            item["top_events"],
            key=lambda event: (
                int(event.get("notability_score") or 0),
                change_type_priority(event.get("change_type")),
                str(event.get("committed_at") or ""),
            ),
            reverse=True,
        )
        item["top_events"] = [compact_event_link(event) for event in unique_by_change(top_events, 3)]
        del item["repos"]

    summaries = list(by_area.values())
    summaries.sort(
        key=lambda item: (
            int(item.get("notable_event_count") or 0),
            int(item.get("release_count") or 0),
            int(item.get("security_event_count") or 0),
            int(item.get("event_count") or 0),
        ),
        reverse=True,
    )
    return summaries[:limit]


def build_top_links(notable_changes: List[Dict[str, Any]], limit: int = 8, per_repo_limit: int = 1) -> List[Dict[str, Any]]:
    selected: List[Dict[str, Any]] = []
    repo_counts: Counter[str] = Counter()
    for event in unique_by_change(notable_changes, len(notable_changes)):
        repo = event_repo(event)
        if repo_counts[repo] >= per_repo_limit:
            continue
        selected.append(event)
        repo_counts[repo] += 1
        if len(selected) >= limit:
            break
    if len(selected) < limit:
        selected_keys = {event_change_key(event) for event in selected}
        for event in unique_by_change(notable_changes, len(notable_changes)):
            key = event_change_key(event)
            if key in selected_keys:
                continue
            selected.append(event)
            selected_keys.add(key)
            if len(selected) >= limit:
                break

    links = []
    for idx, event in enumerate(selected[:limit], start=1):
        links.append(
            {
                "priority": idx,
                "repo": event_repo(event),
                "url": event_url(event),
                "why": why_event_matters(event),
            }
        )
    return links


def build_noise_summary(records: List[Dict[str, Any]]) -> Dict[str, Any]:
    noisy = [
        event
        for event in records
        if event.get("noise_level") in {"medium", "high"}
        or event.get("actor_type") in {"bot", "automation"}
        or event.get("change_type") in {"bulk_automation", "dependency_update"}
    ]
    repo_counter = Counter(event_repo(event) for event in noisy if event_repo(event))
    type_counter = Counter(str(event.get("change_type") or "unknown") for event in noisy)
    actor_counter = Counter(str(event.get("actor_type") or "unknown") for event in noisy)
    return {
        "event_count": len(noisy),
        "top_repos": [{"repo": repo, "event_count": count} for repo, count in repo_counter.most_common(5)],
        "change_types": dict(type_counter.most_common(8)),
        "actor_types": dict(actor_counter.most_common(5)),
    }


def build_plain_english_summary(payload: Mapping[str, Any]) -> List[str]:
    totals = payload.get("totals") or {}
    notable = payload.get("notable_changes") or []
    product_areas = payload.get("product_area_summary") or []
    noise = payload.get("noise_summary") or {}
    release_count = int(totals.get("release_count") or 0)
    repos_with_movement = int(totals.get("repos_with_movement") or 0)
    commit_count = int(totals.get("default_branch_commits") or 0)

    bullets: List[str] = []
    if product_areas:
        top = [
            item.get("product_area", "")
            for item in product_areas[:3]
            if item.get("product_area") and item.get("product_area") != "Unmapped Activity"
        ]
        if top:
            bullets.append(f"{', '.join(top)} led the visible product-area activity in this window.")
    if release_count:
        bullets.append(f"{release_count} release item(s) were detected during the window.")
    security_repos = []
    for event in notable:
        if event.get("change_type") == "security_fix":
            repo = event_repo(event)
            if repo and repo not in security_repos:
                security_repos.append(repo)
    if security_repos:
        bullets.append(f"Security-related changes appeared in {', '.join(security_repos[:3])}.")
    human_repos = []
    for event in notable:
        if event.get("actor_type") == "human":
            repo = event_repo(event)
            if repo and repo not in human_repos:
                human_repos.append(repo)
    if human_repos:
        bullets.append(f"Start with human-authored changes in {', '.join(human_repos[:4])}.")
    noisy_count = int(noise.get("event_count") or 0)
    if noisy_count:
        bullets.append(f"{noisy_count} event(s) look automated, bot-heavy, dependency, or generated; review the curated sections before raw volume.")
    if not bullets:
        bullets.append(f"{repos_with_movement} repo(s) moved with {commit_count} default-branch commit(s).")
    return bullets[:6]


def repo_markdown_link(repo: str) -> str:
    repo = str(repo or "")
    return f"[{md_escape(repo)}](https://github.com/{repo})" if repo else ""


def consumer_why(change_type: Any) -> str:
    change_type = str(change_type or "unknown")
    if change_type == "security_fix":
        return "Review for security, admin, or training impact; this may affect guidance consumers rely on."
    if change_type == "release":
        return "Check release notes or linked PRs if your team consumes this package, sample, SDK, or tool."
    if change_type == "feature":
        return "Scan for new capability or sample behavior that may be useful to builders."
    if change_type == "bug_fix":
        return "Review if you depend on this area; it may remove a known rough edge."
    if change_type in {"docs_update", "reference_update", "training_update", "sample_update"}:
        return "Review for guidance, learning, reference, or sample changes that may affect downstream readers."
    if change_type in {"dependency_update", "bulk_automation", "sdk_generation", "ci_infra"}:
        return "Likely operational or generated activity; keep visible but do not over-rank without context."
    return "Worth a quick scan because it ranked highly in the current signal model."


def audience_label(value: Any) -> str:
    labels = {
        "developer": "Developers",
        "admin": "Admins",
        "architect": "Architects",
        "learner": "Learners",
        "operator": "Operators",
        "unknown": "General MS consumers",
    }
    return labels.get(str(value or "unknown"), str(value or "General MS consumers").title())


def likely_audiences_for_area(area_name: str, payload: Mapping[str, Any], limit: int = 3) -> str:
    audiences: Counter[str] = Counter()
    normalized_area = str(area_name or "")
    for activity in payload.get("activities") or []:
        if not isinstance(activity, dict):
            continue
        activity_area = str(activity.get("product_area") or "")
        if normalized_area == "Unmapped Activity":
            if activity_area and activity_area.lower() != "unknown":
                continue
        elif activity_area != normalized_area:
            continue
        audiences[str(activity.get("audience") or "unknown")] += 1
    selected = [audience_label(name) for name, _ in audiences.most_common(limit) if name]
    return ", ".join(selected) if selected else "General MS consumers"


def area_reader_takeaway(area: Mapping[str, Any]) -> str:
    release_count = int(area.get("release_count") or 0)
    security_count = int(area.get("security_event_count") or 0)
    noisy_count = int(area.get("noisy_event_count") or 0)
    if security_count:
        return "Start with the security/admin-sensitive links, then scan releases."
    if release_count:
        return "Start with releases; consumers may need version or sample awareness."
    if noisy_count:
        return "Use the top links first; some of the movement is likely generated or operational."
    return "Scan top links for meaningful guidance or sample movement."


def brief_status_block(payload: Mapping[str, Any]) -> List[str]:
    generated_at = str(payload.get("generated_at") or "")
    window = payload.get("window") or {}
    totals = payload.get("totals") or {}
    freshness = freshness_payload(generated_at, parse_iso(generated_at) or dt.datetime.now(dt.timezone.utc))
    status_label = "Fresh" if not freshness.get("latest_report_stale") else "Stale"
    hours = effective_window_hours(window)
    return [
        f"> Status: {status_label} at generation. Current freshness is tracked in `reports/status.json`.",
        f"> Generated: {human_utc(generated_at)} - Window: {hours:g}h from {human_utc(window.get('since'))} to {human_utc(window.get('until'))}.",
        (
            f"> {totals.get('repos_with_movement', 0)} repo(s) moved - "
            f"{totals.get('default_branch_commits', 0)} commit(s) - "
            f"{totals.get('release_count', 0)} release item(s) - "
            f"{len((payload.get('summaries') or {}).get('signals', {}).get('high_signal') or [])} high-signal repo(s)."
        ),
    ]


def write_report_markdown(path: str, payload: Dict[str, Any]) -> None:
    totals = payload.get("totals") or {}
    summaries = payload.get("summaries") or {}
    window = payload.get("window") or {}
    filters = payload.get("filters") or {}
    events = payload.get("events_prefilter") or {}
    events_calibration = payload.get("events_calibration") or {}
    signal_summary = ((summaries.get("signals") or {}) if isinstance(summaries, dict) else {})
    releases = payload.get("releases") or {}
    release_items = releases.get("items") or []
    lifecycle = payload.get("lifecycle") or {}
    recent_creations = payload.get("recent_repo_creations") or []
    graphql = payload.get("graphql") or {}
    notable_changes = payload.get("notable_changes") or []
    product_area_summary = payload.get("product_area_summary") or []
    top_links = payload.get("top_links") or []
    noise_summary = payload.get("noise_summary") or {}
    top_repos = payload.get("top_repos") or []
    activities = payload.get("activities") or []

    generated_at = str(payload.get("generated_at") or "")
    title_date = generated_at[:10] if len(generated_at) >= 10 else generated_at

    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# Microsoft Ecosystem Daily Brief - {title_date}\n\n")
        for line in brief_status_block(payload):
            f.write(f"{line}\n")
        f.write("\n")

        f.write("## Plain-English Summary\n\n")
        for bullet in build_plain_english_summary(payload):
            f.write(f"- {md_escape(bullet)}\n")
        f.write("\n")

        f.write("## Headline Metrics\n\n")
        f.write("| Metric | Value |\n")
        f.write("| --- | ---: |\n")
        f.write(f"| Inventory repositories | {totals.get('inventory_repos', 0)} |\n")
        f.write(f"| Repositories after filters | {totals.get('filtered_repos', 0)} |\n")
        f.write(f"| `pushed_at` candidates | {totals.get('pushed_at_candidate_repos', 0)} |\n")
        f.write(f"| Enrichment candidates | {totals.get('candidate_repos', 0)} |\n")
        f.write(f"| Repositories with movement | {totals.get('repos_with_movement', 0)} |\n")
        f.write(f"| Default-branch commits | {totals.get('default_branch_commits', 0)} |\n")
        f.write("\n")

        if notable_changes:
            f.write("## What Changed That Matters\n\n")
            f.write("| Repository | Score | Change | Actor | Noise | Headline | Time |\n")
            f.write("| --- | ---: | --- | --- | --- | --- | --- |\n")
            for event in notable_changes[:15]:
                repo = md_escape(event.get("repo", ""))
                repo_url = f"https://github.com/{event.get('repo', '')}"
                url = event.get("pr_url") or event.get("commit_url") or repo_url
                headline = md_escape(event.get("pr_title") or event.get("headline") or "Change")
                f.write(
                    f"| [{repo}]({repo_url}) | "
                    f"{event.get('notability_score', 0)} | "
                    f"{md_escape(event.get('change_type', 'unknown'))} | "
                    f"{md_escape(event.get('actor_type', 'unknown'))} | "
                    f"{md_escape(event.get('noise_level', 'unknown'))} | "
                    f"[{headline}]({url}) | "
                    f"`{event.get('committed_at', '')}` |\n"
                )
            f.write("\n")

        if product_area_summary:
            f.write("## Product Areas\n\n")
            f.write("| Product area | Signal | Repos | Events | Releases | Security | Top links |\n")
            f.write("| --- | ---: | ---: | ---: | ---: | ---: | --- |\n")
            for area in product_area_summary[:8]:
                top_event_links = []
                for event in area.get("top_events") or []:
                    headline = md_escape(event_headline(event))
                    url = event_url(event)
                    if headline and url:
                        top_event_links.append(f"[{headline}]({url})")
                f.write(
                    f"| {md_escape(area.get('product_area', ''))} | "
                    f"{area.get('notable_event_count', 0)} | "
                    f"{area.get('repo_count', 0)} | "
                    f"{area.get('event_count', 0)} | "
                    f"{area.get('release_count', 0)} | "
                    f"{area.get('security_event_count', 0)} | "
                    f"{md_escape('; '.join(top_event_links))} |\n"
                )
            f.write("\n")

        if top_links:
            f.write("## Today's Top Links\n\n")
            f.write("| Priority | Repository | Why read it |\n")
            f.write("| ---: | --- | --- |\n")
            for link in top_links[:8]:
                repo = md_escape(link.get("repo", ""))
                url = link.get("url") or f"https://github.com/{link.get('repo', '')}"
                f.write(
                    f"| {link.get('priority', '')} | "
                    f"[{repo}](https://github.com/{link.get('repo', '')}) | "
                    f"[{md_escape(link.get('why', ''))}]({url}) |\n"
                )
            f.write("\n")

        if noise_summary:
            f.write("## Noise and Automation\n\n")
            noisy_count = int(noise_summary.get("event_count") or 0)
            if noisy_count:
                f.write(f"- {noisy_count} event(s) look automated, bot-heavy, dependency, generated, or medium/high noise.\n")
                top_noise = noise_summary.get("top_repos") or []
                if top_noise:
                    repos = ", ".join(item.get("repo", "") for item in top_noise[:5] if item.get("repo"))
                    f.write(f"- Top noisy repositories: {md_escape(repos)}.\n")
                change_types = noise_summary.get("change_types") or {}
                if change_types:
                    labels = ", ".join(f"{friendly_change_type(key)}: {value}" for key, value in change_types.items())
                    f.write(f"- Noise mix: {md_escape(labels)}.\n")
            else:
                f.write("- No medium/high-noise automation cluster was detected in the emitted events.\n")
            f.write("\n")

        f.write("<details>\n<summary>Show collection settings and diagnostics</summary>\n\n")

        f.write("## Collection Settings\n\n")
        categories = filters.get("categories")
        if isinstance(categories, list):
            categories_text = ", ".join(categories)
        else:
            categories_text = str(categories or "")
        f.write(f"- Categories: `{categories_text}`\n")
        f.write(f"- Include archived: `{filters.get('include_archived', False)}`\n")
        f.write(f"- Include forks: `{filters.get('include_forks', False)}`\n")
        f.write(f"- State window: `{window.get('state_window_enabled', False)}`\n")
        f.write(f"- Events prefilter: `{filters.get('events_prefilter_mode', 'off')}`\n\n")

        if graphql:
            f.write("## Collection Efficiency\n\n")
            f.write("| Metric | Value |\n")
            f.write("| --- | ---: |\n")
            f.write(f"| GraphQL mode | {md_escape(graphql.get('mode', ''))} |\n")
            f.write(f"| Batch size | {graphql.get('batch_size', '')} |\n")
            f.write(f"| Count batches | {graphql.get('count_batches', 0)} |\n")
            f.write(f"| Detail batches | {graphql.get('detail_batches', 0)} |\n")
            f.write(f"| Repos counted | {graphql.get('repos_counted', 0)} |\n")
            f.write(f"| Repos enriched | {graphql.get('repos_enriched', 0)} |\n")
            f.write("\n")

        if events.get("enabled"):
            f.write("## Events API Prefilter\n\n")
            f.write("| Metric | Value |\n")
            f.write("| --- | ---: |\n")
            f.write(f"| Orgs checked | {events.get('orgs_checked', 0)} |\n")
            f.write(f"| Candidate repositories | {events.get('candidate_repos', 0)} |\n")
            f.write(f"| Pages checked | {events.get('pages_checked', 0)} |\n")
            f.write(f"| Pages changed | {events.get('pages_changed', 0)} |\n")
            f.write(f"| Pages not modified | {events.get('pages_not_modified', 0)} |\n")
            f.write("\n")

        if events_calibration.get("enabled"):
            f.write("## Events API Calibration\n\n")
            f.write("| Metric | Value |\n")
            f.write("| --- | ---: |\n")
            f.write(f"| `pushed_at` candidates | {events_calibration.get('pushed_at_candidates', 0)} |\n")
            f.write(f"| Events candidates in report scope | {events_calibration.get('event_candidates_in_scope', 0)} |\n")
            f.write(f"| Events candidates outside report scope | {events_calibration.get('event_candidates_outside_scope', 0)} |\n")
            f.write(f"| Intersection candidates | {events_calibration.get('intersection_candidates', 0)} |\n")
            f.write(f"| Union candidates | {events_calibration.get('union_candidates', 0)} |\n")
            f.write(f"| Intersect candidate savings | {events_calibration.get('intersect_candidate_savings', 0)} |\n")
            f.write(f"| Intersect potential misses | {events_calibration.get('intersect_potential_miss_count', 0)} |\n")
            f.write("\n")

        f.write("</details>\n\n")
        f.write("<details>\n<summary>Show supporting signal, release, and lifecycle tables</summary>\n\n")

        high_signal = signal_summary.get("high_signal") or []
        if high_signal:
            f.write("## High-Signal Items\n\n")
            f.write("| Repository | Score | Tags |\n")
            f.write("| --- | ---: | --- |\n")
            for item in high_signal[:15]:
                full_name = md_escape(item.get("full_name", ""))
                f.write(
                    f"| [{full_name}](https://github.com/{full_name}) | "
                    f"{item.get('score', 0)} | "
                    f"{md_escape(', '.join(item.get('tags') or []))} |\n"
                )
            f.write("\n")

        watched = signal_summary.get("watched") or []
        if watched:
            f.write("## Watchlist Hits\n\n")
            f.write("| Repository | Score | Matches |\n")
            f.write("| --- | ---: | --- |\n")
            for item in watched[:15]:
                full_name = md_escape(item.get("full_name", ""))
                matches = item.get("watchlist_matches") or {}
                match_text = []
                for key in ("products", "repos", "orgs", "keywords"):
                    if matches.get(key):
                        match_text.append(f"{key}: {', '.join(matches[key])}")
                f.write(
                    f"| [{full_name}](https://github.com/{full_name}) | "
                    f"{item.get('score', 0)} | {md_escape('; '.join(match_text))} |\n"
                )
            f.write("\n")

        if release_items:
            f.write("## Releases\n\n")
            f.write("| Repository | Release | Published |\n")
            f.write("| --- | --- | --- |\n")
            for release in sorted(release_items, key=lambda item: item.get("published_at", ""), reverse=True)[:25]:
                full_name = md_escape(release.get("repo_full_name", ""))
                title = release.get("name") or release.get("tag_name") or "Release"
                f.write(
                    f"| [{full_name}](https://github.com/{full_name}) | "
                    f"[{md_escape(title)}]({release.get('html_url', '')}) | "
                    f"`{release.get('published_at', '')}` |\n"
                )
            f.write("\n")

        lifecycle_counts = lifecycle.get("counts") or {}
        if lifecycle_counts:
            f.write("## Repository Lifecycle\n\n")
            f.write("| Change | Count |\n")
            f.write("| --- | ---: |\n")
            for key, count in sorted(lifecycle_counts.items()):
                f.write(f"| {md_escape(key)} | {count} |\n")
            f.write("\n")

        if recent_creations:
            f.write("## Recently Created Repositories\n\n")
            f.write("| Repository | Category | Created |\n")
            f.write("| --- | --- | --- |\n")
            for repo in recent_creations[:25]:
                full_name = md_escape(repo.get("full_name", ""))
                f.write(
                    f"| [{full_name}]({repo.get('html_url', '')}) | "
                    f"{md_escape(repo.get('category', ''))} | "
                    f"`{repo.get('created_at', '')}` |\n"
                )
            f.write("\n")

        by_category = summaries.get("by_category") or {}
        if by_category:
            f.write("## Category Summary\n\n")
            f.write("| Category | Repositories |\n")
            f.write("| --- | ---: |\n")
            for category, count in sorted(by_category.items()):
                f.write(f"| {md_escape(category)} | {count} |\n")
            f.write("\n")

        by_org = summaries.get("by_org") or {}
        if by_org:
            f.write("## Organization Summary\n\n")
            f.write("| Org | Repositories |\n")
            f.write("| --- | ---: |\n")
            for org, count in sorted(by_org.items(), key=lambda item: item[1], reverse=True):
                f.write(f"| {md_escape(org)} | {count} |\n")
            f.write("\n")

        f.write("</details>\n\n")
        f.write("<details>\n<summary>Show raw repository activity</summary>\n\n")

        if top_repos:
            f.write("## Busiest Repositories\n\n")
            f.write("| Repository | Signal | Category | Commits | Releases | Newest commit |\n")
            f.write("| --- | ---: | --- | ---: | ---: | --- |\n")
            for activity in top_repos:
                full_name = md_escape(activity.get("full_name", ""))
                repo_url = f"https://github.com/{activity.get('full_name', '')}"
                signal = activity.get("signal") or {}
                f.write(
                    f"| [{full_name}]({repo_url}) | "
                    f"{signal.get('score', 0)} | "
                    f"{md_escape(activity.get('category', ''))} | "
                    f"{activity.get('commit_count', 0)} | "
                    f"{len(activity.get('releases') or [])} | "
                    f"`{activity.get('newest_commit_date', '')}` |\n"
                )
            f.write("\n")

        f.write("## Repository Details\n\n")
        if not activities:
            f.write("No default-branch movement matched the current filters.\n")
            f.write("\n</details>\n")
            return

        for activity in activities:
            signal = activity.get("signal") or {}
            tags = signal.get("tags") or []
            f.write(
                f"### {md_escape(activity.get('full_name', ''))} "
                f"({activity.get('commit_count', 0)} commit(s), signal {signal.get('score', 0)})\n\n"
            )
            if tags:
                f.write(f"Tags: `{md_escape(', '.join(tags))}`\n\n")
            activity_releases = activity.get("releases") or []
            for release in activity_releases:
                title = release.get("name") or release.get("tag_name") or "Release"
                f.write(
                    f"- Release: [{md_escape(title)}]({release.get('html_url', '')}) - "
                    f"`{release.get('published_at', '')}`\n"
                )
            commits = activity.get("commits") or []
            if not commits:
                f.write("- No commit headlines returned.\n\n")
                continue
            for commit in commits:
                headline = md_escape(commit.get("headline") or commit.get("oid") or "Commit")
                url = commit.get("url") or ""
                date = commit.get("committed_date") or ""
                author = commit.get("author") or ""
                pr_title = commit.get("pr_title") or ""
                pr_url = commit.get("pr_url") or ""
                suffix = f" - {md_escape(author)}" if author else ""
                if pr_title and pr_url:
                    suffix += f" - PR: [{md_escape(pr_title)}]({pr_url})"
                f.write(f"- [{headline}]({url}) - `{date}`{suffix}\n")
            f.write("\n")

        f.write("</details>\n")


def write_consumer_markdown(path: str, payload: Dict[str, Any]) -> None:
    totals = payload.get("totals") or {}
    window = payload.get("window") or {}
    event_stream = payload.get("event_stream") or {}
    generated_at = str(payload.get("generated_at") or "")
    title_date = generated_at[:10] if len(generated_at) >= 10 else generated_at
    top_links = payload.get("top_links") or []
    product_areas = payload.get("product_area_summary") or []
    notable_changes = payload.get("notable_changes") or []
    releases = (payload.get("releases") or {}).get("items") or []
    noise = payload.get("noise_summary") or {}
    activity_by_repo = report_activity_lookup(payload)

    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# Microsoft Ecosystem Brief - {title_date}\n\n")
        f.write(
            f"> Fresh as of {human_utc(generated_at)}. "
            f"{count_phrase(totals.get('repos_with_movement', 0), 'repo')} moved, "
            f"{count_phrase(totals.get('default_branch_commits', 0), 'commit')}, "
            f"{count_phrase(totals.get('release_count', 0), 'release')}, "
            f"{count_phrase(event_stream.get('event_count', 0), 'tracked event')}.\n\n"
        )

        f.write("## What To Look At First\n\n")
        if top_links:
            for idx, link in enumerate(top_links[:8], start=1):
                repo = str(link.get("repo") or "")
                why = str(link.get("why") or "High-signal change")
                change_type = "unknown"
                for change in notable_changes:
                    if event_repo(change) == repo and event_url(change) == str(link.get("url") or ""):
                        change_type = str(change.get("change_type") or "unknown")
                        break
                f.write(f"### {idx}. [{md_escape(why)}]({link.get('url', '')})\n\n")
                if repo:
                    f.write(f"- Repository: {repo_markdown_link(repo)}\n")
                f.write(f"- Why it matters: {md_escape(consumer_why(change_type))}\n\n")
        else:
            f.write("No high-signal links were selected for this window.\n\n")

        f.write("## Product Area Briefings\n\n")
        if product_areas:
            for area in product_areas[:8]:
                area_name = str(area.get("product_area") or "Unmapped Activity")
                f.write(f"### {md_escape(area_name)}\n\n")
                f.write(
                    f"{count_phrase(area.get('repo_count', 0), 'repo')}, "
                    f"{count_phrase(area.get('event_count', 0), 'tracked event')}, "
                    f"{count_phrase(area.get('release_count', 0), 'release')}, "
                    f"{count_phrase(area.get('security_event_count', 0), 'security/admin signal')}.\n\n"
                )
                f.write(f"- Likely audience: {md_escape(likely_audiences_for_area(area_name, payload))}.\n")
                f.write(f"- Reader takeaway: {md_escape(area_reader_takeaway(area))}\n")
                top_events = area.get("top_events") or []
                if top_events:
                    f.write("- Most useful links:\n")
                    for event in top_events[:3]:
                        headline = md_escape(event_headline(event))
                        url = event_url(event)
                        repo = event_repo(event)
                        repo_part = f" ({repo})" if repo else ""
                        f.write(f"  - [{headline}]({url}){md_escape(repo_part)}\n")
                f.write("\n")
        else:
            f.write("No product-area rollup was generated for this window.\n\n")

        f.write("## Release Radar\n\n")
        release_rows = [
            item for item in releases if isinstance(item, dict) and not item.get("draft")
        ]
        if release_rows:
            f.write("| Product area | Repository | Release | Why it matters |\n")
            f.write("| --- | --- | --- | --- |\n")
            for release in sorted(release_rows, key=lambda item: item.get("published_at", ""), reverse=True)[:12]:
                repo = str(release.get("repo_full_name") or "")
                activity = activity_by_repo.get(repo) or {}
                area = activity.get("product_area") or "Unmapped Activity"
                title = release.get("name") or release.get("tag_name") or "Release"
                why = "Pre-release; inspect before adopting broadly." if release.get("prerelease") else "New release available for consumers of this repo."
                f.write(
                    f"| {md_escape(area)} | {repo_markdown_link(repo)} | "
                    f"[{md_escape(title)}]({release.get('html_url', '')}) | {md_escape(why)} |\n"
                )
            f.write("\n")
        else:
            f.write("No release items were detected in this window.\n\n")

        f.write("## Security And Admin Attention\n\n")
        security_changes = [
            change for change in notable_changes if str(change.get("change_type") or "") == "security_fix"
        ]
        f.write("These are not automatically vulnerabilities; they are items with security/admin-sensitive language or taxonomy.\n\n")
        if security_changes:
            for change in security_changes[:10]:
                f.write(
                    f"- {repo_markdown_link(event_repo(change))}: "
                    f"[{md_escape(event_headline(change))}]({event_url(change)})\n"
                )
            f.write("\n")
        else:
            f.write("- No security/admin-sensitive notable changes were selected.\n\n")

        f.write("## What Was Mostly Noise\n\n")
        noisy_count = int(noise.get("event_count") or 0)
        f.write(
            f"{count_phrase(noisy_count, 'event')} looked automated, bot-heavy, dependency-related, generated, "
            "or medium/high-noise.\n\n"
        )
        top_noise = noise.get("top_repos") or []
        if top_noise:
            f.write("Top noisy clusters:\n\n")
            for item in top_noise[:6]:
                repo = str(item.get("repo") or "")
                f.write(f"- {repo_markdown_link(repo)} - {count_phrase(item.get('event_count', 0), 'event')}\n")
            f.write("\n")
        change_types = noise.get("change_types") or {}
        if change_types:
            labels = ", ".join(f"{friendly_change_type(key)}: {value}" for key, value in change_types.items())
            f.write(f"Noise mix: {md_escape(labels)}.\n\n")

        f.write("## Data Confidence\n\n")
        f.write(f"- Source: GitHub scheduled/manual digest artifacts in this repository.\n")
        f.write(
            f"- Window: {effective_window_hours(window):g} hours "
            f"from `{window.get('since', '')}` to `{window.get('until', '')}`.\n"
        )
        f.write(
            f"- Event stream: {event_stream.get('commit_event_count', 0)} commits, "
            f"{event_stream.get('release_event_count', 0)} releases.\n"
        )
        f.write("- Freshness: tracked in [`reports/status.json`](status.json).\n")
        f.write(
            "- Full data: [`latest.summary.json`](latest.summary.json), "
            "[`latest.events.ndjson`](latest.events.ndjson), [`latest.json`](latest.json).\n"
        )


def load_dated_report_payloads(report_dir: str) -> List[Dict[str, Any]]:
    if not os.path.isdir(report_dir):
        return []
    payloads: List[Dict[str, Any]] = []
    pattern = re.compile(r"^\d{4}-\d{2}-\d{2}\.json$")
    for name in sorted(os.listdir(report_dir)):
        if not pattern.match(name):
            continue
        path = os.path.join(report_dir, name)
        try:
            with open(path, "r", encoding="utf-8") as f:
                payload = json.load(f)
            if isinstance(payload, dict) and payload.get("generated_at"):
                payloads.append(payload)
        except Exception as exc:
            sys.stderr.write(f"[WARN] Skipping malformed report {path}: {exc}\n")
    payloads.sort(key=lambda payload: str(payload.get("generated_at") or ""))
    return payloads


def build_report_index_payload(report_dir: str) -> Dict[str, Any]:
    reports = load_dated_report_payloads(report_dir)
    daily = []
    repo_counter: Counter[str] = Counter()
    product_counter: Counter[str] = Counter()
    for payload in reports:
        totals = payload.get("totals") or {}
        signals = ((payload.get("summaries") or {}).get("signals") or {})
        for product_area in payload.get("product_area_summary") or []:
            product = product_area.get("product_area")
            if product:
                product_counter[str(product)] += int(product_area.get("notable_event_count") or product_area.get("event_count") or 1)
        for activity in payload.get("activities") or []:
            full_name = activity.get("full_name")
            if full_name:
                repo_counter[str(full_name)] += 1
            product_area = activity.get("product_area")
            if product_area and product_area != "Unknown":
                product_counter[str(product_area)] += 1
            signal = activity.get("signal") or {}
            matches = signal.get("watchlist_matches") or {}
            for product in matches.get("products") or []:
                product_counter[str(product)] += 1

        daily.append(
            {
                "date": str(payload.get("generated_at") or "")[:10],
                "generated_at": payload.get("generated_at", ""),
                "repos_with_movement": totals.get("repos_with_movement", 0),
                "default_branch_commits": totals.get("default_branch_commits", 0),
                "release_count": totals.get("release_count", 0),
                "high_signal_count": len(signals.get("high_signal") or []),
                "report_md": f"{str(payload.get('generated_at') or '')[:10]}.md",
                "report_json": f"{str(payload.get('generated_at') or '')[:10]}.json",
            }
        )

    last_7 = daily[-7:]
    last_30 = daily[-30:]
    latest = daily[-1] if daily else {}
    latest_payload = reports[-1] if reports else {}
    return {
        "schema_version": 1,
        "artifact_type": "tracker-report-index",
        "artifact_version": ARTIFACT_VERSION,
        "schema_url": REPORT_INDEX_SCHEMA_URL,
        "generated_at": iso_utc(),
        "report_count": len(daily),
        "latest": {
            "date": latest.get("date", ""),
            "generated_at": latest.get("generated_at", ""),
            "report_md": "latest.md",
            "consumer_md": "latest.consumer.md",
            "report_json": "latest.json",
            "summary_json": "latest.summary.json",
            "event_stream": "latest.events.ndjson",
            "repos_with_movement": latest.get("repos_with_movement", 0),
            "default_branch_commits": latest.get("default_branch_commits", 0),
            "release_count": latest.get("release_count", 0),
            "high_signal_count": latest.get("high_signal_count", 0),
            "product_area_summary": latest_payload.get("product_area_summary") or [],
        },
        "daily": daily,
        "trends": {
            "last_7_days": {
                "report_count": len(last_7),
                "repos_with_movement": sum(int(item.get("repos_with_movement") or 0) for item in last_7),
                "default_branch_commits": sum(int(item.get("default_branch_commits") or 0) for item in last_7),
                "release_count": sum(int(item.get("release_count") or 0) for item in last_7),
            },
            "last_30_days": {
                "report_count": len(last_30),
                "repos_with_movement": sum(int(item.get("repos_with_movement") or 0) for item in last_30),
                "default_branch_commits": sum(int(item.get("default_branch_commits") or 0) for item in last_30),
                "release_count": sum(int(item.get("release_count") or 0) for item in last_30),
            },
        },
        "top_recurring_repos": [
            {"full_name": full_name, "report_count": count}
            for full_name, count in repo_counter.most_common(25)
        ],
        "top_products": [
            {"product": product, "report_count": count}
            for product, count in product_counter.most_common(25)
        ],
    }


def write_report_index(report_dir: str) -> List[str]:
    payload = build_report_index_payload(report_dir)
    json_path = os.path.join(report_dir, "index.json")
    md_path = os.path.join(report_dir, "index.md")

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, sort_keys=True)
        f.write("\n")

    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# Microsoft Ecosystem Change Reports\n\n")
        f.write(f"Generated: `{payload.get('generated_at', '')}`\n\n")
        latest = payload.get("latest") or {}
        if latest:
            f.write("## Latest Brief\n\n")
            f.write("[Read today's brief ->](latest.md)\n\n")
            f.write("## Current Status\n\n")
            generated = latest.get("generated_at", "")
            freshness = freshness_payload(str(generated or ""), parse_iso(str(generated or "")) or dt.datetime.now(dt.timezone.utc))
            status_label = "Fresh" if not freshness.get("latest_report_stale") else "Stale"
            f.write(f"- Status: {status_label} at latest report generation. Current status lives in `status.json`.\n")
            f.write(f"- Last generated: `{human_utc(generated)}`\n")
            f.write(
                "- Latest artifacts: [Daily brief](latest.md), [Consumer brief](latest.consumer.md), [JSON](latest.json), "
                "[Summary](latest.summary.json), [Events](latest.events.ndjson)\n\n"
            )

        trends = payload.get("trends") or {}
        for label, trend in (("7-Day Snapshot", trends.get("last_7_days") or {}), ("30-Day Snapshot", trends.get("last_30_days") or {})):
            f.write(f"## {label}\n\n")
            f.write(f"- Reports: {trend.get('report_count', 0)}\n")
            f.write(f"- Repositories with movement: {trend.get('repos_with_movement', 0)}\n")
            f.write(f"- Default-branch commits: {trend.get('default_branch_commits', 0)}\n")
            f.write(f"- Releases: {trend.get('release_count', 0)}\n\n")

        latest_products = latest.get("product_area_summary") or []
        if latest_products:
            f.write("## Latest Product Areas\n\n")
            f.write("| Product area | Signal | Repos | Events | Releases | Security |\n")
            f.write("| --- | ---: | ---: | ---: | ---: | ---: |\n")
            for item in latest_products[:8]:
                f.write(
                    f"| {md_escape(item.get('product_area', ''))} | "
                    f"{item.get('notable_event_count', 0)} | "
                    f"{item.get('repo_count', 0)} | "
                    f"{item.get('event_count', 0)} | "
                    f"{item.get('release_count', 0)} | "
                    f"{item.get('security_event_count', 0)} |\n"
                )
            f.write("\n")

        top_products = payload.get("top_products") or []
        if top_products:
            f.write("## Most Active Product Areas\n\n")
            f.write("| Product area | Activity score |\n")
            f.write("| --- | ---: |\n")
            for item in top_products[:15]:
                f.write(f"| {md_escape(item.get('product', ''))} | {item.get('report_count', 0)} |\n")
            f.write("\n")

        f.write("## Daily Reports\n\n")
        f.write("| Date | Repositories | Commits | Releases | High-signal | Links |\n")
        f.write("| --- | ---: | ---: | ---: | ---: | --- |\n")
        for item in reversed(payload.get("daily") or []):
            date = item.get("date", "")
            f.write(
                f"| {date} | {item.get('repos_with_movement', 0)} | "
                f"{item.get('default_branch_commits', 0)} | "
                f"{item.get('release_count', 0)} | "
                f"{item.get('high_signal_count', 0)} | "
                f"[md]({item.get('report_md', '')}) / [json]({item.get('report_json', '')}) |\n"
            )
        f.write("\n")

        recurring = payload.get("top_recurring_repos") or []
        if recurring:
            f.write("## Recurring Repositories\n\n")
            f.write("| Repository | Reports |\n")
            f.write("| --- | ---: |\n")
            for item in recurring:
                full_name = md_escape(item.get("full_name", ""))
                f.write(f"| [{full_name}](https://github.com/{full_name}) | {item.get('report_count', 0)} |\n")
            f.write("\n")

    return [json_path, md_path]


def product_area_from_signal(signal: Mapping[str, Any]) -> str:
    tags = signal.get("tags") or []
    for tag in tags:
        value = str(tag)
        if value.startswith("product:"):
            return value.split(":", 1)[1]
    matches = signal.get("watchlist_matches") or {}
    products = matches.get("products") or []
    return str(products[0]) if products else ""


def actor_type_for_author(author: str) -> str:
    lowered = (author or "").lower()
    if not lowered:
        return "unknown"
    if "learn-build-service" in lowered or "github-actions" in lowered:
        return "automation"
    if "[bot]" in lowered or "dependabot" in lowered or "renovate" in lowered:
        return "bot"
    return "human"


def change_type_for_event(event_type: str, category: str, text: str) -> str:
    lowered = text.lower()
    if event_type == "release":
        return "release"
    if any(marker in lowered for marker in BULK_MARKERS):
        return "bulk_automation"
    if is_dependency_text(lowered):
        return "dependency_update"
    if re.search(r"\brelease\b", lowered):
        return "release"
    if is_security_text(lowered):
        return "security_fix"
    if any(marker in lowered for marker in SDK_MARKERS):
        return "sdk_generation"
    if any(marker in lowered for marker in CI_MARKERS):
        return "ci_infra"
    if "bug" in lowered or "fix" in lowered:
        return "bug_fix"
    if "feature" in lowered or "add " in lowered or "enable " in lowered:
        return "feature"
    category_map = {
        "docs": "docs_update",
        "reference": "reference_update",
        "training": "training_update",
        "samples": "sample_update",
    }
    return category_map.get(category, "unknown")


def noise_level_for_event(actor_type: str, change_type: str) -> str:
    if change_type in {"bulk_automation", "dependency_update"}:
        return "high"
    if change_type == "sdk_generation":
        return "medium"
    if actor_type in {"bot", "automation"}:
        return "medium"
    if change_type == "ci_infra":
        return "medium"
    if actor_type == "human":
        return "low"
    return "unknown"


def customer_visible_for_event(change_type: str, category: str) -> str:
    if change_type == "release":
        return "true"
    if change_type in {"dependency_update", "ci_infra"}:
        return "false"
    if category in {"docs", "reference", "training", "samples"}:
        return "unknown"
    return "unknown"


def event_notability(
    *,
    signal: Mapping[str, Any],
    actor_type: str,
    change_type: str,
    noise_level: str,
    text: str,
) -> Tuple[int, List[str]]:
    score = min(int(signal.get("score") or 0), 70)
    reasons: List[str] = []
    tags = set(str(tag) for tag in (signal.get("tags") or []))

    if "watchlist" in tags:
        score += 10
        reasons.append("watchlist")
    if is_security_text(text):
        score += 15
        reasons.append("security_language")
    if change_type == "release":
        score += 20
        reasons.append("release")
    if actor_type == "human":
        score += 10
        reasons.append("human_authored")
    if noise_level == "high":
        score -= 30
        reasons.append("high_noise")
    elif noise_level == "medium":
        score -= 10
        reasons.append("automation_or_bot")
    if change_type in {"bulk_automation", "dependency_update"}:
        score -= 10
        reasons.append(change_type)
    if change_type == "sdk_generation":
        score -= 5
        reasons.append("sdk_generation")

    return max(0, min(100, score)), reasons


def report_activity_lookup(payload: Mapping[str, Any]) -> Dict[str, Dict[str, Any]]:
    by_repo: Dict[str, Dict[str, Any]] = {}
    for section in ("activities", "top_repos"):
        for activity in payload.get(section) or []:
            if not isinstance(activity, dict):
                continue
            repo = str(activity.get("full_name") or "").strip()
            if repo and repo not in by_repo:
                by_repo[repo] = activity
    return by_repo


def release_event_record(
    release: Mapping[str, Any],
    activity_by_repo: Mapping[str, Mapping[str, Any]],
    window: Mapping[str, Any],
    retrieved_at: str,
    source_base: Mapping[str, Any],
) -> Optional[Dict[str, Any]]:
    repo = str(release.get("repo_full_name") or release.get("repo") or "").strip()
    if not repo:
        return None
    activity = activity_by_repo.get(repo) or {}
    org = str(activity.get("org") or (repo.split("/")[0] if "/" in repo else ""))
    repo_name = str(activity.get("name") or (repo.split("/", 1)[1] if "/" in repo else repo))
    category = str(activity.get("category") or "")
    repo_type = str(activity.get("repo_type") or "")
    audience = str(activity.get("audience") or "")
    default_branch = str(activity.get("default_branch") or "")
    signal = activity.get("signal") if isinstance(activity.get("signal"), dict) else {}
    product_area = str(activity.get("product_area") or product_area_from_signal(signal))
    tag_name = str(release.get("tag_name") or "")
    title = str(release.get("name") or tag_name or "Release")
    published_at = str(release.get("published_at") or "")
    if tag_name:
        fallback_release_url = f"https://github.com/{repo}/releases/tag/{tag_name}"
    else:
        fallback_release_url = f"https://github.com/{repo}/releases"
    release_url = str(release.get("html_url") or fallback_release_url)
    release_token = tag_name or release_url or published_at
    if not release_token:
        return None
    text = " ".join([repo, category, title, tag_name])
    notability_score, notability_reason = event_notability(
        signal=signal,
        actor_type="unknown",
        change_type="release",
        noise_level="low",
        text=text,
    )
    return {
        "schema_version": 1,
        "artifact_type": "tracker-event",
        "artifact_version": ARTIFACT_VERSION,
        "schema_url": EVENT_SCHEMA_URL,
        "event_id": f"github_release:{repo}:{release_token}",
        "event_type": "release",
        "dedupe_key": f"release:{repo}:{release_token}",
        "repo": repo,
        "org": org,
        "repo_name": repo_name,
        "category": category,
        "repo_type": repo_type,
        "product_area": product_area,
        "audience": audience,
        "default_branch": default_branch,
        "committed_at": published_at,
        "published_at": published_at,
        "headline": title,
        "author": "",
        "actor_type": "unknown",
        "commit_oid": tag_name or release_token,
        "commit_url": release_url,
        "release_tag": tag_name,
        "release_name": title,
        "release_url": release_url,
        "prerelease": bool(release.get("prerelease")),
        "draft": bool(release.get("draft")),
        "pr_number": None,
        "pr_title": None,
        "pr_url": None,
        "change_type": "release",
        "noise_level": "low",
        "customer_visible": "true",
        "notability_score": notability_score,
        "notability_reason": notability_reason,
        "labels": signal.get("tags") or [],
        "window_since": str(window.get("since") or ""),
        "window_until": str(window.get("until") or ""),
        "retrieved_at": retrieved_at,
        "source": {
            "provider": "github",
            "api": "rest",
            "repo_url": f"https://github.com/{repo}",
            "source_commit": source_base.get("commit", ""),
            "workflow_run_url": source_base.get("workflow_run_url", ""),
        },
    }


def build_event_stream_records(payload: Mapping[str, Any]) -> List[Dict[str, Any]]:
    window = payload.get("window") or {}
    retrieved_at = str(payload.get("generated_at") or "")
    source_base = payload.get("source") if isinstance(payload.get("source"), dict) else {}
    activity_by_repo = report_activity_lookup(payload)
    records: List[Dict[str, Any]] = []

    for activity in payload.get("activities") or []:
        if not isinstance(activity, dict):
            continue
        repo = str(activity.get("full_name") or "")
        org = str(activity.get("org") or (repo.split("/")[0] if "/" in repo else ""))
        repo_name = str(activity.get("name") or (repo.split("/", 1)[1] if "/" in repo else repo))
        category = str(activity.get("category") or "")
        repo_type = str(activity.get("repo_type") or "")
        audience = str(activity.get("audience") or "")
        default_branch = str(activity.get("default_branch") or "")
        signal = activity.get("signal") if isinstance(activity.get("signal"), dict) else {}
        product_area = str(activity.get("product_area") or product_area_from_signal(signal))

        for commit in activity.get("commits") or []:
            if not isinstance(commit, dict):
                continue
            oid = str(commit.get("oid") or "").strip()
            if not oid:
                continue
            headline = str(commit.get("headline") or "")
            author = str(commit.get("author") or "")
            pr_title = str(commit.get("pr_title") or "")
            text = " ".join([repo, category, headline, pr_title, author])
            actor_type = actor_type_for_author(author)
            change_type = change_type_for_event("commit", category, text)
            noise_level = noise_level_for_event(actor_type, change_type)
            customer_visible = customer_visible_for_event(change_type, category)
            notability_score, notability_reason = event_notability(
                signal=signal,
                actor_type=actor_type,
                change_type=change_type,
                noise_level=noise_level,
                text=text,
            )
            records.append(
                {
                    "schema_version": 1,
                    "artifact_type": "tracker-event",
                    "artifact_version": ARTIFACT_VERSION,
                    "schema_url": EVENT_SCHEMA_URL,
                    "event_id": f"github_commit:{repo}:{oid}",
                    "event_type": "commit",
                    "dedupe_key": f"commit:{oid}",
                    "repo": repo,
                    "org": org,
                    "repo_name": repo_name,
                    "category": category,
                    "repo_type": repo_type,
                    "product_area": product_area,
                    "audience": audience,
                    "default_branch": default_branch,
                    "committed_at": str(commit.get("committed_date") or ""),
                    "headline": headline,
                    "author": author,
                    "actor_type": actor_type,
                    "commit_oid": oid,
                    "commit_url": str(commit.get("url") or ""),
                    "pr_number": commit.get("pr_number"),
                    "pr_title": commit.get("pr_title"),
                    "pr_url": commit.get("pr_url"),
                    "change_type": change_type,
                    "noise_level": noise_level,
                    "customer_visible": customer_visible,
                    "notability_score": notability_score,
                    "notability_reason": notability_reason,
                    "labels": signal.get("tags") or [],
                    "window_since": str(window.get("since") or ""),
                    "window_until": str(window.get("until") or ""),
                    "retrieved_at": retrieved_at,
                    "source": {
                        "provider": "github",
                        "api": "graphql",
                        "repo_url": f"https://github.com/{repo}" if repo else "",
                        "source_commit": source_base.get("commit", ""),
                        "workflow_run_url": source_base.get("workflow_run_url", ""),
                    },
                }
            )

    release_items = [
        item
        for item in ((payload.get("releases") or {}).get("items") or [])
        if isinstance(item, dict)
    ]
    if not release_items:
        for activity in payload.get("activities") or []:
            if not isinstance(activity, dict):
                continue
            release_items.extend(item for item in activity.get("releases") or [] if isinstance(item, dict))

    seen_release_keys: Set[str] = set()
    for release in release_items:
        record = release_event_record(release, activity_by_repo, window, retrieved_at, source_base)
        if not record:
            continue
        dedupe_key = str(record.get("dedupe_key") or "")
        if dedupe_key in seen_release_keys:
            continue
        seen_release_keys.add(dedupe_key)
        records.append(record)

    records.sort(key=lambda item: (str(item.get("committed_at") or ""), str(item.get("event_id") or "")), reverse=True)
    return records


def write_ndjson(path: str, records: List[Dict[str, Any]]) -> None:
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        for record in records:
            f.write(json.dumps(record, sort_keys=True, separators=(",", ":")))
            f.write("\n")


def notable_changes_from_events(records: List[Dict[str, Any]], limit: int = 25) -> List[Dict[str, Any]]:
    candidates = [
        record
        for record in records
        if str(record.get("noise_level") or "") != "high" and int(record.get("notability_score") or 0) >= 50
    ]
    if not candidates:
        candidates = records[:]
    candidates.sort(
        key=lambda item: (
            int(item.get("notability_score") or 0),
            change_type_priority(item.get("change_type")),
            str(item.get("committed_at") or ""),
            str(item.get("event_id") or ""),
        ),
        reverse=True,
    )
    notable: List[Dict[str, Any]] = []
    seen_changes: Set[str] = set()
    repo_counts: Counter[str] = Counter()
    repo_change_counts: Counter[Tuple[str, str]] = Counter()
    for record in candidates:
        change_key = str(record.get("pr_url") or record.get("dedupe_key") or record.get("event_id") or "")
        if change_key in seen_changes:
            continue
        repo = str(record.get("repo") or "")
        change_type = str(record.get("change_type") or "unknown")
        if repo_counts[repo] >= 4:
            continue
        if change_type == "release" and repo_change_counts[(repo, change_type)] >= 2:
            continue
        seen_changes.add(change_key)
        repo_counts[repo] += 1
        repo_change_counts[(repo, change_type)] += 1
        notable.append(
            {
                "event_id": record.get("event_id", ""),
                "repo": record.get("repo", ""),
                "category": record.get("category", ""),
                "product_area": record.get("product_area", ""),
                "committed_at": record.get("committed_at", ""),
                "headline": record.get("headline", ""),
                "author": record.get("author", ""),
                "actor_type": record.get("actor_type", "unknown"),
                "change_type": record.get("change_type", "unknown"),
                "noise_level": record.get("noise_level", "unknown"),
                "customer_visible": record.get("customer_visible", "unknown"),
                "notability_score": record.get("notability_score", 0),
                "notability_reason": record.get("notability_reason", []),
                "commit_url": record.get("commit_url", ""),
                "pr_number": record.get("pr_number"),
                "pr_title": record.get("pr_title"),
                "pr_url": record.get("pr_url"),
            }
        )
        if len(notable) >= limit:
            break
    return notable


def build_summary_payload(payload: Mapping[str, Any]) -> Dict[str, Any]:
    generated_at = str(payload.get("generated_at") or "")
    date_slug = generated_at[:10] if generated_at else ""
    return {
        "schema_version": 1,
        "artifact_type": "tracker-summary",
        "artifact_version": ARTIFACT_VERSION,
        "schema_url": SUMMARY_SCHEMA_URL,
        "generated_at": generated_at,
        "source": payload.get("source") if isinstance(payload.get("source"), dict) else source_metadata(),
        "freshness": freshness_payload(generated_at, parse_iso(generated_at) or dt.datetime.now(dt.timezone.utc)),
        "window": payload.get("window") or {},
        "filters": payload.get("filters") or {},
        "totals": payload.get("totals") or {},
        "event_stream": payload.get("event_stream") or {},
        "plain_english_summary": build_plain_english_summary(payload),
        "top_links": payload.get("top_links") or [],
        "product_area_summary": payload.get("product_area_summary") or [],
        "noise_summary": payload.get("noise_summary") or {},
        "artifact_links": {
            "latest_markdown": "reports/latest.md",
            "latest_consumer_markdown": "reports/latest.consumer.md",
            "latest_report_json": "reports/latest.json",
            "latest_summary_json": "reports/latest.summary.json",
            "latest_event_stream": "reports/latest.events.ndjson",
            "report_index": "reports/index.md",
            "dated_markdown": f"reports/{date_slug}.md" if date_slug else "",
            "dated_consumer_markdown": f"reports/{date_slug}.consumer.md" if date_slug else "",
            "dated_report_json": f"reports/{date_slug}.json" if date_slug else "",
            "dated_summary_json": f"reports/{date_slug}.summary.json" if date_slug else "",
            "dated_event_stream": f"reports/{date_slug}.events.ndjson" if date_slug else "",
        },
    }


def manifest_artifact(
    name: str,
    artifact_type: str,
    path: str,
    *,
    schema_url: str = "",
    required: bool = True,
) -> Dict[str, Any]:
    item = {
        "name": name,
        "artifact_type": artifact_type,
        "path": normalize_artifact_path(path),
        "required": required,
    }
    if schema_url:
        item["schema_url"] = schema_url
    return item


def build_status_payload(
    report_dir: str,
    *,
    status: str,
    reason: str,
    now_utc: dt.datetime,
    latest_generated_at: Optional[str] = None,
    source: Optional[Mapping[str, Any]] = None,
) -> Dict[str, Any]:
    latest_generated_at = latest_generated_at if latest_generated_at is not None else latest_report_generated_at(report_dir)
    freshness = freshness_payload(latest_generated_at, now_utc)
    return {
        "schema_version": 1,
        "artifact_type": "tracker-status",
        "artifact_version": ARTIFACT_VERSION,
        "schema_url": STATUS_SCHEMA_URL,
        "generated_at": iso_utc(now_utc),
        "last_attempt_at": iso_utc(now_utc),
        "last_success_at": latest_generated_at if status == "complete" else latest_generated_at,
        "status": status,
        "reason": reason,
        "latest_report_generated_at": latest_generated_at,
        "latest_report_stale": freshness["latest_report_stale"],
        "freshness": freshness,
        "source": dict(source) if source else source_metadata(),
    }


def build_manifest_payload(
    report_dir: str,
    *,
    status_payload: Dict[str, Any],
    generated_at: dt.datetime,
    source: Optional[Mapping[str, Any]] = None,
) -> Dict[str, Any]:
    latest_generated_at = str(status_payload.get("latest_report_generated_at") or "")
    date_slug = latest_generated_at[:10] if latest_generated_at else ""
    latest_event_stream = os.path.join(report_dir, "latest.events.ndjson")
    artifacts = [
        manifest_artifact("latest_human_report", "markdown", os.path.join(report_dir, "latest.md")),
        manifest_artifact("latest_consumer_report", "markdown", os.path.join(report_dir, "latest.consumer.md")),
        manifest_artifact("latest_machine_report", "json", os.path.join(report_dir, "latest.json"), schema_url=REPORT_SCHEMA_URL),
        manifest_artifact(
            "latest_summary",
            "json",
            os.path.join(report_dir, "latest.summary.json"),
            schema_url=SUMMARY_SCHEMA_URL,
            required=os.path.exists(os.path.join(report_dir, "latest.summary.json")),
        ),
        manifest_artifact(
            "latest_event_stream",
            "ndjson",
            latest_event_stream,
            schema_url=EVENT_SCHEMA_URL,
            required=os.path.exists(latest_event_stream),
        ),
        manifest_artifact("report_index_human", "markdown", os.path.join(report_dir, "index.md")),
        manifest_artifact("report_index_machine", "json", os.path.join(report_dir, "index.json"), schema_url=REPORT_INDEX_SCHEMA_URL),
        manifest_artifact("tracker_status", "json", os.path.join(report_dir, "status.json"), schema_url=STATUS_SCHEMA_URL),
        manifest_artifact("digest_csv", "csv", "changes_last24h.csv", schema_url=DIGEST_CSV_SCHEMA_URL),
        manifest_artifact("inventory", "csv", "msft_repo_inventory.csv", schema_url=INVENTORY_SCHEMA_URL),
        manifest_artifact("watchfeeds", "csv", "msft_repo_inventory_watchfeeds.csv", schema_url=WATCHFEEDS_SCHEMA_URL),
        manifest_artifact("tracker_state", "json", "msft_repo_tracker_state.json", schema_url=STATE_SCHEMA_URL),
    ]
    if date_slug:
        dated_event_stream = os.path.join(report_dir, f"{date_slug}.events.ndjson")
        artifacts.extend(
            [
                manifest_artifact("dated_human_report", "markdown", os.path.join(report_dir, f"{date_slug}.md")),
                manifest_artifact("dated_consumer_report", "markdown", os.path.join(report_dir, f"{date_slug}.consumer.md")),
                manifest_artifact("dated_machine_report", "json", os.path.join(report_dir, f"{date_slug}.json"), schema_url=REPORT_SCHEMA_URL),
                manifest_artifact(
                    "dated_summary",
                    "json",
                    os.path.join(report_dir, f"{date_slug}.summary.json"),
                    schema_url=SUMMARY_SCHEMA_URL,
                    required=os.path.exists(os.path.join(report_dir, f"{date_slug}.summary.json")),
                ),
                manifest_artifact(
                    "dated_event_stream",
                    "ndjson",
                    dated_event_stream,
                    schema_url=EVENT_SCHEMA_URL,
                    required=os.path.exists(dated_event_stream),
                ),
            ]
        )

    calibration_json = os.path.join(report_dir, "events-calibration", "latest.json")
    calibration_md = os.path.join(report_dir, "events-calibration", "latest.md")
    if os.path.exists(calibration_json):
        artifacts.append(
            manifest_artifact(
                "events_calibration_machine",
                "json",
                calibration_json,
                schema_url=EVENTS_CALIBRATION_SCHEMA_URL,
                required=False,
            )
        )
    if os.path.exists(calibration_md):
        artifacts.append(
            manifest_artifact(
                "events_calibration_human",
                "markdown",
                calibration_md,
                required=False,
            )
        )

    return {
        "schema_version": 1,
        "artifact_type": "tracker-manifest",
        "artifact_version": ARTIFACT_VERSION,
        "schema_url": MANIFEST_SCHEMA_URL,
        "generated_at": iso_utc(generated_at),
        "source": dict(source) if source else source_metadata(),
        "status": {
            "status": status_payload.get("status", ""),
            "reason": status_payload.get("reason", ""),
            "latest_report_generated_at": latest_generated_at,
            "latest_report_stale": status_payload.get("latest_report_stale", True),
        },
        "freshness": status_payload.get("freshness") or {},
        "artifacts": artifacts,
    }


def write_status_and_manifest(
    report_dir: str,
    *,
    status: str,
    reason: str,
    now_utc: dt.datetime,
    latest_generated_at: Optional[str] = None,
    source: Optional[Mapping[str, Any]] = None,
) -> List[str]:
    os.makedirs(report_dir, exist_ok=True)
    status_payload = build_status_payload(
        report_dir,
        status=status,
        reason=reason,
        now_utc=now_utc,
        latest_generated_at=latest_generated_at,
        source=source,
    )
    status_path = os.path.join(report_dir, "status.json")
    manifest_path = os.path.join(report_dir, "manifest.json")
    with open(status_path, "w", encoding="utf-8") as f:
        json.dump(status_payload, f, indent=2, sort_keys=True)
        f.write("\n")

    manifest_payload = build_manifest_payload(
        report_dir,
        status_payload=status_payload,
        generated_at=now_utc,
        source=source,
    )
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest_payload, f, indent=2, sort_keys=True)
        f.write("\n")

    return [status_path, manifest_path]


def write_reports(report_dir: str, payload: Dict[str, Any]) -> List[str]:
    os.makedirs(report_dir, exist_ok=True)
    date_slug = str(payload.get("generated_at") or "latest")[:10]
    latest_event_path = os.path.join(report_dir, "latest.events.ndjson")
    dated_event_path = os.path.join(report_dir, f"{date_slug}.events.ndjson")
    payload = dict(payload)
    event_records = build_event_stream_records(payload)
    payload["notable_changes"] = notable_changes_from_events(event_records)
    payload["product_area_summary"] = build_product_area_summary(event_records, payload)
    payload["top_links"] = build_top_links(payload["notable_changes"])
    payload["noise_summary"] = build_noise_summary(event_records)
    commit_event_count = sum(1 for record in event_records if record.get("event_type") == "commit")
    release_event_count = sum(1 for record in event_records if record.get("event_type") == "release")
    payload["event_stream"] = {
        "schema_url": EVENT_SCHEMA_URL,
        "latest_path": normalize_artifact_path(latest_event_path),
        "dated_path": normalize_artifact_path(dated_event_path),
        "event_count": len(event_records),
        "commit_event_count": commit_event_count,
        "release_event_count": release_event_count,
    }
    report_json_paths = [
        os.path.join(report_dir, "latest.json"),
        os.path.join(report_dir, f"{date_slug}.json"),
    ]
    summary_paths = [
        os.path.join(report_dir, "latest.summary.json"),
        os.path.join(report_dir, f"{date_slug}.summary.json"),
    ]
    markdown_paths = [
        os.path.join(report_dir, "latest.md"),
        os.path.join(report_dir, f"{date_slug}.md"),
    ]
    consumer_paths = [
        os.path.join(report_dir, "latest.consumer.md"),
        os.path.join(report_dir, f"{date_slug}.consumer.md"),
    ]
    event_paths = [latest_event_path, dated_event_path]
    paths = report_json_paths + summary_paths + markdown_paths + consumer_paths + event_paths

    for path in report_json_paths:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2, sort_keys=True)
            f.write("\n")
    summary_payload = build_summary_payload(payload)
    for path in summary_paths:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(summary_payload, f, indent=2, sort_keys=True)
            f.write("\n")
    for path in markdown_paths:
        write_report_markdown(path, payload)
    for path in consumer_paths:
        write_consumer_markdown(path, payload)
    for path in event_paths:
        write_ndjson(path, event_records)

    index_paths = write_report_index(report_dir)
    status_paths = write_status_and_manifest(
        report_dir,
        status="complete",
        reason="success",
        now_utc=parse_iso(str(payload.get("generated_at") or "")) or dt.datetime.now(dt.timezone.utc),
        latest_generated_at=str(payload.get("generated_at") or ""),
        source=payload.get("source") if isinstance(payload.get("source"), dict) else None,
    )
    return paths + index_paths + status_paths


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Inventory CSV path.")
    parser.add_argument("--hours", type=int, default=24, help="Lookback window in hours.")
    parser.add_argument("--max-commits", type=int, default=5)
    parser.add_argument("--include-archived", action="store_true")
    parser.add_argument("--include-forks", action="store_true")
    parser.add_argument(
        "--categories",
        default="",
        help="Comma-separated categories, or 'all'. Blank defaults to docs/reference/training/samples.",
    )
    parser.add_argument("--include-other", action="store_true")
    parser.add_argument("--min-rest-remaining", type=int, default=100)
    parser.add_argument("--min-graphql-remaining", type=int, default=100)
    parser.add_argument(
        "--graphql-batch-size",
        type=int,
        default=0,
        help="GraphQL repos per batch. Use 0 for adaptive sizing.",
    )
    parser.add_argument(
        "--enrichment-mode",
        choices=["one-stage", "two-stage"],
        default="two-stage",
        help="Use two-stage GraphQL enrichment to fetch rich details only for repos with movement.",
    )
    parser.add_argument("--no-budget-check", action="store_true")
    parser.add_argument("--state", default="", help="Tracker state JSON path.")
    parser.add_argument("--watchlist", default=DEFAULT_WATCHLIST_PATH)
    parser.add_argument(
        "--use-state-window",
        action="store_true",
        help="Extend lookback to the last successful digest timestamp, with overlap.",
    )
    parser.add_argument("--digest-overlap-hours", type=int, default=2)
    parser.add_argument("--max-lookback-hours", type=int, default=168)
    parser.add_argument(
        "--events-prefilter-mode",
        choices=["off", "union", "intersect"],
        default="off",
        help=(
            "Optionally use organization Events API pages as an enrichment candidate hint. "
            "'union' adds event candidates; 'intersect' keeps only repos found by both "
            "pushed_at and events when events return candidates."
        ),
    )
    parser.add_argument("--events-orgs", default="orgs.txt", help="Org list for Events API prefilter.")
    parser.add_argument("--events-max-pages", type=int, default=2)
    parser.add_argument(
        "--events-calibration",
        action="store_true",
        help="Compare pushed_at candidates with Events API candidates without changing the selected mode.",
    )
    parser.add_argument(
        "--release-mode",
        choices=["off", "candidates", "watched", "candidates-and-watched"],
        default="candidates-and-watched",
    )
    parser.add_argument("--max-release-repos", type=int, default=150)
    parser.add_argument("--max-releases-per-repo", type=int, default=5)
    parser.add_argument("--reports-dir", default="reports")
    parser.add_argument("--no-reports", action="store_true")
    return parser


def main() -> int:
    args = build_arg_parser().parse_args()
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        sys.stderr.write("[WARN] GITHUB_TOKEN not set. GitHub GraphQL requires authentication.\n")

    try:
        repos = read_inventory(args.input)
        watchlist = load_watchlist(args.watchlist)
        selected_categories = category_filter(args.categories, args.include_other)

        filtered: List[RepoInput] = []
        for repo in repos:
            if selected_categories is not None and repo.category.strip() not in selected_categories:
                continue
            if not args.include_archived and repo.archived is True:
                continue
            if not args.include_forks and repo.fork is True:
                continue
            filtered.append(repo)

        state = load_state(args.state)
        now_utc = dt.datetime.now(dt.timezone.utc)
        since_dt = compute_since_dt(
            now_utc,
            args.hours,
            state=state,
            use_state_window=args.use_state_window,
            overlap_hours=args.digest_overlap_hours,
            max_lookback_hours=args.max_lookback_hours,
        )
        since_iso = iso_utc(since_dt)
        until_iso = iso_utc(now_utc)

        maybe_changed: List[RepoInput] = []
        if any(repo.pushed_at for repo in filtered):
            for repo in filtered:
                pushed_at = parse_iso(repo.pushed_at)
                if pushed_at is None or pushed_at >= since_dt:
                    maybe_changed.append(repo)
        else:
            maybe_changed = filtered

        pushed_candidate_count = len(maybe_changed)
        events_summary: Optional[Dict[str, Any]] = None
        events_calibration: Optional[Dict[str, Any]] = None
        event_candidate_names: Set[str] = set()
        client = GitHubClient(token=token, user_agent="msft-changes-digest")

        if args.events_prefilter_mode != "off" or args.events_calibration:
            if not args.no_budget_check:
                client.ensure_budget("core", args.min_rest_remaining)
            event_orgs = read_orgs(args.events_orgs)
            event_candidate_names, events_summary = fetch_event_candidates(
                client=client,
                orgs=event_orgs,
                state=state,
                max_pages_per_org=args.events_max_pages,
            )
            events_summary["mode"] = args.events_prefilter_mode
            if isinstance(state.get("last_events_prefilter"), dict):
                state["last_events_prefilter"]["mode"] = args.events_prefilter_mode

            if args.events_calibration:
                events_calibration = build_events_calibration(
                    filtered=filtered,
                    pushed_candidates=maybe_changed,
                    event_candidate_names=event_candidate_names,
                    events_summary=events_summary,
                )
                state["last_events_calibration"] = {
                    **events_calibration,
                    "completed_at": iso_utc(),
                }

        if args.events_prefilter_mode != "off":
            maybe_changed = apply_events_prefilter(
                args.events_prefilter_mode,
                filtered,
                maybe_changed,
                event_candidate_names,
            )

        sys.stderr.write(f"[INFO] Inventory repos: {len(repos)}\n")
        sys.stderr.write(f"[INFO] After filters: {len(filtered)}\n")
        sys.stderr.write(f"[INFO] After pushed_at prefilter: {pushed_candidate_count}\n")
        if args.events_prefilter_mode != "off":
            sys.stderr.write(
                f"[INFO] After events prefilter ({args.events_prefilter_mode}): "
                f"{len(maybe_changed)}\n"
            )

        releases_by_repo: Dict[str, List[ReleaseInfo]] = {}
        release_summary: Dict[str, Any] = {
            "enabled": False,
            "mode": args.release_mode,
        }
        release_repos = select_release_repos(
            mode=args.release_mode,
            filtered=filtered,
            candidates=maybe_changed,
            watchlist=watchlist,
            max_repos=args.max_release_repos,
        )
        if release_repos:
            if not args.no_budget_check:
                client.ensure_budget("core", args.min_rest_remaining)
            releases_by_repo, release_summary = fetch_recent_releases(
                client=client,
                repos=release_repos,
                since_dt=since_dt,
                state=state,
                max_releases_per_repo=args.max_releases_per_repo,
            )
            release_summary["mode"] = args.release_mode
            release_summary["candidate_repo_cap"] = args.max_release_repos
            sys.stderr.write(
                f"[INFO] Release scan: {release_summary.get('repos_checked', 0)} repo(s), "
                f"{release_summary.get('repos_with_releases', 0)} with recent releases.\n"
            )

        graphql_remaining: Optional[int] = None
        if maybe_changed and not args.no_budget_check:
            client.ensure_budget("graphql", args.min_graphql_remaining)
            graphql_remaining = client.remaining("graphql")

        graphql_batch_size, batch_meta = resolve_graphql_batch_size(
            requested=args.graphql_batch_size,
            repo_count=len(maybe_changed),
            max_commits=args.max_commits,
            remaining=graphql_remaining,
        )

        activities, graphql_telemetry = fetch_activity(
            client=client,
            repos=maybe_changed,
            since_iso=since_iso,
            max_commits=args.max_commits,
            include_archived=args.include_archived,
            include_forks=args.include_forks,
            batch_size=graphql_batch_size,
            enrichment_mode=args.enrichment_mode,
        )
        graphql_telemetry.update(batch_meta)

        signals_by_repo = {
            activity.full_name: score_activity(
                activity,
                releases_by_repo.get(activity.full_name, []),
                watchlist,
            )
            for activity in activities
        }

        write_csv(
            "changes_last24h.csv",
            activities,
            args.max_commits,
            since_iso,
            until_iso,
            args.hours,
            args.use_state_window,
            signals_by_repo=signals_by_repo,
            releases_by_repo=releases_by_repo,
        )
        write_md("changes_last24h.md", activities, since_iso)
        report_paths: List[str] = []
        if not args.no_reports:
            payload = build_report_payload(
                activities=activities,
                filtered_repos=filtered,
                inventory_repo_count=len(repos),
                filtered_repo_count=len(filtered),
                pushed_candidate_count=pushed_candidate_count,
                candidate_repo_count=len(maybe_changed),
                since_iso=since_iso,
                since_dt=since_dt,
                generated_at=now_utc,
                until_iso=until_iso,
                hours_requested=args.hours,
                selected_categories=selected_categories,
                include_other=args.include_other,
                include_archived=args.include_archived,
                include_forks=args.include_forks,
                use_state_window=args.use_state_window,
                events_prefilter_mode=args.events_prefilter_mode,
                events_summary=events_summary,
                events_calibration=events_calibration,
                releases_by_repo=releases_by_repo,
                release_summary=release_summary,
                signals_by_repo=signals_by_repo,
                watchlist_summary=build_watchlist_summary(watchlist),
                lifecycle_summary=lifecycle_for_report(state, since_dt),
                graphql_telemetry=graphql_telemetry,
            )
            report_paths = write_reports(args.reports_dir, payload)

        if args.state:
            state["last_digest"] = {
                "completed_at": iso_utc(now_utc),
                "since": since_iso,
                "until": until_iso,
                "hours_requested": args.hours,
                "state_window_enabled": args.use_state_window,
                "digest_overlap_hours": args.digest_overlap_hours,
                "max_lookback_hours": args.max_lookback_hours,
                "inventory_repos": len(repos),
                "filtered_repos": len(filtered),
                "pushed_at_candidate_repos": pushed_candidate_count,
                "candidate_repos": len(maybe_changed),
                "repos_with_movement": len(activities),
                "events_prefilter_mode": args.events_prefilter_mode,
                "events_calibration_enabled": args.events_calibration,
                "release_mode": args.release_mode,
                "repos_checked_for_releases": release_summary.get("repos_checked", 0),
                "repos_with_releases": release_summary.get("repos_with_releases", 0),
                "graphql_enrichment_mode": args.enrichment_mode,
                "graphql_batch_size": graphql_batch_size,
                "graphql_detail_batches": graphql_telemetry.get("detail_batches", 0),
            }
            save_state(args.state, state)

    except RateLimitDeferred as exc:
        if not args.no_reports:
            write_status_and_manifest(
                args.reports_dir,
                status="deferred",
                reason=infer_deferred_reason(str(exc)),
                now_utc=dt.datetime.now(dt.timezone.utc),
            )
        print(f"[DEFERRED] {exc}", file=sys.stderr)
        return DEFERRED_EXIT_CODE

    print("Wrote changes_last24h.csv")
    print("Wrote changes_last24h.md")
    if not args.no_reports:
        print(f"Wrote {len(report_paths)} report file(s) to {args.reports_dir}")
    print(f"Repos with movement: {len(activities)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
