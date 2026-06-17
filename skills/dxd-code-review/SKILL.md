---
name: dxd-code-review
description: >-
  Use when the user asks for DXD code review, dxd-code-review, a thermo-nuclear review, thermonuclear review, harsh maintainability review, deep code quality audit, abstraction review, giant-file review, spaghetti-code review, or structural critique of current branch changes.
disable-model-invocation: true
---

# DXD Code Review

Use this skill for an unusually strict DXD-style review focused on implementation quality, maintainability, abstraction quality, and codebase health.

Above all, be ambitious about structure. Search for behavior-preserving changes that make the implementation smaller, simpler, and more inevitable instead of merely cleaner.

## Goal

Perform a deep code-quality audit of the current branch's changes, with an unusually high bar for maintainability. Push for structural simplification, stronger abstraction boundaries, smaller files, less branching complexity, and more direct implementation without changing behavior.

## When to Use

Use this skill when the user asks for:

- DXD code review or `dxd-code-review`.
- A thermo-nuclear code quality review.
- A thermonuclear review.
- A deep code quality audit.
- An especially harsh maintainability review.
- A review focused on abstraction quality, giant files, or spaghetti-condition growth.

## Review Lens

Review the current branch through these blockers before spending time on style:

| Blocker | What It Looks Like | Cleaner Direction |
|---------|--------------------|-------------------|
| Missed simplification | The diff preserves concepts, branches, helpers, or modes that could disappear. | Reframe the model so the simpler flow becomes obvious. |
| Spaghetti growth | New one-off conditionals, booleans, nullable modes, or special cases land in busy paths. | Move behavior behind a focused abstraction, state model, policy, or pure helper. |
| File sprawl | A changed file crosses or approaches 1000 lines without a strong structural reason. | Split by ownership, feature boundary, or pure logic boundary before it hardens. |
| Wrong layer | Feature logic leaks into shared paths or the package that owns the concept is bypassed. | Move logic to the canonical owner and reuse existing helpers. |
| Weak contracts | Casts, `any`, `unknown`, unnecessary optionality, or silent fallbacks hide invariants. | Make the boundary explicit with typed models, schemas, or narrower APIs. |
| Hollow abstraction | Wrappers, generic magic, or pass-through helpers add indirection without reducing complexity. | Delete the abstraction or replace it with a direct, boring flow. |
| Brittle orchestration | Independent work is serialized or related updates can be left half-applied. | Parallelize or make updates atomic when it also makes the code easier to reason about. |

Do not be satisfied with feedback like "rename this" when the real issue is structural.

## Preferred Fixes

When you flag a problem, point toward behavior-preserving changes such as:

- Delete a layer of indirection instead of polishing it.
- Collapse duplicate branches into one clearer flow.
- Reframe the state model so conditionals disappear.
- Extract a focused helper, module, component, or pure function.
- Move feature logic to the package, service, or module that owns the concept.
- Replace condition chains with a typed model, dispatcher, or explicit policy.
- Reuse the existing canonical helper instead of adding a near-duplicate.
- Make contracts explicit so callers do not need casts, optionality, or silent fallbacks.

## Review Tone

Be direct, serious, and demanding about quality.
Do not be rude, but do not soften major maintainability issues into mild suggestions.
If the code is making the codebase messier, say so clearly.
If the implementation missed an opportunity for a dramatic simplification, say that clearly too.

Useful phrases:

- `this pushes the file past 1k lines. can we decompose this first?`
- `this adds another special-case branch into an already busy flow. can we move this behind its own abstraction?`
- `this works, but it makes the surrounding code more spaghetti. let's keep the behavior and restructure the implementation.`
- `this feels like feature logic leaking into a shared path. can we isolate it?`
- `this abstraction seems unnecessary. can we just keep the direct flow?`
- `why does this need a cast / optional here? can we make the boundary more explicit instead?`
- `this looks like a bespoke helper for something we already have elsewhere. can we reuse the canonical one?`
- `i think there's a simpler framing here that makes these branches disappear.`
- `this refactor moves complexity around, but doesn't really delete it. is there a way to make the model itself simpler?`

## Workflow

1. Inspect the current branch diff and identify every meaningful changed area before reviewing individual files.
2. Check whether any changed file crosses or approaches 1000 lines.
3. For each changed area, search for an existing canonical helper, layer, module, or pattern that should own the behavior.
4. Review the structure before the syntax: ask whether the implementation can delete branches, reduce concepts, or move logic to a clearer boundary.
5. Flag structural regressions and missed simplifications before legibility or naming concerns.
6. For every finding, include the file and line, why the design is worse, and the cleaner direction.
7. State whether the approval bar is met.

## Output Expectations

Lead with findings, ordered by severity. Prioritize structural regressions, missed simplifications, spaghetti growth, boundary problems, file-size concerns, then legibility. Prefer a smaller number of high-conviction comments over a long list of cosmetic notes.

## Approval Bar

Do not approve merely because behavior seems correct. The bar for approval is:

- no clear structural regression
- no obvious missed opportunity to make the implementation dramatically simpler
- no unjustified file-size explosion
- no obvious spaghetti-growth from special-case branching
- no obviously hacky or magical abstraction that makes the code harder to reason about
- no unnecessary wrapper/cast/optionality churn obscuring the real design
- no clear architecture-boundary leak or avoidable canonical-helper duplication
- no missed opportunity for an obvious decomposition that would materially improve maintainability

Treat violations as presumptive blockers unless the author can justify them clearly. If the bar is not met, leave explicit, actionable feedback and push for a cleaner decomposition.

## Guardrails

- Never turn the review into a cosmetic naming pass while larger structural issues are present.
- Never approve a diff that clearly makes the codebase harder to maintain just because behavior appears correct.
- Never recommend broad rewrites without explaining the smaller behavior-preserving restructuring path.
- Never ignore existing project conventions or canonical helpers when proposing decomposition.
- Never conflate performance micro-optimization with maintainability unless the orchestration also becomes simpler.

## Completion Checklist

- [ ] Current branch changes were inspected before reviewing individual files.
- [ ] File-size growth and the 1000-line threshold were checked.
- [ ] Existing abstractions, canonical helpers, and ownership layers were considered.
- [ ] Findings prioritize structural maintainability over cosmetic style.
- [ ] Each finding includes a concrete cleaner direction, not just criticism.
- [ ] The review explicitly states whether the approval bar is met.
