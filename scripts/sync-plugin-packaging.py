#!/usr/bin/env python3
"""Keep the Claude, Codex, and Cursor dxd-skills plugins aligned with skills/.

Sync mode (default) links every canonical skill into the Codex plugin and bumps
all three manifest versions together: a patch bump when skill content changes,
a minor bump when a skill is added or removed. --check validates without writing.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Tuple


PLUGIN = "dxd-skills"
ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
README = ROOT / "README.md"
CODEX_SKILLS_DIR = ROOT / "plugins" / PLUGIN / "skills"
MANIFESTS = (
    ROOT / ".claude-plugin" / "plugin.json",
    ROOT / ".cursor-plugin" / "plugin.json",
    ROOT / "plugins" / PLUGIN / ".codex-plugin" / "plugin.json",
)
CONTENT_PATHS = ("skills", f"plugins/{PLUGIN}/skills")
VERSION_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")
VERSION_FIELD_RE = re.compile(r'("version"\s*:\s*")([^"]+)(")', re.MULTILINE)
SKILL_PATH_RE = re.compile(r"^skills/([^/]+)/SKILL\.md$")

Version = Tuple[int, int, int]


def run_git(*args: str, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=check,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def parse_version(raw: str) -> Version:
    match = VERSION_RE.fullmatch(raw)
    if not match:
        raise ValueError(f"expected semantic version X.Y.Z, got {raw!r}")
    return tuple(int(part) for part in match.groups())


def format_version(version: Version) -> str:
    return ".".join(str(part) for part in version)


def manifest_version(path: Path, revision: str | None = None) -> Version:
    if revision:
        relative = path.relative_to(ROOT).as_posix()
        result = run_git("show", f"{revision}:{relative}", check=False)
        if result.returncode != 0:
            raise FileNotFoundError(f"manifest missing at {revision}: {relative}")
        payload = json.loads(result.stdout)
    else:
        payload = json.loads(path.read_text())
    return parse_version(payload["version"])


def write_manifest_version(path: Path, version: Version) -> bool:
    raw = path.read_text()
    updated, count = VERSION_FIELD_RE.subn(
        rf"\g<1>{format_version(version)}\g<3>", raw, count=1
    )
    if count != 1:
        raise ValueError(
            f"could not find exactly one version field in {path.relative_to(ROOT)}"
        )
    if updated == raw:
        return False
    path.write_text(updated)
    return True


def canonical_skills() -> list[str]:
    return sorted(
        path.name
        for path in SKILLS_DIR.iterdir()
        if path.is_dir() and (path / "SKILL.md").is_file()
    )


def skills_at(revision: str) -> set[str] | None:
    result = run_git("ls-tree", "-r", "--name-only", revision, "--", "skills", check=False)
    if result.returncode != 0:
        return None
    return {
        match.group(1)
        for line in result.stdout.splitlines()
        if (match := SKILL_PATH_RE.match(line))
    }


def expected_link_target(name: str) -> str:
    return os.path.relpath(SKILLS_DIR / name, CODEX_SKILLS_DIR)


def link_issues() -> list[str]:
    expected = set(canonical_skills())
    issues: list[str] = []

    for name in sorted(expected):
        link = CODEX_SKILLS_DIR / name
        target = expected_link_target(name)
        if not link.is_symlink():
            issues.append(f"missing symlink: {link.relative_to(ROOT)} -> {target}")
        elif os.readlink(link) != target:
            issues.append(
                f"wrong symlink: {link.relative_to(ROOT)} -> {os.readlink(link)}; expected {target}"
            )

    if CODEX_SKILLS_DIR.is_dir():
        for entry in sorted(CODEX_SKILLS_DIR.iterdir()):
            if entry.name not in expected:
                kind = "stale symlink" if entry.is_symlink() else "unexpected entry"
                issues.append(f"{kind}: {entry.relative_to(ROOT)}")

    return issues


def sync_links() -> list[str]:
    expected = set(canonical_skills())
    changes: list[str] = []
    CODEX_SKILLS_DIR.mkdir(parents=True, exist_ok=True)

    for entry in sorted(CODEX_SKILLS_DIR.iterdir()):
        if entry.name in expected:
            continue
        if not entry.is_symlink():
            raise RuntimeError(f"refusing to remove non-symlink {entry.relative_to(ROOT)}")
        entry.unlink()
        changes.append(f"removed stale link {entry.relative_to(ROOT)}")

    for name in sorted(expected):
        link = CODEX_SKILLS_DIR / name
        target = expected_link_target(name)
        if link.is_symlink() and os.readlink(link) == target:
            continue
        if link.exists() and not link.is_symlink():
            raise RuntimeError(f"refusing to replace non-symlink {link.relative_to(ROOT)}")
        if link.is_symlink():
            link.unlink()
        link.symlink_to(target)
        changes.append(f"linked {link.relative_to(ROOT)} -> {target}")

    return changes


def frontmatter_issues() -> list[str]:
    issues: list[str] = []
    for name in canonical_skills():
        relative = f"skills/{name}/SKILL.md"
        lines = (SKILLS_DIR / name / "SKILL.md").read_text().splitlines()
        if not lines or lines[0].strip() != "---":
            issues.append(f"{relative}: missing YAML frontmatter")
            continue
        try:
            end = lines.index("---", 1)
        except ValueError:
            issues.append(f"{relative}: unterminated YAML frontmatter")
            continue
        fields = dict(
            line.split(":", 1) for line in lines[1:end] if re.match(r"^[a-z-]+:", line)
        )
        if fields.get("name", "").strip() != name:
            issues.append(f"{relative}: frontmatter name must be {name!r}")
        if not fields.get("description", "").strip():
            issues.append(f"{relative}: frontmatter description is empty")
    return issues


def readme_issues() -> list[str]:
    readme = README.read_text()
    return [
        f"README.md: Available Skills table is missing {name}"
        for name in canonical_skills()
        if f"(skills/{name}/SKILL.md)" not in readme
    ]


def changed_plugin_content(base: str | None) -> bool:
    if base:
        output = run_git("diff", "--name-only", f"{base}...HEAD", "--", *CONTENT_PATHS).stdout
    else:
        # Staged, unstaged, and untracked changes relative to HEAD.
        output = run_git("status", "--porcelain", "--", *CONTENT_PATHS).stdout
    return bool(output.strip())


def baseline(base: str | None) -> tuple[Version | None, set[str] | None]:
    revision = base or "HEAD"
    versions: list[Version] = []
    for path in MANIFESTS:
        try:
            versions.append(manifest_version(path, revision))
        except FileNotFoundError:
            continue
    return (max(versions) if versions else None), skills_at(revision)


def required_version(base: str | None) -> Version | None:
    """Lowest version the manifests must carry, or None when no bump is due."""
    prior_version, prior_skills = baseline(base)
    if prior_version is None or not changed_plugin_content(base):
        return None
    major, minor, patch = prior_version
    if prior_skills is not None and prior_skills != set(canonical_skills()):
        return (major, minor + 1, 0)
    return (major, minor, patch + 1)


def validate(base: str | None) -> list[str]:
    issues = link_issues() + frontmatter_issues() + readme_issues()
    current = [manifest_version(path) for path in MANIFESTS]
    if len(set(current)) != 1:
        rendered = ", ".join(format_version(version) for version in current)
        issues.append(f"plugin manifest versions differ: {rendered}")

    required = required_version(base)
    if required and min(current) < required:
        issues.append(
            f"plugin content changed; manifests need version {format_version(required)} or higher"
        )
    return issues


def synchronize(target_version: str | None) -> list[str]:
    current = max(manifest_version(path) for path in MANIFESTS)
    changes = sync_links()
    required = required_version(None)

    if target_version:
        target = parse_version(target_version)
        if target < current:
            raise ValueError("--version cannot move plugin manifests backwards")
    else:
        target = max(current, required) if required else current

    for path in MANIFESTS:
        if write_manifest_version(path, target):
            changes.append(f"set {path.relative_to(ROOT)} version to {format_version(target)}")
    return changes


def report(issues: list[str]) -> int:
    for issue in issues:
        print(f"ERROR: {issue}", file=sys.stderr)
    return 1 if issues else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="validate without writing")
    parser.add_argument(
        "--base",
        help="git revision used to verify that changed plugin content includes a version bump",
    )
    parser.add_argument(
        "--version",
        help="set an explicit aligned version instead of the automatic bump",
    )
    args = parser.parse_args()

    if args.check and args.version:
        parser.error("--check and --version cannot be used together")

    try:
        if args.check:
            if report(validate(args.base)):
                return 1
            print("Plugin packaging is synchronized.")
            return 0

        changes = synchronize(args.version)
        print("\n".join(changes) if changes else "Plugin packaging was already synchronized.")
        return report(validate(None))
    except (OSError, ValueError, RuntimeError, subprocess.CalledProcessError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
