# agent-skills

Reusable skill definitions for AI coding agents. Each skill is a structured Markdown file that gives an agent the instructions, workflow, and guardrails it needs to perform a specific task — setting up CI, auditing a codebase, scaffolding infrastructure, and so on.

Skills are designed to be loaded by agent routers (Claude Code, Cursor, Copilot, etc.) based on user intent. The YAML frontmatter in each file provides the metadata needed for matching.

## Available Skills

| Skill | Description |
|-------|-------------|
| [agent-native-audit](skills/agent-native-audit/SKILL.md) | Audit and score a codebase for AI agent readiness across five dimensions |
| [ci-verify-setup](skills/ci-verify-setup/SKILL.md) | Set up a project-level `verify` command and GitHub Actions CI workflow |

## Skill Format

Each skill lives in its own directory and contains a single `SKILL.md` with:

1. **YAML frontmatter** — `name` (kebab-case, matches directory) and `description` (includes trigger phrases for routing)
2. **Goal** — What the skill achieves
3. **When to Use** — Trigger conditions and example prompts
4. **Workflow** — Numbered, actionable steps an agent follows
5. **Guardrails** — Safety constraints and "never" rules
6. **Completion Checklist** — Verifiable criteria for success

```
agent-skills/
├── skills/
│   ├── agent-native-audit/
│   │   └── SKILL.md
│   └── ci-verify-setup/
│       └── SKILL.md
├── AGENTS.md
└── README.md
```

## Adding a Skill

1. Create a directory: `mkdir -p skills/<skill-name>` (kebab-case)
2. Add `skills/<skill-name>/SKILL.md` with the required frontmatter and sections
3. Ensure the frontmatter `name` matches the directory name
4. Include `## Guardrails` and `## Completion Checklist` — both are required
5. **Update `README.md`** — add the new skill to the "Available Skills" table above
6. **Update `AGENTS.md`** — add the new skill to the "Existing Skills Reference" table
7. Commit: `Add <skill-name> skill`

See [AGENTS.md](AGENTS.md) for the full file format specification and style guidelines.
