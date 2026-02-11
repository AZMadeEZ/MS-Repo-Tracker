#!/usr/bin/env python3
"""
Microsoft public documentation repo inventory (docs + reference + training + samples).

- Reads orgs from orgs.txt (one org per line)
- Lists all PUBLIC repos in each org
- Classifies repos into docs/reference/training/samples/other
- Writes:
    msft_repo_inventory.csv
    msft_repo_inventory_watchfeeds.csv

Auth:
  Optionally set GITHUB_TOKEN to increase rate limits:
    export GITHUB_TOKEN="ghp_..."

Note:
  This intentionally avoids per-repo topic/file-tree calls (too expensive at Microsoft scale).
"""

from __future__ import annotations

import csv
import os
import re
import sys
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

import requests


API = "https://api.github.com"


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


def gh_get(url: str, token: Optional[str]) -> requests.Response:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "msft-docs-inventory",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    r = requests.get(url, headers=headers, timeout=45)
    # Handle soft failures with clearer messages
    if r.status_code == 404:
        raise RuntimeError(f"404 Not Found: {url}")
    if r.status_code == 403 and "rate limit" in r.text.lower():
        raise RuntimeError("GitHub rate limit hit. Set GITHUB_TOKEN and retry.")
    r.raise_for_status()
    return r


def list_org_repos(org: str, token: Optional[str]) -> List[Dict[str, Any]]:
    repos: List[Dict[str, Any]] = []
    page = 1
    while True:
        url = f"{API}/orgs/{org}/repos?type=public&per_page=100&page={page}&sort=updated&direction=desc"
        batch = gh_get(url, token).json()
        if not batch:
            break
        repos.extend(batch)
        page += 1
    return repos


def classify(org: str, name: str, description: str, homepage: str) -> Tuple[str, int]:
    text = f"{name} {description} {homepage}".strip()
    score = 0

    # Org-based strong signals
    if org in DOC_ORGS:
        return "docs", 100
    if org in TRAINING_ORGS:
        return "training", 100
    if org in SAMPLES_ORGS:
        return "samples", 100

    # Keyword scoring
    if DOC_KEYWORDS.search(text):
        score += 40
    if REFERENCE_KEYWORDS.search(text):
        score += 35
    if TRAINING_KEYWORDS.search(text):
        score += 30
    if SAMPLES_KEYWORDS.search(text):
        score += 25

    # Lightweight name heuristics
    lname = name.lower()
    if "docs" in lname or lname.endswith("-docs") or lname.startswith("docs-"):
        score += 20
    if "reference" in lname or "api" in lname and "docs" in lname:
        score += 15
    if "sample" in lname or "quickstart" in lname:
        score += 15
    if lname.startswith("mslearn-"):
        score += 20

    # Choose category by strongest match (ties resolved by score)
    if score == 0:
        return "other", 0

    # If reference keywords hit strongly, prefer reference
    if REFERENCE_KEYWORDS.search(text):
        return "reference", score
    if TRAINING_KEYWORDS.search(text) or lname.startswith("mslearn-"):
        return "training", score
    if SAMPLES_KEYWORDS.search(text) or "sample" in lname or "quickstart" in lname:
        return "samples", score
    return "docs", score


def make_row(org: str, repo: Dict[str, Any]) -> RepoRow:
    lic = repo.get("license") or {}
    category, score = classify(
        org=org,
        name=repo.get("name") or "",
        description=(repo.get("description") or "") or "",
        homepage=(repo.get("homepage") or "") or "",
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
        license_spdx=lic.get("spdx_id") or "",
        stars=int(repo.get("stargazers_count") or 0),
        forks=int(repo.get("forks_count") or 0),
        open_issues=int(repo.get("open_issues_count") or 0),
        category=category,
        score=score,
    )


def write_csv(path: str, rows: List[RepoRow]) -> None:
    fields = [
        "org","name","full_name","html_url","description","homepage",
        "archived","fork","created_at","updated_at","pushed_at","default_branch",
        "language","license_spdx","stars","forks","open_issues",
        "category","score",
    ]
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({k: getattr(r, k) for k in fields})


def write_watchfeeds(path: str, rows: List[RepoRow]) -> None:
    fields = [
        "full_name",
        "category",
        "default_branch",
        "commits_atom",
        "releases_atom",
    ]
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            if not r.full_name or not r.default_branch:
                continue
            w.writerow({
                "full_name": r.full_name,
                "category": r.category,
                "default_branch": r.default_branch,
                "commits_atom": f"https://github.com/{r.full_name}/commits/{r.default_branch}.atom",
                "releases_atom": f"https://github.com/{r.full_name}/releases.atom",
            })


def main() -> int:
    token = os.environ.get("GITHUB_TOKEN")
    orgs_path = "orgs.txt"
    if not os.path.exists(orgs_path):
        print("Missing orgs.txt (one org per line).", file=sys.stderr)
        return 2

    with open(orgs_path, "r", encoding="utf-8") as f:
        orgs = [line.strip() for line in f if line.strip() and not line.strip().startswith("#")]

    all_rows: List[RepoRow] = []
    for org in orgs:
        try:
            repos = list_org_repos(org, token)
        except Exception as e:
            print(f"[WARN] Skipping org '{org}': {e}", file=sys.stderr)
            continue

        for repo in repos:
            all_rows.append(make_row(org, repo))

    # Keep only docs/reference/training/samples (drop 'other') for your stated goal
    inventory = [r for r in all_rows if r.category != "other"]

    # Sort to put the most recently pushed repos first (highest monitoring value)
    inventory.sort(key=lambda r: (r.pushed_at or ""), reverse=True)

    write_csv("msft_repo_inventory.csv", inventory)
    write_watchfeeds("msft_repo_inventory_watchfeeds.csv", inventory)

    print(f"Wrote {len(inventory)} repos to msft_repo_inventory.csv")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
