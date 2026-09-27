---
name: open-pstack
description: Apply pstack-style engineering workflows across Claude, Codex, and other agents for evidence-led investigation, bug fixes, architecture, adversarial review, performance work, and verified delivery. Use when asked for open-pstack, portable pstack, or a pstack-style workflow.
---

# Open PStack

A portable adaptation of Lauren Tan's pstack (GitHub repository `cursor/plugins`, directory `pstack`).

Use this workflow for the requested task. If the user asks to keep the mode active, apply it to subsequent engineering tasks until they opt out; casual conversation needs no playbook. Invocation does not grant permission to publish, merge, send messages, change global settings, or start recurring work.

## Ground the work

Read the repository guidance and inspect the actual state before selecting a workflow. Establish the intended outcome, the affected data and control flow, and an observable completion check. Trace inputs through ownership, state transitions, side effects, and failure paths. Explain historical intent only when source history or documents support it.

Use the tools actually exposed by the host. Read [references/hosts.md](references/hosts.md) when resolving delegation, model selection, persistence, or a host without execution tools. No Cursor plugin, named subagent type, model family, or external skill is required.

## Select the relevant workflow

Read only the reference needed for the task. Combine workflows when there is a real dependency, such as investigation before a fix.

| Request | Reference |
| --- | --- |
| How/why, root cause, bug fix, runtime or captured-trace diagnosis | [investigation.md](references/investigation.md) |
| Feature, architecture, refactor, prototype, visual parity | [implementation.md](references/implementation.md) |
| Adversarial review, parallel exploration, competing designs | [review-and-delegation.md](references/review-and-delegation.md) |
| Performance improvement or repeated metric optimization | [performance.md](references/performance.md) |
| PR status, CI repair, opening a PR, shipping a stack | [delivery.md](references/delivery.md) |
| Long work, multi-phase work, resume, pause, skill evaluation | [long-running.md](references/long-running.md) |

For an unmatched task, derive a short plan from its outcome, uncertainty, dependencies, and verification needs. Do not force every task through every workflow.

## Engineering discipline

- Name the domain data and invariants before adding stateful logic. Prefer a clear state model or table to scattered flags. Validate external inputs at boundaries and keep internal contracts understandable.
- Choose the smallest change that solves the evidenced problem. Remove obsolete paths within scope; avoid speculative abstractions and unrelated cleanup. Reconsider a premise when repeated fixes based on it fail.
- Split independent mutable resources before adding coordination. Keep retries idempotent where the operation may be repeated. Migrate internal callers together when feasible; respect public compatibility requirements.
- Verify the behavior users consume. Compilation and static inspection are useful evidence, but do not establish runtime behavior. Keep worthwhile regression tests that fail for the original defect; avoid tests that merely mirror implementation.
- Own the final artifact. Inspect delegated changes, integrate them, and verify the combined result. A worker's summary, unanimous review, or green CI alone is not proof of the requested behavior.

Use a short plan for consequential multi-step work and adjust it as evidence changes. No mandatory fan-out, fixed reviewer count, or ritual checklist for trivial edits.

## Report

Lead with the result and its practical effect. Explain the consequential choice, the evidence actually obtained, and any material gap. Distinguish observations from hypotheses. Say what was not verified when tools or access were missing. Include commands, measurements, or artifact links when they make the result reproducible; never invent a run, review, citation, or background process.
