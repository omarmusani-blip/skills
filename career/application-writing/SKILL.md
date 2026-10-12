---
name: application-writing
description: Write or revise cover letters, application question answers, personal statements and recruiter outreach so they read as human, stay strictly inside the evidence, and sound like the applicant rather than a language model. Use this whenever the user is applying for anything — placement, internship, graduate scheme, competition, grant, accelerator — or drafting any prose that will carry their name to an employer, including "help me answer this question", "draft a cover letter", "does this sound AI-written", "make this sound like me", or a pasted job posting with questions attached. Trigger it even for a single quick question, because the evidence and voice checks are precisely what a quick draft skips.
---

# Application writing

Prose that goes out under the applicant's name to an employer. Read
`references/context.md` first: who they are, where their evidence lives, and their voice. Two failure modes matter, and
they are not the same:

1. **It reads as machine-written.** A recruiter skims 200 of these. Generic loses.
2. **It claims something they can't back in an interview.** Worse than generic, and
   several employers now say so explicitly — Airbus's own policy tells candidates not
   to prompt AI to invent skills they do not possess.

The second is the one that ends badly, so it is handled first. Style work on a claim
that shouldn't be there is wasted effort.

## Step 0 — decide who writes what

Before anything carries the applicant's name, work out whether writing it themselves
builds understanding or identity they need. For applications the split is
usually stable, so propose it rather than asking every time:

| Part | Who |
|---|---|
| Structure, order, which evidence goes where | Claude |
| Sentences that state what they want and why this employer | **Applicant** |
| Sentences that describe what they did | Claude drafts, they correct |
| Any claim about motivation, ambition, or values | **Applicant** |

Say this split out loud at the start, in one line, then work inside it. If they want
Claude to draft the motivation sentences anyway, draft them and mark them clearly as
placeholders in their voice, not as finished text.

## Step 1 — the evidence boundary

Before adding any specific detail, know where it came from. Label internally:

- **source** — present in the posting, the notes, a CV, or something they said
- **inference** — follows narrowly from source, adds no new fact
- **placeholder** — useful, and they must confirm it before it ships
- **unsafe** — plausible, would read as fact, nothing supports it

`unsafe` never reaches the page. Not softened, not hedged — out.

The rule that makes this real: **density cannot come from fictional specificity.** When
the honest version is thin, say it is thin and name the missing fact, rather than
inventing a mechanism, a metric, a motivation or a date to fill the gap. A bracketed
`[which mechanism?]` handed back to the applicant beats a confident invention, every time.

Where the evidence lives is set in `references/context.md`. When the notes are thinner
than the CVs, trust the CVs and flag the gap.

Attribution locks, cheap to check and embarrassing to get wrong:

- A metric or action belongs to the one project or employer it happened under. Never
  merge two into one sentence.
- Present tense only for work that is genuinely ongoing.
- No "earlier" or "later" unless the dates have been checked.
- Team size, role and scope as recorded, not rounded up.

## Step 2 — structure, which is the real tell

This is the part worth spending time on. A study of 61,608 texts (StoryScope, Russell
et al. 2026, arXiv:2604.03136) classified human vs AI writing using *only* discourse
structure, with every style feature withheld: 93.2% accuracy. Running the text through
professional sentence-level rewriting moved detection 1.6 points. Word swaps are
cosmetic; shape is the fingerprint.

Audit one at a time — aspect-by-aspect checking found 95% of issues in that study's own
pipeline versus 68% for a single combined pass.

**Stated lessons.** AI explains its own point 77% of the time versus 52% for humans,
and restates the thesis at the end of every section. In a cover letter this is the
sentence after the evidence that tells the reader what the evidence proved. Cut it.
Make the point once, where it lands hardest, and let at least one example stand
uninterpreted.

**Tidiness.** Single causal track, every thread resolved, a closer that ties it all
together. Humans digress and leave things open. One oblique tangent, or one question
raised and not answered, does more for credibility than a tight bow.

**Vague allusion.** Humans name real things at roughly twice the rate — specific
titles, places, prices, versions, dates. "A composites project" is AI. "Oxide/oxide
CMC specimens, four infiltration routes" is a person. This is also where the evidence
boundary bites: name real things, never invented ones.

**Openers.** No "As a second-year Mechanical Engineering student, I...". Real people
say the thing. Announcing credentials before content is a tell and wastes the one
sentence a skimming recruiter definitely reads.

## Step 3 — surface pass, by script not by eye

Run the checker rather than judging by feel. Judging one's own prose for AI-ness is
circular; counting is not.

```bash
python scripts/check.py <file>   # path relative to this skill; context.md has the absolute one
```

It reports em-dash density, sentence-length variance and same-length runs, banned
phrases with line numbers, repeated openers, rule-of-three clusters, passive-voice
estimate, contraction count and over-long sentences. Fix what it flags, then re-run.

Read `references/tells.md` for what each flag means and which ones are advisory.

## Step 4 — voice

Calibrate against real samples, never against a general idea of "human". See
`references/voice.md` for the corpus, the ★ convention for answers the applicant liked, and the
one rule that matters most: **never calibrate voice on assistant-drafted text**, or the
skill converges on its own output and the whole exercise is circular.

## The overcorrection guard

`adewale/anti-slop-writing` A/B-tested borrowed surface rules against its own baseline
across three models with the judging agent kept separate from the writing agent. All 18
paired deltas came back at exactly 0.00 — the imports changed nothing. The rules they
nearly imported were blanket bans: all passive voice, all adverbs, all em dashes. They
had to add a regression test specifically to protect *earned* passive voice and adverbs
from their own rule.

So:

- **Cap, don't ban.** One em dash per 500 words of prose is fine. Zero is its own tell,
  and an em dash in a CV heading is typography, not voice.
- **Earned constructions stay.** Passive voice when the actor is genuinely irrelevant.
  An adverb that carries meaning. A long sentence when the thought is long.
- **Don't swap one default for another.** If every letter now opens mid-scene and ends
  unresolved, that is a new detectable pattern. Rarity is the human signal, so pick one
  or two structural moves per piece and be able to say why this piece got this shape.
- **A vague source stays vague.** Sharpening "some observers suggest" into "the finance
  team suggests" invents an actor. Keep the claim's strength, drop the faceless noun.

## Output

Give the applicant, in this order:

1. **The draft** — plain text, ready to paste, with their parts marked `[You: ...]` if
   unwritten.
2. **Evidence notes** — which claims are source, which are placeholders they must
   confirm, and anything left out because nothing supported it.
3. **Checker output** — the numbers, not a claim that it reads well.

Never call it finished. They accept it at VERIFIED, UNDERSTOOD or PARTIAL; the skill's
job is to make that judgement easy, not to pre-empt it.

## Final pass

- Every claim traceable to source, inference, or a marked placeholder
- No metric attached to the wrong project; tenses match reality
- The point stated once, not restated at each section end
- Real named things, none of them invented
- Checker run, output shown
- Nothing in it they would not want to be asked about in an interview
