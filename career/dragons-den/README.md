# dragons-den

A mock review panel from the employer you're applying to. Five reviewers read your CV,
cover letter or essay in parallel and talk about it candidly, as if you weren't in the room.

## Why a panel

Ask one model to review a CV and you get one voice: polite, generic, and a little too
pleased with a draft it may have helped write. Real applications are read by people who
want different things. A screener checks eligibility in thirty seconds. A hiring manager
asks whether you'd be useful in week one. A technical interviewer reads every claim as a
question they'll ask you. Those readers disagree, and the disagreement is the signal.

So each reviewer is a separate agent with one lens, the real posting, and your document,
and none of them sees the others' output. Independence is what stops the panel from
collapsing into one averaged opinion.

## Pipeline

1. **Inputs:** the document, the posting text, and a list of **known facts** (tools you
   haven't used, things cut on purpose, work in progress). Known facts stop reviewers from
   recommending things you've never done.
2. **Casting:** screener, hiring manager, senior technical interviewer, an adjacent lead
   specialised to the posting's team, and a former intern who now helps screen.
3. **Review:** parallel, read-only, about 350 words each, quoting the exact line before
   saying keep, cut or change.
4. **Verification:** every reviewer claim is checked against the document before it's
   reported. Reviewers misread, and a misreading shouldn't arrive with the panel's authority.
5. **Report:** the room (each reviewer's sharpest point, in their voice), consensus edits
   that need no new facts, dissent where the panel is wrong, and the questions only you
   can answer. You answer; the edits go in as one revision.

**Hard rule:** the panel never suggests claiming something you haven't done. Reframe,
reorder, cut, or do the thing first and list it afterwards.

Works for anything persuasive with a known reader: grant applications, pitch decks, cold
email. Recast the five seats as that reader's organisation.

## Setup

```bash
cp references/context.example.md references/context.md
```

Say where your evidence lives and what every reviewer should know. Gitignored.
Trigger: "dragons den", "mock panel", or "what would the hiring manager think".

## Licence

MIT, see [LICENSE](LICENSE).
