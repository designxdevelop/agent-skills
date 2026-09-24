---
name: test-audit
description: >-
  Evaluate proposed or existing tests for meaningful regression protection, duplication,
  implementation coupling, and test-only production seams. Use when writing substantive
  tests or when asked to review, simplify, or prune a test suite.
---

# Test Audit

Improve confidence per test maintained. Apply the value check when adding or changing
tests; use the audit workflow for an existing suite. Keep the scope tied to the
user's task rather than expanding an ordinary edit into a repository-wide sweep.

## Value check for a proposed test

Before adding a test, identify:

- The observable behavior, invariant, or independent contract it protects.
- A credible regression that would make it fail for the intended reason.
- Why existing tests do not already cover that regression at a stronger boundary.
- Whether it requires an export, flag, injection hook, wrapper, or other production
  seam that no production caller needs.

If those answers are unclear, revise the test or omit it. Prefer extending a
parameterized case or an existing owner suite over repeating the same scenario at
another layer. For a bug regression, demonstrate a pre-fix failure for the
intended reason when practical, then verify it passes after the fix.

## Audit candidates

Look for tests that cannot detect a meaningful failure, including:

- Assertion-free runs, self-comparisons, or expectations calculated by the same
  helper being tested.
- Exact source, import, string, export-list, or fixture inventories that merely
  mirror implementation and break under behavior-preserving refactors.
- Private call-shape or predicate checks already protected by a public boundary.
- Repeated scenarios across unit, integration, and end-to-end layers without a
  distinct risk at each layer.
- Mocks that supply the very behavior being asserted, or negative cases that
  pass because an unrelated guard rejects the request first.
- Tests kept only to justify production code with no non-test caller.
- Test names that promise a contract the assertions do not actually exercise.

These are leads, not automatic deletion rules. Keep a test when it independently
guards a public API, protocol, configuration, migration, storage, security,
platform, release, or other meaningful contract. Source inspection can be the
right guard when a specific byte, key, or path is itself the contract. Slow or
static tests are not inherently low value.

## Audit workflow

1. Read applicable repository instructions. Identify the requested scope, the
   production owner, its callers, existing test layers, and CI routing. Check
   relevant history before calling a test obsolete.
2. Discover candidates without editing. For each candidate, record its path and
   test name, the failure it can detect, overlap with stronger proof, and any
   production or test-support code it alone keeps alive.
3. Classify each candidate as retain, repair, consolidate, or remove. Name the
   surviving owner for every contract moved or deleted. If proof is uncertain,
   retain the test and report the uncertainty.
4. Make one coherent change at an ownership boundary. Remove a test-only seam
   only after confirming it has no production caller and its contract remains
   covered. Preserve unrelated tests and behavior.
5. Run the smallest relevant test command and any required project checks.
   Confirm moved assertions can fail for the intended regression when feasible.
   Inspect the diff for lost coverage, accidental production changes, and
   whitespace errors.

For a whole-subsystem audit, baseline the current tests first, group them by
behavioral owner, and work through those groups in reviewable batches. Recheck
coverage after each batch instead of optimizing for deletion count. Treat a
failing retained test as a possible product defect, not a reason to discard it.

## Handoff

Report what was retained, repaired, consolidated, or removed; the contract that
remains protected; any production seam simplified; the checks actually run; and
unresolved coverage risks. Distinguish pre-existing failures from changes caused
by the audit.

## Source

Adapted from [OpenClaw's Test Audit skill](https://github.com/openclaw/openclaw/blob/main/.agents/skills/test-audit/SKILL.md),
copyright © 2026 OpenClaw Foundation, under the MIT License. See [LICENSE](LICENSE).
