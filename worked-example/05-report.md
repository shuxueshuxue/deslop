# Report: one deslop pass over *The Graveyard Reopens*

Input `00-input.md` · sha256 `021e54a9…2c2eb8` · `spexcode-base` commit `f07c9ac`.
Scene `academic` + paper pack · level `standard` · scope `structural` · citations `audit-only`.
Output `03-output.md`, produced by `apply.py` as 50 explicit (old, new) pairs, so everything not
listed there is byte-identical to the input.

## Indicators

| indicator | before | after | |
|---|---|---|---|
| **em dash** | **38** | **0** | |
| **staged reversal** | **7** | **1** | 1 named survivor |
| **editorial stance** | **7** | **2** | 2 named survivors |
| assistant residue | 0 | 0 | |
| knowledge-cutoff disclaimer | 0 | 0 | |
| emoji | 0 | 0 | ✓/✗ in tables are table glyphs |
| inline-title list item | 1 | 1 | 1 named survivor |
| `-ing` pseudo-analysis tail | 0 | 0 | |
| copula dodge | 0 | 0 | |
| false range | 0 | 0 | |
| signpost | 0 | 0 | cap 32 |
| lecture tone | 0 | 0 | cap 1 |
| exclamation | 0 | 0 | cap 48 |
| hedge stacking | 0 | 0 | cap 0 |
| paragraphs with mid-sentence bold | 2 | 2 | both legitimate; see the demotion note below |
| *sentence-length CV* | *0.655* | *0.645* | report-only |
| *conjunction density /1000* | *2.60* | *2.66* | report-only — **rose, and that is expected** |
| *nominalisation* | *0* | *0* | report-only |
| *mixed metaphor fields* | *1* | *1* | report-only |
| *rule-of-three candidates* | *9* | *9* | report-only, never gated |
| *lexicon candidates* | *8* | *7* | report-only |
| words of prose | 3462 | 3385 | −2.2% |
| sentences | 227 | 242 | +6.6% |

**More sentences, fewer words.** That is the signature of decompression rather than deletion: 38
clauses that had been hung off a dash became sentences, appositions, or parentheses, and the surplus
connective material went with them.

**Conjunction density rose.** Splitting a dashed clause into two sentences sometimes needs an
explicit connective the dash was carrying implicitly. This is exactly why the indicator is never
gated (`SKILL.md` §5.1): a threshold here would have penalised the fix.

## Named survivors

| indicator | what survives | why |
|---|---|---|
| staged reversal | §1, `…was a *precondition for landing the change*, not because writing it was cheap` | **Load-bearing argument.** The first half is a misconception the reader genuinely holds, having just read §1's argument that agents make capture cheap. Deleting it costs §1's two-stage structure its basis. Exemption 1 of 2. |
| staged reversal | §4.1, `So "load-bearing" is not a property of an artifact, a syntax, or a toolchain; it is a property of the gate.` | **Term definition.** Exemption 2 of 2. **It no longer registers on the counter** — rewriting the sentence put commas before the semicolon, which the pattern does not match. It is therefore a survivor the after-count of `1` does not include, and this line is how it stays visible. |
| editorial stance | §2.2, `The strongest available evidence for C0 is…` | Grades the evidence, not the sentence. A methodological statement an author defends. |
| editorial stance | §5.2, `We consider this the strongest feature of the design:` | Same class, and hedged. Removing `We consider` would have strengthened a claim. I cut this one on the first pass and put it back on the reread; see `02-audit.md`. |
| inline-title list item | §2.2, `- **targeting precision**: given a diff, does the graph identify…` | The Humanizer pattern is a bold label whose body restates the label. Here the body *defines* it. |
| mid-sentence bold | abstract `**trigger** / **enforce** / **expression**`; §5.3 `**F**` / `**X**` | Definition on first use, and variable names. |
| mixed metaphor field | `ecosystem`, once, §5.5 | One field, used literally about a software ecosystem. |

## What changed, by family

| family | found | acted | exempt / kept |
|---|---|---|---|
| F1 compression punctuation | 43 marks | 43 | 0 |
| B1 staged reversal | 9 (7 by scanner, 2 by reading) | 7 | 2 |
| A5 editorial stance | 13 (7 by scanner, 6 by reading) | 11 | 2 |
| A4 dramatized closer | 2 | 1 | 1 (`Each was technically sound. Each died.` — the delete test fails; both facts are load-bearing) |
| F3 bold | 8 bolded assertions | 8 | all labels and definitions kept |
| E7 latching | 1 (`available` twice in one sentence) | 1 | 0 |
| E3 vivid verb for an operation | 1 (`have bite`) | 1 | 0 |
| C5 `-ing` tail | 2 | 1 | 1 (`producing a deliberately approximate, task-scoped artifact` carries a fact) |
| B9 enumeration in prose | 2 | 0 | 2 (an abstract has no bullet lists; the `→` ladders are ordered scales) |

Ten of the em dashes and four of the reversals were found by reading rather than by the scanner. The scanner
is the cheap half.

## What the rereads caught

Pass A (fidelity) was clean on the first try: 80 numbers, 16 placeholders, 9 section references,
19 code spans and all 17 quoted runs byte-identical, and no modal or hedge changed.

Passes B and D were not clean, and the details are in `02-audit.md`. In summary:

- **Two of my own over-corrections**, both reverted: I had removed a hedged self-assessment (which
  strengthens a claim) and softened `the overwhelming majority` to `most` (which blurs someone
  else's measurement).
- **Two claims I had narrowed** while removing an adjacent flourish, both restored.
- **Three seam defects created by my own splits**: two sentences left opening with the same phrase
  (and, for one revision, the same phrase printed twice in a row), a broken parallel form in the
  contributions list, and a pronoun whose antecedent moved. Each of the three is correct read on its
  own line. Only the straight-through read finds them.
- **Pass B's mechanical half**: re-running the whole taxonomy over the 1,286 words of replacement
  text returned exactly the two hits I had deliberately carried over, and nothing else.

## Missing-basis notes (`audit-only`: flagged, not rewritten)

1. §2.2, `which is the failure mode this literature is already full of.` A claim about a literature
   with no citation. It is the author's own judgement rather than borrowed authority, so it is not an
   unsourced-citation violation, but it will want a reference.
2. §5.4, `Three independent studies report that LLM judges inflate accuracy worst exactly in the
   high-failure regime`. The studies are counted but not named. Consistent with the draft's stage, and
   flagged so it does not survive into a submission.

## Out of scope, by decision

`Notes on how to write this` is marked in the document as *not part of the paper*. It is drafting
guidance addressed to the author, which is the `status` scene, not `academic`. Left verbatim.

One of its notes is worth repeating, because the audit reached it independently. Note 5 says:
*"Be explicit that the convergence with concurrent work is good news. Do not defend novelty… it
should be stated as such without anxiety."* The two heaviest stance findings in §2.2 and §6 —
`the one that matters most and the one nobody has published` and
`**Three independent groups reaching the same direction is the strongest available evidence that the
direction is right.**` are both the paper defending its novelty in exactly the way its own note
warns against. The register audit and the author's intent point the same way.

## Caveats

- **This is a proposal, not an edit in place.** `00-input.md` belongs to a live session that is still
  writing the paper; the file on disk has already moved past this snapshot.
- **Register only.** This pass did not check whether the numbers are right, whether the §4.1 rows say
  what the cited studies found, whether every § cross-reference resolves, or whether the Olsson
  quotation is transcribed correctly. A cleaner register makes such defects *harder* to see, because
  the surrounding prose is now more confident. `SKILL.md` §11.
- **One exemption is invisible to the counter.** Recorded above rather than left to be rediscovered.
