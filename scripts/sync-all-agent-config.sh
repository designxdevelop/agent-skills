#!/usr/bin/env bash
# Sync agent-skills (skills + rules). PStack is opt-in because its large plugin
# catalog otherwise becomes visible in every harness through the shared hub.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WITH_PSTACK=0
SYNC_ARGS=()

for arg in "$@"; do
  case "$arg" in
    --with-pstack) WITH_PSTACK=1 ;;
    --quiet) SYNC_ARGS+=("$arg") ;;
    *)
      printf 'Unknown option: %s\n' "$arg" >&2
      printf 'Usage: %s [--quiet] [--with-pstack]\n' "$(basename "$0")" >&2
      exit 2
      ;;
  esac
done

"$REPO_ROOT/scripts/sync-agent-symlinks.sh" ${SYNC_ARGS[@]+"${SYNC_ARGS[@]}"}

if [[ "$WITH_PSTACK" -eq 1 ]]; then
  "$REPO_ROOT/scripts/sync-pstack-skills.sh" ${SYNC_ARGS[@]+"${SYNC_ARGS[@]}"}
else
  "$REPO_ROOT/scripts/sync-pstack-skills.sh" --unlink ${SYNC_ARGS[@]+"${SYNC_ARGS[@]}"}
fi
