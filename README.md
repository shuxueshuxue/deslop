<div align="center">

# deslop

**Strip the LLM tells out of prose.**

A [Claude Code](https://claude.ai/code) skill. Chinese and English.

</div>

---

LLM-written or LLM-polished prose carries tells. They are learnable, countable, and removable.

`deslop` audits a document against a marker taxonomy, produces a per-line kill list with plain
replacements, applies them, and re-measures two mechanical indicators plus a manual personification
count — so the result is verifiable rather than asserted.

## The thing most people get wrong

**AI flavor is not "plain, careful wording." Plain, careful wording is the target.**

AI flavor is the writer showing you how clever they are. Every marker below is one form of it — the
vivid analogy, the staged reversal, the punchy closer, the word picked because it sounds learned. They
all do the same job: prove the author is smart. It reads well line by line, which is exactly why it
survives editing.

The test for any sentence:

> Is this **saying the thing**, or **being clever**?

Humble and plain is the target. Sly and clever is the defect.

An editor who mistakes plainness for the problem sands the text into mush and misses every real tell.
The models to aim at are Wikipedia, Hacker News technical comments, and academic papers.

## Two checks that catch most of it

1. **Delete it — is any information lost?**
2. **If a reader asks "what specifically does this mean", can you answer with a fact?**

From the [nofluff](https://nofluff.0x01.me/nofluff.txt) standard, folded in as
`references/nofluff.md`. The tables below tell you where to look; these tell you whether the sentence
should exist. When they disagree, the checks win.

## What it catches

| | |
|---|---|
| **Action metaphor** | `接住每个事件` → `对每个事件创建一条记录` · `costs collapsed` → `costs fell` |
| **Personification** | `状态活不过一次调用` → `调用结束即失效` · `history reminds you` → `history does not indicate` |
| **Staged reversal** | `不是 X，是 Y` · `it's not x, it's y` — the single most reliable tell |
| **Dramatized closer** | a short assertion parked at a paragraph's end to leave an aftertaste |
| **Self-assessment** | `Naur 说得对` → `与 Naur 的结论一致` · `my honest take` → *(cut)* |
| **Em dashes** | counted, and checked for where they land |
| **Latching** | one vivid word reused across a document |
| **Elevated diction** | a rarer, more "professional"-sounding word where a common one exists — 判据 → 判定规则 · utilize → use |
| **Jargon** | 赛道 / 闭环 / 抓手 · load-bearing / key insight / synthesize |

## Install

```sh
git clone https://github.com/shuxueshuxue/deslop.git ~/.claude/skills/deslop
```

Then, in Claude Code:

```
/deslop  the README
/deslop  slides/talk.html — Chinese, conference audience
```

Or just say *"this sounds like AI, fix it"* — the skill's description matches that.

## The scanner

```sh
python3 scan.py --strip draft.md          # candidates, most frequent first
python3 scan.py --strip --lines draft.md  # one row per hit, with line numbers
python3 scan.py --lang zh draft.md        # one language only
```

```
count   term            category   replacement          note
5       leverage        vocab      use
1       不是历史，是     shape      (只说后半句)          对偶反转。计数指标。

# lexicon hits: 7  (2.9 per 1000 chars)
# staged reversal: 1
# em dash: 1
```

Candidate terms in `references/lexicon.tsv`, Chinese and English, each with a plain replacement. It reports
candidates and never rewrites: some entries are correct in context and say so in the note column.

Word choice is the half a script can do. A dramatized closer, a paragraph that ends by restating
itself, an analogy carrying no weight, a heading that narrates instead of naming — none of those are
lookups. Run the scanner for the worklist, then audit for what it cannot see.

## How it works

1. **Extract** the prose so the audit sees what a reader sees, not the markup.
2. **Scan** for lexicon hits — the cheap mechanical pass.
3. **Audit** line by line, in a **fresh-context subagent**. Self-auditing prose you just wrote does
   not work: you re-read your own intent instead of the words on the page.
4. **Count** staged reversals and em dashes mechanically; count personification in the audit table.
5. **Apply** the literal denotation. Never swap one vivid word for another vivid word.
6. **Re-measure** and report both numbers.

`reversals 12 → 0` is evidence. *"now it reads naturally"* is not.

## What it will not do

**It does not flatten terms of art.** If a mechanism is literally named *drift*, then "spec drift" is
the term, not a metaphor. Same for *anchor*, *warm cache*, *starvation*, *back-pressure*. Flattening
those makes text read as though the author does not know the field — worse than leaving a tell.

**It does not edit arguments.** It restates sentences. Restructuring, cutting sections, and changing
claims need the author's sign-off.

**It does not check whether the text is right.** Register and comprehension are different defects. A
document can be perfectly plain and still contain a dangling pronoun, a contradiction between two
pages, or a misread citation. See [`references/worked-example.md`](references/worked-example.md) for a
case where all three existed alongside the register problems.

## Files

```
SKILL.md                        the skill
scan.py                         the scanner (python3, no dependencies)
references/lexicon.tsv          candidate terms, zh + en, with replacements and false-positive notes
references/markers-zh.md        Chinese taxonomy, eight categories
references/markers-en.md        English markers, sourced to HN 48905248
references/titles.md            headings: name the content, don't narrate the reading path
references/nofluff.md           the nofluff standard's two checks, and what it adds
references/worked-example.md    a real audit: 45 findings, 12/10/14 → 0/0/0
```

## Credit

The two checks and four of the rules come from the [nofluff](https://nofluff.0x01.me/nofluff.txt)
writing standard.


The English marker list draws on the Hacker News thread cataloguing "claudish"
([48905248](https://news.ycombinator.com/item?id=48905248)), where readers named the specific words
and sentence shapes. Quotes are attributed in `references/markers-en.md`.

The lexicon is assembled from four kinds of source, and the difference matters — a measured word list
and a curated one fail differently:

- **Measured.** Kobak, González-Márquez, Horvát & Lause, [*Delving into LLM-assisted writing in
  biomedical publications through excess vocabulary*](https://www.science.org/doi/10.1126/sciadv.adt3813)
  (Science Advances 11(27), 2025) — word frequencies in 14M PubMed abstracts before and after
  ChatGPT. Also Juzek & Ward, [*Why Does ChatGPT "Delve" So Much?*](https://arxiv.org/abs/2412.11385) (ACL 2025).
- **Curated with a citation bar.** Wikipedia's
  [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (WP:AIVOCAB) —
  a word is only listed there if its overuse is corroborated by an outside source. It also tracks
  which words belong to which model era, and warns that a word being overused does not make its
  synonyms suspect.
- **Curated by practitioners.** The Chinese lists come from
  [ninehills/public-skills](https://github.com/ninehills/public-skills) (MIT, via
  [nmhjklnm/skills](https://github.com/nmhjklnm/skills)) — the jargon two-tier list, the
  paragraph-closing summary tell, the translationese verb list.
- **Observed.** Entries added from real audits, marked in the note column.

## License

MIT
