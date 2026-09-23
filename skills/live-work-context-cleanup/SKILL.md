---
name: live-work-context-cleanup
description: >-
  Recover and continue ambiguous work that spans live pages, browser or SaaS
  state, local files, releases, or automations. Use when the user asks to find
  the real current state, clean up low-risk noise, or verify a change is live.
---

# Live Work Context Cleanup

## Goal

Find the current source of truth for cross-tool work and complete the smallest
safe continuation, cleanup, or verification the user requested.

## When to Use

Use for recent-work recovery, active-page inspection, low-risk state cleanup,
ambiguous handoffs across tools, or verification of a published, deployed, or
otherwise live change.

## Workflow

1. Inspect the freshest relevant source available: the live page, active tab,
   app, connector, repository, or runtime configuration. Treat memories and
   screenshots as leads until confirmed where the state can drift.
2. Identify the concrete system that owns the behavior or data the user cares
   about. Preserve unrelated local changes and external state.
3. Act only on the requested surface. If local and live state differ, determine
   which one is relevant before editing.
4. Keep cleanup reversible and narrow unless the user specifically authorizes a
   destructive action.
5. Verify the outcome in the system that matters to the user, such as the
   published page, deployed app, actual automation configuration, or intended
   repository state.
6. Hand off the source of truth, result, verification, and any blocker that
   requires user action.

## Guardrails

- Never treat stale screenshots, OCR, memories, or descriptive prompts as proof
  of live state when a current source is available.
- Never delete or irreversibly change emails, tickets, files, automations,
  branches, or production data without explicit authorization.
- Never claim a runtime problem is fixed after changing only descriptive text;
  verify the relevant configuration or behavior.
- Never proceed through login, account, permission, captcha, or destructive
  confirmation barriers by improvising.
- Never continue on a surface the user has corrected or ruled out.

## Completion Checklist

- [ ] The relevant current source of truth was identified.
- [ ] Changes stayed within the requested surface and risk level.
- [ ] The outcome was verified in the system the user cares about.
- [ ] The handoff records any material blocker or unresolved state.
