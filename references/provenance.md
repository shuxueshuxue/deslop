# What came from where, and who won

Four projects, four different pictures of the same problem. This file records what each brought,
where they contradicted each other, and which one this fusion follows. Nothing here is a compromise
for the sake of politeness: every conflict below has a ruling and a reason.

## What each project brought

### deslop: the thesis and the physics

- **The framing that makes the rest sortable**: AI register is the writer proving they are clever;
  plain is the target rather than the defect. Everything in the taxonomy is one form of that move.
- **Compression punctuation** (`——` / `、` / `：` / em dash) as one mechanism rather than three
  punctuation rules, with the test that decides each mark (*did it replace a full stop, or a line
  break?*) and the consequence that fixing them changes the document's shape.
- **The burden-of-proof flip**: keeping a sentence needs a reason, changing it does not.
- **Before/after counted indicators**, and the discipline that an indicator earns a count only if
  its hits are almost always real.
- **The over-correction pass**, including its sharpest observation: re-run the taxonomy on the words
  you just wrote, because `砍掉 → 压掉` and `击穿 → 打穿` are the same defect traded twice by
  someone who had just written the rule against it.
- **The final straight read** for damage at the seam between two edits, which no line-by-line pass
  can see.
- **The jargon-versus-term-of-art test**: one agreed referent, and no ordinary word for it.
- **Register anchors**: the Japanese dubbing register for Chinese; Wikipedia / HN / papers for English.
- **The honest limit**: it fixes how a text sounds and does not check whether it is right.

### 说人话 (shuorenhua): the control surface

- **Level × scope as two independent axes.** The single best idea in the four projects. "How hard do
  I pull the register back" and "may I delete a whole sentence" are different questions, and
  collapsing them is why rewrites either under-edit or silently shrink a document by a third.
- **`bounded` scope and the proposed-deletion list**, which hands length back to the user instead of
  letting the model decide it. The motivating fact is measured: the same long piece comes back at
  −18% or −39% depending on the run.
- **Protected spans and the relations ledger**, including the part no word list catches: which
  number modifies which object, which actor holds which goal, what is based on what.
- **The three unsourced-citation modes**, and the trap they close: deleting `40%` and leaving "it
  will be faster" converts a checkable false claim into an uncheckable vague one.
- **Twenty-five structural anti-patterns** with detection thresholds, default actions, keep
  conditions, and `in-place` alternates for each.
- **Two-stage reread**, fidelity before residual, in that order.
- **The cleaned-up landing contract**: what a sentence is allowed to become after the stance layer
  is gone, and the prohibition on filling the gap with a generic claim.
- **Annotation mode and 材料不足**, the verdict that says the problem is not the writing.
- **The calibration evidence.** The only project of the four that measured a criterion and then
  *deleted it* because the data said so (conjunction density; see below). That is the most
  transferable thing in this fusion.

### natural-talk: the layer split and the brakes

- **Principle layer versus expression layer.** Absolute rules that no scene exempts, against elastic
  rules with named caps. This is what stops "no em dashes" and "do not fabricate" from being treated
  as the same kind of rule.
- **Numeric caps** normalised to a 300–500 character reply: openers ≤1, courtesy closes ≤1,
  collaborative traces ≤1, lecture tone ≤1, signposts ≤2, dashes ≤2, exclamations ≤3.
- **The best anti-overcorrection material of the four**: six worked misjudgements, each with the
  wrong reading, the right reading, and the test that separates them.
- **Three fast tests**: delete test, friend test, substance test.
- **A self-checking harness** with positive *and* negative cases, and the rule that if a negative
  case does not fire or a positive case false-fires, the checker is the bug and gets fixed first.
- **The detection document.** signal aggregation for judging whether a text is model-written, which
  is a different job from rewriting it.

### Humanizer-zh: the pattern inventory

- **Wikipedia's *Signs of AI writing*** as a source with a citation requirement behind each entry,
  translated and worked into Chinese examples.
- **Patterns the other three do not have**: significance inflation, notability inflation, `-ing`
  pseudo-analysis, the "challenges and future prospects" section template, copula avoidance, synonym
  cycling, false ranges, curly quotes, title case, knowledge-cutoff disclaimers, generic positive
  conclusions, overqualification.
- **Formatting tells** treated as first-class: bold spam, inline-title vertical lists, emoji.
- **A scored rubric** (directness, rhythm, trust, authenticity, concision).
- **The diagnosis that voiceless prose is its own tell.** correct, and the one place its prescribed
  remedy had to be rejected.

---

## The conflicts, and the rulings

### 1. "Inject soul" versus "voice without invention": **the substantive one**

Humanizer-zh instructs the editor to add opinion, first person, admitted complexity, and mess. Its
own worked example replaces a flat paragraph about an experiment with invented reactions from an
invented developer community and an invented three-million-line figure.

deslop forbids adding an anecdote, metric, source, emotion, or joke to make a draft feel human.
shuorenhua forbids inventing a personal voice and forbids adding facts the original does not have.

**Ruling: the diagnosis is kept, the remedy is rejected, and the operation is split in two.**
`deslop` is removal and is default-on. `re-voice` is addition, is off by default, requires material
the author actually holds, and never runs in `docs`, `status`, `academic`, or `code-context`. When a
draft is clean and lifeless, the finding is *"this has no position — what do you actually think?"*
addressed to the author. It is not a position supplied on their behalf. `SKILL.md` §8.

Why this way round: two of the four projects treat inventing content as a hard boundary, and they are
right. In a *rewrite*, invented voice is fabrication with a friendlier coat. Humanizer-zh's advice
is sound for *drafting*, which is a different job.

### 2. Rule of three: three projects say break it, one says content decides

**Ruling: never counted; judged per instance, by natural-talk's test** (delete the numbering; is the
content still natural and complete?). deslop supplies the evidence: on the first document it scanned,
all five rule-of-three hits were ordinary enumerations. A number you cannot trust is worse than no
number. The tell is real; the counter is not.

### 3. Conjunction density: Humanizer says cut, shuorenhua measured it

Humanizer-zh's checklist says: *used connectives like 此外 / 然而? consider deleting.*

shuorenhua ran it over 95 passages split into "should change" and "should not change". The criterion
inverted. Median for should-not-change was 5.26 per 1000 against 0.00 for should-change; its maximum
(81.08) was higher than the other group's maximum (80.00). A matched pair pins it: a narrative post
at 80.00 needed half its connectives cut, a migration document at 81.08 needed none, because `docs`
and `status` carry condition and cause on explicit connectives.

**Ruling: shuorenhua wins, decisively. No global threshold exists.** Scene-gated to
`public-writing` narrative, judged by distribution rather than total. This is the model for how any
future indicator gets promoted or demoted here.

### 4. Register target: friend test versus document register

natural-talk targets *would you say this to a friend*. deslop targets Wikipedia, HN technical
comments, and papers, and warns explicitly that plain is not colloquial.

**Ruling: both, scene-scoped.** The friend test is the anchor for `chat` and nothing else. Document
scenes get the written anchors in `SKILL.md` §2. This is exactly why the fusion needs a scene layer:
without one, applying natural-talk's standard to a paper produces mush, and applying deslop's
standard to a chat reply produces a stiff, cold assistant.

### 5. Em dash: three different treatments

natural-talk: ≤2 per 300–500 characters. deslop: drive toward zero, name every survivor.
shuorenhua: density *and* position (first-sentence dash, two or more per paragraph, several
consecutive paragraphs carried by dashes).

**Ruling: all three, as layers, because they answer different questions.** The cap says how many.
The position rule says whether it is a template. deslop's test, *did it replace a full stop, or a
line break?*, is the only one that says **what to do**, which is why it is the one that changes the
document.

### 6. Academic register: three projects decline it, one takes it without guardrails

natural-talk and shuorenhua both list academic polishing as out of scope. Humanizer-zh does not
address it. deslop names papers as a target and holds them up as a register model, but has no
academic-specific rules.

**Ruling: a new scene and a new pack, built here.** `SKILL.md` §2.2. It exists because academic prose
has four false-positive traps none of the four handles: hedges are epistemic status and flattening
one is a principle-layer violation; passive is native; enumerations are contributions rather than
triads; bold marks defined terms. And two things it tightens: significance inflation and em dashes,
which academic prose absorbs so readily that they become the dominant tell.

### 7. Severity model: Tier versus force

shuorenhua separates Tier (how strongly a thing matched) from level (how hard you edit).
natural-talk's tiers are ordered by *how absolute the rule is*, which is a different axis again.

**Ruling: shuorenhua's Tier for density severity, natural-talk's split for the principle/expression
boundary.** They are orthogonal and both are needed. A Tier 1 hit inside a protected span still gets
kept; a principle-layer hit at any tier still gets acted on.

### 8. The scored rubric

Only Humanizer-zh has one (five dimensions, 50 points).

**Ruling: kept, demoted, and never reported alone.** A self-assigned 43/50 is an assertion; "em
dashes 38 → 3, staged reversals 7 → 2, both survivors named" is evidence. The rubric is a private
prompt for the editor, and the output contract in `SKILL.md` §10 requires the mechanical numbers.

### 9. Chinese `你` in documents

Only deslop has this rule.

**Ruling: kept, scene-gated.** Documents drop it by default; a reply written to one person is
dialogue and keeps it. Without the scene gate this rule would strip the second person out of exactly
the text where it belongs.

### 10. Word lists as boundaries

Every one of the four says some version of "this list is examples, not the boundary". shuorenhua says
it most precisely: what is being managed is the rhetorical *move*, not the literal string, so
re-wording a hit and continuing to do the same thing is still a hit. Conversely, a listed word
that carries real meaning in this sentence is protected.

**Ruling: unanimous, and it is why `references/lexicon.tsv` carries a note column and a source
column.** Suppressing the context-heavy rows would hide the over-corrections that the final pass
exists to catch.

---

## What was dropped, and why

- **Humanizer-zh's title-case rule** is kept for English only. Its own note says the pattern does not
  transfer to Chinese, which is correct.
- **Humanizer-zh's curly-quote rule** is narrowed: the tell in Chinese is Latin quotation marks where
  corner quotes belong, and the curl itself is not the issue.
- **natural-talk's absolute caps** are not applied as absolutes outside `chat`. Held as densities at
  the same ratio, they become meaningful for a document; held as absolutes, a 3000-word paper fails
  a rule calibrated on a chat reply.
- **shuorenhua's `automation/eval` harness** is not vendored. Its *conclusions* are (the calibration
  notes are printed in every `measure.py` report), and its idea of a positive/negative case corpus
  is the right next thing to build here. That corpus does not exist yet in this repository and this
  file says so rather than implying otherwise.
- **natural-talk's `tests/cases.json` self-check** is not vendored for the same reason. Its rule is
  adopted in spirit: if a negative case does not fire or a positive case false-fires, the checker is
  the bug and gets fixed before the rule does.

## The evidence standard this fusion inherits

From shuorenhua's calibration and deslop's demoted counters, one rule covers both:

> **An indicator earns a place in the counted set only if its hits are almost always real. When
> measurement says otherwise, the indicator gets demoted and the reason gets written down where the
> next person will read it.**

`tools/measure.py` prints both demotion notes in every report, so nobody re-promotes them quietly.
