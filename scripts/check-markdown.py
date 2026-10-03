#!/usr/bin/env python3
"""Check Markdown whitespace and local link targets without third-party packages."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Iterator
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_DIRS = {".git", ".local", "dist", "node_modules", ".venv"}
LINK_START = re.compile(r"(?<!\\)!?\[[^\]\n]*\]\(")
REFERENCE_DEFINITION = re.compile(
    r"^[ \t]{0,3}\[(?!\^)[^\]\n]+\]:[ \t]*(.*)$",
    re.MULTILINE,
)
FENCE_START = re.compile(r"^[ \t]{0,3}(`{3,}|~{3,})")
HTML_COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)
INLINE_CODE = re.compile(r"(`+).*?\1", re.DOTALL)


def blank_region(text: str, start: int, end: int) -> str:
    """Replace a source range with spaces while preserving line positions."""
    return "".join("\n" if character == "\n" else " " for character in text[start:end])


def mask_code_and_comments(text: str) -> str:
    """Mask fenced/inline code and HTML comments before searching for links."""
    characters = list(text)
    offset = 0
    fence_character: str | None = None
    fence_length = 0

    for line in text.splitlines(keepends=True):
        content = line.rstrip("\r\n")
        start = FENCE_START.match(content)
        if fence_character is not None:
            closing = re.match(
                rf"^[ \t]{{0,3}}{re.escape(fence_character)}{{{fence_length},}}[ \t]*$",
                content,
            )
            characters[offset : offset + len(line)] = blank_region(text, offset, offset + len(line))
            if closing:
                fence_character = None
                fence_length = 0
        elif start:
            marker = start.group(1)
            fence_character = marker[0]
            fence_length = len(marker)
            characters[offset : offset + len(line)] = blank_region(text, offset, offset + len(line))
        offset += len(line)

    masked = "".join(characters)
    for pattern in (HTML_COMMENT, INLINE_CODE):
        matches = list(pattern.finditer(masked))
        for match in reversed(matches):
            masked = (
                masked[: match.start()]
                + blank_region(masked, match.start(), match.end())
                + masked[match.end() :]
            )
    return masked


def markdown_destinations(text: str) -> Iterator[tuple[str, int]]:
    """Yield each Markdown link destination and its source offset."""
    masked = mask_code_and_comments(text)

    for match in LINK_START.finditer(masked):
        # Only parse the destination. Parentheses in a quoted title are not
        # part of the path and must not hide a broken target.
        remainder = masked[match.end() :].split("\n", 1)[0]
        destination = parse_destination(remainder)
        if destination:
            yield destination, match.start()

    for match in REFERENCE_DEFINITION.finditer(masked):
        destination = parse_destination(match.group(1))
        if destination:
            yield destination, match.start()


def parse_destination(value: str) -> str:
    value = value.strip()
    if value.startswith("<"):
        end = value.find(">")
        return value[1:end] if end > 0 else ""

    destination: list[str] = []
    depth = 0
    escaped = False
    for character in value:
        if escaped:
            destination.append(character)
            escaped = False
        elif character == "\\":
            escaped = True
        elif character == "(":
            depth += 1
            destination.append(character)
        elif character == ")":
            if depth == 0:
                break
            depth -= 1
            destination.append(character)
        elif character.isspace() and depth == 0:
            break
        else:
            destination.append(character)
    if escaped:
        destination.append("\\")
    return "".join(destination)


def markdown_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if not any(part in EXCLUDED_DIRS for part in path.relative_to(ROOT).parts)
    )


def check_file(path: Path) -> list[str]:
    relative = path.relative_to(ROOT)
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as error:
        return [f"{relative}: not valid UTF-8 ({error})"]

    issues: list[str] = []
    lines = text.splitlines()
    if text and not text.endswith(("\n", "\r")):
        issues.append(f"{relative}: missing final newline")
    if lines and not lines[-1].strip():
        issues.append(f"{relative}: extra blank line at end of file")

    for line_number, line in enumerate(lines, start=1):
        trailing = len(line) - len(line.rstrip(" \t"))
        if trailing and not (trailing == 2 and line.endswith("  ")):
            issues.append(f"{relative}:{line_number}: trailing whitespace")

    for destination, offset in markdown_destinations(text):
        line_number = text.count("\n", 0, offset) + 1
        try:
            parsed = urlsplit(destination)
        except ValueError:
            issues.append(f"{relative}:{line_number}: invalid link URL: {destination}")
            continue
        if parsed.scheme or destination.startswith("//") or not parsed.path:
            continue

        target = (path.parent / unquote(parsed.path)).resolve()
        try:
            target.relative_to(ROOT)
        except ValueError:
            issues.append(
                f"{relative}:{line_number}: "
                f"local link escapes the repository: {destination}"
            )
            continue
        if not target.exists():
            issues.append(
                f"{relative}:{line_number}: "
                f"local link target does not exist: {destination}"
            )
    return issues


def main() -> int:
    files = markdown_files()
    issues = [issue for path in files for issue in check_file(path)]
    if issues:
        print("\n".join(f"ERROR: {issue}" for issue in issues), file=sys.stderr)
        return 1
    print(f"Markdown check passed ({len(files)} files).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
