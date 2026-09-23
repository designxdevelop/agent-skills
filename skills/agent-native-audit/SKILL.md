---
name: agent-native-audit
description: >-
  Audit a codebase for how easily coding agents can understand, change, and
  verify it. Use for agent-readiness reviews, AI-friendly codebase assessments,
  or plans to improve agent reliability in a repository.
---

# Agent-Native Codebase Audit

## Goal

Produce an evidence-backed assessment of the conditions that let agents make
safe, well-targeted changes, then recommend the highest-leverage improvements.

## When to Use

Use when the user asks to assess agent readiness, score an AI-friendly
codebase, or plan changes that make a repository easier for coding agents to
work in.

## Evaluation Criteria

Assess the dimensions that matter for the repository at hand:

| Dimension | Look for |
| --- | --- |
| Contracts | Types, schemas, explicit boundaries, and helpful failures that make invalid changes hard to write. |
| Navigation | Predictable structure, naming, ownership, and discoverable canonical paths. |
| Verification | Fast, meaningful checks that cover relevant behavior and work locally and in CI. |
| Feedback | Clear commands, actionable errors, and short iteration loops. |
| Context | Documentation, examples, conventions, and comments that explain intent where code cannot. |

Use scores only when they help the user compare baselines or measure progress.
If scoring, state the scale, weighting, uncertainty, and evidence behind each
rating. Letter grades and fixed score bands are optional presentation choices,
not a claim of universal precision.

## Workflow

1. Inspect repository instructions, package and build configuration, CI,
   verification commands, documentation, and representative source and test
   paths. Establish the primary languages and the work an agent would perform.
2. Gather evidence for each relevant criterion. Prefer concrete paths, command
   output, and examples over inferred maturity.
3. Run safe local checks when they can confirm a meaningful claim. Distinguish
   pre-existing failures from the conditions being assessed.
4. Report strengths, friction, and the evidence for each assessment. Identify
   the smallest changes likely to improve multiple criteria.
5. Provide an ordered, executable improvement plan when requested; otherwise
   offer it as the next step.

## Guardrails

- Never fabricate metrics, coverage, test results, or scores.
- Never modify source or repair failures during an audit unless the user expands
  the task.
- Never judge a repository from a single file or tool configuration.
- Adapt the assessment to the repository's languages, architecture, and agent
  environments rather than assuming one IDE or vendor.

## Completion Checklist

- [ ] Findings cite concrete evidence from the repository or checks.
- [ ] Relevant agent-work criteria were assessed with uncertainty stated.
- [ ] Recommendations are prioritized by expected leverage and are actionable.
- [ ] Any score or grade is explained as a chosen reporting convention.
