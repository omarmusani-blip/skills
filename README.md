# clock-in

A [Claude Code](https://claude.com/claude-code) skill that bookends a working day: a short
interview that produces a plan at the start, a short reckoning that records what came of it
at the end, and **silence in between**.

## The problem it solves

Most people who want something like this already have a planning ritual written down. Mine
was three lines at the top of a task file — *change the date, check these three views, pull
anything live into today*. It is a perfectly good ritual and it went unused for five weeks.

Not because it was wrong. Because **nothing fired it**. A note can't interrupt you. The
ritual bet on habit, and the bet lost.

The one thing I do open every working day is Claude Code. So the mechanism here isn't better
planning advice — it's a ritual attached to something that already happens.

## What it actually does

**Clock in** — asks how much day is genuinely left, what's fixed, and two or three real
questions *before* showing you anything. Then it shows what's live that you didn't mention,
names any gap between what your notes say matters and what you've actually been opening, and
writes down the plan you chose.

**During the day** — nothing. No check-ins, no progress pings. The quiet is deliberate: a
ritual that feels like overhead gets skipped, and a skipped ritual is worse than none.

**Clock out** — records what happened and asks one question: *what did today teach you about
the plan?* Not *why didn't you finish*. A plan that changed because the work taught you
something is the plan working, and only that framing tells it apart from drift.

## Three ideas it's built on

**Starting gates, not completion gates.** Every item carries a gate, and the gate marks
*having started*, not having finished. Abandonment happens in the first twenty minutes, when
a task turns uncomfortable and something else looks more interesting — a completion gate
can't see that moment, it just reports hours later on what you already know. A gate has to be
checkable without a judgement call (an artifact exists, or a time box was spent) and has to
be the smallest thing that can't be done without real engagement. Cloning a repo is theatre.
Writing the first function signature isn't.

**A bench, not just a plan.** Alongside the three or four things you picked, it lists three
or four that didn't make it **and why each lost** — waiting on someone else, no deadline,
doesn't fit the hours. The reason is the load-bearing half. It makes swapping easy, and it's
the structural guard against the plan quietly becoming Claude's with your name on it.

**You decide, Claude transcribes.** The thinking is the part worth protecting — the reason to
keep a task file by hand is that it requires mental use. What moves to the assistant is the
typing. The interview deliberately asks its questions before presenting any options, because
a question with candidate answers attached is a menu, and you'd just pick from it.

## Will this work for you?

This was built for my own setup and published because the shape of it might be useful to
someone, not because it's a general-purpose tool. Whether it fits you comes down to one thing.

**Required: a single authoritative list of what's live.** One place that says what your current
threads are and what the next step is on each. Mine is a table in a notes file; a plain
`projects.md` with eight lines would work just as well. The format doesn't matter — having
exactly one of them does.

This is load-bearing, and it's worth being blunt about why. Clock-in's most useful move is
showing you what's live that you *didn't* mention. With no authoritative list there's nothing to
check your answers against, and the skill quietly degrades into a generic interview while still
sounding like it knows what you're neglecting. That is worse than not running it at all.

**Optional. Each one buys something specific:**

| Signal | What it buys | Without it |
|---|---|---|
| Deadline dates on projects | Real arithmetic about what's actually urgent | You state deadlines in the interview |
| A timetable or calendar file | Honest working hours instead of fantasy ones | Clock-in asks what's fixed today |
| Recent file activity | The divergence check — the board says X, your week says Y | No divergence check; the interview carries it alone |

`references/context.example.md` is the full specification of what gets read and in what order of
authority. Skimming it is the fastest way to tell whether this fits your setup.

If you'd rather see a working example than a specification: I'm packaging the structure of my own
vault — the board, the conventions, and the reasoning behind them — as a companion repo under
[github.com/omarmusani-blip](https://github.com/omarmusani-blip). It'll be linked here once it's up.

It was built against an Obsidian vault, and the example config includes Obsidian specifics (open
tabs live in `.obsidian/workspace.json`), but nothing in the skill requires Obsidian.

## Install

```bash
git clone https://github.com/omarmusani-blip/clock-in.git ~/.claude/skills/clock-in
cd ~/.claude/skills/clock-in
cp references/context.example.md references/context.md
```

Then fill in `references/context.md` — where your task file lives, what your sources of truth
are, and where your work happens. The skill reads it at every clock-in and has nothing to work
from without it. It's gitignored, since it holds real paths and project names.

## Use

Say `clock in` or `clock out`. It will also offer itself at the start of the first session of
a day when the dated heading in your task file isn't today's — that offer is the whole point,
so it's worth leaving on.

The offer is deliberately bare: *"Clock in? Last clock-in: 12 Sept."* No thread names, no
deadline arithmetic, no "you haven't." Drift facts belong inside the interview, where they're
input to a decision you're making — not at the door, where they land as a verdict on one
you're declining.

Say `hand over` when a session is ending but your day isn't — context runs out long before the
work does. It appends a one-line state note (done / in flight / next) under today's plan and
touches nothing else, so the next session picks up mid-stride instead of reading a stale morning
plan. It is deliberately not a clock-out: the day gets reckoned once, at the end.

There's no escalation. If you ignore it for two weeks, it has failed, and the honest response
is to rework it or delete it.

## What it won't do

- Decide your day
- Judge whether your work was good
- Check in on you mid-day
- Activate itself without asking
- Insist you make a plan — "nothing today" is a legitimate answer

## Licence

MIT — see [LICENSE](LICENSE).
