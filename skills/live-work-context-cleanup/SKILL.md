---
name: live-work-context-cleanup
description: >-
  Recover the correct live work context and perform conservative cleanup across browser-first tools, SaaS apps, and local repos. Use when the user says "look at what I was doing", "check the active tab", "clean up the noise", "figure out the current task", "use Chronicle", "verify the live page", "fix the automation", or asks an agent to continue work that may span Chrome, Webflow, Gmail, Slack, Google Docs, Jira, PostHog, Expo/EAS, or a local codebase.
---

# Live Work Context Cleanup

## Goal

Find the real source of truth for an ambiguous or cross-tool task, classify the
work lane, and complete the smallest safe cleanup or continuation. This skill is
for agent work where the visible browser/app state, saved context, and local
repo may disagree.

## When to Use

Use this skill when the user asks you to:

- Recover what they were just working on from Chronicle, browser tabs, or saved context.
- Inspect the active Chrome/Webflow/live page before making a change.
- Clean up noisy inbox, task, QA, or automation state without deleting important data.
- Continue a task that spans SaaS tools and local files.
- Verify whether a change is live, published, deployed, submitted, or actually fixed.

Example prompts:

> Look at Chronicle and see what I keep asking agents to do.

> Look at my active Chrome tab and fix the issue.

> Clean up the noise.

> The web app work was fine but not the intended target.

> You did not actually fix it.

## Workflow

1. **Check available context in freshness order.**
   - If live screen or browser context is available, confirm it is fresh before relying on it.
   - Prefer the currently open live tab, published page, app UI, or connector data over stale local snapshots.
   - Use saved memories only as routing context unless you verify drift-prone details in the live system.

2. **Identify the work lane before acting.**
   - `source`: Slack, Google Docs, Google Drive, Google Sites, calendar, Jira, or screenshots.
   - `implementation`: local repo files, Webflow Designer, PostHog setup, automation config, or app code.
   - `verification`: published site, live DOM, deployed app, TestFlight/App Store Connect, CI, or analytics.
   - `cleanup`: inbox triage, noisy task lists, stale automation prompts, duplicate artifacts, or low-risk state.

3. **Name the source of truth explicitly.**
   - For Webflow or marketing-site tasks, inspect the live/published page or Designer state before local files.
   - For browser UI tasks, inspect the active tab and DOM when possible.
   - For mobile/release work, inspect the actual package/app workspace and release tooling output.
   - For automations, inspect the real runtime configuration, cwd, permissions, and schedule, not only prompt text.

4. **Constrain cleanup to reversible or clearly low-risk actions.**
   - Gmail/inbox cleanup: mark obvious noise read or remove low-signal labels only when the user asked for cleanup.
   - Project-board cleanup: do not close, delete, or move tickets unless status is unambiguous or the user asked.
   - Automation cleanup: preserve working cwd, command names, schedule constraints, and permission assumptions.
   - Repo cleanup: avoid broad refactors; fix the target behavior and leave unrelated dirty changes alone.

5. **Act on the correct surface.**
   - If the user redirects from web to mobile, stop working the web surface and move to the mobile implementation.
   - If live markup differs from local files, treat live markup as the inspection baseline and then decide where code changes belong.
   - If prompt-only changes cannot affect runtime behavior, update the actual runtime/config boundary.
   - If a command fails due to environment limits, classify the failure before retrying.

6. **Verify in the same system the user cares about.**
   - For Webflow/site work, verify Designer placement and published/live page behavior.
   - For browser UI work, verify at the relevant desktop/mobile breakpoints or state variants.
   - For release work, report exact command, cwd, artifact path, build number, and final blocker or success.
   - For cleanup, report what changed and what you intentionally left alone.

7. **Return a concise handoff.**
   - State the recovered context, source of truth, actions taken, and verification result.
   - Include remaining blockers only when they require user input or external state.
   - Preserve exact handles that future agents should search first: page names, class names, script names, automation ids, ticket names, or command names.

## Guardrails

- Never rely on screenshots or OCR for complex data extraction when a connector, live DOM, local file, or API source is available.
- Never treat saved memory as confirmed-current for schedules, prices, build numbers, tickets, or published state without live verification.
- Never delete emails, tickets, files, automations, branches, or production data during cleanup unless the user explicitly asked for that exact destructive action.
- Never claim an automation or release is fixed after only changing descriptive prompt text; verify the actual runtime/config condition.
- Never override unrelated dirty work in a repo. Read it, work around it, or ask if it blocks the task.
- Never keep working a surface after the user corrects the target surface or platform.

## Completion Checklist

- [ ] Freshness of live context or saved context was checked and stated.
- [ ] The task lane was identified before edits or cleanup actions.
- [ ] The source of truth was named explicitly.
- [ ] Actions were limited to the requested surface and risk level.
- [ ] Verification happened in the same system the user cares about.
- [ ] The final response included exact handles future agents can reuse.
- [ ] Destructive actions were avoided unless explicitly requested.
