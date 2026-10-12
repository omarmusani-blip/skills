# application-writing

Cover letters, application answers and outreach that read as human and claim nothing the
applicant can't defend in an interview.

## How it works

1. **Split authorship.** Structure and evidence placement are drafted; motivation and
   "why this employer" sentences are left for the applicant, because writing them is the
   part that builds the answer they'll give in the interview.
2. **Evidence boundary.** Every detail is tagged *source*, *inference*, *placeholder* or
   *unsafe*. Unsafe never reaches the page. Density can't come from invented specificity:
   a bracketed `[which mechanism?]` beats a confident fabrication.
3. **Structure audit, one aspect at a time.** Discourse structure classified human vs AI
   text at 93.2% with all style features withheld (StoryScope, arXiv:2604.03136), and
   sentence-level rewriting moved detection 1.6 points. So the audit targets shape:
   self-explained lessons, over-tidy arcs, vague allusion, credential openers.
4. **Surface pass by script.** `scripts/check.py` counts sentence-length variance,
   same-length runs, banned phrases, repeated openers, rule-of-three clusters, passive
   estimate and em-dash density. It counts; it doesn't judge.
5. **Voice from clean samples only.** Calibrating on assistant-drafted text makes the loop
   circular and silently self-approving. Samples carry authorship: *voice samples* (their
   words) set voice; *taste targets* (joint drafts they liked, marked ★) set the bar.

**Overcorrection guard:** caps, not bans. A published A/B test of borrowed blanket rules
(no passive, no adverbs, no em dashes) found zero effect across 18 paired runs, and the
authors had to add a regression test to protect earned constructions from their own rules.

## Setup

```bash
cp references/context.example.md references/context.md
```

`context.md` says where the evidence lives, which files are clean voice samples, and the
standing preferences learned from corrections. It's gitignored.

```bash
python scripts/check.py draft.txt        # or: cat draft.txt | python scripts/check.py -
```

## Licence

MIT, see [LICENSE](LICENSE).
