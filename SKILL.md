---
name: deslop
description: >-
  Take AI register out of text and prove it left. Use when prose needs to read as written by a
  person — a paper, a talk, a README, release notes, a design doc, a reply — or when someone says
  it "sounds like AI", "太像 ChatGPT", "说人话", "去 AI 味", "sounds like marketing", or asks for a
  diagnosis before any rewrite. Picks a scene and a register target, freezes what may not drift,
  audits the text line by line against a merged marker taxonomy, applies plain replacements,
  then re-measures mechanical indicators so the result is checkable instead of asserted.
  Chinese and English.
---

# deslop

Prose written or polished by an LLM carries tells. They are learnable, countable, and removable.

This version merges three other projects into deslop. Each had solved a different half:

| project | what it brought in |
|---|---|
| [说人话 / shuorenhua](https://github.com/MrGeDiao/shuorenhua) | the control surface: scene, protected spans, tier, level × scope, unsourced-citation modes, two-stage reread, annotation mode |
| [natural-talk](https://github.com/chengzhi-c/natural-talk) | the principle/expression split, numeric caps, and the best anti-overcorrection material of the four |
| [Humanizer-zh](https://github.com/op7418/Humanizer-zh) | the Wikipedia *Signs of AI writing* pattern set: significance inflation, `-ing` pseudo-analysis, copula avoidance, synonym cycling, false ranges, formatting tells |

deslop's own half is the thesis (*saying the thing* against *being clever*), compression punctuation,
the burden-of-proof flip, the before/after indicators, and the over-correction pass.

`references/provenance.md` records every place the four disagreed and which one won, with the reason.
Read it before you override anything here.

---

## 0. The one thing to get right first

**AI register is not "plain, careful wording." Plain, careful wording is the target.**

Every marker in the taxonomy is one form of the same move: the writer showing you they are clever.
The vivid analogy, the staged reversal, the punchy closer, the word picked because it sounds learned.
It reads well line by line, which is exactly why it survives editing. The test for any sentence:

> Is this **saying the thing**, or **being clever**?

A pass run by someone who thinks "plain" is the defect will sand the text into mush and miss every
real tell. Plain is also not colloquial. The register anchors are in §2. Overshooting into casual
speech is as wrong as posturing, and it is the more common failure once someone has read the rules.

Two checks, from the nofluff standard, outrank every table in this repository:

1. **Delete it. Is any information lost?** If not, delete it.
2. **If a reader asks "what specifically does this mean", can you answer with a fact?** If not, it is filler.

The tables tell you where to look. These two tell you whether the sentence should exist. When they
disagree, the checks win.

## 0.1 Two layers, and only one of them is negotiable

**Principle layer.** Absolute, no scene exempts it, no cap applies.

1. **Do not fabricate.** No fact, number, source, date, mechanism, or causal relation that is not in
   the original. If you do not know, say so.
2. **Do not judge the person.** No psychological diagnosis, no identity-certifying praise, no
   performed "I completely understand."
3. **Do not change what a sentence claims.** Rewrite the sentence that carries a claim; the claim is
   the author's. Shape is yours, content is not.
4. **Do not rewrite quoted material.** Restating someone's published sentence in plainer words
   misrepresents them. Mark it and move on.
5. **Do not fabricate voice.** Adding an anecdote, a metric, an emotion, or a joke to make a draft
   feel human is fabrication, however friendly it looks. See §8.
6. **Do not build a metaphor.** Never explain a thing by swapping it for a thing from another
   domain. No scene exempts it, no density threshold applies, and "this one field is used
   accurately" is not a defence. The test is on the reader's side: **does the reader have to map A
   onto B to understand it?** If yes, it is a hit. Three things sit outside the rule because they
   are not metaphors in use: a name the field has frozen (*deadlock*, *idempotent*, *back-pressure*,
   *pipeline*, `埋点`), a dead metaphor the language already absorbed (*support*, *framework*,
   `深入`, `流程`, where the reader maps nothing), and a subject that genuinely is in that domain.
   Flattening a name makes the text read as though the author does not know the field, which is
   worse than leaving a tell. `taxonomy.md` H6.

*Identity exception to (2):* if the reader asked who you are or what your limits are, answer plainly
and briefly. The rule bans the unprompted collaborative trace, not honest answers.

**Expression layer.** Elastic, with named caps. Dashes, openers, signposts, action pre-announcements,
triads. The standard is "as few as the text can carry", not literal zero. Real people use a dash.
Caps are in §5 and in `tools/measure.py`. They mark sparseness; nothing asks you to use them up.

## 0.2 The default is to change the sentence

Raw model prose has almost no sentence usable as written. No single word is wrong; the whole
register is off by a constant. An edit that touches a tenth of the lines has
removed the worst offenders and left the text still sounding like a model wrote it.

So the burden of proof runs backwards from ordinary editing: **keeping a sentence needs a reason,
changing it does not.** If you catch yourself writing a list of what you deliberately left alone,
the pass was too timid.

Aggressive means *how much you touch*, never *how the result reads*. The output is still plain, still
shorter than what it replaced. A pass that changes every line and makes the text louder failed twice.

**Except where §3 says otherwise.** The `bounded` and `in-place` scopes exist because long-form text
under a free hand shrinks by an amount nobody can predict. The same 1000-character piece can come
back at −18% or −39% depending on the run. When length is the user's to decide, this default yields
to the scope contract, and only to that.

---

## 1. Execution order

Fixed. Do not skip, do not reorder. Steps 1–5 cost minutes and prevent most of the damage.

1. **Scene.** `chat / status / docs / public-writing / academic / code-context`, plus any scene pack (§2).
2. **Protected spans + fact ledger.** freeze what may not drift, before reading for style (§4).
3. **Tier.** how hard the text is hit, from the density of what matched (§5). Tier is *severity*,
   not force.
4. **Level.** `minimal / standard / aggressive`: how hard you hit back (§3).
5. **Scope.** `structural / bounded / in-place`: whether you may delete a whole sentence (§3).
   Level and scope are independent axes. `aggressive + in-place` is legal and sometimes correct.
6. **Measure before.** `python3 tools/measure.py FILE --scene <scene>`. Save the JSON.
7. **Sweep the physical verbs (zh) / elevated diction (en).** before any table work (§6.1).
8. **Scan.** the lexicon is a worklist of candidates, never a verdict (§6.2).
9. **Audit.** line by line against `references/taxonomy.md`, headings against `references/titles.md`.
   Produce the table in §7. In a fresh-context subagent for anything longer than a page.
10. **Apply.** literal denotation. Never swap one vivid word for another vivid word. Verify the
    input hash first with `python3 tools/freeze.py check FILE <sha>`, and refuse if it moved (§11).
11. **Reread, in four separate passes** (§9). They catch different damage and cannot be merged.
12. **Measure after, and report both numbers.** "Reversals 12 → 0" is evidence. "Now it reads
    naturally" is not.

---

## 2. Scene decides the register target

There is no single "human" register. The friend test that makes a chat reply good would wreck a
paper. Pick the scene first; everything downstream reads from it.

| scene | register anchor | default level | default scope | unsourced citations | what the pass must not do |
|---|---|---|---|---|---|
| `chat` | 会对朋友这样说吗 | minimal | structural | `rewrite-safe` | make a reply harder or colder to prove it is not sycophantic |
| `status` | a standup that respects the reader's time | minimal–standard | structural | `audit-only` | soften a risk, drop a timeline, blur who owns what |
| `docs` | reference material a person searches | minimal | structural | `audit-only` | trade retrievability for friendliness; flatten a term of art |
| `public-writing` | a person with a view, not a poster | standard | `bounded` past ~1000 zh chars | `rewrite-safe` | manufacture a punchline, or shrink by an amount the author did not agree to |
| `academic` | a good methods section: direct, unadorned, specific | standard | structural | **`audit-only`, always** | flatten an epistemic hedge, cut a limitation, or make a claim more confident than the author made it |
| `code-context` | a comment that survives the next reader | minimal | in-place | `audit-only` | change what the comment says the code does |

Chinese register anchor, all scenes: **the dubbing register of Japanese film.** Full sentences,
subjects present, two-syllable verbs (`阻断` not `拦`, `承载` not `装`), no slang, no in-group
shorthand, steady but not stiff. Read the result aloud; if it could be a dubbing line, the register
is right. Both failure directions are audible immediately.

English anchor, all document scenes: **Wikipedia, Hacker News technical comments, and good papers.**

### 2.1 Scene packs

If the text *looks like* one of these, apply the pack whether or not the user said so. Packs bind
tone and publication purpose only. They never override protected spans, tier, level, or scope.

- **README.** first screen answers what this is, who it is for, what it solves. Delete vision copy,
  keep commands, versions, platform support, benchmark counts.
- **release note.** what changed, how it was verified, what breaks. Keep every number, path, and
  issue reference. Delete the release manifesto. If there is no changelog, say so; do not invent one.
- **forum post.** a maintainer's real observations. Keep the community voice and the specific
  experience; strip corporate announcement register.
- **issue reply.** is the problem real, does it reproduce, what happens next. No customer-service
  soothing, no schedule you have not been given.
- **academic paper.** see §2.2. This pack is new here; none of the four upstreams had one, and
  three of them declare academic writing out of scope.
- **slide deck.** headings carry most of the reading. `references/titles.md` applies with full force;
  the body may be terser than prose but the heading may not narrate the reading path.

### 2.2 The academic pack

Three of the four upstream projects hand academic text back untouched, and deslop takes papers in
scope without saying what makes them different. They are different in four ways, and each is a
false-positive trap that will otherwise eat a good draft:

1. **Hedges carry the claim's confidence.** `may`, `suggests`, `we argue`, `appears to`, `is consistent with`
   carry epistemic status. Flattening `X suggests Y` to `X shows Y` strengthens a claim the author
   did not make, which is a principle-layer violation. Only *stacked*
   hedges (`may potentially somewhat`) are a finding.
2. **Passive is native.** `The experiment was conducted`, `was published`, `were sampled`. Report
   passive stacking that hides an agent who matters; leave conventional academic passive alone.
3. **Enumerations are contributions, not triads.** A C1–C4 contribution list, a three-part
   falsifier list, or a three-level taxonomy is content. The rule-of-three tell applies to prose
   that was cut into three to look complete, and it is never counted (§5).
4. **Bold marks defined terms.** In a paper, a bolded term on first use is a definition, not
   emphasis-spam. Count bold density, then name this exemption rather than deleting the marks.

What the academic pack *tightens*: significance inflation, the dramatized closer at the end of a
section, self-assessment about your own argument (`the one that matters most`, `the strongest
feature`), and em dashes, which academic prose absorbs so readily that they become the dominant tell.

---

## 3. Level × scope

Two independent axes. Confusing them is the most common way this goes wrong.

**Level.** How hard the register is pulled back.

- `minimal`. The text is close; strip local template feel, ending ceremony, surplus rhetoric.
- `standard`. Obvious AI register or mixed registers, but the information skeleton is sound.
  Unify the register, cut the performance, merge or re-subject sentences where needed.
- `aggressive`. Tier 1 is dense, or several structural problems stack. Protect facts and terms
  first, then rewrite. `docs` does not go here by default.

**Scope.** Whether whole sentences may go.

- `structural`. Default. Delete empty sentences, merge adjacent facts, re-order lightly, restructure
  locally. This is where the document's *shape* is allowed to change (§6.3).
- `bounded`. Default for Chinese `public-writing` past ~1000 characters. Clean inside sentences
  freely; a sentence that is entirely empty does not get deleted, it goes on a **删除清单 (proposed
  deletions)** the user signs off. Length becomes the user's decision to make.
  A line earns a place on that list only if all three hold:
  1. deleting it changes no information point: no fact, no number, no judgement, no action, no instruction;
  2. it is not the only transition between two substantive sentences;
  3. it matches a purely empty shape: an empty summary, value inflation, unsourced authority
     throat-clearing, a flattery opener, whole-sentence narration.
- `in-place`. User asked for the sentence count preserved, or `bounded` still cut too much. Nothing
  is deleted, not even an empty sentence; you work inside the sentence only. An empty sentence gets
  kept and annotated `[空句，建议人工确认是否删除]`, never softened into a different empty sentence.

The distinction that makes `bounded` work: **a strippable leading phrase is not an empty sentence.**
Delete `值得一提的是` and read what is left. Still a sentence with information → clean it in place.
Nothing left → it goes on the list (`bounded`) or gets annotated (`in-place`).

---

## 4. Protected spans, and the ledger

Freeze these before you read for style. Anything below is protected in every scene, at every level.

- **Numbers, dates, ranges, units, versions.** Do not round, do not blur a span (`未来十年` stays ten
  years), do not add a comparison the original did not make.
- **Names and attribution.** People, organisations, products, modules, issue and PR numbers, and who
  did or said or owns a thing. Never turn the author's own judgement into something already proven.
- **Quoted text and titles.** Inside quotation marks is not yours. Do not paraphrase and re-quote.
- **Commands, code, parameters, fields, paths, environment variables.** Spelling, case, underscores,
  hyphens, all preserved.
- **Errors, logs, status codes, metric names, measurements, baselines.** Never turn *observed* into
  *proven*, never drop a sample range or a comparison baseline.
- **In `code-context`:** the described runtime behaviour, applicable conditions, and boundary notes.
  Strip stance words from a comment; keep what it says the code does. A neighbouring line already
  showing a number does not make the sentence redundant.

Alongside the spans, keep a **relations ledger**. This is where most silent damage happens, and no
word list catches it:

- which number modifies which object;
- which actor performs which action and holds which goal;
- what implements or is based on or handles what.

Abstract stays abstract. `方案` does not become `工具`; `目标` does not become `产品`; "an
architecture with this potential" does not become "a system built on that architecture". Predicate
direction, completion, strength, and effect type are all part of the relation: `improved performance`
may not become `touched on performance`, and `raised throughput` may not expand into `saved time and
cost`. Removing `显著 / 大幅 / significantly` still leaves the claim that something happened.
Co-occurrence in a paragraph is not a relation: if the original does not have the predicate, the
rewrite does not get to have it either.

**When in doubt, keep the protected span and accept a slightly stiff sentence.** Do not gamble.

### 4.1 Unsourced citations: pick a mode before touching the sentence

`研究表明` / `studies show` / `experts say` / `industry reports indicate` with nothing behind them.

- **`rewrite-safe`.** drop the authority frame; keep only what stands without it. If the number,
  the forecast, or the conclusion depends entirely on the missing source, **delete the whole claim**.
  Do not delete `40%` and leave "it will be faster"; do not turn `over the next decade` into "in the
  coming years". Default for `chat` and `public-writing`.
- **`audit-only`.** do not supply a source, and do not rewrite an unsupported claim into something
  that reads as established. Say the attribution is missing. Default for `status`, `docs`, and
  always for `academic`. This constrains the unsourced claim only. Every other defect in the same
  paragraph still gets cleaned.
- **`rewrite-with-placeholder`.** only when the user asked to keep the argument structure. Leave an
  explicit "source needed here". Never invent an institution, a year, a sample size, or a consensus.

Mixed-scene text takes the more conservative mode.

---

## 5. Tier, caps, and what may be counted

**Tier is severity: how strongly something matched. It says nothing about how hard you edit.**

- **Tier 1. Replace by default.** 5–20× more frequent in model text than human text. Openers,
  ceremony closers, flattery, business jargon, performed engineer-speak, over-catching empathy,
  identity-certifying praise, significance inflation, sycophantic openers.
- **Tier 2. A finding only when clustered in one paragraph.** Fine alone. Short paragraph
  (<100 chars/words): 2+. Long paragraph (≥100): 3+. Keep the best-fitting one, rewrite the rest.
- **Tier 3. A finding only at document-level density.** Ordinary words. Short text (<200): same
  word 3+. Medium (200–1000): 5+. Long (>1000): above 0.5%. Delete the surplus or replace some with
  concrete information. **Never rotate synonyms to lower the density.** That converts a density
  problem into a slickness problem, and the density is still there.

### 5.1 What may be counted

An indicator earns a place in the counted set only if its hits are almost always real. A number you
cannot trust is worse than no number. `tools/measure.py` enforces this in three tiers:

- **GATED.** drive to zero or name every survivor: staged reversal, em dash, `顿号`, mid-prose
  `：`, assistant residue, knowledge-cutoff disclaimer, emoji, inline-title list items, `-ing`
  pseudo-analysis tails, copula dodges, false ranges, curly quotes in Chinese.
- **CAPPED.** legitimate below a length-normalised cap; only the excess is a finding: signposts,
  editorial stance, lecture tone, exclamation marks, stacked hedges, bold density. The caps come from
  natural-talk's 300–500 character reply baseline and are held as a density for longer text.
- **REPORTED. Never gates anything.** Sentence-length CV, conjunction density, nominalisation,
  mixed metaphor fields, rule-of-three candidates, lexicon hits by category.

Four families have no counter, three of them by demotion on evidence. The first two are printed in every report so nobody quietly
re-promotes them:

- **Rule of three is not counted.** On the first document deslop scanned, all five hits were ordinary
  enumerations.
- **Conjunction density has no global threshold.** shuorenhua calibrated it on 95 passages and it
  inverted: the median for text that should *not* change was 5.26/1000 against 0.00 for text that
  should, and its maximum was higher too. A matched pair pins it. A narrative post at 80.00/1000
  needed half its connectives cut; a migration doc at 81.08/1000 needed none. Judge by scene and by
  distribution (three consecutive sentences opening with a connective; the same connective three
  times in a paragraph), and only in `public-writing` narrative. Never in `docs`, `status`, or
  `code-context`.

- **Bolded assertion is not counted.** A whole sentence bolded for emphasis is a real and common
  tell, and it cannot be separated mechanically from a bolded list label: `**It does not follow that
  the paradigms simply return.**` and `**Report both per-rule and all-pass rates.**` have the same
  shape (bold at the start of a block, sentence-terminated, followed by more text), and only meaning
  tells them apart. What `measure.py` does count is **bold inside a sentence**, which is high
  precision, after stripping leading labels and blockquotes. The assertion case goes in the audit
  table. (This one was demoted during the worked example, when the counter charged a paper eleven
  violations for using labelled bullet lists.)

- **Metaphor is not counted, and the rule is absolute anyway.** A frozen name (`back-pressure`), a
  literal use (`代码仓库`) and a live metaphor look identical to a word list, so hits are not
  almost-always-real and nothing can be gated. That is not a contradiction with the absolute rule in
  §0.1: the ban is enforced in the audit, and the script's job is to make sure no candidate goes
  unexamined. `python3 tools/measure.py FILE --metaphor` prints every borrowed-domain term and every
  physical verb with a line number. `taxonomy.md` H6.

### 5.2 What "almost always real" is worth as a number

"Almost always real" is a judgement until someone puts a rate on it. Google's engineering practice
puts one on the same decision: a **blocking** check is held to zero effective false positives, an
**advisory** one is capped at 10%, a rate at or above 10% puts the check on probation, and above 25%
it may be turned off outright.

That is the same line this section draws, named from the other side. "Precision too low, so it may
only list candidates" and "false-positive rate too high, so it may not block" are one rule. So the
promotion rule here takes those numbers:

| measured false-positive rate | tier |
|---|---|
| effectively zero | **GATED** — may fail a pass |
| under 10% | **CAPPED** or **REPORTED** — lists candidates, decides nothing |
| 10% and above | probation: report the number next to the indicator, do not act on it alone |
| above 25% | demote, and write down why where the next person will read it |

The three tiers are not a naming choice. They come from the obligation-gates work, which defines
enforcement in three levels and gives the reason there are three rather than two:

- **none.** Nothing happens when the rule is broken. The artifact is available, not obligatory.
- **triage.** The mechanism runs on the change and produces located candidates, which a person or
  an agent then handles one at a time. The mechanism itself decides nothing. It tolerates imprecision,
  because the cost of one false positive is one judgement, not one blocked change.
- **blocking.** The mechanism decides, and a violation stops the change. This demands a
  near-zero false-positive rate, because the cost is a wrong block, and the more expensive cost is
  that a wrong block is a reason to switch the check off.

The middle level is where almost everything lives that a machine can *find* but cannot *judge*.
Collapsing it into "none" throws away the location and makes a person search again; collapsing it
into "blocking" costs the check its legitimacy and takes neighbouring checks down with it. Three
levels is not finer granularity. Two levels leaves a whole class of property with nowhere to sit.

**What is actually measured here, and what is not.** `evals/run.py` scores the lexicon scan as a
whole against 46 cases: currently 100% recall at 96.0% precision, with the single false positive
coming from a deliberately broad rule.

That is a corpus number, and **the decision it is being asked to support is a per-indicator one.**
Aggregate precision tells you whether the scanner is worth running at all. It cannot tell you which
indicator may block, because what licenses one indicator to block is that indicator's own precision.
**Per-indicator precision is not measured here.** The three demotions in this section therefore rest
on inspection rather than on a rate, and the table above is a rule the corpus cannot yet enforce.

This gap is worth naming rather than papering over, because it has the shape §12 is about: the
measurement was taken at one size and the decision is made at a smaller one, so the number reads as
support for a claim it does not actually cover.

**Personification, bolded assertion and metaphor are decided in the audit table. No script decides
them.** Deciding
personification requires knowing whether the subject is abstract and whether the verb is conventional
in the field. A word-list counter would manufacture a number rather than measure one.

---

## 6. The sweeps

### 6.1 Physical verbs first (Chinese), elevated diction first (English)

Do this before any table work; it is the highest-yield pass and the tables cannot see it.

**Chinese.** Find verbs that create a physical image, then ask: *is the image standing in for an
operation the sentence should name?* An abstract object alone is not enough. Report the verb only
when a literal replacement says more precisely what happened. `压掉` a check, `接住` an exception and
`说中` a defect pass this test; `由人签字的那一半` does not, because it identifies authorship and has
no plainer operation to substitute.

One-syllable verbs are the priority, because they read as brisk rather than ornamental:
`跑一遍 扫一遍 抓到 压掉 砍掉 拉满 打穿 接住 扛住 命中 捋一遍`. Two-syllable compounds hide the same
defect and are harder to see because they have hardened into industry speech: `落地 收口 打磨 盘活
撬动 沉淀 对齐`. Replace with what happened: `跑一遍` → `运行一次`, `抓到` → `找出`, `命中` → `报出`,
`落地` → `上线` or `交付`.

The same question decides a second class: **a term standard inside a field but not a word in the
reader's ordinary language.** `回归` for a regression reads as translated rather than spoken;
`命中 收敛 鲁棒 复用` are the same shape. Do not explain the term. Say what happened: `回归` → `改好之后又写回去的毛病`. Ask who is reading, not whether the term is correct.

**English.** The parallel move is the rarer, more "professional" word where a common one exists:
`utilize → use`, `leverage → use`, `facilitate → help`, `commence → start`, `in order to → to`,
`a multitude of → many`, `it is imperative that → X must`. Same pass, same question.

### 6.2 The scanner is the cheap half

`python3 tools/measure.py FILE --hits` matches against `references/lexicon.tsv` (553 rows, Chinese
and English, each with a plain replacement, a note where the word is sometimes legitimate, and the
upstream project it came from).

It catches vocabulary and fixed phrases **as candidates**. A hit is not an instruction to rewrite.
It cannot tell whether a quotation is in play, whether `robust` is the statistics term, whether
`harness` names a mechanism, or whether `判据` fits the written register. It is blind to every one of
these: a dramatized closer, a superfluous paragraph-ending summary, an analogy doing no work, a
heading that narrates instead of naming, uniform cadence, a forced triad, a "challenges and future
prospects" section, a generic optimistic ending, and a sentence that fails both nofluff checks.

Two false-positive classes are predictable enough to expect every time:

- **A document about slop quotes slop.** Scanning this file returns `load-bearing` and `key insight`
  because they are being named, not used. Same for style guides and review notes.
- **Quoted material.** A hit inside someone else's sentence is theirs. `measure.py` masks
  blockquotes, `「」`, long quoted runs, code, links, and table rows before counting, so the author's
  numbers stay the author's.

### 6.3 Compression punctuation, and why fixing it changes the document

Chinese `——`, `、`, `：` all do one job: **let a sentence carry more than one thought without
committing to a second sentence.** Model prose compresses because it optimises coverage per sentence.
A person writing technical prose commits: one thought, full stop, next thought. The English em dash
does the same job and is the single most common tell in English drafts.

The em dash joins clauses, so it is visible. `、` joins list items and `：` stages a reveal, so both
hide behind being grammatical. **Legality was never the test.** Every one of these is correct
Chinese; so is the em dash, and you do not spare that one. The moment you catch yourself writing
"most of these 顿号 are legitimate parallel nouns", the pass has failed. You started defending your
own sentences instead of judging them.

The test for each mark:

> **Did it replace a full stop, or a line break?**

Replaced a full stop → write two sentences. Replaced a line break → write an actual list. Neither →
only then may it stay. The residue is narrow: a two-item pair inside one clause, or a product string
quoted verbatim. Three items on `、` in running prose is a list the document declined to make. A
mid-prose `：` introducing an explanation is a second sentence, sometimes a heading.

**Substitution is not the fix.** Turning `怎么选、状态怎么读、设置里有什么` into
`怎么选，状态怎么读，设置里有什么` keeps the shape and changes the mark. Nothing was decompressed.

**This is where the pass earns its keep, and it changes the document's shape.** Sentences split,
inline enumerations become real lists, overloaded paragraphs split into sections, and headings appear
that were never written because a colon was holding their place. That is in scope: the shape *is* the
tell. What stays out of scope is what the document asserts.

### 6.4 Chinese: drop 你

Chinese drops subjects. Dense `你` in a Chinese document is almost always English documentation
register carried across. Grammatical, and still imported, exactly like `回归` for a regression.

`你像发微信一样给它发消息派活，它在你指定的那台机器上干活` → `像发微信一样给它发消息派活，它就在指定的那台机器上干活`.
Shorter, and it states the fact instead of coaching a reader.

Delete by default. Keep where the sentence genuinely contrasts one person's thing against another's
(`你的 agent` vs `别人的 agent`), or where dropping it makes the actor ambiguous. **This rule is for
documents.** A reply written to one person is dialogue, and `你` belongs there.

---

## 7. The audit table

One row per hit. Over-report; mark uncertain hits `?` rather than dropping them.

| location | verbatim sentence | family | why it is performance, not statement | plain replacement | source domain | keep? |
|---|---|---|---|---|---|---|

**The source-domain column is what catches H6**, the ban on building a metaphor. Leave it blank
unless the hit borrows from a domain the subject is not in; otherwise name the domain in one word.
When the table is done, aggregate that column:

- a domain appearing **once** is a single borrowed word. Handle it as an ordinary hit.
- a domain appearing **twice or more** is a sustained metaphor. Stop and ask whether the document is
  explaining its subject or explaining the domain.

The aggregate is the point. Every row of a sustained metaphor passes on its own, which is why the
per-row judgement never catches it. In the failure recorded in `taxonomy.md` H6 the column would
have read `工厂` fourteen times.

`references/taxonomy.md` holds the twelve families. `references/decisions.md` holds the per-hit
decision procedure, the exemption caps, and the `in-place` alternate for each family.

Two rules that stop an audit from becoming a massacre:

- **Exemption caps.** Some families allow a named number of survivors. The staged reversal allows
  two across a document: one term definition, one argument the following text depends on. Past the cap, "every one of
  them carries the argument" is itself the evidence that the shape is doing the work, and density
  handling resumes. Exempt instances are not counted toward density and are not flattened.
- **Cleaned-up landing.** After the stance layer is gone, the sentence lands on what the original
  actually said, in this priority order:
  1. original has a number, an action, an object, or a definite conclusion → strip the rendering
     words, keep those;
  2. original has no concrete metric or fact → the output is allowed to be shorter and plainer.
     Do not fill with `能提效` / `有改进` / `it improves things` / `faces challenges`;
  3. `status` / `docs` / `academic` where the claim needs a basis the original never gave → mark
     "original gives no basis". Do not supply a number, a feature, or a technology choice.

For anything longer than a page, run the audit in a **fresh-context subagent**. Self-auditing prose
you just wrote does not work. You re-read your own intent instead of the words on the page. Hand it
the extracted text and the taxonomy, and demand the table.

### 7.1 Annotation mode

Only when the user asked to see the problems before any rewrite (`先别改，先标问题` / `这段哪里像 AI`
/ "diagnose it first"). Output the 1–5 most important findings, each with exactly four fields:
**问题族 / 触发点 / 建议动作 / 是否建议改写**. Do not smuggle a full rewrite into an annotation.

One extra verdict lives only here: **材料不足 (not enough material)**. The test is the compression
trial. Strip the stance layer, the inflation, and the boilerplate; if the surviving facts, actions,
numbers, and judgements cannot fill the original length, the problem is not how it is written.
Say what is left and what class of material is missing. Do not design the author's research for
them, and do not re-inflate to restore the word count. `材料不足` is not "leave it alone": clean the
stance layer as usual and say the result will be much shorter.

---

## 8. Voice, and the one place the four sources fought

Humanizer-zh is right that sterile, voiceless prose is its own tell: uniform sentence length, no
position, no acknowledged uncertainty, no first person, reads like a press release. It is wrong
about the remedy. Its worked example replaces a flat paragraph with invented reactions and an
invented three-million-line figure. In a *rewrite* that is fabrication, and deslop and shuorenhua
both forbid it outright.

The resolution is to split one operation into two:

- **deslop.** removal. Safe, default-on, adds nothing.
- **re-voice.** addition. Off by default. Requires material the author actually holds, and never
  runs in `docs`, `status`, `academic`, or `code-context`.

So: keep first person where it records the author's real observation or decision. Keep an admitted
uncertainty. Break a uniform cadence by changing sentence and paragraph *structure*, never by adding
a second summary or a three-item slogan. When a draft is clean and still lifeless, the finding is
**"this has no position — what do you actually think?"** addressed to the author. Not a position you
supplied on their behalf.

Do not introduce deliberate typos or filler either. Mess is not the same thing as a voice.

---

## 9. The reread, in four passes

They catch different damage. Merging them is how each one gets skipped.

**Pass A.** Fidelity. Did anything drift?

1. protected spans intact;
2. no information lost;
3. register consistent;
4. terminology undistorted;
5. no hard seams where something was cut;
6. **analysis/output consistency.** if your finding was "the original names no concrete object,
   capability, or basis", then no new tool, product, feature, implementation relation, or metric may
   appear in the output. Every `X does Y` / `X is based on Y` / `X handles Y` in the result must
   point back to the same predicate in the original. Same-paragraph co-occurrence is not a source.

   Under `bounded` / `in-place`: every information point must be traceable; `in-place` output below
   85% of the original length means check whether you deleted, merged, or compressed something;
   sentence-count change past ~10% means check whether you did unapproved structural work.

**Pass B.** Over-correction. This is a separate pass, not a thing to keep in mind. Skipping it is
the most common way a deslop run makes text worse.

- Did a written word become a spoken one? (`判据` → `怎么判`, `触发源` → `触发的地方`)
- Did a two-syllable verb become one syllable? Chinese written register prefers two.
- Did a heading become a casual question? Headings sit further toward written register than body.
- In `academic`: did a hedge get stronger? Did a limitation get shorter? Did `suggests` become
  `shows`? Any of those is a principle-layer violation, not a style call.
- **Re-run the taxonomy on the words you just wrote.** A replacement is new prose and carries the
  same defect. This happens constantly: `砍掉` swapped for `压掉`, then `击穿` for `打穿`. One
  physical verb on an abstract object traded for another, twice, by someone who had just written the
  rule against it. Coinages leak the same way. Read your replacements as if a stranger wrote them.

If a sentence now sounds like conversation rather than a document, put it back and pick a *common*
word instead of a *spoken* one. The target is common, not casual.

**Pass C.** Residual. Only after Pass A and B, and only if the text still reads slightly of model.
Fixed to five checks, and only light corrections are allowed:

1. leftover openers (`结论先说` / `值得注意的是` / `It's worth noting`);
2. leftover empty closers (`总的来说` / `归根结底` / `In conclusion`);
3. leftover narration, explaining what something means instead of saying it;
4. leftover empty judgements (`方向是对的` / `意义重大` / `a significant step`);
5. cadence too even: every sentence the same length, same lift, same landing; or the same syntactic
   skeleton repeating until you can predict the next sentence's shape.

Fast way to find them: read straight through and circle the paragraphs **another model could have
written verbatim**. Those are the residual. `docs / status / academic / code-context` are more
conservative here. If the second pass would make the register chattier or less precise, stop after
Pass B.

**Pass D.** One straight read of the whole document. The line-by-line passes and the scanner both
work item by item, and there is a class of damage they structurally cannot see: the boundary between
two items. An edit that swallowed the heading between two paragraphs leaves both paragraphs correct
on their own and the seam between them nonsense. Resolving to be more careful does not help. Care
does not produce a second reading. A different kind of pass does.

---

## 10. Output contract

Default: **one recommended version.** No review commentary, no alternate takes, no per-line notes,
unless the user asked for annotation mode.

With the rewrite, report:

1. **the indicator table, before and after.** from `tools/measure.py --diff`;
2. **named survivors.** every gated hit still present, with the reason it stays;
3. **the proposed-deletion list**, if scope was `bounded`;
4. **the missing-basis notes**, if any claim needed one and did not have it;
5. **the scope line, every time, not once.** State that the pass checked register and did not check
   whether the text is right. This is not a disclaimer you make when you feel uncertain. It is
   mandatory output, because a cleaner register makes a factual defect *harder* to see: the
   surrounding prose comes back more confident and the reader's guard drops. §11.
6. **a recurrence note, when one applies.** If a family's hits cluster into what looks like an author
   habit rather than isolated sentences, say so and say which family. Per-sentence replacements do
   not hold against a habit, and the author is the only one who can act on it. The signal is a family
   that reappears across drafts, or one the author has already been corrected on. In the worked
   example this was the novelty defence: two sentences on the page, but the author had been corrected
   on it twice before, which makes the finding "this keeps happening", not "fix these two lines".

Add a one-line explanation only where a high-risk false positive was avoided
(`kept the system subject and the term, to avoid distortion`). Never a paragraph of self-assessment.

---

## 11. What this cannot do

`prose-deslop` fixes how a text sounds. **It does not check whether the text is right.**

In a real audit, three separate reviews of one deck found a dangling pronoun with no antecedent, a
claim on one page contradicting a claim on another, and a quoted authority whose argument had been
subtly misread. None of them is a register defect and none of them is in this taxonomy. They need a
comprehension pass with a different brief, and a rewrite that improves the register can make them
*harder* to see by making the surrounding prose more confident.

If the text is going out under someone's name, run that pass too, separately.

**Say this in the report every time.** §10 item 5 makes it mandatory rather than optional, because
the risk rises exactly when the pass went well. Confident prose is read less carefully.

One more thing this pass cannot see: **whether the input is still current.** A frozen snapshot is
what makes the before/after numbers meaningful, and it is also what goes stale. Record the input's
hash and the commit it came from, and say plainly that edits landing in a region changed since then
no longer apply. A rewrite that silently restores a claim the author has retracted is worse than no
rewrite.

---

## 12. Why the pipeline has this shape

Every check sees a fixed amount of text at once, and a defect whose scope is larger than that gets
missed. It gets missed **silently**, which is the part that matters: each unit passes its own
inspection, nothing is flagged, and the report comes back clean. Under-detection here does not look
like under-detection. It looks like a pass.

So the pipeline runs four checks at four sizes, and each one exists because the size below it cannot
see far enough:

| what it sees at once | the check | what only it can catch |
|---|---|---|
| a word or phrase | the lexicon scan (§6.2) | fixed vocabulary |
| a sentence | one audit row (§7) | the shape of that sentence |
| the document | the counted indicators, the source-domain aggregate, Pass D (§9) | density, sustained metaphor, damage at the junction between two edits |
| the author, across documents | the recurrence note (§10 item 6) | a habit |

This repository has recorded a failure at each of the top two, and both were invisible one row at a
time:

- **Sustained metaphor.** A whole document explained through one borrowed domain. Every row passed on
  its own; fourteen rows shared a source domain. The aggregate column in §7 is what sees it, and
  nothing smaller can. `taxonomy.md` H6.
- **A recurring habit.** Two sentences on one page defending novelty, in a draft whose own writing
  notes forbid exactly that, by an author who had already been corrected on it twice. Deleting the
  two sentences does not hold, because the thing that produced them is larger than the page.

### 12.1 A family without a counter is telling you something, and it is not "unimportant"

Whether a family has a counter is a fact about the family, not about the tooling. But it has two
different causes, and they call for different tools, so the useful move is to say which one applies:

**No counter because of scope.** The defect is a property of the whole, so there is no unit to count.
Symmetry padding (B5), uniform cadence (B10) and sustained metaphor (H6) are all like this: nothing
is wrong at any one place, and the thing that is wrong only exists at document size. There is nothing
to list. Only a whole-document read finds it, which is what Pass D and the source-domain aggregate
are for.

**No counter because of precision.** There *is* a unit, and a script can find it, but hits are not
almost always real. Rule of three, conjunction density, bolded assertion and personification are all
like this. Here the script still earns its keep: it lists candidates with line numbers and refuses to
let one go unexamined, and a person decides each one. `--metaphor` and `--hits` exist for exactly
this case.

So the reading of "no script can count this" is **"only a person can see this"**, never "this matters
less". The two causes tell you which person-shaped check to reach for: a straight read of the whole
document, or a decision per candidate.

**Where to go looking for a rule that has collapsed two causes into one.** This repository wrote H6's
demotion reason as a precision problem, and the failure H6 actually missed was a scope problem. The
generalisation is a usable check on any rule, not just this one:

> **If a rule's stated reason comes from a single event, suspect that it has compressed its causes.**

The mechanism is ordinary. A rule gets written with one counter-example in hand, that counter-example
exposes one cause, and the other cause never enters the author's view at all, so the rule looks
complete and reads complete. Rules written after an incident are the obvious place to look, because
their text will faithfully record exactly the cause the incident happened to expose.

The snapshot guard in §11 is the same shape on a different axis. Whether the input is still the right
input has a scope of the whole file over time, and no per-line check sees it, so it needs its own
gate. That gate is `tools/freeze.py`, run before anything is applied.

The framing is not ours. It comes from the obligation-gates study this repository's worked example is
drawn from, whose claim is that an intent artifact decays in proportion to how many falsifying events
arrive outside whatever forces you to look at it. Applied to editing, the reading is direct. **The
part of a defect that lies outside what your check can see is unmeasurable by that check, and it
will read as absence.** The only useful response is another check
at the larger size, which is why this pipeline has four instead of one.

## Reference files

- `references/taxonomy.md`. The twelve marker families, merged, with source attribution per family.
- `references/decisions.md`. Per-hit decision procedure, exemption caps, keep conditions, `in-place` alternates.
- `references/titles.md`. Headings: name the content, do not narrate the reading path.
- `references/overcorrection.md`. The false-positive corpus: what looks like a tell and is not.
- `references/provenance.md`. What came from where, every conflict between the four, and the ruling.
- `references/lexicon.tsv`. 553 candidate rows, zh and en, each with replacement, note, and source project.
- `references/supplement.tsv`. Hand-kept rows only Humanizer-zh and natural-talk carry.
- `tools/measure.py`. Indicators, worksheet, before/after diff. No dependencies beyond python3.
- `tools/build_lexicon.py`. Rebuilds the lexicon from the four upstream checkouts, deduping by match.
- `worked-example/`. A full run on a real paper draft: measurements, audit, rewrite, re-measurement.
