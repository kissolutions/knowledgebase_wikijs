"""Validate the manifest and file inventory of a KIS project ZIP."""

import argparse
from datetime import datetime
import hashlib
import json
from pathlib import Path
import stat
import sys
import unicodedata
from zipfile import BadZipFile, ZipFile, ZipInfo
import zlib

from jsonschema import Draft202012Validator


SCHEMA_PATH = (
    Path(__file__).resolve().parents[1]
    / "governance-and-doctrine"
    / "project-archive-manifest.schema.json"
)
MANIFEST = "manifest.json"


def check_path(path: str) -> None:
    if (
        any(segment in {"", ".", ".."} for segment in path.split("/"))
        or any(
            character in "\\:" or ord(character) < 32 or ord(character) == 127
            for character in path
        )
    ):
        raise ValueError(f"Unsafe or ambiguous archive path: {path!r}")


def index_archive(archive: ZipFile) -> tuple[ZipInfo, dict[str, ZipInfo]]:
    entries: set[str] = set()
    files: dict[str, ZipInfo] = {}
    canonical_paths: dict[str, str] = {}
    for member in archive.infolist():
        name = member.orig_filename
        is_directory = name.endswith("/")
        path = name[:-1] if is_directory else name
        check_path(path)
        if name in entries:
            raise ValueError(f"Duplicate ZIP member: {name!r}")
        entries.add(name)

        file_type = (
            stat.S_IFMT(member.external_attr >> 16) if member.create_system == 3 else 0
        )
        expected_type = stat.S_IFDIR if is_directory else stat.S_IFREG
        if file_type not in (0, expected_type):
            raise ValueError(f"ZIP member is not a regular file or directory: {name!r}")

        prefix = ""
        for segment in path.split("/"):
            prefix = f"{prefix}/{segment}" if prefix else segment
            key = unicodedata.normalize("NFC", prefix).casefold()
            existing = canonical_paths.setdefault(key, prefix)
            if existing != prefix:
                raise ValueError(f"Ambiguous ZIP paths: {existing!r} and {prefix!r}")

        if not is_directory:
            files[path] = member

    for entry_name in entries:
        parts = entry_name.split("/")
        for end in range(1, len(parts)):
            prefix = "/".join(parts[:end])
            if prefix in files:
                raise ValueError(f"ZIP path is both a file and a directory: {prefix!r}")

    if MANIFEST not in files:
        wrappers = [
            path.split("/")[0] + "/"
            for path in files
            if path.count("/") == 1 and path.endswith("/" + MANIFEST)
        ]
        if len(wrappers) != 1 or not all(name.startswith(wrappers[0]) for name in entries):
            raise ValueError("Expected manifest.json at the ZIP root or inside one wrapper folder")
        wrapper = wrappers[0]
        files = {path[len(wrapper):]: member for path, member in files.items()}

    manifest = files.pop(MANIFEST)
    return manifest, files


def unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON key in {MANIFEST}: {key!r}")
        result[key] = value
    return result


def reject_json_constant(value: str) -> None:
    raise ValueError(f"Invalid JSON value in {MANIFEST}: {value}")


def read_manifest(archive: ZipFile, member: ZipInfo) -> dict:
    data = json.loads(
        archive.read(member).decode("utf-8"),
        object_pairs_hook=unique_object,
        parse_constant=reject_json_constant,
    )
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    error = next(Draft202012Validator(schema).iter_errors(data), None)
    if error is not None:
        location = error.json_path.removeprefix("$")
        message = error.message
        if error.validator in {"contains", "minContains", "maxContains"}:
            message = error.schema.get("description", message)
        raise ValueError(f"{MANIFEST}{location}: {message}")
    try:
        datetime.fromisoformat(data["created_utc"].replace("Z", "+00:00"))
    except ValueError as error:
        raise ValueError(f"{MANIFEST}.created_utc is not a valid UTC timestamp") from error
    return data


def validate_archive(zip_path: Path) -> tuple[str, str, int]:
    with ZipFile(zip_path) as archive:
        manifest_member, files = index_archive(archive)
        manifest = read_manifest(archive, manifest_member)

        expected_hashes: dict[str, str] = {}
        for item in manifest["files"]:
            path = item["path"]
            check_path(path)
            if path == MANIFEST:
                raise ValueError(f"{MANIFEST} cannot list itself")
            if path in expected_hashes:
                raise ValueError(f"Duplicate inventory path in {MANIFEST}: {path!r}")
            expected_hashes[path] = item["sha256"]

        missing = sorted(expected_hashes.keys() - files.keys())
        unlisted = sorted(files.keys() - expected_hashes.keys())
        if missing or unlisted:
            problems = [f"Missing from ZIP: {path!r}" for path in missing]
            problems.extend(f"Unlisted in {MANIFEST}: {path!r}" for path in unlisted)
            raise ValueError("\n".join(problems))

        for path, expected_hash in expected_hashes.items():
            digest = hashlib.sha256()
            with archive.open(files[path]) as handle:
                for block in iter(lambda: handle.read(1024 * 1024), b""):
                    digest.update(block)
            if digest.hexdigest() != expected_hash:
                raise ValueError(f"SHA-256 mismatch: {path!r}")

    return manifest["package_id"], manifest["package_revision"], len(files)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path, help="Path to the completed project ZIP")
    args = parser.parse_args()
    try:
        package_id, revision, file_count = validate_archive(args.archive)
    except (BadZipFile, EOFError, OSError, RuntimeError, ValueError, zlib.error) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    noun = "file" if file_count == 1 else "files"
    print(f"PASS: {package_id!r} revision {revision!r}, {file_count} {noun} verified")
    return 0


if __name__ == "__main__":
    sys.exit(main())
