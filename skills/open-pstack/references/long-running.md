# Long work, handoffs, and evaluation

## Multi-phase and autonomous work

Define a checkable outcome, dependencies, verification gates, and any time, cost, or iteration budget. Separate blocking setup from independent work. Keep a compact decision trail for consequential choices, experiments, and rejected hypotheses. Record enough evidence to resume without reconstructing the whole conversation.

Continue authorized work until the outcome is met or progress genuinely requires missing input or access. Broad autonomy does not waive permission boundaries. Never treat a request to work overnight as evidence that the host can persist after a turn. Use native scheduling only when available and authorized; otherwise report the runtime limit and save current state.

For programs spanning multiple PRs, identify owners and exact revisions. Keep implementation, verification, and landing responsibilities explicit. A stack intended for user review remains unmerged. Do not make worker count or project complexity a reason to invent unsupported orchestration machinery.

## Resume and pause

On resume, inspect the actual checkout, branch, uncommitted diff, processes, and remote state that matter. Treat previous summaries as leads, not proof that code or checks remain current. Preserve work you did not create.

When pausing, save the objective, completed units, current revisions, uncommitted work, running processes, known failures, and the next action. Stop or retain processes according to ownership and the user's request. Use host-managed worktree archival when required; cleanup needs evidence that no work or process depends on the resource. Do not delete a checkout merely because a PR merged.

## Skills and prompt evaluation

When modifying an agent workflow, identify the decision or behavior being improved. Use realistic requests and raw artifacts to compare the old and new guidance. A fresh evaluator gets the task and candidate skill without the intended answer. Run in an isolated workspace with permitted side effects. Evaluate observable outcomes such as correct scope, evidence quality, and handling unavailable tools, not whether it repeated prescribed headings.

Apply fixes supported by failures. Preserve tool protocols and user constraints while removing redundant instructions. Disclose when the evaluation was a static walkthrough rather than an executed agent run.
