#!/usr/bin/env python3
"""Mechanical AI-tell checker for application prose.

Counts what can be counted. Judging your own prose for AI-ness is circular;
counting is not. Nothing here is a verdict -- flags are prompts to look.

Usage:  python check.py <file> [file2 ...]
        cat draft.txt | python check.py -
"""

import re
import sys
import statistics
from pathlib import Path

# ---------------------------------------------------------------------------
# Editable lists. Add to these as real tells turn up in real drafts.
# ---------------------------------------------------------------------------

BANNED_WORDS = """
delve delves delving tapestry testament vibrant pivotal crucial intricate
intricacies meticulous meticulously bolster bolstered garner garnered
underscore underscores interplay multifaceted foster fostering leverage
leveraging utilize utilise commence facilitate encompass encompassing
paramount groundbreaking cutting-edge game-changing transformative
seamless seamlessly endeavour endeavor aforementioned harnessing landscape
spearheading showcasing unprecedented remarkable profound synergy synergies
""".split()

BANNED_PHRASES = [
    "in today's", "it's worth noting", "it is worth noting",
    "it's important to note", "it is important to note",
    "at its core", "in the realm of", "when it comes to", "a testament to",
    "not just", "this is where", "whether you're", "at the end of the day",
    "the bottom line", "here's the thing", "in a nutshell", "in conclusion",
    "i hope this finds you well", "i hope this email finds you well",
    "please don't hesitate", "please do not hesitate",
    "i am excited about the opportunity",
    "i am writing to express my interest",
    "aligns perfectly", "aligns seamlessly", "align perfectly",
    "passionate about", "deep dive", "move the needle", "bridge the gap",
    "take it to the next level", "unlock the", "elevate your",
    "streamline your", "as per my last email", "thought leader",
    "pain points", "value proposition", "moving forward", "touch base",
    "circle back", "rest assured", "it goes without saying",
]

BANNED_OPENERS = [
    "certainly", "absolutely", "sure", "moreover", "furthermore",
    "additionally", "interestingly", "notably", "importantly", "indeed",
    "overall", "firstly", "secondly", "thirdly", "ultimately",
]

CONTRACTIONS = re.compile(
    r"\b\w+'(?:s|t|re|ve|ll|d|m)\b|\bcan't\b|\bwon't\b|\bdon't\b", re.I)

# "was/were/is/are/been/being + past participle" -- an estimate, not a parser.
PASSIVE = re.compile(
    r"\b(?:is|are|was|were|be|been|being)\s+(?:\w+ly\s+)?(\w+(?:ed|en|wn|ne))\b", re.I)

CREDENTIAL_OPENER = re.compile(
    r"^\s*(?:As\s+(?:a|an|the)\s+[^,]{3,60},)", re.I)

# Em dashes allowed per 500 words. Provisional: the intended way to set this is
# from the writer's own clean prose, never from assistant-drafted text.
# Override per-run with --em-cap.
EM_CAP = 1.5


def sentences(text):
    """Split into sentences. Crude but stable: protects common abbreviations."""
    protected = text
    for abbr in ["e.g.", "i.e.", "etc.", "Dr.", "Mr.", "Mrs.", "Ms.", "vs.",
                 "Ltd.", "Inc.", "No.", "Fig.", "approx."]:
        protected = protected.replace(abbr, abbr.replace(".", "\x00"))
    parts = re.split(r"(?<=[.!?])[\"')\]]*\s+", protected)
    out = []
    for p in parts:
        p = p.replace("\x00", ".").strip()
        if p:
            out.append(p)
    return out


def words(s):
    return re.findall(r"\b[\w'-]+\b", s)


def line_of(text, index):
    return text.count("\n", 0, index) + 1


def check(text, label):
    report = []
    flag_count = 0

    def add(level, msg):
        nonlocal flag_count
        if level == "FLAG":
            flag_count += 1
        report.append("  [%-4s] %s" % (level, msg))

    all_words = words(text)
    wc = len(all_words)
    sents = sentences(text)
    lengths = [len(words(s)) for s in sents if words(s)]

    report.append("=" * 72)
    report.append("%s  --  %d words, %d sentences" % (label, wc, len(sents)))
    report.append("=" * 72)

    if not lengths:
        report.append("  (no prose found)")
        return "\n".join(report), 0

    # ---- rhythm -----------------------------------------------------------
    report.append("")
    report.append("RHYTHM")
    mean = statistics.mean(lengths)
    sd = statistics.pstdev(lengths) if len(lengths) > 1 else 0.0
    report.append("  mean sentence %.1f words, stdev %.1f, range %d-%d"
                  % (mean, sd, min(lengths), max(lengths)))
    if sd < 5 and len(lengths) >= 4:
        add("FLAG", "low variance (stdev %.1f): uniform sentence length is the "
                    "single most measurable AI signal. Aim above 6." % sd)
    else:
        add("ok", "sentence-length variance acceptable")

    runs = []
    i = 0
    while i < len(lengths) - 2:
        window = lengths[i:i + 3]
        if max(window) - min(window) <= 2:
            runs.append((i + 1, window))
            i += 3
        else:
            i += 1
    if runs:
        add("FLAG", "%d run(s) of 3 near-identical sentence lengths, starting at "
                    "sentence %s" % (len(runs), ", ".join(str(r[0]) for r in runs[:6])))
    else:
        add("ok", "no runs of three same-length sentences")

    # A long sentence is only a tell in prose with no rhythm. Plenty of human writing
    # runs long and subordinate-clause-heavy on purpose, and flattening that is
    # exactly the blanket-ban failure this checker exists to avoid. So the
    # threshold is conditional: hard flag only when variance is already poor.
    long_s = [(n + 1, L) for n, L in enumerate(lengths) if L > 35]
    if long_s and sd < 8:
        add("FLAG", "sentence(s) over 35 words in low-variance prose: %s -- long "
                    "AND uniform is the bad combination"
            % ", ".join("#%d (%dw)" % (n, L) for n, L in long_s[:6]))
    elif long_s:
        add("note", "long sentence(s): %s. Fine in prose with this much variance "
                    "(stdev %.1f) -- check each carries its length."
            % (", ".join("#%d (%dw)" % (n, L) for n, L in long_s[:6]), sd))
    else:
        add("ok", "no over-long sentences")

    short_run = sum(1 for L in lengths if L <= 8)
    if len(lengths) >= 5 and short_run / len(lengths) > 0.5:
        add("FLAG", "%d of %d sentences are 8 words or fewer: parataxis (chained "
                    "short declaratives) reads as AI. Connect some with clauses."
            % (short_run, len(lengths)))

    # ---- punctuation ------------------------------------------------------
    report.append("")
    report.append("PUNCTUATION")
    em = len(re.findall(r"—|\s---?\s", text))
    per500 = em / wc * 500 if wc else 0
    report.append("  em dashes: %d (%.1f per 500 words, cap %.1f)"
                  % (em, per500, EM_CAP))
    if per500 > EM_CAP:
        add("FLAG", "em-dash density %.1f per 500 words, over the %.1f cap. The most "
                    "cited surface tell; use commas, colons, or a new sentence. "
                    "Raise with --em-cap if this register earns them." % (per500, EM_CAP))
    else:
        add("ok", "em-dash density within cap")

    excl = text.count("!")
    if excl > max(1, wc // 1000):
        add("FLAG", "%d exclamation marks: enthusiasm should come from word choice" % excl)

    semis = text.count(";")
    if semis == 0 and wc > 250:
        add("note", "no semicolons: good writers use them, AI underuses them")

    ell = len(re.findall(r"\.\.\.|…", text))
    if ell > 1:
        add("FLAG", "%d ellipses: only for genuinely trailing off, never as transition" % ell)

    # ---- vocabulary -------------------------------------------------------
    report.append("")
    report.append("VOCABULARY")
    hits = []
    low = text.lower()
    for w in BANNED_WORDS:
        for m in re.finditer(r"\b" + re.escape(w) + r"\b", low):
            hits.append((line_of(text, m.start()), w))
    for p in BANNED_PHRASES:
        start = 0
        while True:
            idx = low.find(p, start)
            if idx == -1:
                break
            hits.append((line_of(text, idx), p))
            start = idx + 1
    if hits:
        seen = set()
        for ln, h in sorted(hits):
            if (ln, h) in seen:
                continue
            seen.add((ln, h))
            add("FLAG", "line %d: \"%s\"" % (ln, h))
    else:
        add("ok", "no banned words or phrases")

    # ---- structure --------------------------------------------------------
    report.append("")
    report.append("STRUCTURE")
    openers = {}
    for n, s in enumerate(sents):
        w = words(s)
        if w:
            openers.setdefault(w[0].lower(), []).append(n + 1)
    repeated = {k: v for k, v in openers.items() if len(v) > 1 and k not in
                ("the", "a", "i") or (k == "i" and len(v) > 3)}
    consecutive = []
    prev = None
    for n, s in enumerate(sents):
        w = words(s)
        first = w[0].lower() if w else None
        if first and first == prev:
            consecutive.append(n + 1)
        prev = first
    if consecutive:
        add("FLAG", "consecutive sentences starting with the same word at: %s"
            % ", ".join(map(str, consecutive[:8])))
    else:
        add("ok", "no consecutive repeated openers")

    for k, v in sorted(repeated.items(), key=lambda x: -len(x[1]))[:3]:
        if len(v) >= 3:
            add("note", "\"%s\" opens %d sentences (%s)" % (k, len(v),
                ", ".join(map(str, v[:8]))))

    bad_open = [(n + 1, words(s)[0]) for n, s in enumerate(sents)
                if words(s) and words(s)[0].lower() in BANNED_OPENERS]
    if bad_open:
        add("FLAG", "AI-signature opener(s): %s"
            % ", ".join("#%d \"%s\"" % (n, w) for n, w in bad_open[:6]))

    if CREDENTIAL_OPENER.search(text):
        add("FLAG", "opens by announcing credentials (\"As a ...,\"). Say the thing "
                    "instead; this wastes the one line a skimmer reads.")

    triples = re.findall(r"\b\w+(?:\s\w+)?,\s\w+(?:\s\w+)?,?\s+and\s+\w+", text)
    if len(triples) >= 2:
        add("FLAG", "%d rule-of-three list(s): AI defaults to threes. Use two or "
                    "four unless the content really has three." % len(triples))
    elif triples:
        add("note", "1 rule-of-three list -- fine unless it repeats")

    neg_par = len(re.findall(r"not (?:just|only|merely|simply)\b[^.]{0,80}\bbut\b",
                             low))
    if neg_par:
        add("FLAG", "%d \"not just X but Y\" construction(s): heavily AI-flagged" % neg_par)

    # ---- voice ------------------------------------------------------------
    report.append("")
    report.append("VOICE")
    con = len(CONTRACTIONS.findall(text))
    report.append("  contractions: %d" % con)
    if con == 0 and wc > 200:
        add("note", "no contractions: acceptable in a formal letter, but it is the "
                    "default register of generated text")

    passives = PASSIVE.findall(text)
    pr = len(passives) / max(1, len(sents))
    report.append("  passive-voice estimate: %d (%.2f per sentence)" % (len(passives), pr))
    if pr > 0.4:
        add("FLAG", "passive voice in roughly %.0f%% of sentences. Keep the earned "
                    "ones; rewrite the rest with the doer as subject." % (pr * 100))
    else:
        add("ok", "passive voice within range")

    # An agentive passive names its own doer, so it is almost always rewritable --
    # and on an application it actively hides who did the work, which is the one
    # thing the reader is trying to find out.
    agentive = re.findall(
        r"\b(?:is|are|was|were|be|been|being)\s+(?:\w+ly\s+)?\w+(?:ed|en|wn)\s+by\s+"
        r"(\w[\w'-]*)", text, re.I)
    if agentive:
        add("FLAG", "%d agentive passive(s) (\"... by %s\"): put the doer first -- on "
                    "an application, burying who did it works against you"
            % (len(agentive), agentive[0]))

    md = len(re.findall(r"^\s*#{1,6}\s|\*\*[^*]+\*\*", text, re.M))
    if md:
        add("note", "%d markdown header/bold marker(s): remove before pasting into a "
                    "plain-text form or email" % md)

    report.append("")
    report.append("  %d flag(s) to look at." % flag_count)
    return "\n".join(report), flag_count


def main():
    global EM_CAP
    args = sys.argv[1:]
    if "--em-cap" in args:
        i = args.index("--em-cap")
        try:
            EM_CAP = float(args[i + 1])
        except (IndexError, ValueError):
            print("--em-cap needs a number, e.g. --em-cap 3")
            return 2
        del args[i:i + 2]
    if not args:
        print(__doc__)
        return 2
    total = 0
    for a in args:
        if a == "-":
            text, label = sys.stdin.read(), "<stdin>"
        else:
            p = Path(a)
            if not p.is_file():
                print("skip (not a file): %s" % a)
                continue
            text, label = p.read_text(encoding="utf-8", errors="replace"), p.name
        out, flags = check(text, label)
        print(out)
        print()
        total += flags
    return 1 if total else 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    sys.exit(main())
