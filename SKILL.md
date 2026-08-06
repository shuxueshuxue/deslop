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

AI flavor is **performance**: vivid analogies, personification, staged reversals, punchy closers.
It reads well line by line, which is exactly why it survives editing. The test for any sentence:

> Is this **stating** something, or **performing** it?

A writer who mistakes "plain" for "the problem" will sand the text into mush and miss every real tell.
Aim at Wikipedia, Hacker News technical comments, and academic papers — direct, unadorned, specific.

## Procedure

1. **Extract the prose.** Strip markup so you audit what a reader actually sees, not the source.
2. **Audit.** Go line by line against `references/markers-zh.md` (Chinese) or `references/markers-en.md`
   (English). Produce a table — one row per hit:

   | location | verbatim sentence | category | why it is performance, not statement | plain replacement |

   Over-report. Mark uncertain hits `?` rather than dropping them.
3. **Count three indicators** before and after. These are the falsifiable part:
   - staged reversals (`it's not X, it's Y` / `不是 X，是 Y`)
   - em dashes (`—` / `——`)
   - personification (abstract subject performing a human or biological action)
4. **Apply.** Replace with the literal denotation. Never swap one vivid word for another vivid word.
5. **Re-measure and report both numbers.** "Reversals 12 → 0" is evidence; "now it reads naturally" is not.

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

- `references/markers-zh.md` — Chinese marker taxonomy, seven categories, with examples.
- `references/markers-en.md` — English markers, sourced to a Hacker News thread cataloguing them.
- `references/worked-example.md` — a real audit: 45 findings, before/after pairs, indicators 12/10/14 → 0/0/0.
