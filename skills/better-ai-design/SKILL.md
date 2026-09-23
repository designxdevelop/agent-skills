---
name: better-ai-design
description: >-
  Design distinctive, usable web and app interfaces when a brief calls for a
  strong visual direction, deliberate exploration, or visual critique beyond a
  routine implementation.
---

# Better AI Design

## Goal

Help consequential interface work arrive at a clear visual point of view while
remaining useful, coherent, and faithful to the product brief.

## When to Use

Use this when the user requests an ambitious or distinctive interface, asks to
explore directions before building, or wants a visual critique of a meaningful
screen or flow. For routine component work, use the project's existing design
system and ordinary implementation judgment.

## Workflow

1. Establish the product purpose, audience, constraints, and feeling the
   interface should create. Preserve explicit user references and existing
   brand or design-system decisions.
2. For work where the direction is genuinely open, compare a few materially
   different concepts before committing. Use references, sketches, or small
   experiments when they help make the choice concrete.
3. Express the chosen direction through hierarchy, composition, typography,
   color, imagery, and interaction, not merely a new palette on a familiar
   layout.
4. Remove decoration, containers, copy, and custom controls that do not improve
   comprehension, task flow, or the chosen aesthetic.
5. Inspect the rendered result. For visually important work, capture a
   screenshot and seek an independent critique or compare it against suitable
   references. Revise the highest-impact gaps, then stop when the result meets
   the brief or further changes no longer improve it.

Generated imagery, animation, and separate critique contexts are tools for a
specific design problem, not a default process. Use them only when they add
meaningful character or confidence. Keep generated-media credentials out of
shipped code. When using a fresh visual critic, provide screenshots and the brief
without implementation details or a target score; start with one or two passes.

## Guardrails

- Never replace a clear user brief with an unrelated aesthetic experiment.
- Never mistake novelty for usability, accessibility, or product fit.
- Never run open-ended critique cycles; set a useful stopping condition.
- Use inspiration to assess mood and craft; when the user requests faithful
  implementation of a supplied design, preserve that reference and requested fidelity.
- Never expose generation credentials or private assets.

## Completion Checklist

- [ ] The chosen direction serves the product and the user's brief.
- [ ] Layout, type, color, and interaction reinforce the same direction.
- [ ] Unnecessary visual and textual elements were removed.
- [ ] The final rendered result was reviewed at an appropriate level of rigor.

## Source

Adapted from Anshu Chimala’s [“How to turn your AI into a world-class designer”](https://www.lennysnewsletter.com/p/how-to-turn-your-ai-into-a-world).
