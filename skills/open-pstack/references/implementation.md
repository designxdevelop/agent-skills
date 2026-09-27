# Design and implementation

## Features and architecture

Trace the surrounding system first. Write the intended caller interaction, then identify the domain data, invariants, ownership, interfaces, and failure behavior needed to support it. For consequential uncertainty, compare structurally different designs or run a focused experiment. A routine local change does not need a design tournament.

Select the design by behavior, maintainability, interface depth, migration cost, and evidence. Record the tradeoff that mattered. Build in verifiable units, resolving dependencies before parallel work. If shared writes prevent useful delegation, keep one implementation owner.

Review differences from the design as new evidence. Repeated casts, caller knowledge of internals, or special-case branches may mean the model is wrong. Revise the design rather than protecting the original sketch.

## Refactoring

Identify behavior that must remain stable and how it is exercised. Move callers with the changed internal contract, remove obsolete paths, and verify behavior after each meaningful unit. Public API or stored-data changes need an explicit compatibility decision; do not infer permission to break them from a cleanup request.

## Prototypes and visual parity

For an empirical question, build the smallest disposable experiment that separates the choices. State the question and what was learned. A prototype does not establish production readiness.

For visual parity, capture the reference and candidate in matched viewport, data, interaction, font, and rendering conditions. Compare relevant states, including scrolling, focus, empty/error states, and motion where affected. Use screenshots or measurements, and investigate meaningful differences. If the visual surface is unavailable, report parity as unverified.

## Finish

Inspect the complete diff for accidental scope, redundant abstractions, stale callers, and comments that explain mechanics already visible in code. Preserve comments that record non-obvious constraints. Run checks appropriate to the changed behavior and repository requirements. Use the delivery reference only when PR or shipping work is part of the request.
