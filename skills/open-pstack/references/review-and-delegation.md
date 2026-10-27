# Independent review and parallel work

## Delegate when useful

Use independent workers for separate investigations, disjoint implementation slices, competing experiments, or fresh review. Native tool availability and the user's instructions determine whether delegation is possible. Sequential work is a valid fallback and must not be described as independent review.

Each brief includes the goal, scope, permitted side effects, source paths or revisions, completion check, and expected artifact. Give writers disjoint files or isolated checkouts. Reviewers default to read-only work. Bound concurrency and cost to the task. Wait for relevant results, inspect artifacts, and verify the integrated outcome yourself.

Workers report evidence and unresolved gaps. A missing worker or missing coverage is not a pass. Do not repeatedly spawn replacements without learning why the prior attempt failed. A lone reviewer can find a real bug; majority agreement is not a substitute for proof.

## Cross-lab bug review

A cross-lab bug hunt is the `adversarial-review` skill. Read [adversarial-review](../../adversarial-review/SKILL.md) and follow that procedure. Do not reproduce it here.

## Competing designs or implementations

Before starting, define the common constraints and comparison criteria. Keep candidates isolated and run the same checks against each. Select on demonstrated behavior and maintenance cost, not presentation. If combining ideas, review and verify the combined patch as a new artifact. Keep provenance clear and preserve user-owned work when retiring experiments.
