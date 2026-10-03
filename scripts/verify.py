#!/usr/bin/env python3
"""Run the repository's local and CI checks."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", help="Git revision to compare plugin versions against")
    args = parser.parse_args()
    packaging = [sys.executable, str(ROOT / "scripts/sync-plugin-packaging.py"), "--check"]
    if args.base:
        packaging.extend(["--base", args.base])
    commands = [
        [sys.executable, str(ROOT / "scripts/check-markdown.py")],
        [
            sys.executable,
            "-B",
            "-m",
            "unittest",
            "discover",
            "-s",
            str(ROOT / "scripts/tests"),
            "-p",
            "test_*.py",
        ],
        packaging,
        [sys.executable, str(ROOT / "scripts/build-openai-submission.py")],
    ]
    for command in commands:
        result = subprocess.run(command, cwd=ROOT)
        if result.returncode:
            return result.returncode
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
