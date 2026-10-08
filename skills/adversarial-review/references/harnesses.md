# Harness detection and invocation

Read this before launching a review. Model ids below are the pinned ids from the cited docs. A harness catalog can show a different string for the same product. Use a catalog id only when that catalog printed it. Otherwise use the CLI path. Never invent an id.

## Caller and reviewer ids

| Role | Product | Pinned id | Where it is valid |
| --- | --- | --- | --- |
| OpenAI reviewer | GPT-6 Astra | `gpt-6-astra` | Codex CLI `-m` / `--model` |
| OpenAI caller example | GPT-6.1 Sol | `gpt-6.1-sol` | Codex CLI `-m` / `--model` |
| Anthropic reviewer, default | Opus 5.5 | `claude-opus-5-5` | Claude Code `--model` and the Claude API |
| Anthropic reviewer, lighter | Sonnet 5.5 | `claude-sonnet-5-5` | Claude Code `--model` and the Claude API |

Sources: [Codex models](https://learn.chatgpt.com/docs/models) (`codex -m gpt-6-astra`, `codex exec -m gpt-6.1-sol`), [Claude Code model configuration](https://code.claude.com/docs/en/model-config) (`claude-opus-5-5`; Opus 5.5 needs Claude Code v2.1.280 or later, Sonnet 5.5 needs v2.1.284 or later), [Opus 5.5](https://platform.claude.com/docs/en/models/opus-5-5/overview), [Sonnet 5.5](https://platform.claude.com/docs/en/models/sonnet-5-5/overview).

On the Anthropic API, the `opus` and `sonnet` aliases currently resolve to those versions and can move. Pass the full ids.

## Which path

| Harness | Lab | How to tell | Invocation |
| --- | --- | --- | --- |
| Claude Code | Anthropic only | Session is `claude`, or the product name is Claude Code | Other lab: `codex exec -m gpt-6-astra` |
| Codex | OpenAI only | Session is `codex`, or the product name is Codex | Other lab: `claude -p --model claude-opus-5-5` (or `claude-sonnet-5-5` when the lighter reviewer applies) |
| Cursor | Multi-model | Cursor editor or the `agent` CLI | Native only if `agent models` lists the reviewer. Otherwise the other lab's CLI |
| OpenCode | Multi-model | `opencode` session | Native only if `opencode models` lists the reviewer. Otherwise the other lab's CLI |
| Anything else | Unknown | The session does not match a row above | Other lab's CLI from the caller table |

A single-lab harness cannot reach the other vendor through its own subagents. Claude Code subagents stay on Claude. Codex subagents stay on OpenAI. Cursor documents a `model` field on agent files. A [Cursor forum report](https://forum.cursor.com/t/marketplace-plugin-agents-not-using-model-frontmatter/168771) says installed agents ignore that field and run on the parent model; Cursor staff called that unexpected. This skill does not ship a pinned agent file. Cursor CLI print mode is the native switch.

Cursor's published pricing page lists Claude Opus 5.5 and documents the fast-mode id `claude-opus-5-5-fast`. It does not list GPT-6 Astra. Treat `agent models` as the list of usable Cursor ids. If Astra or Opus 5.5 is absent there, use the CLI path.

OpenCode selectors are `provider/model` and come from the configured catalog (`opencode models`, `opencode run --model`). Docs examples such as `anthropic/claude-sonnet-4-5` are not these reviewer ids. Match a printed catalog id that contains `gpt-6-astra`, `claude-opus-5-5`, or `claude-sonnet-5-5`, or whose label is that product. If none matches, use the CLI path.

## Detect binaries and auth

Run `command -v` for `codex`, `claude`, `agent`, `cursor-agent`, and `opencode`. `agent` is the documented Cursor binary. Some installs expose `cursor-agent` instead. Use `agent` when both exist, and substitute `cursor-agent` for `agent` in the commands below when it is the only one present.

Check auth before spending a review:

```bash
codex login status
claude auth status
agent status
```

`codex login status` exits 0 when credentials are present and 1 when it prints `Not logged in`. Check it before `codex exec`. A logged-out exec still accepts `-m gpt-6-astra`, then exits 1 with `401 Unauthorized` after retries. That is a failed review.

`claude auth status` exits 0 when logged in and 1 when not. A logged-out `claude -p` run prints `Not logged in · Please run /login` and exits 1. The shell login command is `claude auth login`.

`agent status` can exit 0 while printing `Not logged in`. Read the text. If it says that, the native path is unavailable. An unauthenticated `agent models` list is not an account catalog. On Cursor CLI `2026.10.01-e373342` that list omitted `gpt-6-astra`, `claude-opus-5-5`, and `claude-sonnet-5-5`, so the other lab's CLI is the path.

For OpenCode, `opencode models` is the auth signal: a missing provider means the catalog cannot serve that lab. These status results were checked on Codex CLI 0.161.0 and Claude Code 2.1.293 with no credentials stored.

## Fail closed

Stop and give the user the matching command. Do not continue into a same-lab review.

- `codex` missing: `curl -fsSL https://chatgpt.com/codex/install.sh | sh`
- `codex` present and `codex login status` non-zero: `codex login`
- `claude` missing: `curl -fsSL https://claude.ai/install.sh | bash`
- `claude` present and `claude auth status` non-zero: `claude auth login`
- Cursor native path wanted and `agent` missing: `curl https://cursor.com/install -fsS | bash`, then `agent login`
- Cursor or OpenCode catalog lacks the reviewer: the other lab's install and login command above
- OpenCode has no connected provider for that lab: `/connect` in OpenCode, or the other lab's CLI

Sources: [Codex CLI install](https://learn.chatgpt.com/docs/codex/cli), [Codex login](https://developers.openai.com/codex/cli/reference), [Claude Code setup](https://code.claude.com/docs/en/getting-started), [Claude Code CLI reference](https://code.claude.com/docs/en/cli-reference), [Cursor CLI overview](https://cursor.com/docs/cli/overview).

npm also installs Codex: `npm install -g @openai/codex`. Prefer the install script unless the user already uses npm for it.

## Portable invocations

Write the brief to a file outside the repo first. Pass that file. Do not expand the diff into the shell command.

OpenAI reviewer, from Claude Code or as the fallback elsewhere:

```bash
codex exec -m gpt-6-astra --sandbox read-only \
  --output-last-message "$review_out" - < "$review_brief"
```

`codex exec` defaults to a read-only sandbox; `--sandbox read-only` makes that explicit. `-` reads the prompt from stdin. `--output-last-message` writes the final message and still prints it. Do not pass `--sandbox workspace-write` or `--dangerously-bypass-approvals-and-sandbox`.

Anthropic reviewer, from Codex or as the fallback elsewhere. Swap in `claude-sonnet-5-5` only for the lighter option or the Opus-unavailable fallback:

```bash
cat "$review_brief" | claude -p --model claude-opus-5-5 \
  --tools "Read,Grep,Glob" \
  --permission-prompts none \
  --output-format text \
  "Perform the adversarial review in the piped brief. Do not edit files. Return findings only."
```

`--print` / `-p` is non-interactive. `--tools` limits the built-in tools to reads. `--permission-prompts none` denies anything that would have prompted. Do not pass `--dangerously-skip-permissions`.

Cursor, only with an id printed by `agent models` or `agent --list-models`:

```bash
agent -p --mode ask --model "$cursor_model_id" --output-format text \
  "Read ${review_brief} and perform that adversarial review. Do not edit files. Return findings only."
```

`review_brief` is an absolute path. `--mode ask` is the read-only mode. Print mode otherwise has write and shell tools. Do not pass `--force` or `--yolo`. The parameters page does not document stdin as the prompt, so the prompt points at the brief file. Confirm the flag names against `agent --help` if the installed CLI is older than the docs.

OpenCode, only with an id printed by `opencode models`:

```bash
opencode run --model "$opencode_model_id" --file "$review_brief" \
  "Perform the adversarial review in the attached handoff. Do not edit files. Return findings only."
```

Do not pass `--auto`. Confirm flags with `opencode run --help` before adding any this file does not list.

Sources: [Codex CLI reference](https://developers.openai.com/codex/cli/reference) (`--model`/`-m`, `--sandbox read-only`, `--output-last-message`, stdin prompt), [Codex non-interactive mode](https://developers.openai.com/codex/noninteractive), [Claude Code CLI reference](https://code.claude.com/docs/en/cli-reference) (`-p`, `--model`, `--tools`, `--permission-prompts`), [Cursor CLI parameters](https://cursor.com/docs/cli/reference/parameters) (`--model`, `--list-models`, `-p`, `--mode ask`), [OpenCode CLI](https://opencode.ai/docs/cli/) and [OpenCode models](https://opencode.ai/docs/models/) (`opencode run --model provider/model`, `--file`).
