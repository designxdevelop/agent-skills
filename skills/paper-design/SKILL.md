---
name: paper-design
description: >-
  Create, edit, or review native editable designs in Paper through the direct
  Paper MCP. Use when the user mentions Paper, app.paper.design, a Paper file,
  Paper MCP, Paper artboards, or asks to recreate product screens in Paper.
  Also use when implementation work must keep a Paper design synchronized with
  the application.
---

# Paper Design

## Goal

Create coherent, native, editable Paper designs through Paper's direct MCP.
Preserve the application's design system, verify related screens together, and
leave the Paper file in a reviewable state.

## When to Use

Use this skill when the user:

- Provides an `app.paper.design` link or names a Paper file.
- Asks for Paper artboards, flows, components, or design-system work.
- Wants existing application screens recreated or redesigned in Paper.
- Asks to update a Paper design after application changes.
- Explicitly asks to use the Paper MCP or Paper desktop MCP.

Example prompts:

> Recreate the current web and mobile screens as editable Paper artboards.

> Use Paper MCP to redesign this workflow and keep the light-mode palette consistent.

> Update the Paper file so it matches the implementation.

## Workflow

### 1. Resolve the direct Paper connection

Search the available tools for `mcp__paper__*` before selecting a design
workflow.

If the tools are unavailable:

1. Check whether a `paper` MCP server is configured.
2. In Codex, the local Paper desktop endpoint is commonly
   `http://127.0.0.1:29979/mcp`.
3. Ask for authorization before changing shared agent configuration.
4. After authorization, add or repair the server, verify its saved
   configuration and endpoint, then explain that the agent harness may need a
   restart before the Paper tools appear.

Stop when the direct tools are unavailable. Continue through another UI-control
method only when the user explicitly chooses that method.

### 2. Open and inspect the target

1. Read Paper's MCP guide for the active tool version.
2. Open the exact file and page from the user's link.
3. Inspect the current selection, page tree, existing artboards, and reusable
   tokens.
4. Identify the nodes the user placed in scope. Preserve unrelated pages,
   artboards, and components.

The step is complete when the target file, page, and editable node scope are
known.

### 3. Map the product states

When the design mirrors an application:

1. Inspect the relevant routes, screens, components, and design tokens in the
   repository or running app.
2. Inventory every state requested by the user before creating artboards.
3. Record one canonical palette, type scale, spacing scale, radii system, and
   component treatment for the work.
4. Separate semantic colors from brand colors. Give each accent one consistent
   meaning across the flow.

The step is complete when every requested state maps to an artboard or an
explicitly reported omission.

### 4. Build native editable objects

- Create or reuse Paper tokens before repeating raw values.
- Organize platforms, flows, and states with named pages and artboards.
- Use Paper MCP write and update operations that produce editable Paper layers.
- Batch independent reads, screenshots, and node updates.
- Reuse shared structures instead of rebuilding the same chrome for each state.
- Keep artboard and layer names tied to the product state they represent.

### 5. Run visual checkpoints

After each related screen group:

1. Capture a Paper screenshot.
2. Check spacing, clipping, overflow, hierarchy, contrast, typography, and
   component consistency.
3. Compare related screens side by side.
4. For light-mode flows, verify that surfaces, borders, type, buttons,
   progress, and semantic colors use the canonical system.
5. Fix every visible issue before moving on.

Before handoff, inspect all changed artboards together. Confirm that related
screens share one system, then mark every changed node finished through Paper.

### 6. Hand off

Report:

- The Paper file link.
- Pages and artboards created or changed.
- The design system and semantic color rules used.
- Any state or visual property that could not be verified.

## Guardrails

- Never substitute Computer Use, browser clicks, screenshots, SVG generation,
  or another design connector for direct Paper MCP work unless the user chooses
  that method.
- Never delete, replace, or restyle Paper nodes outside the confirmed scope.
- Never overwrite an existing design system without showing the change in the
  handoff.
- Never claim cross-screen consistency before the final side-by-side review.
- Never expose credentials or copy private product data outside the local
  environment.
- Report a missing or disconnected Paper MCP instead of silently retrying an
  unrelated tool.

## Completion Checklist

- [ ] Direct Paper MCP tools were resolved before design work began.
- [ ] The exact file, page, and node scope were confirmed.
- [ ] Every requested product state was inventoried.
- [ ] Native editable Paper layers were created or updated.
- [ ] Related screens use one documented palette and component system.
- [ ] Each screen group passed a screenshot checkpoint.
- [ ] All changed artboards passed a final side-by-side review.
- [ ] Paper's finish operation was called for every changed node.
- [ ] The handoff identifies changed artboards and any unverified state.
