#!/usr/bin/env bash
# Install local hooks: pre-commit blocks stale plugin packaging; post-commit
# syncs agent skill symlinks after commits.
# Writes only to .local/ (gitignored) and .git/hooks/ (never tracked).
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOCAL_HOOKS="$REPO_ROOT/.local/githooks"
PRE_COMMIT="$LOCAL_HOOKS/pre-commit"
POST_COMMIT="$LOCAL_HOOKS/post-commit"

mkdir -p "$LOCAL_HOOKS"

cat > "$PRE_COMMIT" << 'EOF'
#!/bin/sh
# Local pre-commit hook (gitignored). Blocks skill commits with stale plugin packaging.
ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || exit 0

if git diff --cached --name-only | grep -qE '^(skills/|plugins/|README\.md)'; then
  python3 "$ROOT/scripts/sync-plugin-packaging.py" --check || {
    echo "Run: python3 scripts/sync-plugin-packaging.py, then stage the manifest updates." >&2
    exit 1
  }
fi
EOF

cat > "$POST_COMMIT" << 'EOF'
#!/bin/sh
# Local post-commit hook (gitignored). Syncs skill symlinks when skills/ changes.
ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || exit 0

if git diff-tree --no-commit-id --name-only -r HEAD 2>/dev/null | grep -qE '^(skills/|rules/)'; then
  "$ROOT/scripts/sync-all-agent-config.sh" --quiet || true
fi
EOF

chmod +x "$PRE_COMMIT" "$POST_COMMIT"
ln -sfn "../../.local/githooks/pre-commit" "$REPO_ROOT/.git/hooks/pre-commit"
ln -sfn "../../.local/githooks/post-commit" "$REPO_ROOT/.git/hooks/post-commit"

echo "Installed pre-commit and post-commit hooks -> .local/githooks/"
echo "Running initial symlink sync..."
"$REPO_ROOT/scripts/sync-all-agent-config.sh"
