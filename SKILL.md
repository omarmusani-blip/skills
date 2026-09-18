---
name: clock-in
description: Bookends a working day — a short interview that produces a plan at the start (clock in), and a short reckoning that records what came of it at the end (clock out). Use this whenever the user says "clock in" or "clock out", asks what they should work on today, asks for a plan or a shape for the day, wonders what's live or what they're drifting from, or starts a working session without having planned one. Offer it proactively at the start of the first session of a day when the dated heading in their task file is not today's date — a planning ritual that nothing fires is the problem this exists to solve.
---

# Clock in

A working day gets two bookends: a short interview that produces a plan, and a short
reckoning that records what came of it. Nothing in between.

Read `references/context.md` first — it holds the user's file paths, their sources of truth,
and anything specific to how they work. Without it this skill has nothing to read from.
If it doesn't exist, copy `references/context.example.md` and fill it in with the user.

## What this is actually fixing

Most people who need this already have a planning ritual written down somewhere, and it is
usually a good one. It goes unused because **nothing fires it**. A note cannot interrupt you;
a written ritual bets on habit, and that bet loses more often than not.

Claude Code is something the user already opens. That is the whole mechanism here — not
better planning advice, just a ritual attached to something that already happens.

The job is **sequencing and commitment**, not productivity. Someone reaching for this usually
has more live threads than days, and picks between them by interest rather than by cost. The
plan's purpose is to make that choice deliberate and visible, not to extract more hours.

## The governing principle

Every intervention costs something. This runs twice a day and is silent the rest of the
time — that silence is a design decision, not an omission. If an intervention is not clearly
worth the interruption, don't make it.

The specific failure to avoid: becoming another thing talking at them. A ritual that feels
like overhead gets skipped, and a skipped ritual is worse than none, because it carries a
small reproach each time it is ignored.

## Offering it

Check whether the dated heading in their task file matches today's date. If it doesn't, offer
once, at the start of the session, and keep the offer plain:

> Clock in? Last clock-in: 12 Sept.

That bare date is the whole offer. **No thread names, no deadline arithmetic, no "you
haven't."** Drift facts belong inside the interview, where they are input to a decision being
made — not at the door, where they land as a verdict on one being declined. Being told what
you are neglecting at the moment you say "not today" is how a tool becomes the thing you
avoid.

If they decline, drop it for that session. Don't re-offer, don't hint.

There is **no escalation mechanism**, deliberately. If this is being ignored for a week or
two, it has failed, and the honest response is to rework or kill it — which is the user's
call. Building machinery to push harder would mean deciding, unilaterally, that someone needs
discipline. That isn't this skill's job.

## Clock in

**The order matters more than any individual step.** The failure mode is arriving with a
ranked list of what they should do — they then pick from it, and the plan is yours wearing
their name. Their thinking has to set the frame; yours catches what it missed.

**1. Say how much day is left.** Working hours remaining, out loud, before anything is
picked. At 09:00 four items is reasonable; at 17:00 it is fantasy, and this should be the
thing that says so. Subtract known commitments, and be honest about time already spent.

**2. Ask what's fixed.** Anything today that your sources don't know about? Timetables,
deadlines and meetings can be read, but plans get made by text message.

**3. Interview — before showing any candidates.** Two or three real questions, and wait for
the answers:

> What would make today not wasted?
> Is anything blocked on someone else?
> Anything you've been avoiding?

These are doing real work. The first surfaces their actual priority, which is often not the
most urgent thing on any list. The second catches dependencies before a day is planned around
one. The third is the one they will answer honestly if asked plainly and not followed up on —
and avoidance is usually where the important thing is hiding.

Don't supply candidate answers. A question with options attached is a menu.

**4. Then show what they didn't mention.** Now the candidates, framed as a gap-check rather
than a ranking — what's live that they didn't raise, and what it would cost. This is where
reading their sources pays off, and where the divergence goes:

> The board has the deadline thread at 27 days. It hasn't been opened in 12.
> Which one's wrong, the plan or the week?

State it once. Don't repeat it later in the session, and don't moralise. If their sources and
their attention agree, say nothing — most days there is nothing here.

**5. They choose. You transcribe.** The thinking is theirs, and it is the thing worth
protecting — the reason to keep a task file by hand is that it requires mental use. What
moves to Claude is the typing, not the deciding.

The structural guard is the **bench**: show what didn't make the cut and *why it lost*. Three
things winning only means something if the losers are visible.

**6. Write it.** Format in `references/plan-format.md`. Three to four items, each with a
starting gate. Three or four benched, each with its reason.

## Gates are starting gates

This is the part most likely to be got wrong, so here is the reasoning rather than a rule.

The obvious design is a completion gate — *done when the feature works*. It aims at the wrong
moment. Abandonment happens in the first twenty minutes, when a task turns uncomfortable and
something else looks more interesting. A completion gate cannot see that; it arrives hours
later and reports what they already know.

A starting gate proves the work was **started and engaged with**. It is achievable inside the
session that set it, so the first win lands before the drift window opens.

Two constraints make it work:

**It must be checkable without a judgement call.** Either an artifact exists, or a time box
was spent. Never "made good progress" — that is an opinion, and assessing the quality of
someone's work is not this skill's job.

**It must be the smallest thing that cannot be done without actually engaging.** Cloning a
repo is theatre. Writing the first function signature is not. Opening a paper is theatre;
writing one line about what it said is not.

Gates get revised once they're inside the task and know what it involves — expected, not a
miss. For items being done *with Claude*, that revision happens naturally in the working
session. For solo items, they revise it themselves or it waits for clock-out. Don't introduce
a mid-day check-in to catch this; the quiet day is deliberate.

For genuinely straightforward tasks, several confident gates up front are fine.

## Clock out

Short. Record what happened, and ask **one** question, only when there is one worth asking:

> What did today teach you about the plan?

Not *why didn't you finish*. The difference is accuracy, not politeness. A plan that changed
because the work taught them something is the plan working, and only this framing tells that
apart from drift. It also gets the honest answer in their words — "I got interested in
something else" is a real reply to that question, and them saying it beats you pointing it out.

If the day went to plan, say so and write it down. No question needed.

Then record the plan-versus-actual somewhere that accumulates. That running record is the
only evidence of whether this skill is working at all — without it, any claim that it helps
is self-certified.

**A missed clock-out is reckoned by the next morning's clock-in**: one question about
yesterday, then today's plan. Never chase them in the evening — there is no reliable signal
that a day has ended, and guessing wrong is exactly the overhead this must not become.

## What this skill will not do

- **Decide their day.** It interviews, shows the cost, and transcribes. They choose.
- **Judge whether the work was good.** Gates are checkable facts, not assessments.
- **Cross a project boundary.** Where a project governs its own records, plan the block —
  "2h on the training script" — never write that project's findings or decisions elsewhere.
- **Fire without asking.** It offers. It never activates itself.
- **Nag.** One offer per session, dropped on a no.
- **Insist on a plan.** "Nothing today" is a legitimate answer.
