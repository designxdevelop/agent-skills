# agent-skills

Reusable skill definitions for AI coding agents. Each skill is a structured Markdown file that gives an agent the instructions, workflow, and guardrails it needs to perform a specific task — setting up CI, auditing a codebase, cleaning up live work context, and so on.

Skills are designed to be portable across Codex, Claude Code, Cursor, Copilot, and other agent routers. The YAML frontmatter in each file provides the trigger metadata agents use to decide when to load the skill.

## Available Skills

| Skill                                                                  | Description                                                                                                                   |
| ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| [agent-native-audit](skills/agent-native-audit/SKILL.md)               | Audit and score a codebase for cross-agent readiness across five dimensions                                                   |
| [ci-verify-setup](skills/ci-verify-setup/SKILL.md)                     | Set up a project-level verification command and matching CI workflow                                                          |
| [i-have-adhd](skills/i-have-adhd/SKILL.md)                             | Shape responses for ADHD-friendly reading with direct outcomes, bounded actions, and visible state                            |
| [live-work-context-cleanup](skills/live-work-context-cleanup/SKILL.md) | Recover the correct live work context and perform conservative cleanup across browser-first tools, SaaS apps, and local repos |
| [dxd-code-review](skills/dxd-code-review/SKILL.md)                     | Run an extremely strict DXD-style maintainability review for abstraction quality, giant files, and spaghetti-condition growth |
| [quick-fix-deploy-sync](skills/quick-fix-deploy-sync/SKILL.md)         | Fast-forward sync production and staging branches for hotfixes, backports, and quick deploys                                  |
| [derive-client](skills/derive-client/SKILL.md)                     | Capture browser traffic as HAR, then derive a reusable HTTP/CLI client instead of driving the browser every time              |
| [anti-slop](skills/anti-slop/SKILL.md)                             | Detect and remove AI writing tells from prose while preserving the author's voice                                             |
| [ui-text-audit](skills/ui-text-audit/SKILL.md)                     | Audit every screen for redundant, verbose, or unnecessary UI text and remove what doesn't help the user                      |
| [paper-design](skills/paper-design/SKILL.md)                       | Create and review native editable Paper designs through the direct Paper MCP                                                   |
| [better-ai-design](skills/better-ai-design/SKILL.md)               | Create distinctive interfaces via exploration, critique loops, imagery/motion, and deliberate subtraction                      |

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
│   ├── i-have-adhd/
│   │   └── SKILL.md
│   ├── live-work-context-cleanup/
│   │   └── SKILL.md
│   ├── dxd-code-review/
│   │   └── SKILL.md
│   ├── quick-fix-deploy-sync/
│   │   └── SKILL.md
│   ├── derive-client/
│   │   └── SKILL.md
│   ├── anti-slop/
│   │   └── SKILL.md
│   ├── ui-text-audit/
│   │   └── SKILL.md
│   ├── paper-design/
│   │   └── SKILL.md
│   └── better-ai-design/
│       └── SKILL.md
├── rules/
│   └── pstack-models.mdc   # global pstack model map (Cursor alwaysApply rule)
├── scripts/
│   ├── sync-agent-symlinks.sh
│   ├── sync-pstack-skills.sh
│   └── sync-all-agent-config.sh
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
7. **Sync agent symlinks** — run `./scripts/install-local-githooks.sh` once per clone
   (post-commit hook is gitignored; it re-links skills and rules after commits that touch
   `skills/` or `rules/`)
8. Commit: `Add <skill-name> skill`

## Global Agent Config

This repo is the source of truth for machine-wide agent configuration on Austin's machines.

| Path in repo  | Sync target                                                  | Purpose                                             |
| ------------- | ------------------------------------------------------------ | --------------------------------------------------- |
| `skills/*/`   | `~/.agents/skills/*` (+ Cursor/Claude/Codex/OpenCode spokes; T3 Code aliases the hub) | Custom DXD skills                                   |
| `rules/*.mdc` | `~/.cursor/rules/*.mdc`                                      | Cursor always-applied rules (e.g. pstack model map) |

Run a full sync anytime:

```bash
./scripts/sync-all-agent-config.sh
```

Audit the active roots without changing them:

```bash
./scripts/audit-agent-skills.sh
```

That runs:

1. `./scripts/sync-agent-symlinks.sh` — custom skills + rules

Default sync unlinks any PStack copies from the shared hub so Codex, Claude,
OpenCode, and T3 do not load the Cursor plugin catalog. The Cursor plugin stays
installed and is the only place PStack should run.

Add `--with-pstack` only if you intentionally want that catalog back in every
harness:

```bash
./scripts/sync-all-agent-config.sh --with-pstack
```

T3 Code uses `~/.config/agents/skills`, which should be a directory symlink to
`~/.agents/skills`. The sync script creates the alias when it is absent and
refuses to overwrite a standalone directory; back up that directory first if
you are consolidating an existing T3 installation.

### pstack (Cursor plugin only)

[pstack](https://github.com/cursor/plugins/tree/main/pstack) is a Cursor plugin,
not a global skill pack. It works best inside Cursor. Do not copy it into the
shared hub.

1. In Cursor: `/add-plugin pstack` (user-level, once)
2. Edit model roles in `rules/pstack-models.mdc`, then run `./scripts/sync-all-agent-config.sh`
3. Use `/poteto-mode` (or `/interrogate`, `/how`, etc.) in Cursor

The model rule syncs to `~/.cursor/rules/pstack-models.mdc` only. The
`poteto-agent` subagent still requires the Cursor plugin.

See [AGENTS.md](AGENTS.md) for the full file format specification and style guidelines.
