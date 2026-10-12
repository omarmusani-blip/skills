# skills

Agent skills for [Claude Code](https://claude.com/claude-code), grouped into families. Each
skill is a folder with a `SKILL.md` (when to fire, what to do) plus the references and
scripts it loads on demand, so the model only pays for the detail when the skill runs.

| Family | Skill | What it does |
|---|---|---|
| **career** | [application-writing](career/application-writing) | Drafts application prose inside a hard evidence boundary, audits discourse structure (the durable AI fingerprint), and runs a counting checker instead of judging by feel |
| | [dragons-den](career/dragons-den) | Five isolated reviewer agents from the target employer read a CV or essay in parallel; their claims are verified against the document before being distilled into edits, dissent and open questions |
| **workflow** | [clock-in](workflow/clock-in) | Bookends a working day: an interview that produces a plan with *starting* gates, silence during the day, and a reckoning at the end |
| | [grill-me](workflow/grill-me) | Walks a plan's decision tree one question at a time, with a recommended answer for each, before anything gets built |
| **learning** | class-is-in-session | Tutoring mode where the point is the learner's understanding, not the output. Lives in the screen-tutor project for now |

## Install

Skills load from `~/.claude/skills/<name>/`, so clone once and link the ones you want:

```bash
git clone https://github.com/omarmusani-blip/skills.git ~/skills

# macOS / Linux
ln -s ~/skills/career/dragons-den ~/.claude/skills/dragons-den

# Windows (a junction needs no admin rights)
mklink /J "%USERPROFILE%\.claude\skills\dragons-den" "%USERPROFILE%\skills\career\dragons-den"
```

Skills with personal setup ship a `references/context.example.md`. Copy it to
`context.md` and fill it in; `context.md` is gitignored everywhere in this repo.

## Credits

- `grill-me` is adapted from [Matt Pocock's `grilling`](https://github.com/mattpocock/skills) (MIT).
- Also worth using, not redistributed here: [YK Sugi's `handoff`](https://github.com/ykdojo/claude-code-tips/tree/main/skills/handoff),
  which writes a state document so a fresh session can pick up mid-task.

## Licence

MIT, per skill folder.
