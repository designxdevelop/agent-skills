---
name: quick-fix-deploy-sync
description: >-
  Sync production and staging git branches with fast-forward merges and push.
  Use when the user wants a quick fix deploy, hotfix promotion, backport to
  staging, sync main and dev/staging, fast-forward branches, or keep staging
  and production in sync after a commit.
---

# Quick Fix Deploy Sync

## Goal

Find the production and staging branches in the current project, then sync them
with fast-forward-only merges so both tips match — no merge commits, no force
push, and the cleanest possible branch history.

## When to Use

Use this skill when the user asks to:

- Quick fix deploy, hotfix, or ship a fix to production or staging.
- Promote staging to production or backport a production fix to staging.
- Sync `main` and `dev` / `staging` / `develop` / `preview`.
- Fast-forward branches and keep staging and production aligned.
- Commit a fix on one branch and mirror it to the other.

Example prompts:

- "Quick fix deploy — backport this to staging."
- "Ship what's on staging to main."
- "Keep main and dev in sync after this hotfix."
- "Commit, push main, and sync staging."

## Workflow

### 1. Resolve branch names

Discover production and staging branch names before any git writes. Check, in
order:

1. Project docs: `AGENTS.md`, `README.md`, `docs/setup.md`, `.github/workflows/*`
2. Remote default branch: `git remote show origin | grep 'HEAD branch'`
3. Common defaults:
   - **Production:** `main` or `master`
   - **Staging:** `dev`, `staging`, `develop`, or `preview`

If still ambiguous, ask once:

> Which branch is production and which is staging?

Record the mapping for the rest of the session. Example:

| Role | Branch |
|------|--------|
| Production | `main` |
| Staging | `dev` |

### 2. Preflight (always)

Run in parallel:

```bash
git status
git branch -vv
git fetch origin
```

Then compare remote tips:

```bash
git rev-parse origin/<production> origin/<staging>
git log --oneline origin/<staging>..origin/<production>
git log --oneline origin/<production>..origin/<staging>
```

**Stop and report** if:

- Working tree is dirty — commit or stash first; never commit secrets
- Branches **diverged** (each has unique commits) — fast-forward is impossible
- Either branch is missing locally or on `origin`

Do **not** use plain `git merge`, `git rebase`, or `git push --force` unless
the user explicitly approves after you explain the divergence.

### 3. Choose sync direction

| Situation | Action |
|-----------|--------|
| Fix committed on **production**; staging should match | Fast-forward **staging → production** |
| Fix tested on **staging**; ready to ship | Fast-forward **production → staging** |
| User says "backport to staging" | Staging ← production |
| User says "promote to prod" / "ship staging" | Production ← staging |
| User says "keep them in sync" / "both branches" | Sync the lagging branch to the leading one |

**Leading branch** = the branch with commits the other lacks (ahead after
`git fetch`).

If both sides are equal, report already synced — no push needed.

### 4. Fast-forward sync

Substitute resolved branch names below. Example uses production = `main`,
staging = `dev`.

**A — Production ahead (backport hotfix to staging)**

```bash
git checkout <staging>
git pull --ff-only origin <staging>
git merge --ff-only origin/<production>
git push origin <staging>
git checkout <production>
git status
```

**B — Staging ahead (promote to production)**

```bash
git checkout <production>
git pull --ff-only origin <production>
git merge --ff-only origin/<staging>
git push origin <production>
git checkout <staging>
git status
```

Return to the branch the user was on unless they asked to stay elsewhere.

### 5. Commit + sync (when the user includes a fix)

When the user wants **commit, push, and sync both branches**:

1. Stage **only** files for the fix — exclude unrelated changes
2. Commit with a concise message focused on why, not what
3. Push the branch where the commit was made
4. Run workflow **A** or **B** from step 4 based on which branch received the commit
5. Verify both remote tips match:

```bash
git rev-parse origin/<production> origin/<staging>
git log -1 --oneline --decorate origin/<production> origin/<staging>
```

### 6. Verify and report

After sync:

```bash
git rev-parse origin/<production> origin/<staging>
git log -3 --oneline --decorate origin/<production> origin/<staging>
```

Report using this template:

```markdown
## Branch sync

- **Production:** `<branch>` @ `<sha>` — `<subject>`
- **Staging:** `<branch>` @ `<sha>` — `<subject>`
- **Direction:** `<staging ← production | production ← staging | already synced>`
- **Pushed:** yes/no
- **Current branch:** `<branch>`

### Next step (optional)
- [ ] Verify staging deploy / production deploy if applicable
```

If CI or deploy hooks exist, mention which branch deploys where. Do not trigger
a deploy unless the user asks.

### 7. Diverged branches (escape hatch)

If `git merge --ff-only` fails, stop and present:

1. Commit lists on each side: `git log --oneline --left-right <production>...<staging>`
2. Options: open a merge PR, rebase staging onto production (needs approval), or
   reset staging to production (destructive — needs approval)

Do not pick an option without user confirmation.

## Guardrails

- **Never** `git push --force` to production or staging unless the user explicitly requests it
- **Never** amend or rebase pushed commits without explicit approval
- **Never** update `git config`
- **Never** use plain `git pull` — prefer `git pull --ff-only`
- **Never** use `git merge` without `--ff-only` in this workflow
- **Never** commit secrets, credentials, or `.env` files
- If fast-forward is impossible, **report** the divergence — do not silently rebase or force-push

## Completion Checklist

- [ ] Production and staging branch names were resolved from the repo or confirmed with the user
- [ ] Preflight ran: clean working tree, fetch completed, ahead/behind state is known
- [ ] Sync direction matches user intent (promote vs backport vs already equal)
- [ ] Only `--ff-only` merges were used; no merge commits were created
- [ ] Both remote branch tips match after sync (or divergence was reported with options)
- [ ] Final report includes both SHAs, direction, push status, and current branch
- [ ] No force push, rebase, or git config changes were made without explicit approval
