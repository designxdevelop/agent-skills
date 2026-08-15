---
name: anti-slop
description: >-
  Detect and remove AI writing tells ("slop") from prose while preserving the
  author's voice. Load when drafting or reviewing prose, blog posts, essays,
  white papers, marketing copy, emails, docs, or reports, and when a human asks
  to make writing sound less AI-generated or to review someone else's writing
  for AI tells. Triggers on "sounds like AI", "slop", "AI tell", "make this more
  human", "editorial pass", or "review my writing".
---

# Anti-Slop

## Goal

Remove phrasing that signals machine authorship: filler that announces itself, hedged puffery, formulaic rhythm, and clever-sounding constructions that carry no information. Preserve the author's voice. Do not flatten the piece into voiceless text.

## When to Use

Use this skill when the user:

- Asks to draft, edit, or review prose, blog posts, essays, white papers, marketing copy, emails, docs, or reports.
- Says the writing sounds like AI, has slop, has AI tells, or should sound more human.
- Asks for an editorial pass or a review of someone else's writing for AI tells.

Example prompts:

> This sounds like AI. Make it more human.

> Editorial pass on this draft: cut the slop, keep my voice.

> Review this post for AI tells before I publish.

## Workflow

### Prime directive

Before deleting anything, decide whether it is *slop* (adds no meaning, follows a formula) or *voice* (a deliberate choice the author would defend).

- Cut filler, formula, and hedging.
- Keep rhythm the author earns: a short punchy fragment after a long sentence, a deliberate tricolon, a contrast the argument needs, a strong closing line.
- When unsure, leave it. A false positive that flattens a good sentence is worse than one surviving tell.

Make surgical edits. Change phrasing, not substance. Do not restructure paragraphs, reorder arguments, or change meaning unless asked.

### When reviewing

1. Read the whole piece first. Note voice: punchy, formal, conversational? Match this; do not overwrite it.
2. Scan for the tells in the catalog below. Collect *candidates*. Do not edit yet.
3. Validate each candidate: does removing it lose meaning? Is it formula or voice? Discard false positives.
4. Apply the surviving edits one at a time, each a minimal phrasing change.
5. Re-read the edited passages for rhythm. Fix anything that now reads choppy or flat.
6. Report what changed and the tell category for each, so the author can judge.

For a thorough review, a contested edit, or the reasoning behind a flag, load [references/tells.md](references/tells.md).

### When drafting

Write first, then run the review workflow on your own draft before delivering. Do not self-censor into blandness while drafting; catch tells on the edit pass.

### The tell catalog

| Tell | Why it erodes trust | Fix |
| --- | --- | --- |
| Meta throat-clearing: announcing the point before making it ("It is worth noting that…", "There is a failure mode worth naming…", "Here is the tension.") | Wastes the reader's time; signals padding. | Delete the frame. State the thing. |
| Demonstrative kicker: a vague "This/That + verdict" fragment tacked after a sentence ("That instinct backfires.", "This is where the risk hides.", "That is the whole point.") | Formulaic filler rhythm; the "verdict" usually restates the prior sentence. | Cut it, or fold the idea into the sentence; pivot the next sentence with a real transition ("But…"). |
| Puffery adverbs: genuinely, truly, actually, simply, deeply, structurally, fundamentally. | Intensifiers that add heat, not light. | Delete. If the claim needs the adverb to be true, the claim is weak. |
| Importance-flagging: "Speed is not a footnote here.", "This matters.", "Make no mistake." | Tells the reader what to feel instead of earning it. | Show the consequence directly. |
| Clever metaphor flourish: "an authorization bug wearing the costume of a performance optimization." | Reads as a model performing wit. | State it plainly: "an authorization bug, not a performance optimization." |
| Grandiose prediction: "will define the next decade", "changes everything", "the future of X". | Overclaiming; lowers credibility in serious writing. | Cut or scope to a concrete, defensible claim. |
| Rule-of-three reflex: every list padded to three parallel items. | Predictable cadence; the third item is often filler. | Vary list length. Keep two if two is true. |
| Antithesis overuse: "not X, but Y" as a tic in paragraph after paragraph. | One is rhetoric; five is a template. | Keep the one the argument needs; rewrite the rest as plain statements. |
| Correlative bloat: "not only… but also", "whether… or". | Scaffolding that inflates simple sentences. | Split or simplify. |
| Hedged confidence: "It's important to consider…", "One might argue…", "In many ways…". | Sounds authoritative while committing to nothing. | Take the position or cut the sentence. |
| Section-closing summary: a final sentence that restates what the paragraph just said. | Redundant; a model habit. | Delete if it adds nothing. |
| Overused lexicon: delve, tapestry, realm, landscape, underscore, leverage, seamless, robust, crucial, pivotal, testament, navigate (figurative), foster, elevate, unlock. | Statistically flagged AI vocabulary. | Swap for plain words or cut. See [references/tells.md](references/tells.md). |
| Em dash: `—` or `--` used as a pause, parenthetical, or list separator. | Default AI connector; reads as machine cadence. | Replace with a comma, colon, period, or parentheses. Never insert a new em dash. |
| Faux-weight metaphor: load-bearing, linchpin, through-line, north star. | Sounds like a model performing seriousness. | Name the actual role: the contrast that matters, the claim the argument needs. |

### Concrete before / after

Meta throat-clearing

- Before: "There is a failure mode worth naming directly, because well-intentioned teams walk straight into it. It is the belief that safety means a human approving every step."
- After: "Many teams equate safety with a human approving every step."

Demonstrative kicker

- Before: "…reuse the machinery we already have. That instinct is where most of the risk hides. Four properties break the assumptions."
- After: "…reuse the machinery we already have. But four properties break the assumptions."

Importance-flagging + staccato

- Before: "Speed is not a footnote here. It changes which controls are viable. Anything that depends on a person noticing has already lost."
- After: "Speed changes which controls are viable: anything that depends on a person noticing has already lost."

Clever flourish

- Before: "an authorization bug wearing the costume of a performance optimization"
- After: "an authorization bug, not a performance optimization"

### What to keep

These are voice, not slop. Deleting them is the over-correction failure.

- Earned fragments: "Not flagged after the fact. Removed." A short beat after a long sentence, used sparingly, for emphasis.
- Deliberate parallelism: "You can have either. You cannot have both."
- A strong closing line: "The perimeter fell twelve years ago. The session is next."
- First-person conviction: "We think…", "We are not comfortable saying…" when the author owns a real position.

The test: could the author defend this choice if asked? If yes, keep it. Slop cannot be defended; it is there because a pattern put it there.

## Guardrails

- Never change facts, numbers, names, citations, or technical claims during a phrasing pass.
- Never restructure or re-argue. Phrasing only, unless explicitly asked for more.
- Never flatten voice into generic middle-register prose. Match the author's register.
- Never introduce new slop while removing old (for example, replacing a kicker with a different formulaic kicker).
- Never use an em dash (`—`) or a double hyphen (`--`) as punctuation. Prefer a comma, colon, period, or parentheses. This is not a voice exception.
- Never use *load-bearing*, *linchpin*, *through-line*, or *north star* as emphasis. Say what the sentence actually does.
- Validate every candidate before editing; report false positives you chose to keep and why.
- One tell fixed cleanly beats three fixed clumsily. Stop when the remaining candidates are voice, not slop.

## Completion Checklist

- [ ] Read whole piece; noted the author's voice
- [ ] Collected tell candidates without editing
- [ ] Validated each: slop vs voice; discarded false positives
- [ ] Applied surviving edits as minimal phrasing changes
- [ ] Re-read for rhythm; fixed new choppiness/flatness
- [ ] Facts, numbers, structure untouched
- [ ] No em dashes (`—`) or `--` punctuation remain
- [ ] No *load-bearing*, *linchpin*, *through-line*, or *north star* leftover as emphasis
- [ ] Reported changes + tell category per edit

## Attribution

Adapted from [`elithrar/dotfiles` anti-slop](https://github.com/elithrar/dotfiles/blob/main/.agents/skills/anti-slop/SKILL.md), created by Matt Silverlock and licensed under the MIT License.

```text
The MIT License (MIT)

Copyright (c) 2014 Matt Silverlock

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
