#!/usr/bin/env bash
# Sync skills/ in this repo to ~/.agents/skills and tool-specific spokes.
# T3 Code nightly reads those provider directories. It does not read
# ~/.config/agents/skills.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS_DIR="$REPO_ROOT/skills"
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

link_skill() {
  local source="$1"
  local destination="$2"

  if [[ -L "$destination" ]]; then
    ln -sfn "$source" "$destination"
  elif [[ -e "$destination" ]]; then
    log "  skip $(basename "$destination") (standalone directory; not overwriting)"
  else
    ln -s "$source" "$destination"
  fi
}

if [[ ! -d "$SKILLS_DIR" ]]; then
  log "No skills/ directory at $SKILLS_DIR; nothing to sync."
  exit 0
fi

mkdir -p "$AGENTS_HUB"

# Spoke dirs symlink into the shared hub (relative paths from each spoke root).
# T3 Code nightly (com.t3tools.t3code) does not read ~/.config/agents/skills.
# It discovers skills from the connected provider:
#   Cursor: ~/.cursor/skills, ~/.agents/skills, ~/.codex/skills, ~/.claude/skills,
#           and the same four directories under the session cwd
#   Claude: ~/.claude/skills
#   Codex: ~/.codex/skills, ~/.agents/skills, and installed plugins
#   OpenCode: ~/.config/opencode/skills
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
  link_skill "$skill_path" "$AGENTS_HUB/$name"

  for i in "${!SPOKE_DIRS[@]}"; do
    spoke_dir="${SPOKE_DIRS[$i]}"
    spoke_rel="${SPOKE_REL[$i]}"
    mkdir -p "$spoke_dir"
    link_skill "${spoke_rel}/${name}" "${spoke_dir}/${name}"
  done

  synced=$((synced + 1))
  log "  linked $name"
done

if [[ "$synced" -eq 0 ]]; then
  log "No skills with SKILL.md found under skills/."
else
  log "Synced $synced skill(s) to ~/.agents/skills and agent spokes."
fi
