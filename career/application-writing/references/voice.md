# Voice calibration

The one input no published anti-slop skill has: the writer's actual prose. Everything
else in this skill is generic craft. This is the part that makes an answer sound like
them rather than like competent nobody.

The writer's corpus, voice profile and standing preferences live in
`references/context.md`. This file is the method.

## The rule that protects the whole thing

**Never calibrate voice on assistant-drafted text.**

If the samples include text the model wrote, the skill learns its own output, reports
that the result sounds authentic, and the exercise is circular. This is the same
failure as a model grading its own homework, and it is silent — nothing looks wrong.

So every sample has to carry its authorship. Two kinds, doing two different jobs:

| | What it is | What it's for |
|---|---|---|
| **Voice sample** | Words the writer wrote | How they actually sound |
| **Taste target** | Joint drafts they liked | What passes their judgement |

Both are useful. Only the first sets voice.

## The ★ convention

On any application note with written answers, the writer marks answers they really
liked with a **★** at the start of the heading or the answer:

```markdown
### ★ Q3 — Tell us about a time you worked with little direction
Answer text...
```

Default reading: a ★ answer is a **taste target** — a joint draft that cleared their
bar. If the words are their own, they add `(my words)`:

```markdown
### ★ Q1 — Why this role? (my words)
```

That promotes it to a **voice sample**, the higher-value kind.

Grep for ★ across the notes folder named in `context.md` and read the hits before
drafting anything new. They accumulate with every application, so the skill improves as
a by-product of work being done anyway.

## Building the profile

From clean samples only, record:

- sentence length and how much it varies
- subordination versus short declaratives
- appetite for bluntness, hedging, dry humour, self-deprecation
- punctuation habits, em dashes especially (the checker's cap should come from here)
- how technical they go before glossing a term
- how often they state a position outright versus leaving a tension open
- what they would never say

Show the profile to the writer and get a yes before using it. Then translate: keep their
moves (plain words, the turn mid-thought, the honest question, "we" for team work), drop
what hurts them on the page (typos, run-ons past two clauses), and never add what isn't
theirs.
