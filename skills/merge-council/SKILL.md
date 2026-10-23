---
name: merge-council
description: >-
  Convene Opus 5.5, Grok 4.7, and GPT-6.1 Sol to argue a change before it
  can merge. Use when the user asks to merge, land, or ship, or asks for
  this council before a merge. A cross-lab bug hunt with no merge is
  adversarial-review.
---

# Merge council

Leave the merge unperformed until the seated models have argued with the change. For a single cross-lab bug hunt with no merge, use `adversarial-review`. After this gate allows a merge, `pr-babysit` can land it.

Read [references/harnesses.md](references/harnesses.md) before launching a seat. That file is the harness detection, the model ids, and the invocations.

## When it runs

Run this before a merge, land, or ship, including a merge the user already authorized. Opening a pull request, pushing a branch, or asking for a review leaves the gate closed.

Review the current branch against its base, including uncommitted changes. When the user names a commit, pull request, or files, review that scope. Stop when there is no diff.

## Seats

The council is Opus 5.5, Grok 4.7, and GPT-6.1 Sol. Pass only the ids in the harness reference. Grok 4.7 uses the plain id `grok-4.7`. That id is the xAI API name, the OpenCode catalog id, and the Cursor model id. Reasoning effort (`low`, `medium`, `high`, `xhigh`) is a setting on it, so the seat is not an effort-tier id such as `grok-4.7-medium`. From Claude Code or Codex, that seat is the Cursor CLI command in the harness reference.

Name the model id this session is already running. Use the harness status line or model picker when the conversation does not already show it. Drop the seat whose id is that model. Also drop Grok 4.7 when the session id is `grok-4.7` with an effort suffix, such as `grok-4.7-medium`. A dropped caller seat is not an empty seat. The caller still convenes the remaining seats and answers them. Resolve an alias such as `opus` to a full id before dropping a seat. An unknown caller id drops nothing.

## Brief

Write one brief in a fresh temporary directory outside the repository. Include the base, head, status, diff, and what the change is supposed to do. Redact tokens, keys, and `.env` values before writing. Send that file to every seat.

The brief tells the seat to argue against the merge: real bugs, security holes, wrong assumptions, missing tests, and regressions. Style comments belong in the reply only when they conceal one of those. Each objection needs `file:line`, a severity (`blocker`, `high`, `medium`, or `low`), and a reason someone else could check. The seat leaves the tree unchanged, stays out of the merge, and does not call another model.

## Dispatch

Detect the harness, then launch only the seats that harness can call. Seats run independently, in one round, and receive no other seat's argument.

A missing binary, a failed login, an empty reply, or a reply that is not an objection list leaves that seat empty. Quote the error. Leave the seat empty rather than reviewing the diff as that model or swapping in a different one.

## Decide

Answer every objection. Agree and name the fix, or disagree and give the evidence that makes the objection fail. "Unlikely", "style", or "pre-existing" needs that evidence.

Allow the merge when every seat this harness can call has answered, and every disagreement is fixed or defended. An empty seat blocks the merge. Name the seat, why it is empty, and the setup in the harness reference, then stop. Merge without that seat only after the user has seen the gap and explicitly accepts it.

Lead with the verdict: the scope, the session model, which seats sat, which seats were empty, how each seated model was invoked, and whether the merge is allowed. Treat the replies as objections to answer. Apply fixes only when the user asked for them.
