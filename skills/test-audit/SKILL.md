---
name: test-audit
description: >-
  Simplify test suites around focused end-to-end journeys and API/database contracts,
  pruning redundant unit and component tests. Use when writing substantive tests or
  reviewing, simplifying, or pruning an existing suite.
---

# Test Audit

Prefer a small suite of focused E2Es that proves the product works. Optimize for
confidence and maintenance burden across the whole suite, not the number of
individually defensible tests. Fast execution alone does not justify keeping a test.
Keep the scope tied to the user's task; an ordinary edit is not a repository-wide audit.

## Choose the strongest useful boundary

- **Focused E2Es are the default for user-visible behavior:** critical journeys,
  navigation, forms, approval flows, and downloads. Each test should have one clear
  outcome and exercise the real application through that outcome. Avoid giant
  all-purpose journeys and repeating the same setup-heavy flow for every variation.
- **API/database integration tests own server contracts:** authorization, persistence,
  accounting, idempotency, and failure recovery. Use real local storage where practical;
  mocking away the behavior under test does not establish that contract.
- **Unit tests are selective exceptions:** complex parsing, algorithms, evidence rules,
  serialization, or consequential edge cases that are difficult to exercise reliably
  at a stronger boundary. Require a concrete reason for testing them in isolation.
- **Simple component and helper tests are first candidates for removal:** rendering,
  labels, ordinary callbacks, navigation wiring, trivial transformations, and private
  call shapes rarely need separate tests when a focused journey already covers them.

Do not recreate every deleted unit case as an E2E. Choose representative journeys
and place consequential edge cases at the cheapest boundary that proves the real
contract. Multiple test layers must earn their maintenance cost with distinct,
material regression protection; merely exercising a different layer is insufficient.
External service stubs can make E2Es deterministic, but identify what they leave
unproven. Never mock the application behavior the test claims to verify.

## Value check before adding or retaining a test

Identify:

- The observable outcome and a credible regression the test detects.
- Why a focused E2E or API/database test does not already provide sufficient proof.
- For a unit/component test, why isolated coverage materially improves confidence.
- The setup, mocks, fixtures, and production seams the test requires us to maintain.

Prefer extending an existing owner test over creating another suite. Skip tests for
trivial, reversible changes unless they protect a demonstrated regression or a
consequential contract. Do not add exports, flags, injection hooks, or wrappers solely
to make private implementation details testable.

A test's existence, speed, or ability to fail is not enough reason to retain it.
When several tests defend the same outcome, choose a surviving owner and consolidate.
When a test protects no meaningful contract, remove it without inventing a replacement.
For a bug regression, demonstrate the intended pre-fix failure when practical.

## Audit candidates

Prioritize:

- Unit/component scenarios already covered by a focused journey or integration test.
- Trivial helper checks, exact copy/configuration inventories, and assertions that
  break under behavior-preserving refactors.
- Assertion-free runs, self-comparisons, or expected results computed by the same helper.
- Mocks that supply the asserted behavior; negative cases rejected by an unrelated guard.
- Test names that promise behavior the assertions never exercise.
- Test-only production exports and support machinery with no remaining useful owner.

An exact byte, path, provider field, or migration can be a real contract. Preserve
necessary security, accounting, data-integrity, and platform coverage at an appropriate
boundary. Those labels do not automatically justify duplicate tests at every layer.

## Audit workflow

1. Read repository instructions and CI routing. For broad audits, baseline the suite
   and map critical product journeys and server contracts before reviewing individual
   tests. Check callers and relevant history before calling a test obsolete.
2. Choose the intended owners of those outcomes. Identify redundant lower-level tests
   and setup costs; do not merely collect reasons each current test could be useful.
3. Classify candidates as retain, repair, consolidate, or remove. Record the path,
   test name, credible failure, and surviving owner. For removal without replacement,
   explain why the asserted detail does not warrant regression protection. If coverage
   of a consequential contract is uncertain, retain it temporarily and report the gap.
4. Change one ownership boundary at a time. Establish necessary replacement proof
   before removing existing protection. Remove test-only seams after checking callers.
   Preserve unrelated production behavior.
5. Run focused checks and required project verification. Confirm relocated assertions
   fail for the intended regression where feasible. Review the diff for lost meaningful
   protection and accidental production changes.

Work through broad audits in reviewable batches. Judge success by a simpler suite
with clear ownership, not a deletion quota or exhaustive coverage of every variation.
Treat a failing retained test as a possible product defect, not a deletion opportunity.

## Handoff

Report the maintenance reduced, tests retained/repaired/consolidated/removed, surviving
E2E or integration owners, and why remaining unit tests warrant isolation. Include any
production seam simplified, checks actually run, and unresolved risks. Distinguish
pre-existing failures from audit-introduced failures.

## Source

Adapted from [OpenClaw's Test Audit skill](https://github.com/openclaw/openclaw/blob/main/.agents/skills/test-audit/SKILL.md),
copyright © 2026 OpenClaw Foundation, under the MIT License. See [LICENSE](LICENSE).
