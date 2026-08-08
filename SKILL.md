---
name: deslop
description: >-
  Strip the LLM tells out of prose. Use when text needs to read as written by a person — a talk,
  a README, a design doc, release notes, a paper — or when someone says it "sounds like AI",
  "sounds like marketing", or asks to make it plainer. Audits the text against a marker taxonomy,
  produces a per-line kill list with plain replacements, applies them, and re-measures two
  mechanical indicators plus manual semantic findings so the result is verifiable rather than
  asserted. Chinese and English.
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
2. **Sweep the physical verbs. Do this before anything else.**

   Start with verbs that create an obvious physical image, then ask: **is this image standing in
   for an operation the sentence should name?** An abstract object alone is not enough. Report the
   verb only when a literal replacement says more precisely what happened. `压掉` a check, `接住`
   an exception, and `说中` a defect pass this test. `由人签字的那一半` does not: it identifies
   authorship and has no plainer operation to substitute.

   One-syllable verbs are the priority — they are the ones that slip through, because they read as
   brisk rather than ornamental: `跑一遍` `扫一遍` `抓到` `压掉` `砍掉` `拉满` `打穿` `接住` `扛住`
   `命中` `捋一遍`. Two-syllable compounds hide the same defect and are harder to see because they
   have hardened into industry speech: `落地` `收口` `打磨` `盘活` `撬动` `沉淀` `对齐`.

   Replace with what happened: `跑一遍` → `运行一次`, `抓到` → `找出`, `命中` → `报出`,
   `扫这份文档` → `检查这份文档`, `落地` → `上线` or `交付`.

   The same question decides a second class: **a term that is standard inside a field but is not a
   word in the reader's ordinary language.** `tell` written to someone who does not work on this
   tool. `回归` for a regression — in everyday Chinese that word means something else, so the sentence
   reads as translated rather than spoken. `命中` `落地` `收敛` `鲁棒` `复用` are the same shape. The
   fix is not to explain the term; it is to say what happened: `回归` → `改好之后又写回去的毛病`.
   Ask who is reading, not whether the term is correct.

   Keep established names in a specialist document (`埋点`, `back-pressure`). `缓存击穿` needs a
   narrower call: it has a common textbook meaning, but explanations and loose usage also mix it
   with 穿透 and 雪崩. For a broad audience, report it and ask the writer to name the failure mode;
   for a cache design document that defines the term, leave it.

3. **Run the scanner.** `python3 scan.py --strip FILE` matches the text against
   `references/lexicon.tsv` (Chinese and English) and prints one row per candidate with
   a plain replacement and, where the word is sometimes legitimate, a note. Add `--lines` for line
   numbers, `--lang zh` to restrict.

   The scanner is the cheap mechanical half. It catches vocabulary and fixed phrases as
   **candidates**, and nothing else — a hit is not an instruction to rewrite. It cannot decide
   whether a quotation is being used, whether `robust` is a statistics term, whether `harness` names
   a mechanism, or whether `判据` and `承载` fit the written register. Keep those rows in the lexicon
   with notes so the audit sees them; decide keep or rewrite only after reading the sentence. It also
   cannot see a dramatized closer, a superfluous paragraph-ending summary, an analogy doing no work,
   a heading that narrates instead of naming, or a sentence that survives both nofluff checks. Take
   its output as a worklist, then do the audit below for everything it is blind to.
4. **Audit.** Go line by line against `references/markers-zh.md` (Chinese) or `references/markers-en.md`
   (English), and every heading against `references/titles.md`. Produce a table, one row per hit:

   | location | verbatim sentence | category | why it is performance, not statement | plain replacement |

   Over-report. Mark uncertain hits `?` rather than dropping them.
5. **Count two mechanical indicators** before and after. These are the falsifiable part:
   - staged reversals (`it's not X, it's Y` / `不是 X，是 Y`)
   - em dashes (`—` / `——`)

   Count personification separately in the audit table. It requires knowing whether the subject is
   abstract and whether the verb is conventional, so a word-list counter would manufacture a number
   rather than measure one.
6. **Apply.** Replace with the literal denotation. Never swap one vivid word for another vivid word.
7. **Re-read for over-correction.** This is a separate pass, not a note to keep in mind — skipping it
   is the most common way a deslop run makes text worse. Check every replacement you just made:
   - Did a written word become a spoken one? (`判据` → `怎么判`, `触发源` → `触发的地方`)
   - Did a two-syllable verb become one syllable? Chinese written register prefers two.
   - Did a heading become a casual question? Headings sit further toward written register than body.
   - **Re-run the taxonomy on the words you just wrote in.** A replacement is new prose and can carry
     the same defect it replaced. This happens constantly: `砍掉` swapped for `压掉`, then `击穿`
     swapped for `打穿` — one physical verb on an abstract object traded for another, twice, by
     someone who had just written the rule against it. Coinages leak in the same way (`自扫` for
     "scan the document against itself"). Read your replacements as if someone else wrote them.

   If a sentence now sounds like conversation rather than a document, put it back and pick a
   *common* word instead of a *spoken* one. The target is common, not casual.
8. **Re-measure and report both numbers.** "Reversals 12 → 0" is evidence; "now it reads naturally" is not.

For a document of any size, run step 4 in a **fresh-context subagent**. Self-auditing prose you just
wrote does not work — you re-read your own intent instead of the words on the page. Hand the subagent
the extracted text and the marker file, and demand the table.

Then read the whole document straight through, once, at the end. The line-by-line passes and the
scanner both work item by item, and there is a class of damage they cannot see: the boundary between
two items. An edit that swallowed the heading between two paragraphs leaves both paragraphs correct
on their own and the seam between them nonsense. Resolving to be more careful does not help here —
care does not produce a second reading. A different kind of pass does.

## Jargon: the default is against it

**The ordinary word wins unless the reader needs the exact name.** This is an audit default, not a
word-list rule. Keep a term when the reader works in the field and an ordinary replacement loses its
meaning; otherwise ask the writer to name the concrete operation.

Most jargon fails the second condition. `回归` means regression, and `功能退化` or `实现错误` say the
same thing in words a person uses. `鲁棒` is a transliteration and almost never earns its place.
`复用` is workplace speech, not standard Chinese. When a term survives, it is because a specialist
would lose precision without it — not because it is correct, and not because it is shorter.

A real term of art still stands. If a mechanism is literally named *drift*, then "spec drift" is its
name; same for *idempotent* / *幂等*, *deadlock* / *死锁*, *garbage collection*, *back-pressure*.
Flattening those makes the text read as though the author does not know the field.

The evidence is not merely "a specialist would recognise it" — specialists recognise jargon too. It
includes:

1. **One agreed referent.** A well-defined name earns weight, but it is not a binary test. `缓存击穿`
   has a common definition (a hot key expires and concurrent requests reach storage), while loose
   usage is also often mixed with `缓存穿透` and `缓存雪崩`. Treat this as an audience and explanation
   question, not proof that the term is invalid everywhere.
2. **No ordinary word for it.** `幂等` has none. `功能退化` is the ordinary word for `回归`, so `回归`
   goes.

Note that a term of art can still be a metaphor — *deadlock*, *garbage collection*, *back-pressure*
all are. Being a physical metaphor does not disqualify a word; being an *unsettled* one does. That is
why `击穿` on its own is a verb to replace, while `死锁` is a name to keep.

The exemption is narrow, and it is about the reader: the same word can be a term in a design doc and
jargon in a talk.

The scanner cannot make this call, so it reports surface forms as candidates and leaves their final
judgment to the audit. Context-heavy rows such as `robust`, `harness`, `判据`, `承载`, and `复盘` stay
in the word list with notes; suppressing them would hide the very over-corrections the final pass
must catch. Two false-positive classes are predictable enough to expect in any candidate list:

- **A document about slop quotes slop.** Scanning this skill's own README returns `load-bearing` and
  `key insight` when they are examples being named, not used. Same for style
  guides, review notes, and any text with a "do not write this" table.
- **Quoted material.** A hit inside someone else's sentence is theirs, not yours. Leave it.

An indicator earns a place in the count only if its hits are almost always real. The rule-of-three
tell is real, but it is not counted: on the first document scanned, all five hits were ordinary
enumerations. A number you cannot trust is worse than no number.

## Scope discipline

- Rewrite sentences. Do not restructure arguments, cut sections, or change claims — that is editing,
  not deslopping, and it needs the author's sign-off.
- If a sentence is a **quotation**, leave it and mark it. Translating someone's published line into
  plainer prose misrepresents them.
- If removing a tell would remove information, keep the information and drop only the ornament.

## Reference files

- `scan.py` — the scanner. No dependencies beyond python3.
- `references/lexicon.tsv` — candidate terms, Chinese and English, each with a plain replacement
  and a note where the word is legitimate in some contexts. Sources: Wikipedia's WP:AIVOCAB (every
  word there needs a citation to an outside study), Kobak et al. 2025 on excess vocabulary in
  biomedical abstracts, Juzek & Ward 2025, HN 48905248, and the Chinese lists from
  `ninehills/public-skills` (MIT). Add rows here rather than hard-coding words into prose.
- `references/markers-zh.md` — Chinese marker taxonomy, eight categories, with examples.
- `references/markers-en.md` — English markers, sourced to a Hacker News thread cataloguing them.
- `references/titles.md` — headings: name the content, do not narrate the reading path. Seven rules.
- `references/nofluff.md` — the nofluff standard's two checks and the four rules the tables lack.
- `references/worked-example.md` — a real audit: 45 findings, before/after pairs, indicators 12/10/14 → 0/0/0.
