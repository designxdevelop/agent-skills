# History sources

Use read-only interfaces supported by the installed version. The host running this skill and the histories being analyzed may differ. Inspect CLI help or available tool schemas before relying on a command; OpenCode 1 and 2 are separate adapters.

## Codex

Prefer an available task-history connector or Codex app-server: list stored threads, then read selected threads with full turns (`thread/read`, `includeTurns: true`). Page through listings, include archives when needed for the requested window, and inspect source filters so a default limited to CLI/IDE does not silently omit desktop sessions. Summaries alone are insufficient for attributing corrections; retrieve full relevant turns or mark the evidence incomplete.

For local CLI history without an API, inspect `${CODEX_HOME:-~/.codex}/sessions` and `archived_sessions` for rollout JSONL. Use a JSON parser, inspect a small sample to establish the installed schema, and filter session metadata by project and timestamps before reading message content. Common records include `session_meta`, `response_item`, and `event_msg`; a message can be represented more than once, so choose one canonical representation rather than counting both. Preserve speaker, timestamp, tool/action relationship, and session identity. The prompt index `history.jsonl` alone lacks the context required for this analysis. Do not depend on hidden reasoning being present.

## OpenCode

Confirm commands with `opencode session list --help` and `opencode export --help`. Supported installations can list sessions with `opencode session list --format json` and export one with `opencode export SESSION_ID`. Prefer `--sanitize` when the installed export command supports it, then inspect for remaining sensitive data before including excerpts. Parse the exported JSON; preserve roles and message/part relationships rather than flattening everything into user speech. Verify project and date coverage from the export metadata.

## OpenCode 2

Start with `opencode2 --help` or the installed plugin/SDK schema. Use its available session listing and message-reading interface, or its session export facility. Do not assume OpenCode 1 export flags, storage schema, or commands exist in version 2. If initialization fails, report that source as unavailable and continue with other histories; do not launch an interactive agent, migrate storage, or modify configuration to obtain a transcript. Request an export only if that source is needed to complete the requested scope.

For either OpenCode version, when no export/API is available, locate storage through the installed version's configuration or documentation. Inspect a database schema with a read-only SQLite connection before querying named tables; use consistent read transactions for live databases. Do not copy only a live database's main file and ignore its WAL, open it writable, or hard-code an unverified table layout. Mark unsupported formats as gaps instead of guessing.

## Skill and configuration targets

Inspect project `.agents/skills` and `.opencode/skills`, the shared `~/.agents/skills` hub, Codex's configured skill directories, and OpenCode's configured skill roots. Resolve symlinks before choosing edit destinations. A portable `learn/SKILL.md` can be invoked as `$learn` in Codex and selected as a skill in OpenCode. For a literal `/learn` command on versions that require a separate custom command, configure a thin command that loads the installed learn skill using that version's documented command mechanism; keep the workflow in SKILL.md.

Official references, for resolving installed-version details:

- [Codex app-server](https://learn.chatgpt.com/docs/app-server)
- [Codex skills](https://learn.chatgpt.com/docs/build-skills)
- [OpenCode CLI](https://opencode.ai/docs/cli/)
- [OpenCode 2 plugins](https://opencode.ai/v2/docs/build/plugins)
- [OpenCode 2 skills](https://opencode.ai/v2/docs/skills)
- [OpenCode 2 commands](https://opencode.ai/v2/docs/commands)
