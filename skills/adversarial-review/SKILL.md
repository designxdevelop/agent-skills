---
name: adversarial-review
description: >-
  Send a diff to a different model family for an adversarial bug review, then
  triage every finding. Use when the user asks for an adversarial review, a
  second model, or a cross-lab bug hunt.
---

# Adversarial review

A model reviewing its own diff misses bugs another family catches. Run this only when the user asks for it. The caller identifies its model, sends the scope to a reviewer from the other lab, and answers every finding. Same-family review is a failed run.

Read [references/harnesses.md](references/harnesses.md) before choosing a command. That file has the detection steps, model ids, and the flags each CLI actually accepts.

## Identify the caller

Name the model id the harness already assigned to this session. Use its status command or model picker when the id is not already in the conversation. Stop if the id is still unknown.

| Caller | Reviewer |
| --- | --- |
| Any Anthropic model (Opus, Sonnet, Haiku, Fable) | GPT-6 Astra, `gpt-6-astra` |
| GPT-6.1 Sol, GPT-6 Astra, or any other OpenAI GPT model | Opus 5.5, `claude-opus-5-5` |
| Anything else | Stop. Ask the user which other-lab reviewer to use. |

GPT-6.1 Sol and GPT-6 Astra are the specified OpenAI cases; other GPT models use the same reviewer so the review stays cross-lab. An explicit user override replaces the default when the named reviewer is still the other lab. Say which reviewer you selected and why.

Sonnet 5.5, `claude-sonnet-5-5`, is the lighter OpenAI-caller option. Use it when the user asks for the lighter reviewer, or when the Opus 5.5 invocation fails because that model is unavailable on the account. State that choice. Auth failures, missing binaries, and crashes are not a reason to switch models.

If GPT-6 Astra is missing from the account, stop. Leave the diff unreviewed.

## Prepare the brief

Review the current branch against its base, including uncommitted changes. When the user names files, a commit, or a PR, review that scope instead. Stop when there is no diff and no named files.

Write the brief in a fresh temporary directory outside the repository. Include the base, head, status, and diff, plus a short note on what the change is supposed to do. Redact tokens, keys, and `.env` values before writing. Say in the report that the reviewer received the diff.

The brief tells the reviewer to hunt for real bugs, security holes, wrong assumptions, missing tests, and regressions. Style comments are in scope only when they conceal one of those. The reviewer returns findings only, each with `file:line`, severity (`blocker`, `high`, `medium`, or `low`), and a concrete repro or the reasoning that would let someone reproduce it. It does not edit the tree and does not delegate the review again.

## Invoke the reviewer

Claude Code is Anthropic-only. Codex is OpenAI-only. From either one, start the review by running the other lab's CLI. Cursor and OpenCode may use their own model switch when the live catalog lists the reviewer id. The same CLI invocation is the fallback there, and it is the path for every other harness.

Detect the binaries and authentication with the commands in the harness reference. A missing binary or a failed auth check ends the run. Report the exact install or login command from that reference and stop. Do the same when a multi-model catalog lacks the reviewer and the other lab's CLI is unavailable.

Launch through the portable invocations in the reference. Keep the reviewer's tools read-only. Capture its stdout and exit status.

A non-zero exit, an empty reply, or a reply that is not a finding list is a failed review. Stop and quote the error. Do not replace it with your own pass over the diff.

## Triage

Answer every finding. Agree and give a concrete fix plan, or disagree and give the specific reason. "Unlikely", "style", or "pre-existing" needs the evidence that makes it so. Order by severity.

Lead with a short verdict: what was reviewed, which caller and reviewer ran, how the reviewer was invoked, and whether any agreed findings should block. Then list the triaged findings. When the reviewer reports none, say that the other model reported none. Apply fixes only when the user asked for them.
