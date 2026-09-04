# AGENTS.md

Instructions for AI coding agents working in this repository.

## Repository Overview

This is a **documentation-only** repository containing reusable "skills" for AI coding agents.
Each skill is a structured Markdown file that provides instructions, workflows, and guardrails
for a specific task domain (e.g., CI setup, codebase auditing). These skills should stay
portable across Codex, Claude Code, Cursor, Copilot, and other agent tools unless a skill is
explicitly tool-specific. There is no application code, no build step, no test suite, and no
package manager.

## Project Structure

```
agent-skills/
├── skills/
│   └── <skill-name>/
│       └── SKILL.md      # Skill definition file
├── rules/
│   └── *.mdc             # Cursor always-applied rules (synced to ~/.cursor/rules/)
├── scripts/
│   ├── sync-agent-symlinks.sh
│   ├── sync-pstack-skills.sh
│   └── sync-all-agent-config.sh
├── README.md
└── AGENTS.md             # This file
```

Each skill lives in `skills/<skill-name>/`, containing a single `SKILL.md`.
Global Cursor rules live in `rules/*.mdc` and sync to `~/.cursor/rules/`.

## Build / Lint / Test Commands

There are none. This repository has no `package.json`, no `tsconfig.json`, no linter, and
no test runner. Validation is manual: ensure Markdown renders correctly and YAML frontmatter
parses without errors.

If you need to validate frontmatter syntax, use any YAML parser to check the `---` block
at the top of each SKILL.md file.

## Skill File Format

Every `SKILL.md` must follow this structure:

### 1. YAML Frontmatter (required)

```yaml
---
name: kebab-case-skill-name
description: >-
  One-paragraph description of when this skill should be loaded.
  Include trigger phrases the user might say.
---
```

- `name` — Must match the parent directory name. Always `kebab-case`.
- `description` — A single paragraph of trigger conditions. Include natural-language
  phrases so agent routers can match user intent to the skill, but do not summarize the
  workflow; agents should read the body for process details.

### 2. Markdown Body (required sections)

The body should contain these sections in order:

| Section                   | Purpose                                             |
| ------------------------- | --------------------------------------------------- |
| `# Title`                 | Human-readable skill name                           |
| `## Goal`                 | What the skill achieves (1-3 sentences)             |
| `## When to Use`          | Trigger conditions and example user prompts         |
| `## Workflow`             | Step-by-step instructions the agent follows         |
| `## Guardrails`           | Safety rules and constraints                        |
| `## Completion Checklist` | Checklist to verify the skill was applied correctly |

Optional sections (use when appropriate):

- `## Scoring Dimensions` or `## Evaluation Criteria` — for audit/assessment skills
- `## Template Guidance` — for skills that generate files from templates

## Code Style Guidelines

### Naming Conventions

- **Directories**: `kebab-case` (e.g., `ci-verify-setup`, `agent-native-audit`)
- **Skill names**: Must match directory name exactly, always `kebab-case`
- **Files**: `SKILL.md` (uppercase, always this exact name)

### Markdown Formatting

- Use ATX-style headers (`#`, `##`, `###`) — not underline-style
- One blank line before and after headers
- One blank line before and after code blocks
- Use fenced code blocks with language tags (` ```yaml `, ` ```bash `, etc.)
- Use `|` pipe tables for structured comparisons and rubrics
- Use `- [ ]` task lists for checklists
- Wrap prose lines at a reasonable length (no strict column limit, but prefer readability)
- Use `>` blockquotes for prompts the agent should present to the user

### YAML Frontmatter

- Use `---` delimiters (three dashes, nothing else on the line)
- Keep `name` as a plain string (no quotes needed for kebab-case)
- Use `>-` block scalar for multi-line `description` to fold into a single paragraph
- No trailing whitespace inside frontmatter

### Content Guidelines

- Write instructions in second person imperative ("Read the config", "Check for...")
- Be specific: include file paths, command examples, and expected output formats
- Keep skills tool-agnostic unless the skill is intentionally about one tool. Mention
  Codex, Claude Code, Cursor, Copilot, or SaaS/browser connectors only when the distinction
  changes agent behavior.
- Guardrails must include "never" statements for destructive actions
- Workflow steps should be numbered and actionable by an AI agent
- Prefer composing existing tools/scripts over inventing new ones
- Include concrete examples (file paths, shell commands, expected output)
- Each skill should be self-contained — do not reference other skills unless
  explicitly creating a dependency chain
- Checklist items should be verifiable (an agent can confirm done/not-done)

### Error Handling Patterns

Since skills are instructions, "error handling" means:

- Always include guardrails that prevent destructive actions (`rm -rf`, `git push --force`, etc.)
- Tell the agent to **report** failures rather than silently retry or auto-fix
- Include fallback instructions for when detection/inspection fails
- Distinguish between pre-existing issues and issues introduced by the skill

## Git Conventions

- **Commit messages**: Imperative mood, no prefix/scope convention required.
  Examples: `Add ci-verify-setup skill`, `Update scoring rubric for agent-native-audit`
- **Branch strategy**: Commit to `main` for simple additions. Use feature branches
  for larger refactors or multi-skill changes.
- **One skill per commit** when adding new skills.

## Adding a New Skill

1. Create a directory: `mkdir -p skills/<skill-name>` (kebab-case)
2. Create `skills/<skill-name>/SKILL.md` with the required frontmatter and sections
3. Verify the frontmatter `name` matches the directory name
4. Ensure the `description` includes trigger phrases for agent routing
5. Include `## Guardrails` — every skill must have safety constraints
6. Include `## Completion Checklist` — every skill must be verifiable
7. **Update `README.md`** — add the new skill to the "Available Skills" table
8. **Update `AGENTS.md`** — add the new skill to the "Existing Skills Reference" table
9. Sync local agent symlinks (one-time setup per clone, then automatic after commits):
   - `./scripts/install-local-githooks.sh` — installs a **gitignored** post-commit hook under
     `.local/githooks/` that re-links skills and rules when `skills/` or `rules/` changes
   - Or run manually anytime: `./scripts/sync-all-agent-config.sh`
   - Targets: `~/.agents/skills` (hub), `~/.cursor/skills`, `~/.claude/skills`,
     `~/.codex/skills`, `~/.config/opencode/skills`, and T3 Code through a
     `~/.config/agents/skills` directory symlink to the hub; `~/.cursor/rules`
     receives `rules/*.mdc`
10. Commit with message: `Add <skill-name> skill`

## Common Mistakes to Avoid

- Do not add `package.json`, `tsconfig.json`, or other tooling config — this is not a code project
- Do not create `index.md` or `README.md` inside skill directories — the file is always `SKILL.md`
- Do not use camelCase or PascalCase for directory names
- Do not omit YAML frontmatter — it is required for agent routing
- Do not write vague workflow steps ("improve the code") — be specific and actionable
- Do not reference external URLs that may break — prefer inline instructions
- Do not add skills that duplicate existing ones — check existing skills first
- Do not forget to update `README.md` and `AGENTS.md` after adding a new skill
- Do not forget to create/update the shared skill registry or tool-specific registration after adding or moving a skill

## Existing Skills Reference

| Skill                       | Purpose                                                  |
| --------------------------- | -------------------------------------------------------- |
| `agent-native-audit`        | Audit and score a codebase for cross-agent readiness     |
| `ci-verify-setup`           | Set up one verification command and matching CI          |
| `i-have-adhd`               | Shape responses for ADHD-friendly reading and action     |
| `live-work-context-cleanup` | Recover live context and clean up cross-tool work safely |
| `dxd-code-review`           | Run a strict DXD maintainability and abstraction review  |
| `quick-fix-deploy-sync`     | Fast-forward sync production and staging for hotfixes    |
| `derive-client`              | Capture HAR from browser traffic and derive an HTTP/CLI client |
| `anti-slop`                  | Remove AI writing tells from prose while keeping voice         |
| `ui-text-audit`              | Audit screens for redundant UI text and remove what doesn't help the user |
| `paper-design`               | Create and review native editable Paper designs through the direct MCP |
| `better-ai-design`           | Distinctive UI via exploration, critique, imagery, and subtraction |
