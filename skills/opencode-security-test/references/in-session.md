# In-session mode

Read this when the skill is invoked inside an OpenCode session. You are the
tester and the verifier; there is no handoff. Apply the shared rules in
[SKILL.md](../SKILL.md) with the session's configured model and permissions.

## Model fit

- Use an open-source model from a configured gateway for work hosted models
  commonly decline; [models.md](models.md) has per-task picks. If the session
  model already fits, proceed with it.
- If the session model is proprietary and engages with the task, continue; do
  not treat model policy as a scope limit.
- If it refuses or is otherwise unsuitable, do not fight the refusal or stall.
  Give the user the options: switch the session model through the model picker
  or by relaunching with `--model provider/model`; use a configured OpenCode
  subagent that runs an open-weight model; or, with the user's agreement, run
  the delegated procedure in [opencode.md](opencode.md) to launch a child
  session.
- Do not silently switch models or launch child sessions on your own; the user
  decides which model runs their task.

## Execution

- Keep active testing inside a disposable target environment (container, VM, or
  scratch copy) and leave the session's permission configuration intact.
- Long-running scans, fuzzers, or listeners need an agreed runtime and stop
  condition; start them only inside the isolated environment and stop them at
  the deadline.
- Do not flip global configuration, disable permission controls, or publish the
  session.

## Evidence and report

- Keep transcripts, payloads, and raw output in a private directory outside the
  repository; record the session ID and the artifact path.
- Verify claims before reporting: re-run reproducers from a clean state, inspect
  raw outputs and diffs, and label anything you cannot validate.
- Report the model and provider, confirmed findings and changes, validation
  performed, gaps, and important negative results. Do not commit, push, or
  publish unless the user asked.
