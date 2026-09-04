# Agent guidance

This repository contains portable agent skills and Cursor rules.

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
- Validate changed YAML frontmatter, relative links, and Markdown whitespace. This documentation repository has no application build or test suite.

## Rules and local installation

- Cursor rules live in `rules/*.mdc`.
- Run `./scripts/install-local-githooks.sh` once to install local links, or `./scripts/sync-all-agent-config.sh` to refresh them.

## Git

- Use imperative commit messages. A simple skill addition can go to `main` in one commit; use a feature branch for multi-skill or refactor work.
