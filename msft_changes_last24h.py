#!/usr/bin/env python3
"""
Summarize changes on the default branch in the last N hours for repos listed in an inventory CSV.

Inputs:
  - inventory CSV produced by your repo inventory script(s)
    Must include: full_name
    Optional: pushed_at, archived, fork, category, org

Outputs:
  - changes_last24h.csv : machine-friendly
  - changes_last24h.md  : human-friendly digest

Usage:
  export GITHUB_TOKEN="..."  # recommended
  python msft_changes_last24h.py --input msft_repo_inventory.csv --hours 24 --max-commits 5

Notes:
  - "main branch" is interpreted as the repo's default branch.
  - Uses pushed_at as a *prefilter* if present to avoid querying thousands of repos.
  - Uses GitHub GraphQL to fetch commit history since a timestamp on defaultBranchRef.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import os
import sys
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import quote

import requests


GQL_ENDPOINT = "https://api.github.com/graphql"


@dataclass
class RepoInput:
    full_name: str                    # Owner/Repo
    org: str = ""
    name: str = ""
    category: str = ""
    pushed_at: str = ""               # ISO string
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


def parse_bool(val: str) -> Optional[bool]:
    if val is None:
        return None
    s = str(val).strip().lower()
    if s in ("true", "1", "yes", "y"):
        return True
    if s in ("false", "0", "no", "n"):
        return False
    return None


def read_inventory(path: str) -> List[RepoInput]:
    with open(path, "r", encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        cols = {c.strip() for c in (r.fieldnames or [])}

        if "full_name" not in cols:
            raise RuntimeError(f"{path} is missing required column: full_name")

        out: List[RepoInput] = []
        for row in r:
            full_name = (row.get("full_name") or "").strip()
            if not full_name or "/" not in full_name:
                continue

            org = (row.get("org") or "").strip()
            name = (row.get("name") or "").strip()
            if not org or not name:
                # fall back to splitting full_name
                parts = full_name.split("/", 1)
                org = org or parts[0]
                name = name or parts[1]

            out.append(
                RepoInput(
                    full_name=full_name,
                    org=org,
                    name=name,
                    category=(row.get("category") or "").strip(),
                    pushed_at=(row.get("pushed_at") or "").strip(),
                    archived=parse_bool(row.get("archived")),
                    fork=parse_bool(row.get("fork")),
                )
            )
        return out


def iso_utc(dt_obj: dt.datetime) -> str:
    # Ensure Z suffix
    if dt_obj.tzinfo is None:
        dt_obj = dt_obj.replace(tzinfo=dt.timezone.utc)
    return dt_obj.astimezone(dt.timezone.utc).isoformat().replace("+00:00", "Z")


def parse_iso(s: str) -> Optional[dt.datetime]:
    if not s:
        return None
    try:
        # GitHub uses Z; normalize
        if s.endswith("Z"):
            s = s[:-1] + "+00:00"
        return dt.datetime.fromisoformat(s)
    except Exception:
        return None


def gql_request(query: str, variables: Dict[str, Any], token: Optional[str]) -> Dict[str, Any]:
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "msft-changes-digest",
    }
    if token:
        headers["Authorization"] = f"bearer {token}"

    resp = requests.post(
        GQL_ENDPOINT,
        headers=headers,
        json={"query": query, "variables": variables},
        timeout=60,
    )

    if resp.status_code == 401:
        raise RuntimeError("Unauthorized (401). Check GITHUB_TOKEN.")
    if resp.status_code == 403:
        raise RuntimeError(f"Forbidden (403). Possibly rate-limited or token lacks access. Body: {resp.text[:200]}")
    resp.raise_for_status()

    payload = resp.json()
    if "errors" in payload and payload["errors"]:
        # Keep going when possible; caller can handle missing data entries.
        # Still surface the first error for debugging.
        first = payload["errors"][0]
        msg = first.get("message", "GraphQL error")
        # Don't hard-fail here; return payload so we can salvage partial data.
        sys.stderr.write(f"[WARN] GraphQL returned errors: {msg}\n")
    return payload.get("data", {})


def chunked(lst: List[Any], n: int) -> List[List[Any]]:
    return [lst[i : i + n] for i in range(0, len(lst), n)]


def build_query(repos: List[RepoInput]) -> str:
    # One GraphQL query with many repository() calls using aliases.
    # defaultBranchRef -> target(Commit) -> history(since: $since, first: $maxCommits)
    parts = [
        "query($since: GitTimestamp!, $maxCommits: Int!) {"
    ]
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
    repos: List[RepoInput],
    since_iso: str,
    max_commits: int,
    token: Optional[str],
    include_archived: bool,
    include_forks: bool,
) -> List[RepoActivity]:
    activities: List[RepoActivity] = []
    for batch in chunked(repos, 35):  # 35 keeps queries comfortably sized
        query = build_query(batch)
        data = gql_request(query, {"since": since_iso, "maxCommits": max_commits}, token)

        for i, repo in enumerate(batch):
            node = data.get(f"r{i}")
            if not node:
                continue

            # Reconcile server-truth flags with CLI include options in one place.
            if (not include_archived and node.get("isArchived") is True) or (
                not include_forks and node.get("isFork") is True
            ):
                continue

            dbr = node.get("defaultBranchRef") or {}
            branch_name = (dbr.get("name") or "").strip()
            target = dbr.get("target") or {}
            history = target.get("history") or {}

            total = int(history.get("totalCount") or 0)
            if total <= 0:
                continue

            commit_nodes = history.get("nodes") or []
            commits: List[CommitInfo] = []
            newest_date = ""

            for c in commit_nodes:
                assoc = c.get("associatedPullRequests") or {}
                prs = assoc.get("nodes") or []
                pr = prs[0] if prs else None

                committed_date = c.get("committedDate") or ""
                if committed_date and (not newest_date or committed_date > newest_date):
                    newest_date = committed_date

                commits.append(
                    CommitInfo(
                        oid=c.get("oid") or "",
                        committed_date=committed_date,
                        headline=(c.get("messageHeadline") or "").strip(),
                        url=c.get("url") or "",
                        author=summarize_author(c.get("author") or {}),
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

    # Sort: most commits, then most recent activity
    activities.sort(key=lambda a: (a.commit_count, a.newest_commit_date), reverse=True)
    return activities


def write_csv(path: str, activities: List[RepoActivity], max_commits: int) -> None:
    # Flatten first N commits into columns
    fields = [
        "full_name", "org", "name", "category",
        "default_branch", "commit_count_24h", "newest_commit_date",
    ]
    for i in range(1, max_commits + 1):
        fields += [
            f"commit{i}_date",
            f"commit{i}_headline",
            f"commit{i}_url",
            f"commit{i}_author",
            f"commit{i}_pr_number",
            f"commit{i}_pr_title",
            f"commit{i}_pr_url",
        ]

    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()

        for a in activities:
            row: Dict[str, Any] = {
                "full_name": a.full_name,
                "org": a.org,
                "name": a.name,
                "category": a.category,
                "default_branch": a.default_branch,
                "commit_count_24h": a.commit_count,
                "newest_commit_date": a.newest_commit_date,
            }
            for idx in range(max_commits):
                if idx < len(a.commits):
                    c = a.commits[idx]
                    row.update({
                        f"commit{idx+1}_date": c.committed_date,
                        f"commit{idx+1}_headline": c.headline,
                        f"commit{idx+1}_url": c.url,
                        f"commit{idx+1}_author": c.author,
                        f"commit{idx+1}_pr_number": c.pr_number or "",
                        f"commit{idx+1}_pr_title": c.pr_title or "",
                        f"commit{idx+1}_pr_url": c.pr_url or "",
                    })
                else:
                    row.update({
                        f"commit{idx+1}_date": "",
                        f"commit{idx+1}_headline": "",
                        f"commit{idx+1}_url": "",
                        f"commit{idx+1}_author": "",
                        f"commit{idx+1}_pr_number": "",
                        f"commit{idx+1}_pr_title": "",
                        f"commit{idx+1}_pr_url": "",
                    })
            w.writerow(row)


def write_md(path: str, activities: List[RepoActivity], since_iso: str) -> None:
    # Group by category then org for readability
    def key_cat(a: RepoActivity) -> str:
        return a.category.strip() or "uncategorized"

    grouped: Dict[str, Dict[str, List[RepoActivity]]] = {}
    for a in activities:
        cat = key_cat(a)
        grouped.setdefault(cat, {})
        grouped[cat].setdefault(a.org or a.full_name.split("/")[0], [])
        grouped[cat][a.org or a.full_name.split("/")[0]].append(a)

    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# Changes on default branch since {since_iso}\n\n")
        f.write(f"Repos with movement: **{len(activities)}**\n\n")

        for cat in sorted(grouped.keys()):
            f.write(f"## {cat}\n\n")
            orgs = grouped[cat]
            for org in sorted(orgs.keys()):
                f.write(f"### {org}\n\n")
                # Sort per org: most commits first
                org_items = sorted(orgs[org], key=lambda a: (a.commit_count, a.newest_commit_date), reverse=True)
                for a in org_items:
                    f.write(f"- **{a.full_name}** (`{a.default_branch}`) — **{a.commit_count}** commit(s)\n")
                    for c in a.commits:
                        pr_part = ""
                        if c.pr_url and c.pr_title:
                            pr_part = f" — PR: [{c.pr_title} #{c.pr_number}]({c.pr_url})"
                        f.write(f"  - [{c.headline}]({c.url}) — {c.committed_date} {('— ' + c.author) if c.author else ''}{pr_part}\n")
                    f.write("\n")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, help="Inventory CSV (e.g., msft_repo_inventory.csv)")
    ap.add_argument("--hours", type=int, default=24, help="Lookback window in hours (default 24)")
    ap.add_argument("--max-commits", type=int, default=5, help="Max commit headlines per repo (default 5)")
    ap.add_argument("--include-archived", action="store_true", help="Include archived repos (default: exclude)")
    ap.add_argument("--include-forks", action="store_true", help="Include forks (default: exclude)")
    ap.add_argument("--categories", default="", help="Comma-separated categories to include (optional)")
    args = ap.parse_args()

    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        sys.stderr.write("[WARN] GITHUB_TOKEN not set. You may hit low rate limits.\n")

    repos = read_inventory(args.input)

    # Basic filtering based on inventory columns
    cats_filter = {c.strip() for c in args.categories.split(",") if c.strip()}
    filtered: List[RepoInput] = []
    for r in repos:
        if cats_filter and (r.category.strip() not in cats_filter):
            continue
        if not args.include_archived and r.archived is True:
            continue
        if not args.include_forks and r.fork is True:
            continue
        filtered.append(r)

    # Compute since timestamp
    now_utc = dt.datetime.now(dt.timezone.utc)
    since_dt = now_utc - dt.timedelta(hours=args.hours)
    since_iso = iso_utc(since_dt)

    # Prefilter using pushed_at if present (saves a TON of queries)
    maybe_changed: List[RepoInput] = []
    if any(r.pushed_at for r in filtered):
        for r in filtered:
            pdt = parse_iso(r.pushed_at)
            if pdt is None:
                # If unknown, keep it (safe but might increase queries slightly)
                maybe_changed.append(r)
                continue
            if pdt >= since_dt:
                maybe_changed.append(r)
    else:
        maybe_changed = filtered

    sys.stderr.write(f"[INFO] Inventory repos: {len(repos)}\n")
    sys.stderr.write(f"[INFO] After filters: {len(filtered)}\n")
    sys.stderr.write(f"[INFO] After pushed_at prefilter: {len(maybe_changed)}\n")

    activities = fetch_activity(
        repos=maybe_changed,
        since_iso=since_iso,
        max_commits=args.max_commits,
        token=token,
        include_archived=args.include_archived,
        include_forks=args.include_forks,
    )

    write_csv("changes_last24h.csv", activities, args.max_commits)
    write_md("changes_last24h.md", activities, since_iso)

    print("Wrote changes_last24h.csv")
    print("Wrote changes_last24h.md")
    print(f"Repos with movement: {len(activities)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
