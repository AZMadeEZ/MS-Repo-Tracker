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
import sys
from collections import Counter
from dataclasses import dataclass
from typing import Any, Dict, List, Mapping, Optional, Set, Tuple

from github_api import (
    DEFERRED_EXIT_CODE,
    GitHubClient,
    RateLimitDeferred,
    iso_utc,
    update_conditional_cache,
)


DEFAULT_DIGEST_CATEGORIES = {"docs", "reference", "training", "samples"}
DEFAULT_STATE_PATH = "msft_repo_tracker_state.json"


@dataclass
class RepoInput:
    full_name: str
    org: str = ""
    name: str = ""
    category: str = ""
    pushed_at: str = ""
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
                    category=(row.get("category") or "other").strip() or "other",
                    pushed_at=(row.get("pushed_at") or "").strip(),
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


def build_query(repos: List[RepoInput]) -> str:
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


def fetch_activity(
    client: GitHubClient,
    repos: List[RepoInput],
    since_iso: str,
    max_commits: int,
    include_archived: bool,
    include_forks: bool,
) -> List[RepoActivity]:
    activities: List[RepoActivity] = []
    for batch in chunked(repos, 35):
        query = build_query(batch)
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
    return activities


def write_csv(path: str, activities: List[RepoActivity], max_commits: int) -> None:
    fields = [
        "full_name",
        "org",
        "name",
        "category",
        "default_branch",
        "commit_count_24h",
        "newest_commit_date",
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


def activity_to_dict(activity: RepoActivity) -> Dict[str, Any]:
    return {
        "full_name": activity.full_name,
        "org": activity.org,
        "name": activity.name,
        "category": activity.category,
        "default_branch": activity.default_branch,
        "commit_count": activity.commit_count,
        "newest_commit_date": activity.newest_commit_date,
        "commits": [commit_to_dict(commit) for commit in activity.commits],
    }


def build_report_payload(
    *,
    activities: List[RepoActivity],
    inventory_repo_count: int,
    filtered_repo_count: int,
    pushed_candidate_count: int,
    candidate_repo_count: int,
    since_iso: str,
    generated_at: dt.datetime,
    hours_requested: int,
    selected_categories: Optional[Set[str]],
    include_other: bool,
    include_archived: bool,
    include_forks: bool,
    use_state_window: bool,
    events_prefilter_mode: str,
    events_summary: Optional[Dict[str, Any]],
) -> Dict[str, Any]:
    category_counts = Counter(activity.category or "uncategorized" for activity in activities)
    org_counts = Counter(activity.org or activity.full_name.split("/")[0] for activity in activities)
    total_commits = sum(activity.commit_count for activity in activities)

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
        },
        "summaries": {
            "by_category": dict(sorted(category_counts.items())),
            "by_org": dict(sorted(org_counts.items())),
        },
        "top_repos": [activity_to_dict(activity) for activity in activities[:20]],
        "activities": [activity_to_dict(activity) for activity in activities],
        "events_prefilter": events_summary
        or {
            "enabled": False,
            "mode": events_prefilter_mode,
        },
    }


def md_escape(value: Any) -> str:
    return str(value if value is not None else "").replace("|", "\\|").replace("\n", " ")


def write_report_markdown(path: str, payload: Dict[str, Any]) -> None:
    totals = payload.get("totals") or {}
    summaries = payload.get("summaries") or {}
    window = payload.get("window") or {}
    filters = payload.get("filters") or {}
    events = payload.get("events_prefilter") or {}
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
            f.write("| Repository | Category | Commits | Newest commit |\n")
            f.write("| --- | --- | ---: | --- |\n")
            for activity in top_repos:
                full_name = md_escape(activity.get("full_name", ""))
                repo_url = f"https://github.com/{activity.get('full_name', '')}"
                f.write(
                    f"| [{full_name}]({repo_url}) | "
                    f"{md_escape(activity.get('category', ''))} | "
                    f"{activity.get('commit_count', 0)} | "
                    f"`{activity.get('newest_commit_date', '')}` |\n"
                )
            f.write("\n")

        f.write("## Repository Details\n\n")
        if not activities:
            f.write("No default-branch movement matched the current filters.\n")
            return

        for activity in activities:
            f.write(
                f"### {md_escape(activity.get('full_name', ''))} "
                f"({activity.get('commit_count', 0)} commit(s))\n\n"
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

    return paths


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
    parser.add_argument("--no-budget-check", action="store_true")
    parser.add_argument("--state", default="", help="Tracker state JSON path.")
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
        client = GitHubClient(token=token, user_agent="msft-changes-digest")

        if args.events_prefilter_mode != "off":
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

        if maybe_changed and not args.no_budget_check:
            client.ensure_budget("graphql", args.min_graphql_remaining)

        activities = fetch_activity(
            client=client,
            repos=maybe_changed,
            since_iso=since_iso,
            max_commits=args.max_commits,
            include_archived=args.include_archived,
            include_forks=args.include_forks,
        )

        write_csv("changes_last24h.csv", activities, args.max_commits)
        write_md("changes_last24h.md", activities, since_iso)
        report_paths: List[str] = []
        if not args.no_reports:
            payload = build_report_payload(
                activities=activities,
                inventory_repo_count=len(repos),
                filtered_repo_count=len(filtered),
                pushed_candidate_count=pushed_candidate_count,
                candidate_repo_count=len(maybe_changed),
                since_iso=since_iso,
                generated_at=now_utc,
                hours_requested=args.hours,
                selected_categories=selected_categories,
                include_other=args.include_other,
                include_archived=args.include_archived,
                include_forks=args.include_forks,
                use_state_window=args.use_state_window,
                events_prefilter_mode=args.events_prefilter_mode,
                events_summary=events_summary,
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
