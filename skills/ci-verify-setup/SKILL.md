---
name: ci-verify-setup
description: >-
  Use when a project lacks a single reliable verification command, has missing or broken CI, asks to add GitHub Actions, asks to make agents able to verify their work, or needs lint/type/test checks standardized across local and remote environments.
---

# CI Verify Setup

## Goal

Give any coding agent one dependable command that verifies the project locally, then mirror that command in CI so local and remote feedback agree.

## When to Use

Use this skill when the user asks you to:

- Add or repair a project-level `verify`, `check`, or equivalent command.
- Set up GitHub Actions or another CI workflow for lint, typecheck, build, or tests.
- Make the repo easier for Codex, Claude Code, Cursor, or other agents to validate.
- Replace scattered manual checks with one documented verification path.

## Workflow

1. **Inspect before editing.**
   - Identify the package manager, language, framework, and existing scripts.
   - Read current CI config, contributor docs, and agent instructions if present.
   - Note whether tests, linting, typechecking, formatting, and builds already exist.

2. **Define the smallest honest local verification command.**
   - Prefer an existing command if it already covers the important checks.
   - If no command exists, add one named according to local convention: `verify`, `check`, or the repo's established equivalent.
   - Compose existing scripts instead of introducing new tooling unless a required check has no existing runner.

3. **Make CI run the same contract.**
   - Add or update the CI workflow so it installs dependencies, restores cache if appropriate, and runs the local verification command.
   - Keep local and CI commands aligned; do not let CI become a separate checklist.
   - Use the repo's default branch, package manager lockfile, and supported runtime versions.

4. **Document the verification path.**
   - Update README, contributing docs, or agent instructions with the exact command agents should run before handing off.
   - Mention any checks that are intentionally excluded and why.

5. **Verify the setup.**
   - Run the local verification command if the environment allows it.
   - Validate workflow syntax when possible.
   - If checks fail for pre-existing reasons, report the failure clearly instead of hiding it.

## Guardrails

- Never add a new package manager, lockfile, linter, formatter, or test framework just to make CI exist.
- Never delete existing CI jobs without explaining what replaces their coverage.
- Never make CI pass by weakening tests, suppressing type errors, or skipping meaningful checks.
- Never claim verification works unless you ran it or clearly state why it could not be run.
- Never commit secrets, tokens, or environment-specific credentials into workflow files.

## Completion Checklist

- [ ] Existing local scripts and CI were inspected before editing.
- [ ] A single local verification command exists or an existing one was documented.
- [ ] CI runs the same verification contract as local development.
- [ ] Runtime versions, package manager, and lockfile usage match the repo.
- [ ] Verification instructions were documented for future agents.
- [ ] Local verification or workflow validation was run, or the blocker was reported.
