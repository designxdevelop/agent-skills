#!/usr/bin/env python3
"""Notify the website about this checked-out source revision."""

import json
import os
from pathlib import Path
import subprocess
import sys
import urllib.error
import urllib.request


def main():
    root = Path(__file__).resolve().parent.parent
    token = os.environ.get("DXD_WEBSITE_DISPATCH_TOKEN")
    if not token:
        sys.exit("Missing DXD_WEBSITE_DISPATCH_TOKEN; see docs/website-sync.md.")
    sha = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=root, text=True
    ).strip()
    version = json.loads((root / ".codex-plugin/plugin.json").read_text())["version"]
    payload = {
        "event_type": "agent-skills-updated",
        "client_payload": {
            "source_repository": "designxdevelop/agent-skills",
            "source_sha": sha,
            "version": version,
        },
    }
    request = urllib.request.Request(
        "https://api.github.com/repos/designxdevelop/dxd-2026/dispatches",
        data=json.dumps(payload).encode(),
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
            "Content-Type": "application/json",
            "User-Agent": "dxd-skills-website-sync",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            if response.status != 204:
                sys.exit(f"Unexpected dispatch status: {response.status}")
    except urllib.error.HTTPError as error:
        sys.exit(f"Website dispatch rejected: HTTP {error.code}")
    except urllib.error.URLError:
        sys.exit("Website dispatch failed: network error")
    print(f"Notified dxd-2026: {version} at {sha}")


if __name__ == "__main__":
    main()
