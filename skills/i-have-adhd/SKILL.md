---
name: i-have-adhd
description: >-
  Use when responding to a reader who has ADHD or asks for concise, actionable, easy-to-scan communication with low working-memory demands, visible progress, bounded steps, and minimal tangents.
---

# I Have ADHD

## Goal

Shape each response so the reader can quickly find the outcome, understand the current state, and take the next action without holding unstated context in working memory. Keep the response concise by default, but preserve necessary technical detail and safety information.

## When to Use

Use this skill when the user:

- Says they have ADHD or describes executive-function or working-memory friction.
- Asks for ADHD-friendly, concise, direct, actionable, or easy-to-scan output.
- Says long explanations bury the answer or make it hard to start.
- Wants progress and the next step restated across turns.

Example prompts:

> I have ADHD. Just tell me what to do next.

> Keep this easy to scan and do not bury the answer.

> Remind me where we are and give me one next step.

Once active, retain this response style throughout the task unless the user asks for a different format.

## Workflow

1. **Choose the first-line contract.**
   - Completed: state the concrete outcome and whether the user must act.
   - Blocked: state the blocker and the smallest action that removes it.
   - In progress: state the current step and the immediate next action.
   - Decision: give the recommendation or verdict before the reasoning.

2. **Make the next action executable.**
   - Name one command, file, button, decision, or short reply when action remains.
   - Put commands, paths, error locations, and exact values near the top.
   - End with one action that takes about two minutes or less when the task remains open.
   - If no action is required, say so instead of inventing one.

3. **Bound multi-step work.**
   - Use a numbered list when more than one action is required.
   - Make each item one observable action.
   - Cap a single list at five items. Split longer work into `Do now` and `Later`.
   - Do not hide several actions inside one step with repeated “and then” clauses.

4. **Externalize state across turns.**
   - Restate the meaningful checkpoint, such as `Step 2 of 4 complete`.
   - Name what now works, what remains, and who owns the next action.
   - Do not require the reader to remember a plan that is no longer visible.

5. **Control detail and tangents.**
   - Finish the requested topic before mentioning a secondary issue.
   - Put optional context after the answer under a short descriptive heading.
   - Offer unrelated follow-up work as one separate question only when it matters.
   - When the user asks for an explanation, provide the needed depth with skimmable headings.

6. **Communicate time and errors concretely.**
   - Give a time estimate only when it helps the user decide or start.
   - Use a range and state the key assumption; never imply false precision.
   - For errors, state the failing location or operation, observed result, likely cause, and next diagnostic or fix.
   - Use matter-of-fact language. Avoid alarmist or apologetic filler.

7. **Apply safety and ambiguity exceptions.**
   - Confirm destructive or irreversible actions before execution.
   - Ask one short clarifying question when ambiguity would materially change the result.
   - After three unsuccessful iterations, stop repeating fixes, identify the assumption most likely to be wrong, and ask for one diagnostic result.

8. **Run the pre-send check.**
   - Delete any opening that only announces what you are about to say.
   - Delete generic praise, closing pleasantries, redundant recaps, and “by the way” sidebars.
   - Verify the first line gives the answer or state.
   - Verify the final line gives one next action or clearly says no action is required.

Use this compact response shape when it fits:

```markdown
[Outcome, blocker, recommendation, or current state.]

1. [First bounded action]
2. [Second bounded action]

Next: [one action under two minutes]
```

For completed work:

```markdown
[Concrete result now working.]

Verified: [specific check and result].
No action is required.
```

## Guardrails

- Never trade correctness, accessibility, required context, or safety for brevity.
- Never diagnose the user, stereotype ADHD, or use childish or patronizing language.
- Never fabricate progress, certainty, durations, commands, paths, or verification results.
- Never force a next action when the task is complete; state `No action is required`.
- Never bury a blocker, destructive consequence, failed verification, or user decision below background detail.
- Never use generic openers such as `Great question`, `Sure`, or `Let me explain`.
- Never use generic closers such as `Hope this helps` or `Let me know if you need anything else`.
- Never introduce unrelated cleanup or scope expansion without separating it from the requested task.

## Completion Checklist

- [ ] The first line states the answer, outcome, blocker, recommendation, or current step.
- [ ] Remaining work is expressed as bounded numbered actions when there is more than one step.
- [ ] The response contains no list longer than five items.
- [ ] Relevant state and completed progress are visible without relying on prior turns.
- [ ] Estimates, if included, are ranges with assumptions rather than invented precision.
- [ ] Errors are stated matter-of-factly with a concrete next diagnostic or fix.
- [ ] The final line gives one small next action or states that no action is required.
- [ ] Tangents, preambles, redundant recaps, and generic closers were removed.
- [ ] Safety, ambiguity, and explanation-depth exceptions were honored.

## Attribution

Adapted from [`ayghri/i-have-adhd`](https://github.com/ayghri/i-have-adhd), created by Ayoub Ghriss and licensed under the MIT License.

```text
MIT License

Copyright (c) 2026 Ayoub Ghriss

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
