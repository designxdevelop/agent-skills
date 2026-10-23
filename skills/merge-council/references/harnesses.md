# Harness detection and seat invocation

Read this before launching a seat. Model ids below are the pinned ids from the cited docs. A catalog id is usable only when that catalog printed it. Otherwise the seat is empty. Never invent an id.

## Seat ids

| Seat | Pinned id | Where that id is valid |
| --- | --- | --- |
| Opus 5.5 | `claude-opus-5-5` | Claude Code `--model` and the Claude API. On OpenCode or T3, a printed catalog slug whose model segment is `claude-opus-5-5` |
| GPT-6.1 Sol | `gpt-6.1-sol` | Codex CLI `-m` / `--model`. On OpenCode or T3, a printed catalog slug whose model segment is `gpt-6.1-sol` |
| Muse Wonder Full | `muse-wonder-full` | A printed catalog slug whose model segment is `muse-wonder-full`, including `meta/muse-wonder-full` |

Sources: [Codex models](https://learn.chatgpt.com/docs/models) (`codex --model gpt-6.1-sol`, `codex exec -m gpt-6.1-sol`), [Claude Code model configuration](https://code.claude.com/docs/en/model-config) (`claude-opus-5-5`; the `opus` alias moves, so pass the full id), [Meta models](https://dev.meta.ai/docs/models) (Muse Wonder Full is a Muse Code subscription model on Power Usage and Maximum Usage; `muse-wonder-1.0` on the Model API is the other variant, and maximum reasoning effort does not select Full), [Muse Wonder Full on models.dev](https://models.opencode.ai/models/meta/muse-wonder-full/) (`meta/muse-wonder-full`, no provider row as of 2026-10-23).

OpenCode selectors are `provider/model`. Docs examples include `opencode/gpt-6.1-sol`, `openai/gpt-6.1-sol`, and `anthropic/claude-sonnet-5-5`. Match the seat against the model segment of a line `opencode models` printed. A Zen or direct-provider prefix is fine. `muse-wonder-1.0` does not match Muse Wonder Full.

## Which harness

Check in this order. T3 Code and OpenCode win when they are the host, even if the inner provider is Claude Code or Codex. Launch a remaining seat only when that row can call its id.

| Order | Harness | How to tell | Dispatch |
| --- | --- | --- | --- |
| 1 | T3 Code | The host or product name is T3 Code | Connected T3 providers only. Do not execute `claude`, `codex`, or `opencode` |
| 2 | OpenCode | The session or product name is OpenCode | `opencode models`, then `opencode run`. Do not execute `claude` or `codex` |
| 3 | Claude Code | The product is Claude Code, or `CLAUDECODE` is `1` | Codex CLI for GPT-6.1 Sol. Codex has no Opus 5.5 or Muse Wonder Full id |
| 4 | Codex | The product is Codex | Claude Code CLI for Opus 5.5. Claude has no GPT-6.1 Sol or Muse Wonder Full id |
| 5 | Anything else | No row above matches | Stop. Name the host. Leave every seat empty |

`CLAUDECODE=1` is set in subprocesses Claude Code spawns ([Claude Code environment variables](https://code.claude.com/docs/en/env-vars)). Detect T3 Code and OpenCode by the product name. A `T3CODE_` variable is not required.

A same-provider subagent is not a seat. The turn has to be the pinned model for that seat.

Claude Code is Anthropic-only, and Codex is OpenAI-only. From Claude Code the opposite CLI is `codex`. From Codex the opposite CLI is `claude`. Neither CLI can host the other lab's seat or Muse Wonder Full. Report those seats empty. Do not point `codex exec` at `claude-opus-5-5` or `muse-wonder-full`, and do not point `claude` at `gpt-6.1-sol` or `muse-wonder-full`.

On Claude Code, Opus 5.5 is empty unless this session's resolved id is `claude-opus-5-5`, in which case the caller already is that seat and the seat stays dropped. On Codex, GPT-6.1 Sol is empty unless this session's resolved id is `gpt-6.1-sol`, in which case the seat stays dropped. Say which of those two descriptions applies.

## T3 Code

Use the model list T3 already shows for connected providers. Match a printed slug with the seat table. Start one read-only review turn per match on that provider instance, and give it the brief file. The turn must leave the tree unchanged.

When this session cannot start a turn on the matching provider, the seat is empty. Say which provider is not connected. Connecting `muse-wonder-1.0` does not fill Muse Wonder Full. Models.dev currently lists no API provider for `meta/muse-wonder-full`; Full is the Muse Code subscription model.

## OpenCode

`opencode models` is the catalog and the auth signal. A provider that is absent there cannot fill its seat. In OpenCode, `/connect` adds a provider. Then match a printed slug and run:

```bash
opencode run --model "$printed_id" --file "$brief" \
  "Argue against the merge in the attached brief. Leave the tree unchanged. Return objections only."
```

Do not pass `--auto`. Confirm flags with `opencode run --help` before adding any this file does not list. `$printed_id` is the catalog line, not a guessed prefix.

Sources: [OpenCode models](https://dev.opencode.ai/docs/models/) (`provider/model`, `opencode/gpt-6.1-sol`), [OpenCode CLI](https://opencode.ai/docs/cli/) (`opencode run --model`, `--file`).

## Claude Code and Codex

Check the opposite binary and its login before launching.

```bash
command -v codex
command -v claude
codex login status
claude auth status
```

`codex login status` exits 0 when credentials are present and 1 when it prints `Not logged in`. `claude auth status` exits 0 when logged in and 1 when not.

Write the brief first. Pass the file. Do not expand the diff into the shell command.

GPT-6.1 Sol from Claude Code:

```bash
codex exec -m gpt-6.1-sol --sandbox read-only \
  --output-last-message "$review_out" - < "$brief"
```

`codex exec` defaults to a read-only sandbox; `--sandbox read-only` makes that explicit. `-` reads the prompt from stdin. `--output-last-message` writes the final message and still prints it. Do not pass `--sandbox workspace-write` or `--dangerously-bypass-approvals-and-sandbox`.

Opus 5.5 from Codex:

```bash
cat "$brief" | claude -p --model claude-opus-5-5 \
  --tools "Read,Grep,Glob" \
  --permission-prompts none \
  --output-format text \
  "Argue against the merge in the piped brief. Leave the tree unchanged. Return objections only."
```

`--print` / `-p` is non-interactive. `--tools` limits the built-in tools to reads. `--permission-prompts none` denies anything that would have prompted. Do not pass `--dangerously-skip-permissions`.

Sources: [Codex CLI reference](https://developers.openai.com/codex/cli/reference), [Codex non-interactive mode](https://developers.openai.com/codex/noninteractive), [Claude Code CLI reference](https://code.claude.com/docs/en/cli-reference).

## When a seat is empty

Report the matching setup and stop that seat.

| Gap | What to report |
| --- | --- |
| `codex` missing | `curl -fsSL https://chatgpt.com/codex/install.sh | sh` |
| `codex` present, `codex login status` non-zero | `codex login` |
| `claude` missing | `curl -fsSL https://claude.ai/install.sh | bash` |
| `claude` present, `claude auth status` non-zero | `claude auth login` |
| Opposite CLI cannot host the seat | Say the CLI has no id for that seat. Claude Code can seat GPT-6.1 Sol. Codex can seat Opus 5.5. Muse Wonder Full needs a T3 or OpenCode catalog entry |
| T3 provider not connected | Name the provider in T3's provider settings. Do not launch `claude`, `codex`, or `opencode` to replace it |
| OpenCode catalog lacks the seat | `/connect` for that provider, then rerun `opencode models` |
| Muse Wonder Full absent from every catalog | `muse-wonder-full` is the Muse Code model on Power Usage and Maximum Usage. `muse-wonder-1.0` is the Model API variant, and models.dev lists no API provider for Full |

Sources: [Codex CLI install](https://learn.chatgpt.com/docs/codex/cli), [Codex login](https://developers.openai.com/codex/cli/reference), [Claude Code setup](https://code.claude.com/docs/en/getting-started).

npm also installs Codex: `npm install -g @openai/codex`. Prefer the install script unless the user already uses npm for it.
