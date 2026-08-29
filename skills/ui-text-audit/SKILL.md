---
name: ui-text-audit
description: >-
  Audit every user-facing screen for redundant, verbose, or unnecessary UI text
  and remove what doesn't help the user decide or act. Triggers on "audit UI
  text", "trim copy", "remove redundant labels", "verbose UI", "too many words",
  "clean up screen text", "UI text review", "cut unnecessary copy", or any
  request to tighten interface language across a project.
---

# UI Text Audit

## Goal

Find and remove every piece of user-facing text that does not help the user make a decision or complete a task. Leave text that carries genuinely new information. The result is fewer words per screen, faster scanning, and no loss of usability.

## When to Use

Use this skill when the user:

- Asks to audit, review, or tighten UI text across a project.
- Says screens feel verbose, wordy, or cluttered with copy.
- Wants redundant labels, filler descriptions, or unnecessary subheadings removed.
- Asks to "trim the copy", "clean up the UI text", or "cut the noise".

Example prompts:

> Audit every screen for unnecessary text and remove it.

> The UI is too wordy. Cut anything that doesn't help the user.

> Review all the labels and descriptions — trim what's redundant.

## Workflow

### 1. Inventory screens

Identify every user-facing screen, page, modal, drawer, and multi-step flow in the project. List them so nothing is missed.

### 2. Scan each screen against the pattern catalog

For every screen, check for each pattern below. Collect candidates — do not edit yet.

#### Pattern catalog

| #  | Pattern | Test | Action |
|----|---------|------|--------|
| 1  | **Eyebrow restates heading** — labels like "STEP 2 OF 4" or "SETTINGS · ACCOUNT" above a heading that already names the screen | Does the eyebrow add information the heading lacks (e.g. progress the heading omits)? | If no, remove the eyebrow. If yes, keep it. |
| 2  | **Heading + subheading say the same thing** — "Manage your team" / "Add, remove, and manage members of your team" | Does the subheading add a fact or action the heading doesn't? | If no, kill the subheading or merge the pair into one line. |
| 3  | **Explanatory text describes what's visible** — "Use the form below to update your profile" above a profile form | Can the user see what to do without this sentence? | If yes, remove it. |
| 4  | **Section heading for a single item** — "Your selection" above one item, "Results" above one result | Is there only ever one item in this section? | If yes, remove the heading. If the section can have multiple items, keep it. |
| 5  | **Confidence badge / internal-system label** — "HIGH CONFIDENCE", "STRONG MATCH" | Can the user take a different action based on this label? | If no, remove it. |
| 6  | **Disclaimer that duplicates a confirm step** — "Don't worry, nothing changes until you confirm" when a confirm step exists | Does the UI already have a confirmation gate? | If yes, remove the disclaimer. If no, add a confirm step instead. |
| 7  | **Redundant nested label** — a `<summary>` says "Add extra notes", the revealed `<label>` says "Extra notes" | Does the inner label add information beyond the summary? | If no, remove the inner label. |
| 8  | **Same data presented multiple ways** — "75%", "About 75% of items match", "Strong match" | Is the same fact stated more than once? | Keep one presentation (number + brief label). Remove the rest. |
| 9  | **Filler footer text** — "More details will be available after this step" | Does this text help the user decide what to do now? | If no, remove it. |
| 10 | **Verbose button label** — "Approve this improvement", "Mark as not relevant" | Is the context already clear from the surrounding UI? | If yes, trim to verb + object: "Approve", "Skip", "View draft". |

### 3. Validate candidates

For each candidate, ask: **does removing this text make it harder for the user to complete the task?**

- If **no** → confirmed for removal.
- If **yes** → discard the candidate. Leave the text.

Never remove:

- Progress indicators when the heading does not already convey progress.
- Error messages and validation hints.
- Accessibility labels (`aria-label`, `sr-only` text, `alt` text).
- Text that provides genuinely new information the user needs to act.

### 4. Apply changes

For each confirmed removal:

1. Remove the text from the component.
2. Remove any CSS rules, classes, or styled-component blocks that only styled the removed element.
3. Remove unused imports introduced by the deletion.
4. If a disclaimer was removed and no confirm step exists, add a confirm step.

### 5. Verify the build

Run the project's build/lint/type-check command after all changes. Fix any breakage before moving on.

### 6. Report

Produce a summary table:

| Screen | Pattern # | What was removed | Reason |
|--------|-----------|------------------|--------|

Group by screen. Include the pattern number so the user can cross-reference the catalog.

## Guardrails

- Never remove error messages, validation hints, or accessibility labels.
- Never remove text that provides information the user cannot infer from the surrounding UI.
- Never remove progress indicators unless the heading already conveys the same progress information.
- Never guess whether a section can have multiple items — check the data source or ask.
- Never restructure component hierarchy, reorder elements, or change behavior — only remove text and its dedicated styling.
- Never introduce new copy. This skill removes; it does not rewrite (exception: merging a heading + subheading into one line, or shortening a button label).
- Always verify the build passes after changes. Do not leave broken imports or dead CSS.
- Report every removal so the user can review and revert if needed.

## Completion Checklist

- [ ] Every user-facing screen, modal, drawer, and flow step was scanned.
- [ ] Each removal maps to a pattern in the catalog.
- [ ] No error messages, validation hints, or accessibility labels were removed.
- [ ] Removed CSS/imports that only served deleted elements.
- [ ] Build/lint/type-check passes with no new errors.
- [ ] Summary table delivered listing every change by screen and pattern.
