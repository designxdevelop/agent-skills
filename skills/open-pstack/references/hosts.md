# Host capabilities

Discover capabilities from the current tool schemas and repository instructions. Tool names below describe roles, not calls to invent.

| Capability | Portable behavior |
| --- | --- |
| Files and terminal available | Inspect and edit the checkout; run the project's own verification commands. |
| Native subagents available | Use the host's delegation API with supported parameters and the user's model preferences. |
| Only one agent/model available | Perform scoped investigation, implementation, and a separate self-review in sequence. Label self-review honestly. |
| Browser/device control available | Reproduce and verify on the affected surface. |
| No execution or repository access | Analyze supplied artifacts, produce a proposed patch or plan, and name the missing validation. Request the minimal missing source when necessary. |
| Native scheduling available | Use it only for authorized ongoing work. Otherwise save a handoff; do not promise to keep running after the turn. |

## Claude Code

Load the installed skill through the skill mechanism or ask to use `open-pstack`. Use the exposed agent/task tools when available, respecting their actual model options. Do not pass Cursor's `poteto-agent`, cloud environment flags, or model slugs to them. Local project instructions and permissions continue to apply.

## Codex

Invoke `$open-pstack` when installed as a local skill, or select the plugin's namespaced skill. Use native collaboration tools if exposed; respect project model selection. A user-visible chat is not a substitute for an internal subagent: create or message another chat only when authorized. Use native worktree, scheduling, and review attachment tools when the host requires them.

## ChatGPT or another chat host

This is Markdown guidance, not a ChatGPT app or a promise of repository access. Supply `SKILL.md` and the relevant reference files in a supported file/context surface, or use an installed integration that exposes the skill. Ask the host to follow Open PStack for the task. Plain chat can inspect provided code and propose changes; tool-backed execution, persistent memory, and parallel agents depend on the actual environment. Never describe proposed commands as executed.

## Model roles and setup

No setup command or global rule is necessary. Honor explicit user/project choices first. Otherwise use the host's configured model; if assigning a role requires an explicit model, choose among supported options. Multiple models are optional. Do not silently substitute for a specifically requested unavailable model; report the limitation and continue independent work where possible. Do not read or rewrite Cursor's `pstack-models.mdc` as cross-host configuration.
