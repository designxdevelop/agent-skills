"""Regression tests for Markdown parsing and local target validation."""

from __future__ import annotations

import runpy
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from pathlib import Path
from unittest.mock import patch


CHECKER = runpy.run_path(str(Path(__file__).resolve().parents[1] / "check-markdown.py"))
CHECK_FILE = CHECKER["check_file"]


class MarkdownCheckTests(unittest.TestCase):
    def check(self, text: str, targets: tuple[str, ...] = ()) -> list[str]:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            source = root / "docs/source.md"
            source.parent.mkdir()
            source.write_text(text, encoding="utf-8")
            for target in targets:
                path = root / target
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("target\n", encoding="utf-8")
            with patch.dict(CHECK_FILE.__globals__, ROOT=root):
                return CHECK_FILE(source)

    def test_local_links_and_images_resolve_from_source_directory(self):
        text = (
            "[parent](../README.md) ![image](image.svg)\n"
            "[encoded](file%20name.md#heading) [query](../README.md?raw=1)\n"
        )
        self.assertEqual(
            self.check(text, ("README.md", "docs/image.svg", "docs/file name.md")),
            [],
        )

    def test_missing_local_target_reports_source_line(self):
        issues = self.check("# Heading\n\n[missing](missing.md)\n")
        self.assertEqual(
            issues,
            ["docs/source.md:3: local link target does not exist: missing.md"],
        )

    def test_external_and_fragment_links_do_not_require_local_files(self):
        text = (
            "[web](https://example.com/missing) [mail](mailto:hello@example.com)\n"
            "[host](//example.com/missing) [heading](#heading)\n"
        )
        self.assertEqual(self.check(text), [])

    def test_examples_in_code_and_comments_are_ignored(self):
        text = (
            "`[inline](missing.md)`\n"
            "````markdown\n[example](missing.md)\n```\n````\n"
            "~~~markdown\n[example](missing.md)\n~~~\n"
            "<!--\n[comment](missing.md)\n-->\n"
            "\\[escaped](missing.md)\n"
        )
        self.assertEqual(self.check(text), [])

    def test_reference_definitions_are_checked_but_footnotes_are_not_links(self):
        text = "[guide][target]\n[target]: ../guide.md \"Guide\"\n[^note]: Footnote text.\n"
        self.assertEqual(self.check(text, ("guide.md",)), [])
        self.assertIn(
            "local link target does not exist: ../guide.md",
            self.check(text)[0],
        )

    def test_reference_definition_with_escaped_space(self):
        text = '[guide][target]\n[target]: file\\ name.md "Guide"\n'
        self.assertEqual(self.check(text, ("docs/file name.md",)), [])

    def test_parentheses_escaped_paths_and_angle_destinations(self):
        text = (
            '[nested](file(one).md "A title")\n'
            "[escaped](file\\(two\\).md)\n"
            '[space](<file name.md> "A title")\n'
        )
        self.assertEqual(
            self.check(text, ("docs/file(one).md", "docs/file(two).md", "docs/file name.md")),
            [],
        )

    def test_parentheses_in_title_do_not_hide_missing_target(self):
        issues = self.check('[missing](missing.md "Title (draft")\n')
        self.assertEqual(
            issues,
            ["docs/source.md:1: local link target does not exist: missing.md"],
        )

    def test_repository_escape_is_rejected(self):
        issues = self.check("[outside](../../outside.md)\n")
        self.assertEqual(
            issues,
            ["docs/source.md:1: local link escapes the repository: ../../outside.md"],
        )

    def test_invalid_url_has_actionable_error(self):
        issues = self.check("[invalid](https://[invalid)\n")
        self.assertEqual(
            issues,
            ["docs/source.md:1: invalid link URL: https://[invalid"],
        )

    def test_whitespace_errors_and_markdown_hard_breaks(self):
        self.assertEqual(self.check("Hard break.  \nNext line.\n"), [])
        self.assertEqual(self.check("CRLF.\r\n"), [])
        self.assertEqual(
            self.check("Trailing space. \n"),
            ["docs/source.md:1: trailing whitespace"],
        )
        self.assertEqual(
            self.check("No newline."),
            ["docs/source.md: missing final newline"],
        )
        self.assertEqual(
            self.check("Extra blank line.\n\n"),
            ["docs/source.md: extra blank line at end of file"],
        )

    def test_repository_command_ignores_generated_files_and_fails_on_broken_links(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            readme = root / "README.md"
            readme.write_text("# Valid Markdown\n", encoding="utf-8")
            generated = root / "dist/generated.md"
            generated.parent.mkdir()
            generated.write_text("[broken](missing.md)", encoding="utf-8")
            output = StringIO()
            errors = StringIO()
            main = CHECKER["main"]
            with patch.dict(main.__globals__, ROOT=root), redirect_stdout(output), redirect_stderr(errors):
                self.assertEqual(main(), 0)
                self.assertIn("1 files", output.getvalue())
                readme.write_text("[broken](missing.md)\n", encoding="utf-8")
                self.assertEqual(main(), 1)
                self.assertIn("README.md:1: local link target does not exist", errors.getvalue())


if __name__ == "__main__":
    unittest.main()
