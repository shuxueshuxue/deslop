---
name: deslop
description: >-
  Strip the LLM tells out of prose. Use when text needs to read as written by a person — a talk,
  a README, a design doc, release notes, a paper — or when someone says it "sounds like AI",
  "sounds like marketing", or asks to make it plainer. Audits the text against a marker taxonomy,
  produces a per-line kill list with plain replacements, applies them, and re-measures three
  countable indicators so the result is verifiable rather than asserted. Chinese and English.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, Agent
---

# deslop

Prose written or polished by an LLM carries tells. They are learnable, countable, and removable.

## The one thing to get right first

**AI flavor is not "plain, careful wording." Plain, careful wording is the target.**

AI flavor is the writer showing you how clever they are. Every marker in the taxonomy is one form
of it: the vivid analogy, the staged reversal, the punchy closer, the word picked because it sounds
learned. They all do the same job — prove the author is smart. It reads well line by line, which is
exactly why it survives editing. The test for any sentence:

> Is this **saying the thing**, or **being clever**?

Humble and plain is the target. Sly and clever is the defect.

A writer who mistakes "plain" for "the problem" will sand the text into mush and miss every real tell.
Aim at Wikipedia, Hacker News technical comments, and academic papers: direct, unadorned, specific.

Plain is also not colloquial. `references/markers-zh.md` opens with a register anchor for Chinese —
the dubbing register of Japanese films — that pins the target between written and spoken language.
Read it before editing Chinese text; overshooting into casual speech is as wrong as posturing.

## Two checks that catch most of it

Before working through the taxonomy, run every sentence past these:

1. **Delete it — is any information lost?** If not, delete it.
2. **If a reader asks "what specifically does this mean", can you answer with a fact?** If not, it is
   filler.

These come from the nofluff standard (`references/nofluff.md`), which also supplies four rules the
marker tables do not: do not stress what no reader would misread; delete rather than patch; do not
substitute intensity for argument; coining a term usually means the thinking is not finished.

The tables tell you where to look. These two checks tell you whether it should exist at all. When they
disagree, the checks win.

## Procedure

1. **Extract the prose.** Strip markup so you audit what a reader actually sees, not the source.
2. **Audit.** Go line by line against `references/markers-zh.md` (Chinese) or `references/markers-en.md`
   (English), and every heading against `references/titles.md`. Produce a table, one row per hit:

   | location | verbatim sentence | category | why it is performance, not statement | plain replacement |

   Over-report. Mark uncertain hits `?` rather than dropping them.
3. **Count three indicators** before and after. These are the falsifiable part:
   - staged reversals (`it's not X, it's Y` / `不是 X，是 Y`)
   - em dashes (`—` / `——`)
   - personification (abstract subject performing a human or biological action)
4. **Apply.** Replace with the literal denotation. Never swap one vivid word for another vivid word.
5. **Re-read for over-correction.** This is a separate pass, not a note to keep in mind — skipping it
   is the most common way a deslop run makes text worse. Check every replacement you just made:
   - Did a written word become a spoken one? (`判据` → `怎么判`, `触发源` → `触发的地方`)
   - Did a two-syllable verb become one syllable? Chinese written register prefers two.
   - Did a heading become a casual question? Headings sit further toward written register than body.

   If a sentence now sounds like conversation rather than a document, put it back and pick a
   *common* word instead of a *spoken* one. The target is common, not casual.
6. **Re-measure and report both numbers.** "Reversals 12 → 0" is evidence; "now it reads naturally" is not.

For a document of any size, run step 2 in a **fresh-context subagent**. Self-auditing prose you just
wrote does not work — you re-read your own intent instead of the words on the page. Hand the subagent
the extracted text and the marker file, and demand the table.

## The false-positive that matters

Domain terms often look vivid. **Do not flatten a term of art.**

If a project's mechanism is literally named *drift*, then "spec drift" is the term, not a metaphor.
Same for *anchor*, *warm cache*, *garbage collection*, *starvation*. The test: would a specialist
reader recognize this as the standard name for the thing? If yes, keep it. Flatten the surrounding
prose instead.

Getting this wrong is worse than leaving a tell, because it makes the text sound like it was written
by someone who does not know the field.

## Scope discipline

- Rewrite sentences. Do not restructure arguments, cut sections, or change claims — that is editing,
  not deslopping, and it needs the author's sign-off.
- If a sentence is a **quotation**, leave it and mark it. Translating someone's published line into
  plainer prose misrepresents them.
- If removing a tell would remove information, keep the information and drop only the ornament.

## Reference files

- `references/markers-zh.md` — Chinese marker taxonomy, eight categories, with examples.
- `references/markers-en.md` — English markers, sourced to a Hacker News thread cataloguing them.
- `references/titles.md` — headings: name the content, do not narrate the reading path. Seven rules.
- `references/nofluff.md` — the nofluff standard's two checks and the four rules the tables lack.
- `references/worked-example.md` — a real audit: 45 findings, before/after pairs, indicators 12/10/14 → 0/0/0.
