# PRs, CI, and shipping

## Status and repair

Map the request to scope before acting. A status question gets a read-only snapshot of the PR's current head, checks, conflicts, and review state. A request to repair CI or address feedback authorizes the relevant work. Monitoring or merging requires the corresponding user intent; neither follows automatically from asking for status. When a credible behavior report lacks a reproduced pass or decisive disproof, report behavior readiness as unverified even if CI and mergeability are green.

For repair, inspect the actual failing logs and current patch. Triage feedback as fix, dismiss with evidence, or unresolved. Do not modify code just to satisfy a mistaken bot comment. Rerun relevant checks after fixes and distinguish environment failures from regressions.

## Open a PR

When requested or included in the authorized workflow, inspect the complete diff against the correct base, check for unrelated changes and secrets, and complete required verification. Follow the repository's commit and PR conventions. Describe the problem, resulting behavior, and validation. Keep local-only work local when publishing is outside scope.

## Ship a PR or stack

Resolve current base/head revisions, required checks, mergeability, and review evidence. For consequential changes, seek an independent verifier when available. If unavailable, disclose self-verification and honor any user or repository requirement for independent approval.

For a stack, build an explicit bottom-to-top dependency list. Land only the contiguous verified portion, stopping before the first unverified or blocked dependency. Prepare and merge one PR at a time through the authorized forge; do not arm descendants early.

Tie verification to the code and base actually reviewed. After changes, rebases, or retargeting, inspect the resulting diff and rerun affected validation. A matching patch can still behave differently on a changed base. Checks from an earlier head are not current checks.

After each merge, confirm the forge reports it merged, fetch the new base, and reassess the next PR. Auto-merge armed or queued is not merged. Respect branch protection and the repository's merge method. Report what landed, what remains, and the concrete blocker. Use supported scheduling only if ongoing monitoring was requested.
