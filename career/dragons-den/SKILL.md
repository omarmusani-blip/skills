---
name: dragons-den
description: Runs a mock review panel on a CV, cover letter, application essay or short answer — five in-character reviewers from the target employer (screener, hiring manager, technical interviewer, adjacent-team lead, former intern) read it in parallel and talk about it candidly as if the candidate weren't in the room, then the panel's views are distilled into consensus changes, honest dissent, and the questions only the candidate can answer. Use this whenever the user says "dragons den", "mock panel", "have recruiters review this", "what would the hiring manager think", "pressure-test my CV/essay", or asks for feedback from the employer's point of view on any application document — and offer it proactively once a tailored CV or essay for a specific posting is drafted and before it is submitted.
---

# Dragons' Den

A tailored application gets read by several different people at the employer, each looking
for something different: the screener checks boxes in thirty seconds, the hiring manager
asks whether you'd be useful in week one, the technical interviewer reads every claim as
something to probe. A single reviewer — or Claude reviewing its own draft — collapses all of
that into one generic voice. The panel keeps the voices separate, so the feedback disagrees
with itself the way real feedback does, and the disagreements are where the useful
decisions are.

Read `references/context.md` first if it exists. It holds the user's own setup: where their
evidence lives, what is already known to be true or false about them, how their CVs are
built. Without it, gather the same things by asking.

## 1. Gather the inputs

You need four things before casting anyone. Missing any of them makes the panel guess, and
a guessing panel invents.

- **The document(s)** — a file path each reviewer can read. CV, essay, cover letter, or a
  short answer with its exact prompt. If it is LaTeX, tell reviewers to judge the rendered
  text and ignore `%` comments (those are private working notes).
- **The target** — the posting text, saved to a file, with the exact line range for this
  role if the file holds several. Reviewers should read the real posting, not a summary of
  it; summaries drop the phrases that matter (a "stand out" skill, an eligibility clause).
- **Known facts** — a short list of what is true and false about the candidate that bears on
  this application: tools never used, work deliberately cut and why, things that are in
  progress, constraints the candidate has set (page count, tone). This is the single most
  important input. Without it, reviewers confidently recommend adding things the candidate
  has never done.
- **What the candidate is unsure about** — the specific worry, if they've named one ("we
  seem under-qualified", "is the essay too bold?"). Point at least one reviewer at it.

## 2. Cast five reviewers for *this* employer

Default cast, specialised to the actual team named in the posting — read
`references/personas.md` for each persona's lens and how to adapt them:

1. **Screener / university recruiter** — 30-second skim, eligibility boxes, clarity to a
   reader from another country or field.
2. **Hiring manager** who owns this req — useful in week one? real or padded?
3. **Senior technical interviewer** in the team's discipline — terminology, overclaiming,
   what they'll probe.
4. **Adjacent lead** — whoever else the intern would work with (lab lead, tools engineer,
   customer-facing lead), chosen from what the posting says the job involves.
5. **Former intern, now junior staff** — what successful applicants had, how this compares
   with the real pool, what's memorable.

Name each one concretely ("hiring manager, Reliability and Statistics Department") — a
named seat produces specific feedback, a generic "hiring manager" produces generic feedback.
Swap a seat when the document calls for it (for an essay, the screener who reads 200 of
these beats a second technical seat).

## 3. Brief them and launch all five at once

Use the brief in `references/brief-template.md`. Launch the five as parallel general-purpose
agents in a single message — they are independent, and running them together means none
is anchored by another's opinion.

The rules every brief carries, and why:

- **Read-only.** Reviewers critique; only the main thread edits files.
- **Never suggest claiming what isn't done.** Suggest reframing, reordering, cutting, or
  something genuinely doable before the deadline — and anything new is listed only once
  it's real. An honest panel is worth more than a flattering CV that falls apart in
  interview.
- **Quote the exact line** before saying keep / cut / change. Vague feedback can't be acted
  on.
- **Speak to colleagues, not to the candidate.** Candour comes from the candidate not being
  in the room.
- **Word cap (~300–350).** Long reviews bury their one good point.

## 4. Check before you relay

Reviewers misread things — a LaTeX macro, a date, which project a metric belongs to. Before
passing any point on, check it against the document and the known facts. Drop or correct a
point that rests on a misreading rather than repeating it with the panel's authority. If a
reviewer recommends something that would need a claim the candidate can't make, it does not
reach the consensus list, however many reviewers said it.

## 5. Report in four parts

Open with one line saying all five are back, then:

**🎥 The room** — one short paragraph per reviewer, in their voice, as if overheard through
the meeting-room camera. Keep each one's sharpest point, not everything they said. Where
they disagree with each other, let it show.

**The changes** — the consensus edits: raised by two or more reviewers, or by one with an
obvious case, *and* needing no new fact from the candidate. Written so they can be applied
as-is.

**Where I disagree** — your honest dissent from the panel, with the reason (usually a phrase
in the posting the panel underweighted, or a known fact they didn't have). A panel is a
simulation of readers, not the readers; its majority isn't automatically right.

**What only you can answer** — numbered questions about facts, dates, or choices of taste
that decide the remaining edits. Ask only what changes the document.

Then stop. Apply the consensus batch and the answers together once the candidate replies —
one revision, not a trickle.

## Notes

- The panel works on any persuasive document aimed at a known reader: grant applications,
  pitch decks, a cold email. Recast the five seats as that reader's organisation.
- Running the panel again after a big revision is fine; running it after every small edit
  is not — the second panel mostly re-discovers the first one's points.
- Save the posting and the panel's raw output if the application is worth keeping a record
  of; the questions it raised tend to come back in the interview.
