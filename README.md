# agent-skills

Reusable skill definitions for AI coding agents. Each skill is a structured Markdown file that gives an agent the instructions, workflow, and guardrails it needs to perform a specific task — setting up CI, auditing a codebase, resuming work across tools, and so on.

Skills are designed to be portable across Codex, Claude Code, Cursor, Copilot, and other agent routers. The YAML frontmatter in each file provides the trigger metadata agents use to decide when to load the skill.

## Available Skills

| Skill                                                                  | Description                                                                                                                   |
| ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| [agent-native-audit](skills/agent-native-audit/SKILL.md)               | Assess agent readiness with repository evidence; use optional scores for comparisons                                          |
| [anti-slop](skills/anti-slop/SKILL.md)                                 | Detect and remove AI writing tells from prose while preserving the author's voice                                             |
| [better-ai-design](skills/better-ai-design/SKILL.md)                   | Develop a strong visual direction for consequential interface work, with optional exploration and critique                    |
| [ci-verify-setup](skills/ci-verify-setup/SKILL.md)                     | Set up a project-level verification command and matching CI workflow                                                          |
| [company-profile](skills/company-profile/SKILL.md)                     | Create a reusable company fact sheet and ready-to-use descriptions, bios, and page copy                                        |
| [derive-client](skills/derive-client/SKILL.md)                         | Capture browser traffic as HAR, then derive a reusable HTTP/CLI client instead of driving the browser every time              |
| [dxd-code-review](skills/dxd-code-review/SKILL.md)                     | Run an extremely strict DXD-style maintainability review for abstraction quality, giant files, and spaghetti-condition growth |
| [i-have-adhd](skills/i-have-adhd/SKILL.md)                             | Shape responses for ADHD-friendly reading with direct outcomes, bounded actions, and visible state                            |
| [learn](skills/learn/SKILL.md)                                         | Learn from Codex and OpenCode sessions to propose evidence-backed skill and instruction improvements                          |
| [paper-design](skills/paper-design/SKILL.md)                           | Create and review native editable Paper designs through the direct Paper MCP                                                  |
| [quick-fix-deploy-sync](skills/quick-fix-deploy-sync/SKILL.md)         | Fast-forward sync production and staging branches for hotfixes, backports, and quick deploys                                  |
| [resume-work](skills/resume-work/SKILL.md)                             | Find the current state across tools, then continue or verify the requested work                                              |
| [test-audit](skills/test-audit/SKILL.md)                               | Evaluate test value and audit suites for duplicate coverage, implementation coupling, and test-only seams                    |
| [ui-text-audit](skills/ui-text-audit/SKILL.md)                         | Audit every screen for redundant, verbose, or unnecessary UI text and remove what doesn't help the user                       |

## Skill Format

Each skill lives in `skills/<name>/SKILL.md` with YAML `name` and `description`
fields. The name matches the directory; the description identifies when to load it.

The body contains only guidance that changes useful decisions: local conventions,
non-obvious tool procedures, preferences, and concrete acceptance criteria. Choose
headings and checklists to fit the task rather than repeating a fixed template.
Keep substantial conditional procedures in linked references and state when to
read them. Preserve real safety constraints without repeating generic policy in
every skill.

```
agent-skills/
├── skills/<name>/SKILL.md          # canonical skills
├── .claude-plugin/                 # Claude Code plugin + marketplace
├── .codex-plugin/plugin.json       # Codex plugin
├── assets/                         # public plugin logo and composer icon
├── .cursor-plugin/                 # Cursor plugin + marketplace
├── .agents/plugins/marketplace.json  # Codex marketplace
├── scripts/
│   ├── sync-plugin-packaging.py    # aligned plugin version bumps
│   ├── build-openai-submission.py  # public skills-only ZIP
│   ├── sync-agent-symlinks.sh
│   ├── sync-pstack-skills.sh
│   └── sync-all-agent-config.sh
├── AGENTS.md
└── README.md
```

## Adding a Skill

1. Check the current inventory for overlap, then create `skills/<skill-name>/SKILL.md`.
2. Add precise YAML routing metadata and the task-specific instructions it needs.
3. Validate frontmatter, relative links, and Markdown whitespace.
4. Update the Available Skills table when adding, removing, or changing a skill's scope.
5. Run `python3 scripts/sync-plugin-packaging.py` to bump all plugin manifest
   versions, then confirm with `--check`.
6. Run `./scripts/sync-agent-symlinks.sh` to refresh custom skill links, or install the
   local hooks once with `./scripts/install-local-githooks.sh`.
7. Commit the skill and the manifest bumps together, with an imperative message such
   as `Add <skill-name> skill`.

## Plugin

The same skills ship as the `dxd-skills` plugin for teammates and other machines.
Skills load namespaced, for example `dxd-skills:anti-slop`.

| Tool        | Marketplace file                   | Install                                                                                             |
| ----------- | ---------------------------------- | --------------------------------------------------------------------------------------------------- |
| Claude Code | `.claude-plugin/marketplace.json`  | `/plugin marketplace add designxdevelop/agent-skills`, then `/plugin install dxd-skills@dxd-skills` |
| Codex       | `.agents/plugins/marketplace.json` | Add this repo as a plugin marketplace, then install `dxd-skills`                                    |
| Cursor      | `.cursor-plugin/marketplace.json`  | Add this repo as a plugin marketplace, then install `dxd-skills`                                    |

On a machine that already runs `sync-all-agent-config.sh`, the global symlinks load the
same skills, so installing the plugin as well gives duplicate entries.

### Public OpenAI submission

Run `python3 scripts/build-openai-submission.py` from the repository root. It checks
the plugin packaging, then creates `dist/dxd-skills-<version>-openai-submission.zip`
with the Codex plugin manifest, canonical skills, and branding assets. Upload that ZIP through
the OpenAI Platform's **Skills only** plugin submission flow. The `dist/` folder is
ignored by Git; build a fresh ZIP after each version bump.

## Global Agent Config

This repo is the source of truth for machine-wide agent configuration on Austin's machines.

| Path in repo  | Sync target                                                  | Purpose                                             |
| ------------- | ------------------------------------------------------------ | --------------------------------------------------- |
| `skills/*/`   | `~/.agents/skills/*` (+ Cursor/Claude/Codex/OpenCode spokes; T3 Code aliases the hub) | Custom DXD skills                                   |

Run a full sync anytime:

```bash
./scripts/sync-all-agent-config.sh
```

Audit the active roots without changing them:

```bash
./scripts/audit-agent-skills.sh
```

That runs:

1. `./scripts/sync-agent-symlinks.sh` — custom skills

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
2. Edit model roles in `~/.cursor/rules/pstack-models.mdc`
3. Use `/poteto-mode` (or `/interrogate`, `/how`, etc.) in Cursor

The `poteto-agent` subagent still requires the Cursor plugin.

See [AGENTS.md](AGENTS.md) for the full file format specification and style guidelines.
