import hashlib
import json
from pathlib import Path
import stat
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest
import warnings
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

from jsonschema import Draft202012Validator

from scripts.validate_project_archive import SCHEMA_PATH, validate_archive


LOG_PATH = "project-status-log.md"
LOG_BYTES = (
    b"# Project Status Log\n\n## Current state\n\n"
    b"Next action: Verify deliverable R01.\n\n## Dated log\n\n"
    b"2026-11-22: Recorded working revision R01.\n"
)


def inventory_entry(path, role, content):
    return {"path": path, "role": role, "sha256": hashlib.sha256(content).hexdigest()}


def manifest_for(files, package_id="SYNTHETIC"):
    return {
        "manifest_schema_version": "1.0.0",
        "package_id": package_id,
        "package_revision": "R01",
        "status": "review",
        "created_utc": "2026-11-22T17:00:00Z",
        "files": [
            inventory_entry(path, "documentation" if path == LOG_PATH else "artifact", content)
            for path, content in files.items()
        ],
    }


class ArchiveValidationTest(unittest.TestCase):
    def setUp(self):
        folder = TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        self.archive = Path(folder.name) / "project.zip"

    def write_archive(self, manifest, files, wrapper="", extra=()):
        with ZipFile(self.archive, "w", compression=ZIP_DEFLATED) as archive:
            if wrapper:
                archive.writestr(wrapper, b"")
            encoded = json.dumps(manifest) if isinstance(manifest, dict) else manifest
            archive.writestr(wrapper + "manifest.json", encoded)
            for path, content in files.items():
                archive.writestr(wrapper + path, content)
            for path, content in extra:
                archive.writestr(path, content)

    def assert_rejected(self, manifest, files, message, **options):
        self.write_archive(manifest, files, **options)
        with self.assertRaisesRegex(ValueError, message):
            validate_archive(self.archive)

    def test_schema_and_valid_archives_across_domains(self):
        Draft202012Validator.check_schema(json.loads(SCHEMA_PATH.read_text(encoding="utf-8")))
        cases = [
            ("CONTROLS", "artifact/point-schedule.csv", b"point,type\nP01,AI\n", ""),
            ("LIGHTING", "artifact/fixture-schedule.csv", b"fixture,type\nF01,A\n", "LIGHT-R01/"),
        ]
        for package, path, content, wrapper in cases:
            with self.subTest(package=package):
                files = {LOG_PATH: LOG_BYTES, path: content}
                self.write_archive(manifest_for(files, package), files, wrapper)
                self.assertEqual(validate_archive(self.archive), (package, "R01", 2))

    def test_status_log_inventory_is_required_once_with_documentation_role(self):
        for entries in (
            [],
            [inventory_entry(LOG_PATH, "artifact", LOG_BYTES)],
            [inventory_entry(LOG_PATH, "documentation", LOG_BYTES)] * 2,
        ):
            with self.subTest(entries=entries):
                files = {LOG_PATH: LOG_BYTES}
                self.assert_rejected(
                    {**manifest_for(files), "files": entries}, files, "exactly one"
                )

    def test_missing_file_unlisted_file_and_changed_bytes_fail(self):
        files = {LOG_PATH: LOG_BYTES, "schedule.csv": b"original"}
        manifest = manifest_for(files)
        for actual, message in (
            ({"schedule.csv": b"original"}, r"Missing from ZIP: 'project-status-log.md'"),
            ({**files, "unlisted.csv": b"extra"}, r"Unlisted in manifest.json: 'unlisted.csv'"),
            ({**files, LOG_PATH: b"changed log"}, r"SHA-256 mismatch: 'project-status-log.md'"),
            ({**files, "schedule.csv": b"changed schedule"}, r"SHA-256 mismatch: 'schedule.csv'"),
        ):
            with self.subTest(message=message):
                self.assert_rejected(manifest, actual, message)

    def test_duplicate_inventory_and_zip_members_fail(self):
        files = {LOG_PATH: LOG_BYTES, "schedule.csv": b"content"}
        manifest = manifest_for(files)
        manifest["files"].append(manifest["files"][1])
        self.assert_rejected(manifest, files, "Duplicate inventory path")
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)
            self.assert_rejected(
                manifest_for(files), files, "Duplicate ZIP member",
                extra=[("schedule.csv", b"duplicate")],
            )

    def test_ambiguous_and_nonportable_paths_fail(self):
        files = {LOG_PATH: LOG_BYTES, "Evidence/primary.csv": b"primary"}
        symlink = ZipInfo("link")
        symlink.create_system = 3
        symlink.external_attr = (stat.S_IFLNK | 0o777) << 16
        for path, message in (
            ("evidence/secondary.csv", "Ambiguous ZIP paths"),
            ("../outside.csv", "Unsafe or ambiguous archive path"),
            (r"C:\\outside.csv", "Unsafe or ambiguous archive path"),
            ("Evidence", "both a file and a directory"),
            (symlink, "not a regular file"),
        ):
            with self.subTest(path=path):
                self.assert_rejected(
                    manifest_for(files), files, message, extra=[(path, b"extra")]
                )
        self.assert_rejected(
            manifest_for(files), files, "one wrapper folder",
            wrapper="project/", extra=[("outside.csv", b"extra")],
        )

    def test_invalid_manifest_version_timestamp_and_json_fail(self):
        files = {LOG_PATH: LOG_BYTES}
        manifest = manifest_for(files)
        self.assert_rejected(
            {**manifest, "manifest_schema_version": "0.1.0"}, files, "manifest_schema_version"
        )
        self.assert_rejected(
            {**manifest, "created_utc": "2026-02-30T17:00:00Z"}, files, "created_utc"
        )
        self.assert_rejected(
            '{"package_id":"FIRST","package_id":"SECOND"}', files, "Duplicate JSON key"
        )
        self.assert_rejected(
            {**manifest, "files": [*manifest["files"], inventory_entry(
                "manifest.json", "documentation", b"self"
            )]},
            files, "cannot list itself",
        )

    def test_command_exit_status_blocks_a_failed_archive(self):
        files = {LOG_PATH: LOG_BYTES}
        command = [
            sys.executable, str(SCHEMA_PATH.parents[1] / "scripts" / "validate_project_archive.py"),
            str(self.archive),
        ]
        self.write_archive(manifest_for(files), files)
        passed = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(passed.returncode, 0, passed.stderr)
        self.assertIn("1 file verified", passed.stdout)
        self.write_archive(manifest_for(files), {})
        failed = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(failed.returncode, 1)
        self.assertIn("Missing from ZIP", failed.stderr)


if __name__ == "__main__":
    unittest.main()
