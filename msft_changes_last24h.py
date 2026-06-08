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
BOT_MARKERS = ("[bot]", "dependabot", "renovate", "github-actions", "learn-build-service")
DEPENDENCY_MARKERS = ("bump ", "dependabot", "renovate", "dependency", "dependencies")
RELEASE_MARKERS = ("release", "version", "ga ", "generally available", "preview")
SECURITY_MARKERS = ("security", "cve-", "vulnerab", "credential", "secret")


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
    parts = [activity.full_name, activity.name, activity.category]
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
        "default_branch",
        "commit_count_24h",
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
                "default_branch": activity.default_branch,
                "commit_count_24h": activity.commit_count,
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
        "generated_at": iso_utc(generated_at),
        "window": {
            "since": since_iso,
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
    top_repos = payload.get("top_repos") or []
    activities = payload.get("activities") or []

    generated_at = str(payload.get("generated_at") or "")
    title_date = generated_at[:10] if len(generated_at) >= 10 else generated_at

    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# Microsoft Repo Change Brief - {title_date}\n\n")
        f.write(f"Generated: `{generated_at}`\n\n")
        f.write(f"Window since: `{window.get('since', '')}`\n\n")

        f.write("## Summary\n\n")
        f.write("| Metric | Value |\n")
        f.write("| --- | ---: |\n")
        f.write(f"| Inventory repositories | {totals.get('inventory_repos', 0)} |\n")
        f.write(f"| Repositories after filters | {totals.get('filtered_repos', 0)} |\n")
        f.write(f"| `pushed_at` candidates | {totals.get('pushed_at_candidate_repos', 0)} |\n")
        f.write(f"| Enrichment candidates | {totals.get('candidate_repos', 0)} |\n")
        f.write(f"| Repositories with movement | {totals.get('repos_with_movement', 0)} |\n")
        f.write(f"| Default-branch commits | {totals.get('default_branch_commits', 0)} |\n")
        f.write("\n")

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

        if top_repos:
            f.write("## Top Repositories\n\n")
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
        for activity in payload.get("activities") or []:
            full_name = activity.get("full_name")
            if full_name:
                repo_counter[str(full_name)] += 1
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
    return {
        "schema_version": 1,
        "generated_at": iso_utc(),
        "report_count": len(daily),
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
        f.write("# Microsoft Repo Tracker Report Index\n\n")
        f.write(f"Generated: `{payload.get('generated_at', '')}`\n\n")
        trends = payload.get("trends") or {}
        for label, trend in (("Last 7 Days", trends.get("last_7_days") or {}), ("Last 30 Days", trends.get("last_30_days") or {})):
            f.write(f"## {label}\n\n")
            f.write("| Metric | Value |\n")
            f.write("| --- | ---: |\n")
            f.write(f"| Reports | {trend.get('report_count', 0)} |\n")
            f.write(f"| Repositories with movement | {trend.get('repos_with_movement', 0)} |\n")
            f.write(f"| Default-branch commits | {trend.get('default_branch_commits', 0)} |\n")
            f.write(f"| Releases | {trend.get('release_count', 0)} |\n\n")

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


def write_reports(report_dir: str, payload: Dict[str, Any]) -> List[str]:
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
        write_report_markdown(path, payload)

    return paths + write_report_index(report_dir)


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
