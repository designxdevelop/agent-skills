#!/usr/bin/env bash
# Install a local post-commit hook that syncs agent skill symlinks after commits.
# Writes only to .local/ (gitignored) and .git/hooks/ (never tracked).
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOCAL_HOOKS="$REPO_ROOT/.local/githooks"
POST_COMMIT="$LOCAL_HOOKS/post-commit"
GIT_HOOK="$REPO_ROOT/.git/hooks/post-commit"

mkdir -p "$LOCAL_HOOKS"

cat > "$POST_COMMIT" << 'EOF'
#!/bin/sh
# Local post-commit hook (gitignored). Syncs skill symlinks when skills/ changes.
ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || exit 0

if git diff-tree --no-commit-id --name-only -r HEAD 2>/dev/null | grep -qE '^(skills/|rules/)'; then
  "$ROOT/scripts/sync-all-agent-config.sh" --quiet || true
fi
EOF

chmod +x "$POST_COMMIT"
ln -sfn "../../.local/githooks/post-commit" "$GIT_HOOK"

echo "Installed post-commit hook -> .local/githooks/post-commit"
echo "Running initial symlink sync..."
"$REPO_ROOT/scripts/sync-all-agent-config.sh"
