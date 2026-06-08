#!/usr/bin/env python3
"""Shared GitHub API helpers for MS-Repo-Tracker."""

from __future__ import annotations

import datetime as dt
import os
import sys
import time
from dataclasses import dataclass
from typing import Any, Dict, Mapping, MutableMapping, Optional

import requests


API_ROOT = os.environ.get("GITHUB_API_ROOT", "https://api.github.com")
API_VERSION = os.environ.get("GITHUB_API_VERSION", "2022-11-28")
DEFERRED_EXIT_CODE = 75


class RateLimitDeferred(RuntimeError):
    """Raised when non-urgent API work should be deferred."""


@dataclass
class GitHubResponse:
    status_code: int
    data: Any
    headers: Mapping[str, str]
    url: str
    not_modified: bool = False


def utc_now() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def iso_utc(value: Optional[dt.datetime] = None) -> str:
    value = value or utc_now()
    if value.tzinfo is None:
        value = value.replace(tzinfo=dt.timezone.utc)
    return value.astimezone(dt.timezone.utc).isoformat().replace("+00:00", "Z")


def reset_epoch_to_iso(value: str) -> str:
    try:
        return iso_utc(dt.datetime.fromtimestamp(int(value), tz=dt.timezone.utc))
    except Exception:
        return value


class GitHubClient:
    def __init__(
        self,
        token: Optional[str],
        user_agent: str,
        api_root: str = API_ROOT,
        timeout: int = 60,
        max_retries: int = 3,
    ) -> None:
        self.token = token
        self.user_agent = user_agent
        self.api_root = api_root.rstrip("/")
        self.timeout = timeout
        self.max_retries = max_retries

    def _url(self, path_or_url: str) -> str:
        if path_or_url.startswith("http://") or path_or_url.startswith("https://"):
            return path_or_url
        return f"{self.api_root}/{path_or_url.lstrip('/')}"

    def _base_headers(self) -> Dict[str, str]:
        headers = {
            "Accept": "application/vnd.github+json",
            "User-Agent": self.user_agent,
            "X-GitHub-Api-Version": API_VERSION,
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    def _retry_wait_seconds(self, response: requests.Response, attempt: int) -> int:
        retry_after = response.headers.get("retry-after")
        if retry_after:
            try:
                return max(1, int(retry_after))
            except ValueError:
                return 60

        remaining = response.headers.get("x-ratelimit-remaining")
        reset_at = response.headers.get("x-ratelimit-reset")
        if remaining == "0" and reset_at:
            try:
                wait = int(reset_at) - int(time.time()) + 5
                return max(1, wait)
            except ValueError:
                pass

        return min(60, max(1, 2**attempt))

    def _is_rate_limited(self, response: requests.Response) -> bool:
        text = response.text.lower()
        return (
            response.status_code in (403, 429)
            and (
                "rate limit" in text
                or "secondary rate" in text
                or "abuse detection" in text
                or response.headers.get("retry-after") is not None
                or response.headers.get("x-ratelimit-remaining") == "0"
            )
        )

    def _request(
        self,
        method: str,
        url: str,
        *,
        headers: Optional[Mapping[str, str]] = None,
        json: Optional[Mapping[str, Any]] = None,
        allow_304: bool = False,
    ) -> requests.Response:
        merged_headers = self._base_headers()
        if headers:
            merged_headers.update(headers)

        for attempt in range(self.max_retries + 1):
            response = requests.request(
                method,
                url,
                headers=merged_headers,
                json=json,
                timeout=self.timeout,
            )

            if allow_304 and response.status_code == 304:
                return response

            if 200 <= response.status_code < 300:
                return response

            if self._is_rate_limited(response):
                wait = self._retry_wait_seconds(response, attempt)
                reset_at = response.headers.get("x-ratelimit-reset")
                if response.headers.get("x-ratelimit-remaining") == "0" and wait > 60:
                    reset_msg = reset_epoch_to_iso(reset_at or "")
                    raise RateLimitDeferred(
                        f"GitHub API budget exhausted until {reset_msg}."
                    )
                if attempt < self.max_retries:
                    sys.stderr.write(
                        f"[WARN] GitHub rate limit response ({response.status_code}); "
                        f"retrying in {wait}s.\n"
                    )
                    time.sleep(wait)
                    continue
                raise RateLimitDeferred(
                    f"GitHub API rate limit response after retries: {response.text[:200]}"
                )

            if response.status_code in (502, 503, 504) and attempt < self.max_retries:
                wait = self._retry_wait_seconds(response, attempt)
                sys.stderr.write(
                    f"[WARN] GitHub transient response ({response.status_code}); "
                    f"retrying in {wait}s.\n"
                )
                time.sleep(wait)
                continue

            if response.status_code == 401:
                raise RuntimeError("Unauthorized (401). Check GITHUB_TOKEN.")

            response.raise_for_status()

        raise RuntimeError("Unexpected GitHub request retry exhaustion.")

    def get_json(
        self,
        path_or_url: str,
        *,
        params: Optional[Mapping[str, Any]] = None,
        cache: Optional[Mapping[str, Any]] = None,
        use_conditional: bool = True,
    ) -> GitHubResponse:
        request = requests.Request("GET", self._url(path_or_url), params=params).prepare()
        url = request.url or self._url(path_or_url)

        headers: Dict[str, str] = {}
        entry: Mapping[str, Any] = {}
        if use_conditional and cache:
            entry = cache.get(url, {}) or {}
            etag = entry.get("etag")
            last_modified = entry.get("last_modified")
            if etag:
                headers["If-None-Match"] = str(etag)
            if last_modified:
                headers["If-Modified-Since"] = str(last_modified)

        response = self._request("GET", url, headers=headers, allow_304=use_conditional)
        if response.status_code == 304:
            return GitHubResponse(
                status_code=response.status_code,
                data=None,
                headers=response.headers,
                url=url,
                not_modified=True,
            )

        data = response.json() if response.text else None
        return GitHubResponse(
            status_code=response.status_code,
            data=data,
            headers=response.headers,
            url=url,
            not_modified=False,
        )

    def graphql(self, query: str, variables: Mapping[str, Any]) -> Dict[str, Any]:
        response = self._request(
            "POST",
            f"{self.api_root}/graphql",
            headers={"Content-Type": "application/json"},
            json={"query": query, "variables": dict(variables)},
        )
        return response.json()

    def rate_limit_status(self) -> Dict[str, Any]:
        response = self.get_json("/rate_limit", use_conditional=False)
        return response.data or {}

    def remaining(self, resource: str) -> Optional[int]:
        status = self.rate_limit_status()
        bucket = (status.get("resources") or {}).get(resource) or {}
        remaining = bucket.get("remaining")
        try:
            return int(remaining)
        except (TypeError, ValueError):
            return None

    def ensure_budget(self, resource: str, minimum_remaining: int) -> None:
        if minimum_remaining <= 0:
            return
        remaining = self.remaining(resource)
        if remaining is None:
            sys.stderr.write(
                f"[WARN] Could not read GitHub {resource} rate budget; continuing.\n"
            )
            return
        if remaining < minimum_remaining:
            raise RateLimitDeferred(
                f"GitHub {resource} budget too low: {remaining} remaining, "
                f"need at least {minimum_remaining}."
            )


def update_conditional_cache(
    cache: MutableMapping[str, Any],
    response: GitHubResponse,
    *,
    item_count: Optional[int] = None,
    repo_full_names: Optional[list[str]] = None,
    has_next: Optional[bool] = None,
) -> None:
    if response.not_modified:
        return

    entry = dict(cache.get(response.url, {}) or {})
    etag = response.headers.get("etag")
    last_modified = response.headers.get("last-modified")
    if etag:
        entry["etag"] = etag
    if last_modified:
        entry["last_modified"] = last_modified
    if item_count is not None:
        entry["item_count"] = item_count
    if repo_full_names is not None:
        entry["repo_full_names"] = repo_full_names
    if has_next is not None:
        entry["has_next"] = has_next
    entry["cached_at"] = iso_utc()
    cache[response.url] = entry
