# clock-in

Bookends a working day: a short interview that produces a plan at the start, a short
reckoning at the end, and **silence in between**.

## Why it exists

A written planning ritual (change the date, check three views, pull anything live into
today) went unused for five weeks. Not because it was wrong: **nothing fired it**. A note
can't interrupt you. The fix is attaching the ritual to something already opened every
working day, the coding assistant, rather than writing better planning advice.

## Mechanism

- **Clock in.** Asks how much day is genuinely left, what's fixed, and two or three real
  questions *before* showing any options, because a question with candidate answers
  attached is a menu. Then it surfaces what's live that you didn't mention, flags any gap
  between what your notes say matters and what you've actually been opening, and writes
  down the plan you chose.
- **During the day:** nothing. A ritual that feels like overhead gets skipped.
- **Clock out.** Records what happened and asks one question: *what did today teach you
  about the plan?* A plan that changed because the work taught you something is the plan
  working; that framing is what separates it from drift.
- **Hand over.** When a session ends but the day doesn't, it appends a one-line state
  note (done / in flight / next) under today's plan, so the next session starts mid-stride.

## Design ideas

**Starting gates, not completion gates.** Abandonment happens in the first twenty minutes,
when a task turns uncomfortable. A completion gate can't see that moment. Each item's gate
marks *having started*: checkable without judgement, and the smallest step that needs real
engagement. Cloning a repo is theatre; writing the first function signature isn't.

**A bench, with reasons.** Next to the three or four picks sit three or four that lost,
each with why (blocked, no deadline, doesn't fit the hours). The reasons make swaps easy
and stop the plan from quietly becoming the assistant's with your name on it.

**Bare offer at the door.** *"Clock in? Last clock-in: 12 Sept."* Drift facts belong inside
the interview, where they inform a decision, not at the door, where they read as a verdict.

## Requirements

**Required: one authoritative list of what's live** (threads and next step on each). Its
best move is showing what you *didn't* mention; with no list to check against, it degrades
into a generic interview that still sounds informed, which is worse than nothing.

**Optional:** deadline dates (real urgency arithmetic), a timetable (honest hours), recent
file activity (the divergence check). `references/context.example.md` is the full spec of
what's read and in what order of authority. Built against an Obsidian vault; nothing
requires Obsidian.

## Setup

```bash
cp references/context.example.md references/context.md
```

Fill in your task file, sources of truth and work locations. Gitignored.
Trigger: "clock in", "clock out", "hand over".

## Licence

MIT, see [LICENSE](LICENSE).
