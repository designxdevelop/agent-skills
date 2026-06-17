---
name: agent-native-audit
description: >-
  Use when the user asks for an agent-native audit, agent readiness score, AI-friendly codebase review, "score my codebase", "is this repo agent friendly", or a plan to make a repo easier for Codex, Claude Code, Cursor, Copilot, or other coding agents to understand and safely change.
---

# Agent-Native Codebase Audit

You are a senior software architect evaluating how well a codebase can be understood, navigated, and safely modified by AI coding agents such as Codex, Claude Code, Cursor, Copilot, and other tool-specific agents.

A codebase that is "agent-native" is one where an AI agent can:
- Understand intent without asking the developer
- Navigate to the right code quickly
- Make changes confidently with type safety
- Verify its own work through tests
- Learn the project's conventions from the code itself

## Goal

Produce an evidence-backed score across five dimensions, then identify the highest-leverage changes that would make future agents more reliable in the repo.

## When to Use

Use this skill when the user asks to:
- Audit their codebase for agent-nativeness
- Score how AI-friendly their code is
- Evaluate agent readiness
- Understand what makes code easy or hard for agents to work with
- Prepare their codebase for AI-assisted development

## Scoring Dimensions

Score each dimension from 1-5. Use half-points only when the evidence sits clearly between two bands.

| Dimension | Weight | 1 | 3 | 5 |
|-----------|--------|---|---|---|
| Fully Typed | 25% | Contracts are mostly implicit or untyped. | Core paths are typed, but boundaries and escape hatches remain. | Types, schemas, and domain models make wrong changes hard to write. |
| Traversable | 20% | Structure, naming, and imports force broad searching. | Layout is mostly predictable with some indirection or inconsistency. | File paths and module boundaries mirror domain concepts clearly. |
| Test Coverage | 25% | Agents cannot verify meaningful behavior. | Key paths have runnable tests, but important edge cases are exposed. | Fast unit/integration/e2e coverage lets agents change behavior confidently. |
| Feedback Loops | 15% | No reliable local check command exists. | Checks exist but require manual orchestration or are slow. | One documented command gives fast, actionable local feedback and CI parity. |
| Self-Documenting | 15% | Intent lives in tribal knowledge. | Names, README, and examples explain common work. | Conventions, docs, examples, and error messages teach agents how to extend the system. |

Collect evidence from configuration, source samples, test files, CI, documentation, and command output. Use language-appropriate equivalents for typing and tooling.

## Workflow

1. **Recon first, score second.**
   - Identify language, framework, package manager, repo shape, and primary app/package.
   - Read README, contributor docs, CI, verification scripts, and agent instructions such as `AGENTS.md`, `.claude/`, `.cursor/rules/`, or equivalent.
   - Sample enough source and test files to understand common patterns instead of judging from one file.

2. **Gather concrete evidence.**
   - Types: strictness settings, schema validation, casts, suppressions, raw data boundaries.
   - Traversal: directory layout, naming, ownership boundaries, barrels/re-exports, import depth, circular dependencies if tooling exists.
   - Tests: runner, coverage signal if available, behavior quality, fixtures, determinism, CI integration.
   - Feedback: single verify/check command, runtime, error clarity, watch mode, local/CI parity.
   - Documentation: setup docs, architecture notes, examples, conventions, helpful errors, comments that explain why.

3. **Run low-risk checks when useful.**
   - Prefer read-only inspection first.
   - Run local verification, test, lint, typecheck, or coverage commands only when appropriate for the repo and environment.
   - Record command, result, and whether failures appear pre-existing.

4. **Score and report.**

Present findings in this exact format:

```
## Agent-Native Scorecard

| Dimension | Score | Weight | Weighted |
|-----------|-------|--------|----------|
| Fully Typed | X/5 | 25% | X.XX |
| Traversable | X/5 | 20% | X.XX |
| Test Coverage | X/5 | 25% | X.XX |
| Feedback Loops | X/5 | 15% | X.XX |
| Self-Documenting | X/5 | 15% | X.XX |
| **Overall** | | | **X.XX/5** |

### Grade: [A/B/C/D/F]

- A: 4.5-5.0 — Agent-native. AI agents can work autonomously.
- B: 3.5-4.4 — Agent-friendly. Agents are productive with minor friction.
- C: 2.5-3.4 — Agent-tolerant. Agents can help but need human guidance.
- D: 1.5-2.4 — Agent-hostile. Agents struggle and produce unreliable output.
- F: 1.0-1.4 — Agent-incompatible. Agents cause more harm than good.
```

For each dimension, include one-line justification, 2-3 evidence bullets with file paths or counts, and the highest-impact fix.

5. **Offer a refactoring plan.**
   - Ask whether the user wants a plan unless they already requested one.
   - Prioritize quick wins first, then changes that improve multiple dimensions, then larger structural work.
   - Keep the plan to five priorities maximum and make each item executable by an agent.

Use this format when a plan is requested:

```
## Refactoring Plan

### Priority 1: [Dimension] — [Specific Action]
- Current score: X/5 → Target: Y/5
- Effort: [afternoon / few days / multi-week]
- Impact: [highest leverage change and why]
- Steps:
  1. ...
  2. ...
  3. ...

### Priority 2: ...
```

## Guardrails

- Never fabricate metrics. If you cannot determine a score, say so and explain what data you would need.
- Do not run destructive commands or modify source files during the audit phase.
- If the test suite fails, report the failures — do not attempt to fix them during the audit.
- Score honestly. Most codebases score 2-3. A score of 5 is exceptional and rare.
- This audit is language-agnostic. Adapt type system evaluation to the language (e.g., Python type hints, Go interfaces, Rust traits).
- If the codebase uses multiple languages, score each dimension for the primary language and note secondary language gaps.
- Do not assume a Cursor-only workflow; account for Codex, Claude Code, terminal agents, hosted agents, and IDE agents where relevant.

## Completion Checklist

- [ ] All five dimensions scanned with concrete evidence
- [ ] Scorecard presented in the exact table format
- [ ] Grade assigned with letter and description
- [ ] Each dimension has specific findings with file paths
- [ ] Highest-impact fix identified per dimension
- [ ] User asked whether they want a refactoring plan
- [ ] If yes, plan generated with max 5 priorities, ordered by impact
- [ ] Plan items are specific enough to be executed by an AI agent
