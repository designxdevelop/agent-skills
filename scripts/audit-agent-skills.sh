#!/usr/bin/env bash
# Report shared-skill drift without changing any local configuration.
set -euo pipefail

HUB="$HOME/.agents/skills"
declare -a ROOTS=(
  "$HOME/.agents/skills"
  "$HOME/.cursor/skills"
  "$HOME/.codex/skills"
  "$HOME/.config/opencode/skills"
  "$HOME/.claude/skills"
)

printf '%-34s %7s %9s %9s\n' 'Root' 'Entries' 'Symlinks' 'Standalone'
for root in "${ROOTS[@]}"; do
  [[ -d "$root" ]] || continue
  entries=0
  links=0
  standalone=0
  for entry in "$root"/*; do
    [[ -e "$entry" || -L "$entry" ]] || continue
    entries=$((entries + 1))
    if [[ -L "$entry" ]]; then
      links=$((links + 1))
    elif [[ -d "$entry" && -f "$entry/SKILL.md" ]]; then
      standalone=$((standalone + 1))
    fi
  done
  printf '%-34s %7s %9s %9s\n' "${root#$HOME/}" "$entries" "$links" "$standalone"
done

pstack_hub=0
if [[ -d "$HUB" ]]; then
  for entry in "$HUB"/*; do
    [[ -L "$entry" ]] || continue
    target="$(readlink "$entry")"
    if [[ "$target" == *"/.cursor/plugins/cache/cursor-public/pstack/"* ]]; then
      pstack_hub=$((pstack_hub + 1))
    fi
  done
fi

if [[ "$pstack_hub" -eq 0 ]]; then
  printf '\nPStack: absent from the shared hub (Cursor plugin only).\n'
else
  printf '\nPStack: %s skill(s) still linked into the shared hub.\n' "$pstack_hub"
fi

printf '\nT3 Code reads the hub and the Cursor, Claude, Codex, and OpenCode spokes.\n'
printf 'It does not read ~/.config/agents/skills.\n'
if [[ -L "$HOME/.config/agents/skills" ]]; then
  t3_target="$(readlink -f "$HOME/.config/agents/skills")"
  printf 'Legacy alias remains at ~/.config/agents/skills -> %s.\n' "$t3_target"
elif [[ -d "$HOME/.config/agents/skills" ]]; then
  printf 'Legacy directory remains at ~/.config/agents/skills and is not a T3 skill root.\n'
fi
