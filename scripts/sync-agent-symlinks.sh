#!/usr/bin/env bash
# Sync skills/ in this repo to ~/.agents/skills and tool-specific spokes.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS_DIR="$REPO_ROOT/skills"
RULES_DIR="$REPO_ROOT/rules"
CURSOR_RULES_DIR="$HOME/.cursor/rules"
AGENTS_HUB="$HOME/.agents/skills"
QUIET=0

if [[ "${1:-}" == "--quiet" ]]; then
  QUIET=1
fi

log() {
  if [[ "$QUIET" -eq 0 ]]; then
    printf '%s\n' "$*"
  fi
}

if [[ ! -d "$SKILLS_DIR" ]]; then
  log "No skills/ directory at $SKILLS_DIR; nothing to sync."
  exit 0
fi

mkdir -p "$AGENTS_HUB"

# Spoke dirs symlink into the shared hub (relative paths from each spoke root).
declare -a SPOKE_DIRS=(
  "$HOME/.cursor/skills"
  "$HOME/.claude/skills"
  "$HOME/.codex/skills"
  "$HOME/.config/opencode/skills"
)

declare -a SPOKE_REL=(
  "../../.agents/skills"
  "../../.agents/skills"
  "../../.agents/skills"
  "../../../.agents/skills"
)

synced=0

for skill_path in "$SKILLS_DIR"/*/; do
  [[ -d "$skill_path" ]] || continue
  [[ -f "${skill_path}SKILL.md" ]] || continue

  name="$(basename "$skill_path")"
  ln -sfn "$skill_path" "$AGENTS_HUB/$name"

  for i in "${!SPOKE_DIRS[@]}"; do
    spoke_dir="${SPOKE_DIRS[$i]}"
    spoke_rel="${SPOKE_REL[$i]}"
    mkdir -p "$spoke_dir"
    ln -sfn "${spoke_rel}/${name}" "${spoke_dir}/${name}"
  done

  synced=$((synced + 1))
  log "  linked $name"
done

if [[ "$synced" -eq 0 ]]; then
  log "No skills with SKILL.md found under skills/."
else
  log "Synced $synced skill(s) to ~/.agents/skills and agent spokes."
fi

rules_synced=0
if [[ -d "$RULES_DIR" ]]; then
  mkdir -p "$CURSOR_RULES_DIR"
  for rule_path in "$RULES_DIR"/*.mdc; do
    [[ -f "$rule_path" ]] || continue
    name="$(basename "$rule_path")"
    ln -sfn "$rule_path" "$CURSOR_RULES_DIR/$name"
    rules_synced=$((rules_synced + 1))
    log "  linked rule $name -> ~/.cursor/rules/$name"
  done
fi

if [[ "$rules_synced" -eq 0 ]]; then
  log "No rules/*.mdc found to sync."
fi
