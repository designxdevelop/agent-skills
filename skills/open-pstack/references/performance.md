# Performance and hillclimbing

Select a realistic workload that exhibits the problem. Fix a metric, its units, direction of improvement, and correctness constraints. For repeated optimization, establish a target and a bounded budget or stopping condition using the user's constraints. Do not manufacture a minimum iteration count.

Build or reuse a repeatable measurement command. Show it can distinguish relevant workloads, sample enough to understand noise, and record the baseline with the regression gate passing. Keep environment and harness stable while comparing candidates.

Each attempt tests one mechanism-backed hypothesis. Measure before and after, then run the correctness gate. Keep improvements that exceed noise and preserve behavior; revert only that experiment's changes when it fails. Do not stack unmeasured changes or erase unrelated work.

For sustained work, keep a compact log of hypothesis, revision, workload, before/after, sample method, regression result, and kept/reverted decision. Parallel candidates need isolated resources so they do not distort measurements.

Stop at the agreed target or budget, a real blocker, or when remaining experiments do not justify their cost. Report baseline and final measurements, uncertainty, accepted changes, and whether the target was reached. Code inspection alone establishes no performance gain.
