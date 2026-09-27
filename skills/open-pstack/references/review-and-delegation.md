# Independent review and parallel work

## Delegate when useful

Use independent workers for separate investigations, disjoint implementation slices, competing experiments, or fresh review. Native tool availability and the user's instructions determine whether delegation is possible. Sequential work is a valid fallback and must not be described as independent review.

Each brief includes the goal, scope, permitted side effects, source paths or revisions, completion check, and expected artifact. Give writers disjoint files or isolated checkouts. Reviewers default to read-only work. Bound concurrency and cost to the task. Wait for relevant results, inspect artifacts, and verify the integrated outcome yourself.

Workers report evidence and unresolved gaps. A missing worker or missing coverage is not a pass. Do not repeatedly spawn replacements without learning why the prior attempt failed.

## Adversarial review

Freeze the intended behavior and exact diff/base being reviewed. Give independent reviewers the same intent and necessary source context, without leading them toward a preferred conclusion. Different models add diversity when available; multiple roles played by one model do not create that diversity.

Ask for concrete defects or consequential design problems with a trigger, location, impact, and supporting evidence. Include state transitions, concurrency, boundary handling, failure recovery, compatibility, and verification gaps where relevant.

Reproduce or trace findings yourself. Deduplicate them, resolve disagreements using evidence, and distinguish actionable issues, unresolved questions, and dismissed claims. A lone reviewer can find a real bug; majority agreement is not a substitute for proof. A review-only request returns a verdict without applying fixes or posting comments externally.

## Competing designs or implementations

Before starting, define the common constraints and comparison criteria. Keep candidates isolated and run the same checks against each. Select on demonstrated behavior and maintenance cost, not presentation. If combining ideas, review and verify the combined patch as a new artifact. Keep provenance clear and preserve user-owned work when retiring experiments.
