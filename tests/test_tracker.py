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
                        "default_branch",
                        "commit_count_24h",
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
                        "default_branch": "main",
                        "commit_count_24h": "1",
                        "newest_commit_date": "2026-01-01T00:00:00Z",
                    }
                )
            digest_md_path.write_text(
                "# Changes on default branch since 2026-01-01T00:00:00Z\n\n",
                encoding="utf-8",
            )

            rows = validate_tracker.validate_inventory(inventory_path)
            validate_tracker.validate_watchfeeds(watchfeeds_path, rows)
            validate_tracker.validate_state(state_path, rows)
            validate_tracker.validate_digest(digest_csv_path, digest_md_path)

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
                        }
                    )
            with self.assertRaisesRegex(RuntimeError, "duplicate"):
                validate_tracker.validate_inventory(path)


if __name__ == "__main__":
    unittest.main()
