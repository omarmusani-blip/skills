# Context — fill this in

Copy this file to `context.md` in the same directory and replace the bracketed parts.
`context.md` is gitignored, because it holds real paths, real project names, and sometimes
notes about how a particular person works.

The skill reads this at clock-in. Without it, it has nothing to read from.

## Paths

**Notes / task file root:**
`[absolute path to the vault, notes directory, or wherever the task file lives]`

**Task file:** `[e.g. Tasks.md]` — the file the plan is written into. Name the sections:

- `[## Today — <date>]` — the dated heading, rewritten each clock-in
- `[## Done this week]` — appended at clock-out
- `[## Focus log]` — where plan-versus-actual accumulates; never cleared
- `[## A good day]` — a standing time shape, if they keep one. Treat it as a target to
  measure against, **not** an assumption about available hours.

## The four inputs, in order of authority

### 1. What matters — the board

`[Where the authoritative list of live threads lives — a workstream table, a project board,
a list of goals. Say which file and which section, and note anything about how it is ordered.]`

This is the agenda and it is authoritative. Don't invent a ranking mechanism beside it.

### 2. What is fixed today

`[Timetable file, if any. Note anything conditional about it — alternating weeks, rotating
groups, sessions that only run some weeks. A conditional entry is a candidate, not a fact.]`

`[Deadline sources — frontmatter fields, saved views, a calendar file.]`

`[Meetings and one-off dated things — where they live.]`

If they also keep a calendar in an external service, say so here, and note that it **cannot
be read**. That is exactly why clock-in asks "anything fixed today the notes don't know
about?" rather than treating the local calendar layer as complete.

### 3. Where attention actually went — the divergence check

`[How to see recent activity. For Obsidian: open tabs live in .obsidian/workspace.json —
walk the leaf nodes for state.state.file. Also: modification times on note files, excluding
.git and any plugin cache directories.]`

Two limits on this signal, both of which should temper how hard the divergence is stated:

- **It only sees what it can see.** Work in other repos, other applications, or offline
  leaves no trace. A thread that looks cold may simply be worked on elsewhere.
- **A tab left open is not attention.** Finished work sits open for days.

So the divergence is a question worth asking, never a conclusion worth asserting.

### 4. Work that lives outside these paths

`[List the projects that have their own home — repos, other tools, coursework. Include any
hard deadlines, because a plan that can only see the notes directory will miss them.]`

Plan blocks of time against these freely. **Don't write their substance into the notes
directory** where a project governs its own records — "2h on the training script" is a task
line; what the session concluded about the model is not.

## Anything else worth knowing

`[Optional. How this person works, what has failed before, preferences that should shape the
interview. Keep it to things that change what the skill does — this file is loaded every
clock-in, so it earns its length or it gets cut.]`
