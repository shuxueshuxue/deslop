<div align="center">
  <img src="assets/banner.png" width="900" alt="deslop">
</div>

<div align="center">

[中文（默认）](./README.md) | English

</div>
<br>

deslop is a Claude Code skill. Give it Chinese or English prose and it measures the text, audits it
line by line, rewrites it, and measures again, returning two sets of numbers you can check. It
changes how the text says things. It does not change what the text claims.

<br>

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/flow-dark.svg">
    <img src="assets/flow-light.svg" width="900" alt="deslop's nine steps: entry test, scene, protected spans, measure before, lexicon scan, line-by-line audit, apply, four rereads, measure after and report">
  </picture>
</div>

<br>

## What it looks for

Model prose has a fixed set of defects. They can be listed and they can be counted. They fall into
two groups, and the two sell different things.

**The first group proves the writer is clever.** The vivid analogy, the staged reversal, the short
assertion at the end of a paragraph, the word picked because it sounds learned. One question decides
any sentence:

> Is this **saying the thing**, or **being clever**?

**The second group proves the writer belongs.** Jargon, manufactured colloquialism, knowing asides,
shorthand only a colleague can catch. This group is harder to defend against. Elevated diction
sounds like posturing and a reader hears it immediately; jargon sounds like fluency and a reader
often does not, while the writer almost never does, because in their own ear it is the trade
spoken well. The test is the term-of-art pair: is there one agreed referent, and is there an
ordinary word for it? If both, it is a term and it stays. If not, it is jargon and it goes.

The goal is not simpler prose. Plain, careful wording is the target. Editing a document into
conversation is the other way to get it wrong. Write serious things with an unjaded eye, and be
willing to look clumsy doing it.

That last part is not a pose. It works against the failure documented under "Which way this tool
fails" below: what makes a sentence blunt is usually its qualifiers, so a pass optimising for
readability keeps pressure on removing them. A writer who already prefers the blunter version
narrows that path. The boundary is that clumsy is not sloppy. The tests are unchanged: delete it,
is any information lost, and can you answer "what specifically does this mean" with a fact.

All fourteen marker families are in [`references/taxonomy.md`](./references/taxonomy.md), each
attributed to the upstream project it came from.

## Install and run

```bash
git clone https://github.com/shuxueshuxue/deslop ~/.claude/skills/deslop
```

Once it is there, asking Claude Code to "take the AI register out of this" or invoking `/deslop`
triggers it. These run on their own, without a model:

```bash
python3 tools/measure.py FILE --scene academic      # measure before
python3 tools/measure.py FILE --hits                # lexicon candidates
python3 tools/measure.py FILE --metaphor            # borrowed-domain and physical-verb candidates
python3 tools/measure.py FILE --comments            # temporal and room-context candidates in comments
python3 tools/measure.py FILE --worksheet           # per-sentence audit worksheet
python3 tools/measure.py --diff before.json after.json
python3 evals/run.py                                # regression score for lexical detection
python3 tools/selfcheck.py                          # run the gates on this repository's own prose
```

## The procedure

The diagram above is the whole of it. Fixed order, no skipping. Three steps are worth calling out:

1. **Freeze before you touch anything.** Numbers, quotations, commands, error strings and
   attribution get marked, plus a separate record of relations: which number modifies which object,
   who did what, what is based on what. No word list can do this layer, and its damage is probably
   not recoverable from the finished text, because the finished text no longer holds the relations.
2. **Only step 06 must run in a fresh context.** Whatever wrote the text is a poor auditor of it,
   because it re-reads its own intent rather than the words on the page. In this repository's runs
   that has held for an agent as reliably as for a person. A human enters the loop twice, to decide
   the proposed-deletion list under `bounded` scope and to read the report.
3. **Four rereads, and they may not be merged.** They see different things. B checks the replacement
   text just written; D checks the junction between two edits, which the first three passes
   structurally cannot see because they work item by item.

## How far it edits is the author's call

**Scene sets the register target.** Seven of them, each with its own anchor and defaults: `chat`,
`status`, `docs`, `public-writing`, `academic`, `code-context`, `ui-copy`. A paper and a tooltip do
not want the same kind of plainness.

**Level and scope are independent axes.** Level is how hard the register gets pulled back
(`minimal` / `standard` / `aggressive`). Scope is whether a whole sentence may go
(`structural` / `bounded` / `in-place`). Collapsing them into one axis is the main reason a rewrite
either under-edits or quietly removes a third of the document. Under `bounded` the proposed
deletions go to the author, so length is never the tool's decision.

**A length cap is a third instrument and it has to be given.** A cap the editor invents is the same
one-third problem under a new name.

**Chinese has three register anchors, each settling one question.**

| anchor | what it settles |
|---|---|
| the dubbing register of Japanese film | syntax: whole sentences, subjects present, two-syllable verbs |
| the encyclopedia entry | pace and footing: no withheld surprises, disagreement attributed, confidence marked |
| the broadcast-news register | who is addressed, and how to stop: everyone, no assumed in-group, end when the facts end |

The third brings in as much as it gives: significance inflation, slogans, collective subjects with
no referent, formulaic positive closings. Only the first half is taken. The English anchors are
Wikipedia, Hacker News technical comments, and good papers.

The details are in [`SKILL.md`](./SKILL.md), which is the behavioural contract.

## What can be counted, and what cannot

An indicator earns a place in the counted set only if its hits are almost always real. When
measurement says otherwise it is demoted, and the reason is printed in every report so nobody
quietly puts it back.

| tier | authority | contents |
|---|---|---|
| **GATED** | drive to zero, or name every survivor | em dash · staged reversal · `顿号` · mid-prose `：` · assistant residue · knowledge-cutoff disclaimer · emoji · `-ing` pseudo-analysis · copula dodge · false range |
| **CAPPED** | only the excess is a finding | signposts · editorial stance · lecture tone · exclamations · stacked hedges · mid-sentence bold · inline-title list item · trailing contrastive tail |
| **REPORTED** | printed, never gates anything | sentence-length CV · conjunction density · nominalisation · metaphor fields · rule-of-three candidates · lexicon hits |

Five have been demoted on evidence:

- **Rule of three.** The defect is real, the counter is not. On the first document scanned, all five
  hits were ordinary enumerations.
- **Conjunction density.** Calibrated on 95 passages and the criterion inverted. Text that should
  *not* change had a median of 5.26 per 1000 against 0.00 for text that should. A matched pair pins
  it: a narrative post at 80.00 needed half its connectives cut, a migration doc at 81.08 needed none.
- **Bolded assertion.** After the counter was fixed it turned out not to catch the real defect, and
  a bolded assertion is shape-identical to a bolded list label. Only meaning separates them.
- **The trailing contrastive tail** and **the inline-title list item**, both demoted when the gates
  were first run over this repository's own prose. Six hits against one, and eleven against none.

**Four families never enter the counted set, for two different reasons.** One is scope: the defect
exists only at the size of the whole document, so there is no unit to count. A sustained metaphor
and a uniform cadence are like this, and only a straight read finds them. The other is precision:
there is a unit and a script can find it, but the hits are not almost always real. Personification
and the rule of three are like this, so the script still lists candidates with line numbers and a
person decides each one.

So "no script can count this" reads as "only a person can see this", never as "this matters less".

## A real run

`worked-example/` is a full pass over a real paper draft, with the input frozen in `00-input.md`.

| indicator | before | after |
|---|---|---|
| em dashes | 38 | **0** |
| staged reversals | 7 | 1 (exempt, named) |
| editorial stance | 7 | 2 (kept deliberately) |
| body words | 3462 | 3385 |
| sentences | 227 | 242 |

More sentences, fewer words. That is decompression rather than deletion: 38 clauses hanging off an
em dash became sentences, appositives or parentheses.

The part worth reading is the last section of `02-audit.md`. The second and fourth rereads reversed
seven of my own decisions. Two were over-correction, where deleting a hedged self-assessment
strengthened a claim the author had not made, and three were damage at a junction created by
splitting a sentence, which neither line-by-line pass saw.

## Which way this tool fails

Worth saying up front, because the pipeline causes it.

Readability is the goal, and **what makes a sentence blunt is exactly its conditions of
applicability**. `in a clean-entry container`, `a single run`, `a smoke test`, `autonomously`. These
look like any other clause, and across the signatures tried so far none has separated them from
ordinary prose, so a pass that goes well is likely to remove them by preference. Compare:

> In one smoke run, in a clean-entry container, a fresh session adopted the workflow zero times on its own.
>
> An agent passed every check and never used the workflow.

The second reads better, and the register instincts in this repository mostly prefer it. It is also
a different claim, and no check further down this pipeline reports the difference, because what
remains is well formed and correctly attributed.

The fix is order, not care. **Qualifiers are frozen before the register work starts**, marked once by
whoever knows where the number came from, after which the tooling only has to leave them alone. That
is why scope loss in relay runs at step 02 rather than in the audit, and why it annotates instead of
rewriting: the information it needs is not in the text.

## This repository runs it on itself

`python3 tools/selfcheck.py` runs the gates in the table above over the 15 files that speak in
deslop's own voice. Every hit is either fixed or named in
[`references/selfcheck.tsv`](./references/selfcheck.tsv) with its reason. An unnamed hit fails the
check, and so does a reason left behind after its hit is gone, which is what stops the list turning
into a blanket exemption.

The last two of the five demotions above came from that run. Zero em dashes across every file, which
is measured. No live metaphor introduced by the author was found, which is a read rather than a
count, for the reason given above.

`evals/run.py` scores lexical detection against 61 cases: 100% recall, with two known false
positives, both from deliberately broad rules (`你` in documents, `请求` under over-catching empathy).

## Where it came from

deslop's own half was the test, compression punctuation, the burden-of-proof flip, before/after
indicators and the over-correction pass. This version merged three more projects in.

| project | what it brought |
|---|---|
| [说人话 / shuorenhua](https://github.com/MrGeDiao/shuorenhua) | the control surface: scene, protected spans, tier, level × scope, unsourced-citation modes, two-stage reread, annotation mode |
| [natural-talk](https://github.com/chengzhi-c/natural-talk) | the principle/expression split, numeric caps, and the best anti-overcorrection material of the four |
| [Humanizer-zh](https://github.com/op7418/Humanizer-zh) | the Wikipedia *Signs of AI writing* pattern set: significance inflation, `-ing` pseudo-analysis, copula avoidance, synonym cycling, false ranges, formatting tells |

They contradicted each other in several places. Every ruling and its reason is in
[`references/provenance.md`](./references/provenance.md). The two that mattered: **"inject soul"**
was split into deslop (removal, on by default) and re-voice (addition, off by default, needs material
the author actually holds); and **conjunction density** lost its global threshold to measurement.

Public complaint threads are a fifth source and not a fifth merge: they report what strangers
notice rather than a ruleset. What was usable, with a citation per claim, is in
[`references/field-reports.md`](./references/field-reports.md). What came in was mostly the comment
and interface-text family and one check this repository had never run on itself. What was declined
is the most popular design in that space, handing the text to a second model to rewrite; the reason
and its cost are in the same file.

## Files

| | |
|---|---|
| [`SKILL.md`](./SKILL.md) | the behavioural contract, nine fixed steps |
| [`references/taxonomy.md`](./references/taxonomy.md) | fourteen marker families, each attributed to the project it came from |
| [`references/decisions.md`](./references/decisions.md) | per-hit decision procedure, exemption caps, keep conditions, `in-place` alternates |
| [`references/overcorrection.md`](./references/overcorrection.md) | the false-positive corpus: what looks like a tell and is not |
| [`references/code-comments.md`](./references/code-comments.md) | comments and interface text: who the reader is, and which step removes what |
| [`references/provenance.md`](./references/provenance.md) | what came from where, every conflict, and the ruling |
| [`references/field-reports.md`](./references/field-reports.md) | what the public complaint threads are worth, attributed line by line |
| [`references/lexicon.tsv`](./references/lexicon.tsv) | 625 candidate rows, zh and en, each with replacement, note and source project |
| [`references/selfcheck.tsv`](./references/selfcheck.tsv) | this repository's own surviving gate hits, each with a reason |
| [`tools/measure.py`](./tools/measure.py) | indicators, lexicon scan, metaphor worklist, comment worklist, worksheet, before/after diff |
| [`tools/selfcheck.py`](./tools/selfcheck.py) | runs the gates on this repository's own prose |
| [`docs/pipeline.html`](./docs/pipeline.html) | the diagram and the step notes, one 28 KB page, no external files |
| [`worked-example/`](./worked-example/) | one complete run |

The lexicon is generated by `tools/build_lexicon.py` from the four upstream checkouts rather than
typed by hand. Dedupe is by match, not by string equality, or the same word would carry four rows
under four names.

The artwork behind the banner was generated by an image model, with a prompt that asked for no
letters at all; the type is set afterwards in real fonts. Image models garble letterforms, and
garbled letterforms on a repository about removing AI tells would be the loudest tell available. What
the artwork draws is lines of set type, dense and ornamented on the left, thinning to a few clean
rules on the right, which is the subject drawn as itself rather than as an analogy for itself, the
one case the metaphor ban exempts. The artwork is kept at `assets/banner-art.jpg` and the
composition script is [`tools/make_banner.py`](./tools/make_banner.py), so the banner can be rebuilt.
The strapline carries no number that can go stale.

## License

MIT
