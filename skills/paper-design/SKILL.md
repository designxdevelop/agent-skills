---
name: paper-design
description: >-
  Create, edit, or review native editable designs in Paper using an available
  direct Paper integration. Use when a user names Paper, shares a Paper file,
  requests Paper artboards, or wants implementation and Paper designs aligned.
---

# Paper Design

## Goal

Create coherent, editable Paper designs while preserving the confirmed file
scope and the product's existing design system.

## When to Use

Use when the task concerns a Paper file, Paper artboards, Paper components, a
Paper design system, or synchronization between Paper and an application.

## Workflow

1. Discover the available Paper connection and its current guidance. Use direct
   Paper operations when they are available. If they are not, report the
   limitation and use another method only when the user chooses it.
2. Open the requested file, page, and nodes. Inspect existing pages, artboards,
   components, and tokens before making changes; preserve everything outside
   the confirmed scope.
3. When mirroring an application, inspect the relevant product states and
   design tokens. Map requested states to artboards and report any meaningful
   omission.
4. Create or update native editable layers. Reuse existing tokens and shared
   structures where they fit, and name artboards and layers for their product
   state.
5. Review changed screens at an appropriate level of rigor. Use screenshots or
   the native preview when available to check hierarchy, contrast, spacing,
   clipping, typography, and consistency across related states.
6. Report the changed file locations, artboards, design-system decisions, and
   anything that could not be verified.

## Guardrails

- Never substitute a different design surface for direct Paper work unless the
  user chooses it.
- Never delete, replace, or restyle Paper content outside the confirmed scope.
- Never overwrite an existing design system without making the change clear in
  the handoff.
- Never claim cross-screen consistency without reviewing the changed screens.
- Never expose credentials or private product data outside the local working
  environment.

## Completion Checklist

- [ ] The active Paper integration and requested scope were established.
- [ ] Changes use native editable Paper objects.
- [ ] Requested states are represented or any omissions are reported.
- [ ] Changed screens were reviewed for visual consistency.
- [ ] The handoff identifies changed artboards and unverified details.
