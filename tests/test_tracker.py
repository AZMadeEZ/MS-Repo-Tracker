from __future__ import annotations

import csv
import datetime as dt
import json
import tempfile
import unittest
from pathlib import Path

import msft_changes_last24h as changes
import msft_docs_inventory as inventory
from scripts import validate_tracker


class DigestFilterTests(unittest.TestCase):
    def test_blank_categories_default_to_focused_set(self) -> None:
        self.assertEqual(changes.category_filter("", False), changes.DEFAULT_DIGEST_CATEGORIES)

    def test_include_other_extends_default_set(self) -> None:
        selected = changes.category_filter("", True)
        self.assertIsNotNone(selected)
        self.assertIn("other", selected or set())
        self.assertIn("docs", selected or set())

    def test_categories_all_disables_filter(self) -> None:
        self.assertIsNone(changes.category_filter("all", False))

    def test_explicit_categories_are_trimmed(self) -> None:
        self.assertEqual(changes.category_filter("docs, samples", False), {"docs", "samples"})

    def test_state_window_extends_to_last_successful_digest(self) -> None:
        now = dt.datetime(2026, 6, 8, 12, 0, tzinfo=dt.timezone.utc)
        since = changes.compute_since_dt(
            now,
            24,
            state={"last_digest": {"completed_at": "2026-06-06T12:00:00Z"}},
            use_state_window=True,
            overlap_hours=2,
            max_lookback_hours=168,
        )
        self.assertEqual(since, dt.datetime(2026, 6, 6, 10, 0, tzinfo=dt.timezone.utc))

    def test_state_window_caps_long_outages(self) -> None:
        now = dt.datetime(2026, 6, 8, 12, 0, tzinfo=dt.timezone.utc)
        since = changes.compute_since_dt(
            now,
            24,
            state={"last_digest": {"completed_at": "2026-05-01T12:00:00Z"}},
            use_state_window=True,
            overlap_hours=2,
            max_lookback_hours=168,
        )
        self.assertEqual(since, dt.datetime(2026, 6, 1, 12, 0, tzinfo=dt.timezone.utc))

    def test_load_state_accepts_utf8_bom(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "state.json"
            path.write_text('{"schema_version": 1}', encoding="utf-8-sig")
            self.assertEqual(changes.load_state(str(path))["schema_version"], 1)

    def test_extract_event_repo_names_reads_github_event_payloads(self) -> None:
        events = [
            {"type": "PushEvent", "repo": {"name": "MicrosoftDocs/azure-docs"}},
            {"type": "WatchEvent", "repo": {"name": "not-a-full-name"}},
            {"type": "ReleaseEvent", "repo": {"name": "Azure-Samples/sample"}},
        ]
        self.assertEqual(
            changes.extract_event_repo_names(events),
            {"MicrosoftDocs/azure-docs", "Azure-Samples/sample"},
        )

    def test_events_intersect_keeps_pushed_candidates_when_events_are_empty(self) -> None:
        repos = [
            changes.RepoInput(full_name="Org/one"),
            changes.RepoInput(full_name="Org/two"),
        ]
        selected = changes.apply_events_prefilter("intersect", repos, [repos[0]], set())
        self.assertEqual([repo.full_name for repo in selected], ["Org/one"])

    def test_write_reports_creates_latest_and_dated_files(self) -> None:
        activity = changes.RepoActivity(
            full_name="Org/repo",
            org="Org",
            name="repo",
            category="docs",
            default_branch="main",
            commit_count=1,
            newest_commit_date="2026-01-01T00:00:00Z",
            commits=[],
        )
        payload = changes.build_report_payload(
            activities=[activity],
            filtered_repos=[changes.RepoInput(full_name="Org/repo", org="Org", name="repo")],
            inventory_repo_count=2,
            filtered_repo_count=1,
            pushed_candidate_count=1,
            candidate_repo_count=1,
            since_iso="2026-01-01T00:00:00Z",
            since_dt=dt.datetime(2026, 1, 1, tzinfo=dt.timezone.utc),
            generated_at=dt.datetime(2026, 1, 2, 3, 4, tzinfo=dt.timezone.utc),
            until_iso="2026-01-02T03:04:00Z",
            hours_requested=24,
            selected_categories={"docs"},
            include_other=False,
            include_archived=False,
            include_forks=False,
            use_state_window=True,
            events_prefilter_mode="off",
            events_summary=None,
            events_calibration=None,
            releases_by_repo={},
            release_summary={"enabled": False},
            signals_by_repo={"Org/repo": {"score": 50, "tags": ["human-authored"]}},
            watchlist_summary={"repo_count": 1},
            lifecycle_summary={},
            graphql_telemetry={"mode": "two-stage", "batch_size": 35},
        )
        with tempfile.TemporaryDirectory() as tmp:
            paths = changes.write_reports(str(Path(tmp) / "reports"), payload)
            self.assertEqual(len(paths), 14)
            self.assertTrue((Path(tmp) / "reports" / "latest.json").exists())
            self.assertTrue((Path(tmp) / "reports" / "latest.summary.json").exists())
            self.assertTrue((Path(tmp) / "reports" / "2026-01-02.md").exists())
            self.assertTrue((Path(tmp) / "reports" / "latest.consumer.md").exists())
            self.assertTrue((Path(tmp) / "reports" / "2026-01-02.consumer.md").exists())
            self.assertTrue((Path(tmp) / "reports" / "2026-01-02.summary.json").exists())
            self.assertTrue((Path(tmp) / "reports" / "latest.events.ndjson").exists())
            self.assertTrue((Path(tmp) / "reports" / "2026-01-02.events.ndjson").exists())
            self.assertTrue((Path(tmp) / "reports" / "index.md").exists())
            self.assertTrue((Path(tmp) / "reports" / "manifest.json").exists())
            self.assertTrue((Path(tmp) / "reports" / "status.json").exists())

    def test_product_area_summary_keeps_compact_top_links(self) -> None:
        records = [
            {
                "repo": "Azure/repo",
                "product_area": "Azure",
                "change_type": "release",
                "notability_score": 100,
                "noise_level": "low",
                "headline": "Release one",
                "commit_url": "https://github.com/Azure/repo/commit/1",
                "committed_at": "2026-01-01T00:00:00Z",
                "event_id": "commit:provider:Azure/repo:1",
                "labels": ["watchlist"],
            }
        ]
        payload = {"releases": {"items": [{"repo_full_name": "Azure/repo"}]}}
        summary = changes.build_product_area_summary(records, payload)

        self.assertEqual(summary[0]["product_area"], "Azure")
        self.assertEqual(summary[0]["release_count"], 1)
        self.assertEqual(summary[0]["top_events"][0]["headline"], "Release one")
        self.assertNotIn("labels", summary[0]["top_events"][0])
        self.assertNotIn("event_id", summary[0]["top_events"][0])

    def test_build_event_stream_records_emits_release_events(self) -> None:
        payload = {
            "generated_at": "2026-01-02T00:00:00Z",
            "window": {"since": "2026-01-01T00:00:00Z", "until": "2026-01-02T00:00:00Z"},
            "activities": [
                {
                    "full_name": "Azure/repo",
                    "org": "Azure",
                    "name": "repo",
                    "category": "samples",
                    "repo_type": "samples",
                    "product_area": "Azure",
                    "audience": "developer",
                    "default_branch": "main",
                    "signal": {"score": 80, "tags": ["watchlist"]},
                    "commits": [],
                    "releases": [],
                }
            ],
            "releases": {
                "items": [
                    {
                        "repo_full_name": "Azure/repo",
                        "tag_name": "v1.2.3",
                        "name": "Release v1.2.3",
                        "published_at": "2026-01-01T12:00:00Z",
                        "html_url": "https://github.com/Azure/repo/releases/tag/v1.2.3",
                        "prerelease": False,
                        "draft": False,
                    }
                ]
            },
        }

        records = changes.build_event_stream_records(payload)

        self.assertEqual(len(records), 1)
        release = records[0]
        self.assertEqual(release["event_type"], "release")
        self.assertEqual(release["dedupe_key"], "release:Azure/repo:v1.2.3")
        self.assertEqual(release["release_tag"], "v1.2.3")
        self.assertEqual(release["release_url"], "https://github.com/Azure/repo/releases/tag/v1.2.3")
        self.assertEqual(release["source"]["api"], "rest")
        self.assertEqual(release["customer_visible"], "true")

    def test_notable_changes_prioritize_security_and_cap_release_bursts(self) -> None:
        records = [
            {
                "event_id": "release-1",
                "dedupe_key": "release:Azure/repo:v1",
                "repo": "Azure/repo",
                "change_type": "release",
                "notability_score": 100,
                "noise_level": "low",
                "committed_at": "2026-01-02T12:00:00Z",
                "headline": "Release v1",
            },
            {
                "event_id": "release-2",
                "dedupe_key": "release:Azure/repo:v2",
                "repo": "Azure/repo",
                "change_type": "release",
                "notability_score": 100,
                "noise_level": "low",
                "committed_at": "2026-01-02T11:00:00Z",
                "headline": "Release v2",
            },
            {
                "event_id": "release-3",
                "dedupe_key": "release:Azure/repo:v3",
                "repo": "Azure/repo",
                "change_type": "release",
                "notability_score": 100,
                "noise_level": "low",
                "committed_at": "2026-01-02T10:00:00Z",
                "headline": "Release v3",
            },
            {
                "event_id": "security-1",
                "dedupe_key": "commit:security",
                "repo": "Azure/security",
                "change_type": "security_fix",
                "notability_score": 100,
                "noise_level": "low",
                "committed_at": "2026-01-01T00:00:00Z",
                "headline": "Fix security issue",
            },
        ]

        notable = changes.notable_changes_from_events(records)

        self.assertEqual(notable[0]["event_id"], "security-1")
        self.assertEqual(
            [item["event_id"] for item in notable if item["repo"] == "Azure/repo"],
            ["release-1", "release-2"],
        )

    def test_build_top_links_prefers_repo_diversity(self) -> None:
        notable = [
            {"event_id": "one", "repo": "Org/a", "commit_url": "https://example.test/a1", "headline": "A1"},
            {"event_id": "two", "repo": "Org/a", "commit_url": "https://example.test/a2", "headline": "A2"},
            {"event_id": "three", "repo": "Org/b", "commit_url": "https://example.test/b1", "headline": "B1"},
        ]

        links = changes.build_top_links(notable, limit=2)

        self.assertEqual([link["repo"] for link in links], ["Org/a", "Org/b"])

    def test_watchlist_scores_human_watched_repo_above_bot_noise(self) -> None:
        watched = changes.RepoActivity(
            full_name="Org/repo",
            org="Org",
            name="repo",
            category="docs",
            default_branch="main",
            commit_count=2,
            newest_commit_date="2026-01-01T00:00:00Z",
            commits=[
                changes.CommitInfo(
                    oid="1",
                    committed_date="2026-01-01T00:00:00Z",
                    headline="Add migration guide",
                    url="https://example.test/1",
                    author="Ada",
                )
            ],
        )
        noise = changes.RepoActivity(
            full_name="Org/noise",
            org="Org",
            name="noise",
            category="docs",
            default_branch="main",
            commit_count=2,
            newest_commit_date="2026-01-01T00:00:00Z",
            commits=[
                changes.CommitInfo(
                    oid="2",
                    committed_date="2026-01-01T00:00:00Z",
                    headline="Bump requests from 1 to 2",
                    url="https://example.test/2",
                    author="dependabot[bot] (@dependabot[bot])",
                )
            ],
        )
        watchlist = {
            "repos": {"org/repo"},
            "orgs": set(),
            "keywords": {"migration"},
            "products": [],
        }
        self.assertGreater(
            changes.score_activity(watched, [], watchlist)["score"],
            changes.score_activity(noise, [], watchlist)["score"],
        )

    def test_events_calibration_counts_intersect_risk(self) -> None:
        filtered = [
            changes.RepoInput(full_name="Org/a"),
            changes.RepoInput(full_name="Org/b"),
            changes.RepoInput(full_name="Org/c"),
        ]
        calibration = changes.build_events_calibration(
            filtered=filtered,
            pushed_candidates=[filtered[0], filtered[1]],
            event_candidate_names={"Org/a", "Org/c", "Org/not-in-inventory"},
            events_summary={"enabled": True},
        )
        self.assertEqual(calibration["intersection_candidates"], 1)
        self.assertEqual(calibration["union_candidates"], 3)
        self.assertEqual(calibration["intersect_potential_miss_count"], 1)

    def test_adaptive_batch_size_shrinks_on_low_budget(self) -> None:
        batch_size, meta = changes.resolve_graphql_batch_size(
            requested=0,
            repo_count=600,
            max_commits=8,
            remaining=150,
        )
        self.assertLessEqual(batch_size, 8)
        self.assertEqual(meta["strategy"], "very-low-budget")


class InventoryHelperTests(unittest.TestCase):
    def test_read_orgs_strips_utf8_bom(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "orgs.txt"
            path.write_text("\ufeffPowerShell\n# skip\nAzure\n", encoding="utf-8")
            self.assertEqual(inventory.read_orgs(str(path)), ["PowerShell", "Azure"])

    def test_write_csv_uses_lf_line_endings(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "inventory.csv"
            row = inventory.RepoRow(
                org="TestOrg",
                name="repo",
                full_name="TestOrg/repo",
                html_url="https://github.com/TestOrg/repo",
                description="",
                homepage="",
                archived=False,
                fork=False,
                created_at="2026-01-01T00:00:00Z",
                updated_at="2026-01-01T00:00:00Z",
                pushed_at="2026-01-01T00:00:00Z",
                default_branch="main",
                language="Python",
                license_spdx="MIT",
                stars=1,
                forks=2,
                open_issues=3,
                category="other",
                score=0,
            )
            inventory.write_csv(str(path), [row])
            content = path.read_bytes()
            self.assertIn(b"\n", content)
            self.assertNotIn(b"\r\n", content)

    def test_response_has_next_parses_link_header(self) -> None:
        self.assertTrue(inventory.response_has_next({"Link": '<x>; rel="next"'}))
        self.assertFalse(inventory.response_has_next({"Link": '<x>; rel="last"'}))

    def test_lifecycle_summary_detects_new_and_changed_repos(self) -> None:
        before = [
            inventory.RepoRow(
                org="Org",
                name="repo",
                full_name="Org/repo",
                html_url="https://github.com/Org/repo",
                description="",
                homepage="",
                archived=False,
                fork=False,
                created_at="2026-01-01T00:00:00Z",
                updated_at="2026-01-01T00:00:00Z",
                pushed_at="2026-01-01T00:00:00Z",
                default_branch="main",
                language="Python",
                license_spdx="MIT",
                stars=1,
                forks=2,
                open_issues=3,
                category="docs",
                score=40,
            )
        ]
        after = [
            inventory.RepoRow(
                org="Org",
                name="repo",
                full_name="Org/repo",
                html_url="https://github.com/Org/repo",
                description="",
                homepage="",
                archived=True,
                fork=False,
                created_at="2026-01-01T00:00:00Z",
                updated_at="2026-01-02T00:00:00Z",
                pushed_at="2026-01-02T00:00:00Z",
                default_branch="main",
                language="Python",
                license_spdx="MIT",
                stars=1,
                forks=2,
                open_issues=3,
                category="docs",
                score=40,
            ),
            inventory.RepoRow(
                org="Org",
                name="new",
                full_name="Org/new",
                html_url="https://github.com/Org/new",
                description="",
                homepage="",
                archived=False,
                fork=False,
                created_at="2026-01-02T00:00:00Z",
                updated_at="2026-01-02T00:00:00Z",
                pushed_at="2026-01-02T00:00:00Z",
                default_branch="main",
                language="Python",
                license_spdx="MIT",
                stars=1,
                forks=2,
                open_issues=3,
                category="docs",
                score=40,
            ),
        ]
        summary = inventory.build_lifecycle_summary(
            before,
            after,
            completed_orgs={"Org"},
            mode="incremental",
            completed_at="2026-01-02T00:00:00Z",
        )
        self.assertEqual(summary["counts"]["new_repos"], 1)
        self.assertEqual(summary["counts"]["archived_changed"], 1)


class ValidationScriptTests(unittest.TestCase):
    def test_validate_tracker_accepts_minimal_valid_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            inventory_path = root / "inventory.csv"
            watchfeeds_path = root / "watchfeeds.csv"
            state_path = root / "state.json"
            digest_csv_path = root / "changes.csv"
            digest_md_path = root / "changes.md"

            with inventory_path.open("w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=inventory.CSV_FIELDS, lineterminator="\n")
                writer.writeheader()
                writer.writerow(
                    {
                        "org": "TestOrg",
                        "name": "repo",
                        "full_name": "TestOrg/repo",
                        "html_url": "https://github.com/TestOrg/repo",
                        "description": "",
                        "homepage": "",
                        "archived": "False",
                        "fork": "False",
                        "created_at": "",
                        "updated_at": "",
                        "pushed_at": "",
                        "default_branch": "main",
                        "language": "",
                        "license_spdx": "",
                        "stars": "0",
                        "forks": "0",
                        "open_issues": "0",
                        "category": "other",
                        "score": "0",
                        "repo_type": "other",
                        "product_area": "Unknown",
                        "audience": "unknown",
                        "classification_confidence": "0.25",
                        "classification_reason": "fallback:other",
                        "classification_version": "2026-06-08",
                    }
                )

            with watchfeeds_path.open("w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(
                    f,
                    fieldnames=[
                        "full_name",
                        "category",
                        "default_branch",
                        "commits_atom",
                        "releases_atom",
                    ],
                    lineterminator="\n",
                )
                writer.writeheader()
                writer.writerow(
                    {
                        "full_name": "TestOrg/repo",
                        "category": "other",
                        "default_branch": "main",
                        "commits_atom": "https://github.com/TestOrg/repo/commits/main.atom",
                        "releases_atom": "https://github.com/TestOrg/repo/releases.atom",
                    }
                )

            state_path.write_text(
                json.dumps(
                    {
                        "schema_version": 1,
                        "orgs": {"TestOrg": {"last_successful_scan_at": "2026-01-01T00:00:00Z"}},
                        "last_run": {"repos_written": 1},
                    }
                ),
                encoding="utf-8",
            )

            with digest_csv_path.open("w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(
                    f,
                    fieldnames=[
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
                    ],
                    lineterminator="\n",
                )
                writer.writeheader()
                writer.writerow(
                    {
                        "full_name": "TestOrg/repo",
                        "org": "TestOrg",
                        "name": "repo",
                        "category": "other",
                        "repo_type": "other",
                        "product_area": "Unknown",
                        "audience": "unknown",
                        "default_branch": "main",
                        "commit_count_24h": "1",
                        "commit_count_window": "1",
                        "window_since": "2026-01-01T00:00:00Z",
                        "window_until": "2026-01-02T00:00:00Z",
                        "hours_requested": "24",
                        "state_window_enabled": "True",
                        "newest_commit_date": "2026-01-01T00:00:00Z",
                    }
                )
            digest_md_path.write_text(
                "# Changes on default branch since 2026-01-01T00:00:00Z\n\n",
                encoding="utf-8",
            )
            report_dir = root / "reports"
            report_dir.mkdir()
            report_payload = {
                "schema_version": 1,
                "artifact_type": "tracker-report",
                "artifact_version": changes.ARTIFACT_VERSION,
                "schema_url": changes.REPORT_SCHEMA_URL,
                "generated_at": "2026-01-01T00:00:00Z",
                "window": {
                    "since": "2026-01-01T00:00:00Z",
                    "until": "2026-01-02T00:00:00Z",
                    "hours_requested": 24,
                    "state_window_enabled": True,
                },
                "totals": {"repos_with_movement": 1},
                "summaries": {"signals": {"high_signal": []}},
                "top_repos": [],
                "graphql": {"mode": "two-stage"},
                "releases": {"summary": {"enabled": False}, "items": []},
                "event_stream": {
                    "schema_url": changes.EVENT_SCHEMA_URL,
                    "latest_path": str(report_dir / "latest.events.ndjson"),
                    "dated_path": str(report_dir / "2026-01-01.events.ndjson"),
                    "event_count": 1,
                    "commit_event_count": 1,
                    "release_event_count": 0,
                },
                "activities": [
                    {
                        "full_name": "TestOrg/repo",
                        "org": "TestOrg",
                        "name": "repo",
                        "category": "other",
                        "repo_type": "other",
                        "product_area": "Unknown",
                        "audience": "unknown",
                        "default_branch": "main",
                        "signal": {},
                        "releases": [],
                        "commits": [
                            {
                                "oid": "abc123",
                                "committed_date": "2026-01-01T00:00:00Z",
                                "headline": "Add docs",
                                "url": "https://github.com/TestOrg/repo/commit/abc123",
                                "author": "Ada",
                                "pr_number": 1,
                                "pr_title": "Add docs",
                                "pr_url": "https://github.com/TestOrg/repo/pull/1",
                            }
                        ],
                    }
                ],
            }
            for name in ("latest.json", "2026-01-01.json"):
                (report_dir / name).write_text(json.dumps(report_payload), encoding="utf-8")
            summary_payload = {
                "schema_version": 1,
                "artifact_type": "tracker-summary",
                "artifact_version": changes.ARTIFACT_VERSION,
                "schema_url": changes.SUMMARY_SCHEMA_URL,
                "generated_at": "2026-01-01T00:00:00Z",
                "freshness": {"latest_report_stale": False},
                "window": report_payload["window"],
                "totals": report_payload["totals"],
                "event_stream": report_payload["event_stream"],
                "plain_english_summary": ["One useful change landed."],
                "top_links": [],
                "product_area_summary": [],
                "noise_summary": {},
                "artifact_links": {},
            }
            for name in ("latest.summary.json", "2026-01-01.summary.json"):
                (report_dir / name).write_text(json.dumps(summary_payload), encoding="utf-8")
            for name in ("latest.md", "2026-01-01.md"):
                (report_dir / name).write_text(
                    (
                        "# Microsoft Ecosystem Daily Brief - 2026-01-01\n\n"
                        "> Status: Fresh at generation.\n\n"
                        "## Plain-English Summary\n\n"
                        "- One useful change landed.\n\n"
                        "## What Changed That Matters\n\n"
                        "| Repository | Score | Change | Actor | Noise | Headline | Time |\n"
                        "| --- | ---: | --- | --- | --- | --- | --- |\n"
                        "| [TestOrg/repo](https://github.com/TestOrg/repo) | 10 | Feature | human | low | [Add docs](https://github.com/TestOrg/repo/pull/1) | `2026-01-01T00:00:00Z` |\n\n"
                        "## Today's Top Links\n\n"
                        "| Priority | Repository | Why read it |\n"
                        "| ---: | --- | --- |\n"
                        "| 1 | [TestOrg/repo](https://github.com/TestOrg/repo) | [Feature signal](https://github.com/TestOrg/repo/pull/1) |\n\n"
                        "## Noise and Automation\n\n"
                        "- No medium/high-noise automation cluster was detected.\n\n"
                        "<details>\n<summary>Show collection settings and diagnostics</summary>\n\n"
                        "</details>\n\n"
                        "<details>\n<summary>Show raw repository activity</summary>\n\n"
                        "</details>\n"
                    ),
                    encoding="utf-8",
                )
            consumer_text = (
                "# Microsoft Ecosystem Brief - 2026-01-01\n\n"
                "> Fresh as of 2026-01-01 00:00 UTC.\n\n"
                "## What To Look At First\n\n"
                "No high-signal links were selected for this window.\n\n"
                "## Product Area Briefings\n\n"
                "No product-area rollup was generated for this window.\n\n"
                "## Release Radar\n\n"
                "No release items were detected in this window.\n\n"
                "## Security And Admin Attention\n\n"
                "These are not automatically vulnerabilities.\n\n"
                "## What Was Mostly Noise\n\n"
                "0 event(s) looked automated.\n\n"
                "## Data Confidence\n\n"
                "- Source: test fixture.\n"
            )
            for name in ("latest.consumer.md", "2026-01-01.consumer.md"):
                (report_dir / name).write_text(consumer_text, encoding="utf-8")
            (report_dir / "index.json").write_text(
                json.dumps(
                    {
                        "schema_version": 1,
                        "artifact_type": "tracker-report-index",
                        "artifact_version": changes.ARTIFACT_VERSION,
                        "schema_url": changes.REPORT_INDEX_SCHEMA_URL,
                        "daily": [],
                    }
                ),
                encoding="utf-8",
            )
            (report_dir / "index.md").write_text(
                "# Microsoft Ecosystem Change Reports\n\n[Read today's brief ->](latest.md)\n\n",
                encoding="utf-8",
            )
            event_record = {
                "schema_version": 1,
                "artifact_type": "tracker-event",
                "artifact_version": changes.ARTIFACT_VERSION,
                "schema_url": changes.EVENT_SCHEMA_URL,
                "event_id": "github_commit:TestOrg/repo:abc123",
                "event_type": "commit",
                "dedupe_key": "commit:abc123",
                "repo": "TestOrg/repo",
                "org": "TestOrg",
                "repo_name": "repo",
                "category": "other",
                "repo_type": "other",
                "product_area": "Unknown",
                "audience": "unknown",
                "default_branch": "main",
                "committed_at": "2026-01-01T00:00:00Z",
                "headline": "Add docs",
                "author": "Ada",
                "actor_type": "human",
                "commit_oid": "abc123",
                "commit_url": "https://github.com/TestOrg/repo/commit/abc123",
                "pr_number": 1,
                "pr_title": "Add docs",
                "pr_url": "https://github.com/TestOrg/repo/pull/1",
                "change_type": "feature",
                "noise_level": "low",
                "customer_visible": "unknown",
                "notability_score": 10,
                "notability_reason": ["human_authored"],
                "window_since": "2026-01-01T00:00:00Z",
                "window_until": "2026-01-02T00:00:00Z",
                "retrieved_at": "2026-01-01T00:00:00Z",
                "source": {
                    "provider": "github",
                    "api": "graphql",
                    "repo_url": "https://github.com/TestOrg/repo",
                },
            }
            event_text = json.dumps(event_record, sort_keys=True, separators=(",", ":")) + "\n"
            for name in ("latest.events.ndjson", "2026-01-01.events.ndjson"):
                (report_dir / name).write_text(event_text, encoding="utf-8")
            status_payload = {
                "schema_version": 1,
                "artifact_type": "tracker-status",
                "artifact_version": changes.ARTIFACT_VERSION,
                "schema_url": changes.STATUS_SCHEMA_URL,
                "generated_at": "2026-01-01T00:00:00Z",
                "last_attempt_at": "2026-01-01T00:00:00Z",
                "last_success_at": "2026-01-01T00:00:00Z",
                "status": "complete",
                "reason": "success",
                "latest_report_generated_at": "2026-01-01T00:00:00Z",
                "latest_report_stale": False,
                "freshness": {
                    "max_age_hours": 30,
                    "age_hours": 0,
                    "latest_report_stale": False,
                    "state": "fresh",
                },
            }
            (report_dir / "status.json").write_text(json.dumps(status_payload), encoding="utf-8")
            manifest_payload = {
                "schema_version": 1,
                "artifact_type": "tracker-manifest",
                "artifact_version": changes.ARTIFACT_VERSION,
                "schema_url": changes.MANIFEST_SCHEMA_URL,
                "generated_at": "2026-01-01T00:00:00Z",
                "status": {
                    "status": "complete",
                    "reason": "success",
                    "latest_report_generated_at": "2026-01-01T00:00:00Z",
                    "latest_report_stale": False,
                },
                "freshness": status_payload["freshness"],
                "artifacts": [
                    {"name": "latest_human_report", "artifact_type": "markdown", "path": str(report_dir / "latest.md"), "required": True},
                    {"name": "latest_consumer_report", "artifact_type": "markdown", "path": str(report_dir / "latest.consumer.md"), "required": True},
                    {"name": "latest_machine_report", "artifact_type": "json", "path": str(report_dir / "latest.json"), "required": True, "schema_url": changes.REPORT_SCHEMA_URL},
                    {"name": "latest_summary", "artifact_type": "json", "path": str(report_dir / "latest.summary.json"), "required": True, "schema_url": changes.SUMMARY_SCHEMA_URL},
                    {"name": "latest_event_stream", "artifact_type": "ndjson", "path": str(report_dir / "latest.events.ndjson"), "required": True, "schema_url": changes.EVENT_SCHEMA_URL},
                    {"name": "tracker_status", "artifact_type": "json", "path": str(report_dir / "status.json"), "required": True, "schema_url": changes.STATUS_SCHEMA_URL},
                ],
            }
            (report_dir / "manifest.json").write_text(json.dumps(manifest_payload), encoding="utf-8")

            rows = validate_tracker.validate_inventory(inventory_path)
            validate_tracker.validate_watchfeeds(watchfeeds_path, rows)
            validate_tracker.validate_state(state_path, rows)
            digest_rows = validate_tracker.validate_digest(digest_csv_path, digest_md_path)
            report_payload = validate_tracker.validate_reports(report_dir, digest_rows)
            validate_tracker.validate_event_stream(report_dir, report_payload)
            validate_tracker.validate_manifest_status(report_dir)

    def test_validate_tracker_rejects_duplicate_full_names(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "inventory.csv"
            with path.open("w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=inventory.CSV_FIELDS, lineterminator="\n")
                writer.writeheader()
                for _ in range(2):
                    writer.writerow(
                        {
                            "org": "TestOrg",
                            "name": "repo",
                            "full_name": "TestOrg/repo",
                            "html_url": "https://github.com/TestOrg/repo",
                            "description": "",
                            "homepage": "",
                            "archived": "False",
                            "fork": "False",
                            "created_at": "",
                            "updated_at": "",
                            "pushed_at": "",
                            "default_branch": "main",
                            "language": "",
                            "license_spdx": "",
                            "stars": "0",
                            "forks": "0",
                            "open_issues": "0",
                            "category": "other",
                            "score": "0",
                            "repo_type": "other",
                            "product_area": "Unknown",
                            "audience": "unknown",
                            "classification_confidence": "0.25",
                            "classification_reason": "fallback:other",
                            "classification_version": "2026-06-08",
                        }
                    )
            with self.assertRaisesRegex(RuntimeError, "duplicate"):
                validate_tracker.validate_inventory(path)


if __name__ == "__main__":
    unittest.main()
