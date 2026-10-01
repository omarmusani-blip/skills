# dragons-den

A [Claude Code](https://claude.com/claude-code) skill that puts your CV, cover letter or
application essay in front of a mock panel from the company you're applying to: five
reviewers who read it at the same time and talk about it candidly, as if you weren't in the
room. Then it turns what they said into the changes to make, where it thinks they're wrong,
and the questions only you can answer.

## The problem it solves

When you ask an AI to review your CV, you get one voice: polite, generic, and usually a
little too pleased with the draft it helped write. Real applications aren't read by one
person. A recruiter skims for eligibility in thirty seconds. The hiring manager wants to
know if you'd be useful in week one. The technical interviewer reads every claim as
something they're going to ask you about. Those people want different things, and they'd
disagree with each other.

So the skill keeps them apart. Each reviewer is a separate agent with one lens, given the
real job posting and your document, and none of them sees what the others said.

## How a run goes

1. **Inputs.** Your document, the actual posting text, and a short list of **known facts**
   (tools you haven't used, things you cut on purpose, work that's still in progress). The
   known facts are what stop the panel from telling you to add things you've never done.
2. **Casting.** Five seats, specialised to the team in the posting: screener, hiring
   manager, senior technical interviewer, an adjacent lead (lab, tools, customer-facing,
   data, whatever fits the job), and a former intern who now helps screen.
3. **Review.** All five run in parallel, read-only, under ~350 words each, quoting the exact
   line before saying keep, cut or change.
4. **Check.** Before anything gets passed on, it's checked against your document: reviewers
   misread things, and a misreading shouldn't arrive with the panel's authority.
5. **Report.**
   - 🎥 **The room**: each reviewer's sharpest point, in their own voice.
   - **The changes**: the consensus edits that need no new facts from you.
   - **Where I disagree**: honest dissent from the panel, with reasons.
   - **What only you can answer**: the questions that decide the rest.

You answer, and the edits go in as one revision.

## The one rule

**The panel never suggests claiming something you haven't done.** It can suggest
reframing, reordering, cutting, or something you could genuinely do before you apply, and
then you list it only once it's done. A CV that only looks stronger falls apart in the
interview.

## Install

```bash
git clone https://github.com/omarmusani-blip/dragons-den.git ~/.claude/skills/dragons-den
cd ~/.claude/skills/dragons-den
cp references/context.example.md references/context.md
```

Fill in `references/context.md` with where your evidence lives and anything every reviewer
should know about you. It's gitignored, since it holds personal details.

## Use

Say `dragons den` (or "mock panel", or "what would the hiring manager think of this") with a
document and a posting. It'll also offer itself once a tailored CV or essay is drafted and
before you submit.

It's built for job applications, but anything persuasive aimed at a known reader works:
grant applications, a pitch deck, a cold email. Recast the five seats as that reader's
organisation.

## What it won't do

- Edit your files before you've answered its questions
- Treat the panel's majority as automatically right
- Invent experience, metrics or skills to fill a gap

## Licence

MIT, see [LICENSE](LICENSE).
