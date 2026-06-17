# agent-skills

Reusable skill definitions for AI coding agents. Each skill is a structured Markdown file that gives an agent the instructions, workflow, and guardrails it needs to perform a specific task — setting up CI, auditing a codebase, cleaning up live work context, and so on.

Skills are designed to be portable across Codex, Claude Code, Cursor, Copilot, and other agent routers. The YAML frontmatter in each file provides the trigger metadata agents use to decide when to load the skill.

## Available Skills

| Skill | Description |
|-------|-------------|
| [agent-native-audit](skills/agent-native-audit/SKILL.md) | Audit and score a codebase for cross-agent readiness across five dimensions |
| [ci-verify-setup](skills/ci-verify-setup/SKILL.md) | Set up a project-level verification command and matching CI workflow |
| [live-work-context-cleanup](skills/live-work-context-cleanup/SKILL.md) | Recover the correct live work context and perform conservative cleanup across browser-first tools, SaaS apps, and local repos |
| [dxd-code-review](skills/dxd-code-review/SKILL.md) | Run an extremely strict DXD-style maintainability review for abstraction quality, giant files, and spaghetti-condition growth |

## Skill Format

Each skill lives in its own directory and contains a single `SKILL.md` with:

1. **YAML frontmatter** — `name` (kebab-case, matches directory) and `description` (trigger phrases only, not workflow summary)
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
│   ├── ci-verify-setup/
│   │   └── SKILL.md
│   ├── live-work-context-cleanup/
│   │   └── SKILL.md
│   └── dxd-code-review/
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
