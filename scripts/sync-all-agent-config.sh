#!/usr/bin/env bash
# Sync agent-skills (skills + rules) and optional pstack plugin skills.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

"$REPO_ROOT/scripts/sync-agent-symlinks.sh" "$@"
"$REPO_ROOT/scripts/sync-pstack-skills.sh" "$@"
