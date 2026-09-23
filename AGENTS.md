# Agent guidance

This repository contains portable agent skills, Cursor rules, and the `dxd-skills` plugin for Claude Code, Codex, and Cursor.

## Skill changes

- Each skill belongs in `skills/<kebab-case-name>/SKILL.md`.
- Keep frontmatter names equal to their directory and descriptions clear about when to load.
- Keep skills portable across agent tools unless the task fundamentally depends on one tool.
- Put tool-specific setup behind a clearly triggered pointer.
- Reuse repository scripts and conventions. Check `skills/` for overlap before adding a skill.
- Update README only when its inventory or setup instructions change.
- Keep each instruction once. Use sections, checklists, and examples only when they add useful guidance; no fixed body template is required.
- Preserve tool protocols, user preferences, and concrete failure boundaries. Avoid mandatory design rituals, vendor defaults, and generic repeated verification.
- Put substantial mode-specific procedures in references and explain when to read them.
- Validate changed relative links and Markdown whitespace. The packaging check below covers frontmatter names and README inventory; there is no application build or test suite.

## Plugin packaging

`skills/` is the canonical copy of every skill. The `dxd-skills` plugin ships it three ways from the repository root: `.claude-plugin/`, `.cursor-plugin/`, and `.codex-plugin/` (listed by `.agents/plugins/marketplace.json`). All three read `skills/` directly; do not add symlinked copies, because Codex drops symlinks when it caches a plugin.

After adding, removing, or editing a skill, run:

```bash
python3 scripts/sync-plugin-packaging.py
```

It bumps all three manifest versions together once per change: minor when a skill is added or removed, patch for edits. Pass `--version X.Y.Z` for an intentional major release.

Before finishing any change under `skills/` or a plugin manifest, run:

```bash
python3 scripts/sync-plugin-packaging.py --check
```

Done means the check passes: matching Claude, Codex, and Cursor versions, bumped above the last commit whenever skill content changed; frontmatter `name` equal to the directory; and a README table row for every skill. Commit the manifest bumps in the same commit as the skill change. CI runs the same check against the PR base.

## Rules and local installation

- Cursor rules live in `rules/*.mdc`.
- Run `./scripts/install-local-githooks.sh` once to install local links and a pre-commit packaging check, or `./scripts/sync-all-agent-config.sh` to refresh links.

## Git

- Use imperative commit messages. A simple skill addition can go to `main` in one commit; use a feature branch for multi-skill or refactor work.
