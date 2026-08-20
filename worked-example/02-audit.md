# Audit: *The Graveyard Reopens*, draft skeleton

Input: `00-input.md`, sha256 `021e54a9…2c2eb8`, taken from `spexcode-base` at commit `f07c9ac`.

**The input is superseded.** Commit `1c8c2a1` changed the file (current hash `c4037d0d…`), retracting
two claims that this pass preserved verbatim and backfilling real measurements. A sibling draft may
replace the file entirely. Do not merge this output; see the status section in `05-report.md`.

## Frame

| | |
|---|---|
| scene | `academic` + the paper scene pack (`SKILL.md` §2.2) |
| register anchor | a good methods section: direct, unadorned, specific |
| level | `standard` — the arguments are settled and the information skeleton is sound; the register is the defect |
| scope | `structural` — decompressing 38 em dashes requires splitting sentences, which `bounded` and `in-place` forbid |
| unsourced citations | `audit-only`, as `academic` always is |
| output | one recommended version, plus this table and the before/after indicators |

**This is a proposal, not an edit in place.** The source file belongs to a live session that is still
writing it. `03-output.md` is a separate artifact.

## Protected spans, frozen before reading for style

- **Block quotes**. Olsson/Ericsson/Wingkvist, Grudin, the reflexion-models quote, the Rust RFC
  README line. Verbatim, including the `**not a lack of methods or tools**` staged reversal inside
  the Olsson quote, which is *their* sentence and is excluded from the author's counts.
- **Every number**. ~5%, .94, .21, k=1..10, 22, 90.1%, 70.4%, 49 of 54, 3.5%, κ = 0.163, 2–5 hours,
  three-quarters, eight axes, five surfaces, nine probe builds, n=1, and every `[N]` / `[M]` / `[K]`.
- **Placeholders**. `[TO MEASURE]`, `[DECISION PENDING]`, `[TO WRITE]`, `[System name]`, `[metric]`.
- **Names**. Murphy, Notkin, Sullivan, Terra, Valente, Olsson, Ericsson, Wingkvist, Grudin, Gotel,
  Finkelstein, Fagan, RFC/PEP/KEP, Rust, TypeScript, ArchUnit, SACC, MDA.
- **Terms of art**. trigger, enforce, expression, scope, rot law, reflexion models, against-prior,
  precision@k, drift, conformance, traceability, design rationale, `.d.ts`, `spec lint`.
- **Hedges, all of them**. *We argue*, *should grow*, *would falsify*, *appears*, *may*, *is
  consistent with*. In `academic` these carry epistemic status and strengthening one is a
  principle-layer violation, not a style call.
- **§ cross-references**. §2.1, §2.2, §3, §4, §4.2, §5, §5.2.

**Relations ledger.** Which cost class attaches to which paradigm (Table 1); which axis each existing
system is fixed at (§3.1); which row of the §4.1 table is the control pair (rows 4 and 5, not 3 and 4);
which of the three related-work groups lacks which arm. None of these may be simplified or merged.

## Findings

52 findings. `?` marks an uncertain call reported rather than dropped.

### F1: Compression punctuation (38 em dashes)

The dominant defect, and the one that changes the document. Classified by deslop's test: *did the
dash replace a full stop, or a line break?*

| # | location | verbatim | what the dash replaced | replacement |
|---|---|---|---|---|
| 1 | §status, L5 | `placeholders marked` `[TO MEASURE]` `— they state what goes there` | full stop | two sentences |
| 2 | abstract, L11 | `is a *human* cost — the effort of maintaining a mapping, of writing down…` | full stop before a three-item list | second sentence naming the three costs |
| 3–4 | abstract, L13 | `three independent literatures — traceability, design rationale, and executable specification — we find` | parenthesis pair inside an already four-clause sentence | split; the list becomes its own clause |
| 5–6 | abstract, L13 | `three design axes — **trigger** (…), **enforce** (…), and **expression** (…) — and show that` | parenthesis pair | split into two sentences |
| 7 | §1, L28 | `is not writing for a stranger — with no memory across sessions` | full stop | see F2 |
| 8–9 | §1, L32 | `that survived a decade — the RFC, PEP and KEP processes are the only ones we found — survived because` | parenthesis pair | split; the finding gets its own sentence |
| 10–14 | §1.1, L38–42 | `- **C0 — The revival claim…**` ×5 | a label separator, i.e. a line break | `- **C0.** …` |
| 15–16 | §1.1, L40 | `existing systems — inline types, `.d.ts` stubs, … — are points rather than rivals` | parenthesis pair | recast as a sentence |
| 17 | Table 1, L55 | `✗ (removed — the writer *is* the reader)` | in-cell full stop | `;` |
| 18–19 | §2.1, L70 | `partly of the mapping cost — which agents remove — but the technique's` | parenthesis pair | commas, then split |
| 20–21 | §2.2, L74 | `the artifact that killed SACC — the mapping from code to intended structure — is maintained` | apposition | commas (correct form for an apposition, not a substitution) |
| 22 | §2.2 new, L87 | `**Pre-define the denominator** — the set of eligible…` | label separator | `**Pre-define the denominator.**` |
| 23–24 | §3, L99 | `An intent artifact — a comment, a spec node, a lint rule, a type — can be characterised` | apposition carrying the definition | split: the list becomes the subject of its own sentence |
| 25–28 | §3, L101/111/113/123 | `**Trigger — does an event bring you into contact with it?**` ×4 | label separator on what is really a heading | `**Trigger.** Does an event…` |
| 29–30 | §3 tables, L105/106 | `no — always present, never fires` | in-cell full stop | parentheses |
| 31 | §3, L109 | `remains in context throughout — joint compliance falls from .94 to .21` | colon before evidence | colon (English evidence colon is not the staging colon; see note) |
| 32 | §3, L115 | `The converse does not hold — a fully machine-decidable artifact` | full stop | two sentences |
| 33 | §3.1, L139 | `**A blocking check nobody runs blocks nothing** — this is not a joke but` | full stop | two sentences; see F3 |
| 34 | §4.1 table, L155 | `≈ 0 — *almost nothing falsifies it*` | in-cell parenthesis | parentheses |
| 35–36 | §4.1, L160 | `The best-known finding in this area — that abstract documentation is judged accurate… — has been handled` | apposition | commas |
| 37 | §5.1 table, L185 | `baseline — the rule exists and is stated` | in-cell full stop | `;` |
| 38 | §5.4, L221 | `These diverge sharply — one study's per-requirement metric *rose*` | full stop | two sentences |
| 39 | §5.5, L227 | `It has no enforce axis — which is our contribution` | full stop | two sentences |
| 40 | §6, L252 | `must be placed *outside* the agent — and does not test it` | dramatic beat | comma |
| 41–42 | §6, L253 | `a single cell of our cube — expression and enforce both fixed… — and therefore cannot separate` | apposition | commas |
| 43 | §7, L268 | `fleet observability data — host memory pressure, process health, session lifecycle events` | colon before a list | colon |

**Note on the evidence colon.** English uses `:` to introduce evidence and that is not the Chinese
mid-prose `：` this taxonomy counts (`taxonomy.md` F1). Rows 31 and 43 keep a colon; nothing was
compressed by doing so.

**Named survivors: 0 em dashes in the paper body.** The `Notes on how to write this` section, which
the document itself marks *not part of the paper*, is left verbatim by scope decision and contains
none.

### F2: Staged reversals (7 found, 2 exempt, 5 rewritten)

| # | location | verbatim | ruling |
|---|---|---|---|
| 1 | §1, L28 | `An agent writing down a rationale is not writing for a stranger — … it is writing for itself.` | rewrite → `An agent writing down a rationale has no memory across sessions, so the future reader it is writing for is itself.` |
| 2 | §1, L32 | `survived because writing the record was a precondition for landing the change, not because writing it was cheap` | **EXEMPT — load-bearing argument.** The first half is a misconception the reader genuinely holds, having just read §1's argument that agents make capture cheap. Deleting it costs §1's two-stage structure its basis. |
| 3 | §2.2, L93 | `which is a literature argument, not a measurement` | rewrite → `which argues from the literature rather than from measurement` |
| 4 | §3, L121 | `That is an expressiveness ceiling, not an enforcement ceiling` | rewrite → two sentences. **This is the exemption cap doing work:** three instances each had a defensible claim to exemption, the cap is two, and `decisions.md` says that when every instance can justify itself the shape is what is carrying the argument. This was the weakest of the three and it decomposes cleanly. |
| 5 | §4.1, L164 | `"load-bearing" is not a property of an artifact, a syntax, or a toolchain. It is a property of the gate.` | **EXEMPT — term definition.** Corrects a misreading of what the term names; the two-sentence form is the definition, not a flourish. |
| 6 | §5.7, L242 | `The dependent variable is not a memorisable answer; the residual risk is repository familiarity` | rewrite → `The dependent variable is a behaviour rather than a memorisable answer, so the residual risk is repository familiarity.` |
| 7 | §6, L255 | `Our contribution is not to establish it a fourth time; it is to separate the axes` | rewrite → drop the first half. The preceding sentence already says three groups found the direction, so nothing is lost. |

Two more of the same shape, below the reporting threshold in the scanner, were also recast:
`the positioning is *convergent*, not competitive` (§6) → `convergent rather than competitive`; and
`Prompt is therefore the **baseline**, not an arm` (§5.1) → `the baseline rather than an arm`.

### F3: Editorial stance and self-assessment (7 found, 5 rewritten, 2 kept)

| # | location | verbatim | ruling |
|---|---|---|---|
| 1 | §2.1, L70 | `We note one instructive near-miss.` | rewrite. `instructive` is the author scoring their own example. → `Reflexion models are a near-miss.` |
| 2 | §2.2, L74 | `The strongest available evidence for C0 is…` | **keep `?`**. It grades the evidence, which is a methodological statement an author is entitled to make and defend, and not a grade on their own sentence. |
| 3 | §2.2, L80 | `The third of these is the one that matters most and the one nobody has published:` | rewrite. Two defects: a self-grade, and a novelty defence that the draft's own writing note 5 warns against (*"Do not defend novelty"*). → `The third bounds the rest, and has not been reported for any comparable system:` |
| 4 | §3, L109 | `We stress that *presence in context is not a trigger*.` | rewrite → `Presence in context is not a trigger.` The stress is the claim; announcing it adds nothing. |
| 5 | §3.1, L139 | `— this is not a joke but the cleanest available separation` | rewrite. The author defending their own line against a reading nobody was going to make (`taxonomy.md` J3). Cut the defence. |
| 6 | §4.1, L164 | `This licenses a restatement worth keeping:` | rewrite → `This restates what "load-bearing" means.` |
| 7 | §5.2, L198 | `We consider this the strongest feature of the design:` | rewrite → `The design can therefore distinguish…` |

Also handled, same family, below the scanner's phrase list:

- §5.3 `The construction constraint is severe and it is forced by…` → cut `severe and it is`. Intensity
  substituting for argument; the four conditions that follow *show* the severity.
- §5.3 `We note that this criterion is equivalent to…` → cut `We note that`. Throat-clearing.
- §5.4 `The precedent is stark:` → cut `stark`. The fact that follows is the point.
- §5.4 `These diverge sharply` → cut `sharply`. The numbers that follow carry it.
- §6 `the overwhelming majority of violations` → `most violations`. No number is attached to the
  superlative; the 3.5% figure belongs to the other half of the sentence.
- §7 `The survey's strongest single principle applies to us:` → `One principle from the survey applies
  to us:`. A self-grade on the authors' own companion artifact.

### F4: Dramatized closers (2)

| # | location | verbatim | ruling |
|---|---|---|---|
| 1 | §3, L109 | `Being available is not being consulted.` | **delete.** It restates the paragraph's opening sentence in different words, with the evidence sandwiched between. Delete test: no information lost. |
| 2 | §1, L11 | `Each was technically sound. Each died.` | **keep `?`** — reads as a dramatic fragment pair, but the delete test fails: both facts are load-bearing and stated nowhere else. Kept as written. |

### F5: Bold overuse (11 paragraphs above the cap)

Bold is doing three different jobs in this draft. Two of them are legitimate and one is the tell.

**Keep, definition on first use** (`SKILL.md` §2.2, named exemption): `**trigger**`, `**enforce**`,
`**expression**` in the abstract and §3; `**F**` and `**X**` in the well-formedness conditions.

**Keep, list-item labels:** `**Threat.**`, `**Fork.**`, `**Build.**`, `**Prediction.**`,
`**Rationale.**`, `**Deterministic checks only**`, `**Degenerate compliance.**` and the rest of the
§5.7 threat labels, `**C0**`–`**C4**`.

**Remove, whole sentences bolded for emphasis** (8 instances):

| location | verbatim |
|---|---|
| §1, L28 | `**Every one of these is a labour cost, and it is a labour cost that a language-model agent does not pay.**` |
| §1, L32 | `**It does not follow that the paradigms simply return.**` |
| §1, L34 | `**Agents make the artifact affordable. Something else has to make it survive.**` |
| §2.2, L80 | `**an enforcement mechanism's strength is bounded above by its targeting precision.**` |
| §3, L115 | `**you cannot mechanically enforce prose.**` |
| §3.1, L139 | `**A blocking check nobody runs blocks nothing**` |
| §4, L145–147 | the three clauses of the law, bolded *inside* a block quote — doubled emphasis |
| §4.2, L170–171 | falsifiers 3 and 4 bolded while 1 and 2 are not, which reads as a ranking the list does not state |
| §5.2, L198 | `**A null interaction falsifies the mechanism**` |
| §6, L255 | `**Three independent groups reaching the same direction is the strongest available evidence…**` |

Every one of these sentences survives unbolded. If a sentence needs bold to land, the sentence is the
problem.

### F6: Latching (1)

§3.1, L139: `the cleanest **available** separation … it is **available** in a deployed system`.
The same word twice in one sentence in two different senses. → `…and it exists in a deployed system`.

### F7: Vivid verb standing in for the operation (1)

§5.3, L213: `the pairs that have bite`. → `the pairs where the rule changes what a compliant
implementation looks like`. Says the operation instead of gesturing at it.

### F8: `-ing` pseudo-analysis tail (2, both `?`)

- §2.1, L70: `producing a deliberately approximate, task-scoped artifact`. **Keep.** It carries a
  fact about what the technique yields, and is not decoration.
- §5.5, L227: `making this additive rather than a reconstruction`. Rewritten into its own clause when
  the sentence split anyway (F1 #39).

### F9: Enumerations in running prose (2, both kept and named)

- Abstract, L11: five paradigms strung on commas. In an abstract a bullet list is not available, and
  Table 1 does the structured version. **Keep.**
- §3, L113/123: the expression and scope ladders written with `→` in running prose. These are ordered
  scales where the arrow *is* the semantics. **Keep.**

### F10: Inline-title list item (1, kept)

§2.2: `- **targeting precision**: given a diff, does the graph identify the intent node that should
have been updated?` The Humanizer pattern is a bold label whose body then restates the label. Here the
body *defines* the label. **Keep, named.**

## Missing-basis notes (`audit-only`, no rewriting)

Two claims carry no attribution and were left exactly as the author wrote them:

1. §2.2 new material: `which is the failure mode this literature is already full of.` A claim about
   the state of a literature, with no citation. It is the author's own judgement, not borrowed
   authority, so the unsourced-citation rule does not apply, but it will want a reference.
2. §5.4: `Three independent studies report that LLM judges inflate accuracy worst exactly in the
   high-failure regime`. The studies are counted but not named. Consistent with the draft's stage, and
   flagged so it does not survive into a submission.

## Out of scope, by decision

The final section, `Notes on how to write this`, is marked in the document as *not part of the paper*.
It is drafting guidance addressed to the author, which puts it in the `status` scene, not `academic`.
Left verbatim. Its two `X, not Y` constructions are therefore named survivors in the after-count, not
misses.

## What this audit did not check

Register only. It did not verify that the numbers are right, that §4.1's table rows say what the cited
studies found, that every § cross-reference points where it claims, or that the Olsson quotation is
transcribed correctly. Those need a comprehension pass with a different brief (`SKILL.md` §11), and
this rewrite makes the surrounding prose more confident, which makes such defects *harder* to see.

---

## Pass B and Pass D corrections

The rereads changed seven rulings. Recorded here rather than edited into the table above, because
what the second and fourth passes catch is the point of having them.

### From Pass B: over-correction

| # | what I had done | why it was wrong | corrected to |
|---|---|---|---|
| 1 | `We consider this the strongest feature of the design:` → `The design can therefore distinguish…` | **Reverted by me, then reinstated by the author.** My reasoning for reverting was that removing a hedged self-assessment strengthens a claim I do not own. That reasoning was right about the limit of my authority and wrong about the outcome. The author ruled: it grades their own design rather than the evidence, and the clause that follows already shows why the feature is strong. **Whoever owns the claim decides.** The consistency argument against `The strongest available evidence` does not hold either, because that one grades the evidence base, which the author kept. | cut |
| 2 | `the overwhelming majority of violations` → `most violations` | **My over-correction.** The phrase reports the magnitude of someone else's measurement. Softening it blurs a protected quantity. Only the em dash in that sentence was ever the finding. | reverted, kept verbatim |
| 3 | `the one nobody has published` → `has not been reported for any comparable system` | I narrowed a claim while removing an adjacent self-grade. The self-grade (`the one that matters most`) was the finding; the novelty claim was not mine to shrink. | `The third has not been published, and it bounds the others:` |
| 4 | `the pairs that have bite` → `the pairs where the rule changes what a compliant implementation looks like` | Replacing the vivid verb was right, but my replacement paraphrased the claim rather than naming the operation. | `precisely the pairs where the rule constrains the implementation` |

The rule these four settle, now written into `decisions.md`: **keep a self-assessment that the
following clause justifies; cut one that nothing follows from.** `We consider this the strongest
feature of the design:` is followed by what the feature does. `The survey's strongest single
principle applies to us:` is followed by a principle that applies regardless of its rank.

### From Pass D: damage at the seam between two edits

| # | what the split produced | fix |
|---|---|---|
| 5 | Abstract: `…handles only by exception. The law makes a falsifiable prediction:` — my split left two consecutive sentences both opening `The law`, and an intermediate revision briefly produced the phrase **twice in a row**. Neither line-by-line pass saw it; both sentences are correct on their own. | merged into one sentence: `…only by exception, and it makes a falsifiable prediction:` |
| 6 | §1.1: turning `**C0 — …**` into `**C0. …**` broke the list's parallel form. C0, C1, C2 and C4 ended `.**`; C3 alone continued `**C3. An experimental program** whose primary result…` (`titles.md` rule 7). | `- **C3. An experimental program.** Its primary result is an *interaction*: …` |
| 7 | §3.1: `**A blocking check nobody runs blocks nothing** — this is not a joke but…` → `…blocks nothing. That is the cleanest…`. In the original, `this` referred to *the pair of table rows*. After the split, `That` reads as referring to the slogan. A dangling reference created by my own edit. | `That pair is the cleanest available separation…` |

Also from Pass D: `"Load-bearing", then, is not a property…` capitalised a scare-quoted term at the
start of a sentence, which made the quoted run differ from the original by one character. Recast to
`So "load-bearing" is not a property…`. All 17 quoted runs are now byte-identical to the input.

### A third demoted indicator

The first after-measurement reported **11 paragraphs with more than one bold run**, above the cap.
Inspecting the eleven, nine were label lists (`**C0.**`, `**Threat.**`, `**Degenerate compliance.**`)
and one was bold *inside the Olsson quotation*, which belongs to Olsson.

Two conclusions, and the second is the more useful:

1. The counter was charging the author for structure and for someone else's emphasis.
   `tools/measure.py` now strips a leading bold label from each paragraph and list item, and excludes
   blockquote lines, before counting. Corrected, the input scores **2**, both legitimate: the axis
   names on first use, and `**F**` / `**X**` in the well-formedness conditions. natural-talk's rule
   applies: *if a negative case false-fires, the checker is the bug, and the checker gets fixed
   first.*
2. The corrected counter does not detect the defect that actually mattered here. The tell was
   **eight whole sentences bolded for emphasis**, and each of those is a *single* bold run in its
   paragraph, so `>1 bold run` never sees them. Trying to catch them mechanically fails on precision:
   `**It does not follow that the paradigms simply return.**` and
   `**Report both per-rule and all-pass rates.**` are structurally identical (bold at the start of a
   block, sentence-terminated, followed by more text). Only meaning separates a label from an
   assertion.

   So **bolded assertion joins personification as an audit-table family with no counter**, for the
   same reason: a word-list or shape counter would manufacture a number rather than measure one.
   Third demotion, same rule as the other two, recorded in `SKILL.md` §5.1.
