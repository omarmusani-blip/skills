# What the checker flags, and how much to trust each one

Run: `python scripts/check.py <file>` (add `--em-cap N` to loosen the em-dash cap).

The checker counts; it does not judge. A flag means look, not fix. Roughly half of
what it raises will be correct as written, and forcing every flag to zero produces
prose that is uniformly odd instead of uniformly bland — a different tell, not an
improvement.

## Hard signals — usually act on these

**Low sentence-length variance (stdev under 5).** The single most measurable AI
marker. Human prose swings between 4-word sentences and 40-word ones. Fix by merging
two short sentences with a subordinate clause, or splitting a long one, not by
paraphrasing.

**Runs of three near-identical lengths.** Same cause, local version.

**Parataxis** — more than half the sentences at eight words or fewer. Short sentence.
Then another. Then another. Reads like a poem and signals AI immediately. Connect
related thoughts so the syntax shows how they relate: causation, contrast,
qualification.

**Banned words and phrases.** Statistically flagged across several studies. The
application-specific ones matter most because a recruiter has read them 500 times:
*I am writing to express my interest*, *passionate about*, *aligns perfectly*, *I am
excited about the opportunity*, *I hope this finds you well*.

**Credential opener.** "As a second-year Mechanical Engineering student, I..." wastes
the one sentence a skimmer certainly reads, and announces status instead of content.

**"Not just X, but Y."** Negative parallelism. Heavily flagged, and it usually hides a
weak claim: cut the "not just" half and see whether the rest still says anything.

**Agentive passive** — "the analysis was run by me". On an application this actively
buries the thing the reader is looking for, which is who did the work.

**Consecutive sentences with the same opening word.** Especially "I". A letter where
six sentences start with "I" reads as a list of assertions rather than an argument.

## Soft signals — judgement required

**Em-dash density.** The most cited surface tell, and the most over-corrected. The cap
is provisional: set it from the writer's own clean prose (see `voice.md`), never from a
sample that may contain assistant-drafted text.
Zero em dashes is its own tell. An em dash in a CV heading is typography, not voice.

**Long sentences.** Only flagged hard when variance is *also* poor. Long and uniform is
the bad combination; long and varied is a person with something to say. Plenty of writers'
prose averages above 30 words a sentence with healthy variance, and flattening that
would remove the thing that makes it theirs.

**Passive voice.** Keep it where the actor is genuinely unknown or irrelevant, or where
the convention expects it — a lab method section, for instance. The repo that tested
this had to add a regression guard protecting *earned* passive voice from its own
blanket rule.

**Rule of three.** One list of three is fine. Three lists of three is a fingerprint.

**Contractions, semicolons, markdown.** Advisory. No contractions is normal in a formal
letter. No semicolons in 400 words suggests a narrow range. Markdown bold and headers
must come out before pasting into a plain-text form.

## What the checker cannot see

It has no opinion on whether the writing is *good*, whether a claim is true, or whether
it sounds like the writer. It counts surface features, which is the small half of the problem
— structure is the durable fingerprint and a script cannot measure it.

The structural audits in `SKILL.md` step 2 are the half that matters, and they need
reading, not running. So does the evidence boundary in step 1. A draft that scores zero
flags and claims something the applicant cannot defend in an interview has failed completely
while passing every test here.
