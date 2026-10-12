# Plan format

Read this when writing or updating the plan. The shape matters less than the two things it
protects: that the choice was **theirs**, and that "done" can be checked without an opinion.

Adapt the markdown to whatever their task file already uses — matching the file they have
beats imposing a format on it.

## Today

Replace the dated section in their task file. One such section only — carry-over works by
items staying put, which is why there is no note-per-day.

```markdown
## Today — 19 Sept, 2026

*Clocked in 09:12. ~5h working time (fixed commitment 11:15–13:05).
Divergence: the board has the deadline thread at 27 days. Last opened 14 Sept.*

- [ ] **Scaffold the training and inference scripts** — [[Deadline Project]] · ~2h · *with Claude*
      Start gate: data-loading stub written and runs on one sample.

- [ ] **Install the tool and use it for real** — [[Side Project]] · ~45m · *solo, hands off*
      Start gate: it is running and I have asked it one real question while working.

- [ ] **Reading** — [[Reading]] · ~1h30 · *solo*
      Start gate: 20 minutes in, no page target.

*Benched today:*
- Research follow-ups — needs ~40m of browsing, doesn't fit what's left
- Tidy the attachments folder — no deadline; loses to anything that has one
- Reply to the recruiter — not time-critical, and the meeting on Sunday comes first
```

### The fields, and why each is there

**Thread link** — makes the goal tie visible without a sentence explaining it. If an item
links to nothing, say so: either it belongs to something not on the board, or it isn't really
today's work.

**Who** — `with Claude`, `solo`, or `solo, hands off`. The third is an **opt-in** commitment
that Claude won't do it for them today; if they come back and ask Claude to do that item,
point at the plan rather than simply doing it. It bites **only** where they marked it.
Deciding on their behalf that they need discipline is not this skill's job.

**Time** — rough, and it has to sum to something the day can actually hold.

**Start gate** — see the gate section in `SKILL.md`. Always either *an artifact exists* or *a
time box was spent*, never a judgement.

### The bench

Three or four, each with **the reason it lost** — that reason is the load-bearing half, not
the item. Losing for "waiting on someone else" and losing for "no deadline" are different
kinds of losing, and swapping intelligently is only possible if you can see which.

The bench is also the structural guard against this becoming Claude's plan that they
rubber-stamp. Winners only mean something when the losers are on the page.

## Hand over

One italic line appended under the dated heading when a session ends but the day does not.
Never a rewrite of the plan, and never an entry in the accumulating log — see the hand-over
section in `SKILL.md` for why.

```markdown
*Handed over 14:20 — items 1 and 2 done; gate on 2 revised. In flight: the install, nothing
written yet. Next: finish it, then sport.*
```

Several in a day is fine. They read as a trail, which is what the next session needs.

## Clock out

Append one line per item, honest about partials:

```markdown
**19 Sept** — training scripts scaffolded, running on one sample (gate met, ~2h).
Reading 1h30. Tool install not started — swapped out at 14:00 for an urgent reply.
```

Then one line in whatever accumulating log they keep, but only when the week's shape actually
became clearer. A log that is never cleared only earns an entry when there is something a
future session would want.

## When the plan changes mid-day

Expected, not a failure. Update the item in place and let clock-out record what changed — the
useful record is *what the work taught them*, not a diff.

Don't rewrite the whole section mid-day. It makes the morning's reasoning invisible, and that
reasoning is exactly what clock-out's question examines.
