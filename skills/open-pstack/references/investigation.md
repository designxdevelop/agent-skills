# Investigation and debugging

## Explain how or why

Trace the relevant entry point through data ownership, state changes, persistence, cancellation, and errors. Read callers as well as definitions. Use source locations and a small concrete example to explain the mechanism. Search history, design documents, or available read-only connectors for rationale only when needed. Missing history means intent is uncertain, not that the implementation was accidental.

For a read-only question, return the explanation and evidence. Do not turn it into a code change, PR repair, or publication.

## Fix a bug

1. Reproduce on the affected interface with the reported conditions. If access is missing, narrow the trigger using available artifacts and state the remaining gap; do not label a synthetic proxy as the original reproduction.
2. Trace the mechanism and choose experiments that separate plausible causes. Add focused temporary instrumentation when state is unclear. Discard hypotheses refuted by evidence.
3. Fix the cause with the smallest coherent change. Consider impacted callers and invariants. If repeated fixes fail, question the shared premise before adding another guard.
4. Rerun the original reproduction and relevant regressions. When a cheap durable test exists, show that it fails before the fix and passes after. Remove temporary instrumentation unless it has an ongoing purpose.

Report symptom, cause, fix, and observed verification. A blocked or inconclusive run stays a gap.

## Runtime and trace forensics

For diagnosis requests, collect a baseline before changing code. Record workload, process/build identity, collection method, and time window. Inspect the relevant signal: allocation and retained objects for leaks, stacks and scheduling for CPU, frames and layout for visual glitches. Distinguish a hot stack from the mechanism that makes it hot.

For supplied traces, establish format, units, sampling limits, and missing context before drawing conclusions. Rank hypotheses by evidence and identify the smallest discriminating experiment. Deliver diagnosis and confidence; implementing a fix is separate unless requested.
