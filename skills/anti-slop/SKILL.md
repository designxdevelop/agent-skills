---
name: anti-slop
description: >-
  Edit prose for specific AI-writing tells while preserving the author's voice.
  Use when a user asks to make a draft sound less AI-generated, remove slop, or
  perform an editorial pass focused on formulaic phrasing.
---

# Anti-Slop

## Goal

Remove formulaic filler, vague puffery, and repeated rhetorical patterns without
changing the author's meaning, register, or intentional style.

## When to Use

Use this for a requested anti-slop or voice-preserving editorial pass. Do not
load it for ordinary drafting or a general proofreading request unless the user
identifies AI-sounding prose as the problem.

## Workflow

1. Read the whole piece and identify its voice, audience, and argument.
2. Mark candidates that add little meaning or repeat a recognizable formula.
   Common candidates include meta introductions, unearned importance claims,
   vague conclusions, inflated predictions, and decorative metaphors.
3. Keep candidates that serve a deliberate rhetorical purpose. When uncertain,
   preserve the original.
4. Make the smallest phrasing edits that improve clarity or specificity. Keep
   facts, structure, and the author's position unchanged unless asked.
5. Re-read edited passages for rhythm and report material edits when reviewing.

For a contested edit or a broader catalog of tells, read
[references/tells.md](references/tells.md).

## Guardrails

- Never change facts, names, citations, technical claims, or argument during a
  phrasing pass.
- Never treat particular words, punctuation, fragments, parallelism, or
  rhetorical devices as automatically wrong. Judge their effect in context.
- Preserve intentional cadence, humor, conviction, and register.
- Stop when further edits would be taste rather than a clear improvement.

## Completion Checklist

- [ ] The author's voice and intent were understood before edits.
- [ ] Each edit removes a concrete tell or improves specificity.
- [ ] Meaning and factual content remain intact.
- [ ] The revised passages still sound intentional when read aloud.

## Attribution

Adapted from [`elithrar/dotfiles` anti-slop](https://github.com/elithrar/dotfiles/blob/main/.agents/skills/anti-slop/SKILL.md), created by Matt Silverlock and licensed under the MIT License.
