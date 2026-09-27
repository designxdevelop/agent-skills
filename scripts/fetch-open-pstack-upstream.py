#!/usr/bin/env python3
"""Fetch open-pstack's pinned public source into a new directory for review.

Example: python3 scripts/fetch-open-pstack-upstream.py --output /tmp/pstack-upstream
Use --ref main to inspect the current upstream revision instead of the pin.
"""

import argparse
import json
import re
import shutil
import subprocess
import tarfile
import tempfile
from pathlib import Path, PurePosixPath


METADATA = Path(__file__).resolve().with_name("open-pstack-upstream.json")


def git(*args: str, cwd: Path, capture: bool = False) -> str:
    result = subprocess.run(
        ["git", "-c", "core.hooksPath=/dev/null", *args],
        cwd=cwd,
        check=True,
        text=True,
        stdout=subprocess.PIPE if capture else subprocess.DEVNULL,
        stderr=subprocess.PIPE,
    )
    return result.stdout.strip() if capture else ""


def source_metadata() -> dict[str, str]:
    data = json.loads(METADATA.read_text(encoding="utf-8"))
    for key in ("repository", "revision", "subdirectory"):
        if not isinstance(data.get(key), str) or not data[key]:
            raise ValueError(f"{METADATA}: missing {key}")
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", data["repository"]):
        raise ValueError(f"{METADATA}: repository must be a GitHub owner/repository name")
    subdirectory = PurePosixPath(data["subdirectory"])
    if subdirectory.is_absolute() or any(part in ("", ".", "..") for part in subdirectory.parts):
        raise ValueError(f"{METADATA}: unsafe subdirectory")
    if data["subdirectory"] != subdirectory.as_posix():
        raise ValueError(f"{METADATA}: subdirectory must be normalized")
    return data


def unpack_source(archive: Path, destination: Path, subdirectory: str) -> None:
    prefix = PurePosixPath(subdirectory)
    seen: set[Path] = set()
    with tarfile.open(archive, "r:") as source:
        for member in source:
            path = PurePosixPath(member.name)
            if path == prefix:
                continue
            elif path.is_relative_to(prefix):
                relative = path.relative_to(prefix)
            else:
                raise ValueError(f"unexpected archive path: {member.name}")
            if relative.is_absolute() or any(part in ("", ".", "..") for part in relative.parts):
                raise ValueError(f"unsafe archive path: {member.name}")
            target = destination.joinpath(*relative.parts)
            if member.isdir():
                target.mkdir(parents=True, exist_ok=True)
            elif member.isfile():
                if target in seen:
                    raise ValueError(f"duplicate archive path: {member.name}")
                target.parent.mkdir(parents=True, exist_ok=True)
                with source.extractfile(member) as content, target.open("xb") as output:
                    shutil.copyfileobj(content, output)
                seen.add(target)
            else:
                raise ValueError(f"unsupported archive entry: {member.name}")
    if not (destination / "LICENSE").is_file() or "MIT License" not in (destination / "LICENSE").read_text(encoding="utf-8"):
        raise ValueError("upstream pstack LICENSE is missing or is not an MIT license")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="new directory for the fetched source")
    parser.add_argument("--ref", help="upstream Git ref to fetch (defaults to repository metadata revision)")
    args = parser.parse_args()

    requested_output = args.output.expanduser()
    if requested_output.is_symlink():
        parser.error(f"output is a symlink: {requested_output}")
    output = requested_output.resolve()
    if output.exists():
        parser.error(f"output already exists: {output}")
    if not output.parent.is_dir():
        parser.error(f"output parent does not exist: {output.parent}")

    try:
        metadata = source_metadata()
        with tempfile.TemporaryDirectory(prefix=".open-pstack-fetch-", dir=output.parent) as temporary:
            work = Path(temporary)
            repository = work / "repository"
            repository.mkdir()
            git("init", "-q", cwd=repository)
            git("remote", "add", "origin", f"https://github.com/{metadata['repository']}.git", cwd=repository)
            git("fetch", "--depth", "1", "origin", args.ref or metadata["revision"], cwd=repository)
            revision = git("rev-parse", "FETCH_HEAD^{commit}", cwd=repository, capture=True)
            archive = work / "source.tar"
            git(
                "archive", "--format=tar", f"--output={archive}", revision,
                metadata["subdirectory"], cwd=repository,
            )
            staged = work / "staged"
            staged.mkdir()
            unpack_source(archive, staged, metadata["subdirectory"])
            (staged / "upstream.json").write_text(
                json.dumps({**metadata, "revision": revision}, indent=2) + "\n",
                encoding="utf-8",
            )
            if output.exists():
                raise FileExistsError(f"output appeared during fetch: {output}")
            staged.rename(output)
    except (OSError, ValueError, json.JSONDecodeError, subprocess.CalledProcessError) as error:
        parser.exit(1, f"fetch failed: {error}\n")
    print(f"Fetched {metadata['repository']} at {revision} to {output}")


if __name__ == "__main__":
    main()
