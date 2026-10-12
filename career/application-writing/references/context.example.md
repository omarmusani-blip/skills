# Context — your setup

Copy to `context.md` (gitignored) and fill in. The skill reads it before every draft.

## Who writes what

Any change to the default split in `SKILL.md` step 0, e.g. "I always write the opening
line myself".

## Where the evidence lives

- Notes folder: `<path>`
- Experience record: `<file listing what you've actually done, in progress, and excluded>`
- CV / resume sources: `<path>`
- Per-application notes: `<path or naming convention>`

## Checker

```bash
python "<path to this skill>/scripts/check.py" <file>
```

## ★ answers

```bash
grep -rn "★" --include="*.md" "<notes folder>"
```

## Standing corpus

Files, or parts of files, confirmed as your own unedited writing. Say which columns or
passages count and which were drafted by an assistant.

## Voice profile

Built from the corpus, then confirmed by you: sentence length and variance, openers,
hedges, punctuation habits, how you emphasise, your strongest register.

## Known preferences

Rules that came out of real corrections, dated, with the reason.
