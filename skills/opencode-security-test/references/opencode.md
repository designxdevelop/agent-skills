# OpenCode session handoff

Read this when launching or collecting a security-testing session. The installed
CLI is authoritative: OpenCode versions have different configuration and export
interfaces. These instructions require a host with terminal access; a chat-only
host should report that limitation and provide the prepared handoff.

## Discover the installed interface

Use `command -v opencode`, `opencode --version`, `opencode run --help`, and
`opencode models --help`. List models through the supported interface. Inspect
agent and permission configuration without exposing credential values. Resolve
setup or permission failures through the host rather than disabling controls.
Do not launch a model just to discover CLI flags.

Check session/export help before collecting a transcript. Older releases use
`opencode export SESSION_ID`; newer releases may use
`opencode session export SESSION_ID`. Use sanitization if supported and inspect
the result for residual secrets before including excerpts in a report.

## Launch and monitor

Create a private temporary artifact directory and save `handoff.md` there.
Use the host's file tools or a quoted heredoc to write literal text. Never
interpolate the user's request into shell code. Set the working directory
through the process tool; avoid assuming every version supports `--dir`.

After verifying these flags in installed help, a typical invocation is:

```bash
opencode run --model "$security_model" --format json \
  --title "Scoped security testing" --file "$security_handoff" \
  "Perform the scoped task in the attached handoff. Return evidence and results."
```

Set `security_model` to the selected exact provider/model ID and
`security_handoff` to the absolute handoff path. Prefer a subprocess argument
array when available. Capture stdout and stderr separately in the private
artifact directory without losing the process exit status. Do not use
`--continue`: an unrelated previous session can contaminate context.

If installed help supports `--standalone`, prefer it for a private server
instead of reusing an unrelated background service. Inspect effective sharing
and tool permissions before launch, using that version's supported controls.
Ensure automatic sharing is disabled for this session; do not overwrite global
settings. Existing plugins, MCP servers, and broad permissions can expose more
than the handoff describes. Restrict them through supported per-run controls
or an isolated environment; if that cannot be done within authorization,
report the limitation before launch. For a source-only audit, configure the
installed version's permissions to deny edit, bash, and mutating MCP/custom
tools while allowing only necessary reads and searches. If test commands are
needed, use a disposable environment with a read-only source mount and a
separate writable scratch directory, or narrowly permit verified commands
through a supported approval interface. Do not assume built-in agent names
such as `plan` enforce read-only behavior on every installation.

Use the host's process/session handle to monitor output and stop at the agreed
deadline. Do not add `--auto` or equivalent permission bypass flags. If the run
cannot service an approval request, stop and report the pending action.

Parse JSON events according to their observed structure, recording the exact
session ID and assistant output. Handle errors, interrupted runs, missing final
answers, and permission blocks explicitly. Never choose the latest session by
timestamp when other sessions may be running. Continue only by the captured
session ID, with the same scope and model unless the user changes them.

## Sources

- [OpenCode CLI](https://opencode.ai/docs/cli/)
- [OpenCode V2 CLI commands](https://opencode.ai/v2/docs/cli/commands/)
- [OpenCode models](https://opencode.ai/docs/models/)
- [OpenCode permissions](https://opencode.ai/docs/permissions/)
