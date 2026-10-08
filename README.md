# agent-skills

Reusable skill definitions for AI coding agents. Each skill is a structured Markdown file that gives an agent the instructions, workflow, and guardrails it needs to perform a specific task — setting up CI, auditing a codebase, resuming work across tools, and so on.

Skills are designed to be portable across Codex, Claude Code, Cursor, Copilot, and other agent routers. The YAML frontmatter in each file provides the trigger metadata agents use to decide when to load the skill.

## Quick start

On this machine, refresh the installed skills from this checkout:

```bash
./scripts/sync-all-agent-config.sh
```

Then ask your agent to use a skill by name, for example:
`Use anti-slop to make this paragraph clearer while preserving my voice.`

For a separate installation, follow [Plugin](#plugin). Use either local sync or
the plugin, not both, to avoid duplicate skills.

## Available Skills

| Skill                                                                  | Description                                                                                                                   |
| ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| [adversarial-review](skills/adversarial-review/SKILL.md)               | Send a diff to a different model family for an adversarial bug review, then triage every finding                              |
| [agent-native-audit](skills/agent-native-audit/SKILL.md)               | Assess agent readiness with repository evidence; use optional scores for comparisons                                          |
| [anti-slop](skills/anti-slop/SKILL.md)                                 | Detect and remove AI writing tells from prose while preserving the author's voice                                             |
| [better-ai-design](skills/better-ai-design/SKILL.md)                   | Develop a strong visual direction for consequential interface work, with optional exploration and critique                    |
| [ci-verify-setup](skills/ci-verify-setup/SKILL.md)                     | Set up a project-level verification command and matching CI workflow                                                          |
| [company-profile](skills/company-profile/SKILL.md)                     | Create a reusable company fact sheet and ready-to-use descriptions, bios, and page copy                                        |
| [derive-client](skills/derive-client/SKILL.md)                         | Capture browser traffic as HAR, then derive a reusable HTTP/CLI client instead of driving the browser every time              |
| [dxd-code-review](skills/dxd-code-review/SKILL.md)                     | Run an extremely strict DXD-style maintainability review for abstraction quality, giant files, and spaghetti-condition growth |
| [i-have-adhd](skills/i-have-adhd/SKILL.md)                             | Shape responses for ADHD-friendly reading with direct outcomes, bounded actions, and visible state                            |
| [learn](skills/learn/SKILL.md)                                         | Learn from Codex and OpenCode sessions to propose evidence-backed skill and instruction improvements                          |
| [open-pstack](skills/open-pstack/SKILL.md)                           | Apply portable pstack-style investigation, implementation, review, performance, and delivery workflows                        |
| [opencode-security-test](skills/opencode-security-test/SKILL.md)     | Run authorized security testing with ranked open-source models in OpenCode, in-session or delegated                        |
| [paper-design](skills/paper-design/SKILL.md)                           | Create and review native editable Paper designs through the direct Paper MCP                                                  |
| [pr-babysit](skills/pr-babysit/SKILL.md) | Watch or repair PRs with existing monitors, one writer, and safe merge and stack handling |
| [quick-fix-deploy-sync](skills/quick-fix-deploy-sync/SKILL.md)         | Fast-forward sync production and staging branches for hotfixes, backports, and quick deploys                                  |
| [resume-work](skills/resume-work/SKILL.md)                             | Find the current state across tools, then continue or verify the requested work                                              |
| [simplified-technical-english](skills/simplified-technical-english/SKILL.md) | Write, rewrite, and check technical documentation in ASD-STE100 Simplified Technical English |
| [test-audit](skills/test-audit/SKILL.md)                               | Prefer focused E2Es and API/database contracts; prune redundant unit and component tests                    |
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
│   ├── verify.py                  # local and CI verification
│   ├── check-markdown.py          # local links and whitespace
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
3. Update the Available Skills table when adding, removing, or changing a skill's scope.
4. Run `python3 scripts/sync-plugin-packaging.py` to bump all plugin manifest versions.
5. Run `python3 scripts/verify.py` to check Markdown, frontmatter, packaging, and the submission ZIP.
6. Run `./scripts/sync-agent-symlinks.sh` to refresh custom skill links, or install the
   local hooks once with `./scripts/install-local-githooks.sh`.
7. Commit the skill and the manifest bumps together, with an imperative message such
   as `Add <skill-name> skill`.

## Verification

Run the same checks locally as CI:

```bash
python3 scripts/verify.py
```

This checks Markdown whitespace and local link targets, tests the Markdown
checker, validates plugin packaging, and builds and verifies the public
submission ZIP in `dist/`. External URLs and link fragments are not checked.

For Markdown-only edits, run `python3 scripts/check-markdown.py`.

## Plugin

Website update notifications and activation instructions are documented in
[website sync](docs/website-sync.md).

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
ignored by Git; build a fresh ZIP after each version bump. The ZIP includes
`PRIVACY.md`; the listing links to the published policy at
[designxdevelop.com/agent-skills/privacy](https://designxdevelop.com/agent-skills/privacy). Keep that page
and the packaged policy aligned, and publish the page before submitting.

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
installed. Use `open-pstack` for the portable adaptation in other hosts.

Add `--with-pstack` only if you intentionally want that catalog back in every
harness:

```bash
./scripts/sync-all-agent-config.sh --with-pstack
```

T3 Code uses `~/.config/agents/skills`, which should be a directory symlink to
`~/.agents/skills`. The sync script creates the alias when it is absent and
refuses to overwrite a standalone directory; back up that directory first if
you are consolidating an existing T3 installation.

### Open PStack (Claude, Codex, and chat hosts)

[open-pstack](skills/open-pstack/SKILL.md) is a self-contained adaptation of
[Lauren Tan's pstack](https://github.com/cursor/plugins/tree/main/pstack), shipped
inside `dxd-skills`. It includes investigation, debugging, architecture, review,
performance, PR delivery, and handoff workflows without Cursor dependencies.

After installing the plugin or syncing local skills, ask Claude Code to use
`open-pstack`, or invoke `$open-pstack` in Codex. For example:

```text
Use open-pstack to reproduce this bug, fix its cause, and verify the result.
Use open-pstack to challenge this diff. Review only; do not change files.
```

For ChatGPT, supply `skills/open-pstack/SKILL.md` and the relevant files from its
`references/` directory as context in a surface that accepts files. This provides
workflow guidance; execution and repository access depend on the tools available
in that chat. It does not install a ChatGPT app. The full skill is included in
the standard `dxd-skills` plugin submission ZIP; no separate export is needed.

The adaptation pins its reviewed upstream revision and includes the MIT license.
See [adaptation boundaries](skills/open-pstack/references/upstream.md) for scope.
Maintainer metadata lives in `scripts/open-pstack-upstream.json` and is excluded
from the skill bundle. Updates are deliberate, not automatic imports of Cursor
instructions.

#### Review Open PStack updates
From a checkout of this repository, fetch the pinned source into a new directory:

```bash
python3 scripts/fetch-open-pstack-upstream.py --output /tmp/pstack-pinned
```

To inspect the latest upstream separately:

```bash
python3 scripts/fetch-open-pstack-upstream.py --ref main --output /tmp/pstack-candidate
```

The helper retrieves source for review; it never installs skills, executes upstream scripts, or overwrites this adaptation. Compare the two snapshots, read relevant changed source files, and deliberately port useful changes. Preserve host permission boundaries and tool availability fallbacks. Update `scripts/open-pstack-upstream.json` only after reviewing the candidate revision; keep the license when adapting upstream material. Run the repository's packaging sync and check after editing the skill.

The helper lives at the repository root and is a maintainer utility, not a runtime dependency of the installed skill. All normal workflows work offline from the bundled Markdown references.

### Original pstack (Cursor plugin only)

[pstack](https://github.com/cursor/plugins/tree/main/pstack) is a Cursor plugin,
not a global skill pack. It works best inside Cursor. Do not copy it into the
shared hub.

1. In Cursor: `/add-plugin pstack` (user-level, once)
2. Edit model roles in `~/.cursor/rules/pstack-models.mdc`
3. Use `/poteto-mode` (or `/interrogate`, `/how`, etc.) in Cursor

The `poteto-agent` subagent still requires the Cursor plugin.

See [AGENTS.md](AGENTS.md) for the full file format specification and style guidelines.
