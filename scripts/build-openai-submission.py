#!/usr/bin/env python3
"""Build the skills-only ZIP for OpenAI's public plugin submission portal."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path
from xml.etree import ElementTree
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / ".codex-plugin" / "plugin.json"
SKILLS = ROOT / "skills"
ASSETS = ROOT / "assets"
DIST = ROOT / "dist"


def main() -> int:
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "sync-plugin-packaging.py"), "--check"],
        cwd=ROOT,
        check=True,
    )

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    interface = manifest["interface"]
    if manifest.get("skills") != "./skills/":
        raise ValueError("skills-only manifest must reference ./skills/")
    if len(interface["displayName"]) > 30:
        raise ValueError("public listing displayName must be at most 30 characters")
    if len(interface["shortDescription"]) > 30:
        raise ValueError("public listing shortDescription must be at most 30 characters")
    if len(interface["developerName"]) > 80:
        raise ValueError("public listing developerName must be at most 80 characters")
    if len(interface.get("defaultPrompt", [])) > 3:
        raise ValueError("public listing allows at most three default prompts")
    if any(len(prompt) > 128 for prompt in interface.get("defaultPrompt", [])):
        raise ValueError("public listing default prompts must be at most 128 characters")
    if any(key in manifest for key in ("apps", "mcpServers")):
        raise ValueError("skills-only submissions cannot include app or MCP configuration")

    for key in ("logo", "composerIcon"):
        relative = interface.get(key)
        if not isinstance(relative, str) or not relative.startswith("./assets/"):
            raise ValueError(f"public listing {key} must reference an asset under ./assets/")
        asset = ROOT / relative
        if not asset.is_file() or asset.suffix != ".svg" or asset.stat().st_size > 5 * 1024 * 1024:
            raise ValueError(f"public listing {key} must be an SVG under 5 MiB")
        svg = ElementTree.parse(asset).getroot()
        if svg.tag != "{http://www.w3.org/2000/svg}svg":
            raise ValueError(f"public listing {key} is not an SVG")
        size = svg.attrib.get("viewBox", "").split()
        if len(size) != 4 or size[2] != size[3] or float(size[2]) < 48:
            raise ValueError(f"public listing {key} must be a square SVG at least 48px wide")

    files = [
        MANIFEST,
        *sorted(path for path in SKILLS.rglob("*") if path.is_file()),
        *sorted(path for path in ASSETS.rglob("*") if path.is_file()),
    ]
    if any(path.is_symlink() for path in files):
        raise ValueError("submission ZIP cannot contain symlinks")
    if not any(path.name == "SKILL.md" for path in files):
        raise ValueError("submission ZIP must include at least one skill")

    DIST.mkdir(exist_ok=True)
    archive = DIST / f"dxd-skills-{manifest['version']}-openai-submission.zip"
    with ZipFile(archive, "w", compression=ZIP_DEFLATED) as zip_file:
        for path in files:
            zip_file.write(path, path.relative_to(ROOT).as_posix())

    with ZipFile(archive) as zip_file:
        if zip_file.testzip() is not None:
            raise ValueError("submission ZIP failed integrity check")
        if set(zip_file.namelist()) != {path.relative_to(ROOT).as_posix() for path in files}:
            raise ValueError("submission ZIP contents differ from selected source files")

    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    print(f"Created {archive}")
    print(f"Files: {len(files)} | SHA-256: {digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
