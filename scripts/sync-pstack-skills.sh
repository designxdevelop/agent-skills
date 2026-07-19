#!/usr/bin/env bash
# Symlink pstack plugin skills into ~/.agents/skills and tool spokes.
# Requires the pstack Cursor plugin (/add-plugin pstack) or PSTACK_SKILLS_DIR.
set -euo pipefail

QUIET=0
if [[ "${1:-}" == "--quiet" ]]; then
  QUIET=1
fi

log() {
  if [[ "$QUIET" -eq 0 ]]; then
    printf '%s\n' "$*"
  fi
}

resolve_pstack_skills_dir() {
  if [[ -n "${PSTACK_SKILLS_DIR:-}" && -d "$PSTACK_SKILLS_DIR" ]]; then
    printf '%s\n' "$PSTACK_SKILLS_DIR"
    return 0
  fi

  local candidate
  for candidate in "$HOME"/.cursor/plugins/cache/cursor-public/pstack/*/skills; do
    if [[ -d "$candidate" ]]; then
      printf '%s\n' "$candidate"
      return 0
    fi
  done

  return 1
}

AGENTS_HUB="$HOME/.agents/skills"
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

if ! PSTACK_SKILLS="$(resolve_pstack_skills_dir)"; then
  log "pstack skills not found."
  log "Install the Cursor plugin: /add-plugin pstack"
  log "Or set PSTACK_SKILLS_DIR to a checkout of cursor/plugins/pstack/skills."
  exit 0
fi

mkdir -p "$AGENTS_HUB"

synced=0
skipped=0

for skill_path in "$PSTACK_SKILLS"/*/; do
  [[ -d "$skill_path" ]] || continue
  [[ -f "${skill_path}SKILL.md" ]] || continue

  name="$(basename "$skill_path")"
  hub_link="$AGENTS_HUB/$name"

  if [[ -L "$hub_link" ]]; then
    current_target="$(readlink "$hub_link")"
    if [[ "$current_target" == *"/agent-skills/skills/"* ]]; then
      skipped=$((skipped + 1))
      continue
    fi
  elif [[ -e "$hub_link" && ! -L "$hub_link" ]]; then
    log "  skip $name (exists and is not a symlink; not overwriting)"
    skipped=$((skipped + 1))
    continue
  fi

  ln -sfn "$skill_path" "$hub_link"

  for i in "${!SPOKE_DIRS[@]}"; do
    spoke_dir="${SPOKE_DIRS[$i]}"
    spoke_rel="${SPOKE_REL[$i]}"
    mkdir -p "$spoke_dir"
    ln -sfn "${spoke_rel}/${name}" "${spoke_dir}/${name}"
  done

  synced=$((synced + 1))
  log "  linked pstack/$name"
done

if [[ "$synced" -eq 0 && "$skipped" -eq 0 ]]; then
  log "No pstack skills with SKILL.md found under $PSTACK_SKILLS."
else
  log "Synced $synced pstack skill(s) from $PSTACK_SKILLS (skipped $skipped owned by agent-skills)."
fi
