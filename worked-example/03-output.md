# The Graveyard Reopens

### Why Failed Software-Engineering Paradigms Work for Agents, and the Law That Decides Whether They Survive

**Status: draft skeleton.** Sections 1–4 are written at close to final register because the arguments are settled. Sections 5–8 are structured placeholders marked `[TO MEASURE]`. They state what goes there and what would falsify it, but contain no results. Nothing in this document reports an experiment we have run.

---

## Abstract

Software engineering has a graveyard: architecture conformance checking, design-rationale capture, requirements traceability, formal inspection, heavyweight specification. Each was technically sound. Each died. We observe that in every case the recorded cause of death is a *human* cost. Someone has to maintain a mapping, write down a rationale whose beneficiary is a stranger, or attend a meeting. LLM coding agents do not bear those costs. We argue this makes the graveyard's inhabitants viable again, and we present a working system that has run two of them for [N] months as an existence proof.

But affordability is not survival. We surveyed three independent literatures: traceability, design rationale, and executable specification. They converge, each as a residual rather than a thesis, on a single variable: whether something stops you when you do not consult the artifact. We formalise this as a rot law over three design axes. **Trigger** asks whether an event brings you into contact, **enforce** asks whether you can proceed anyway, and **expression** asks how much of your intent can enter the mechanism at all. The law explains cases the existing literature handles only by exception, and it makes a falsifiable prediction: the effect of trigger and enforce should grow with the *scope* of the claim, and vanish where scope is local.

We contribute (i) the revival argument with a discriminator that says which dead paradigms return and which do not, (ii) the rot law and its design space, (iii) an experimental program that tests the law by varying trigger × enforce × expression under scope stratification, and (iv) an open, deployed instrument.

---

## 1. Introduction

Ask a software engineer what happened to architectural conformance checking and you will not hear that it was wrong. Murphy, Notkin and Sullivan's reflexion models worked; Terra and Valente's dependency constraint language worked; the tools shipped. What happened is recorded plainly in the field's own retrospectives:

> "a major reason why SACC has not reached widespread adoption is **not a lack of methods or tools**, but rather that it requires a mapping from the source code entities to the modules of the intended architecture. Generally, such a mapping does not exist, and if it does, **it is not actively maintained**. To create or even validate a mapping manually requires too much effort."
> — Olsson, Ericsson & Wingkvist, *JSS* 2022

The same shape appears elsewhere. Design rationale capture failed on what Grudin named in 1988 as the disparity "between those who will benefit from an application and those who must do additional work to support it." Requirements traceability failed on Gotel and Finkelstein's *establish and end-use conflict*. Fagan's inspection meeting, the most ceremonial part of the most rigorous review process ever standardised, contributed a measured ~5% of the defects it was credited with and cost the most of any phase.

Every one of these is a labour cost, and it is a labour cost that a language-model agent does not pay. An agent maintaining a mapping does not find it tedious. An agent writing down a rationale has no memory across sessions, so the future reader it is writing for is itself. An agent does not attend meetings.

This paper takes that observation seriously and asks what follows.

It does not follow that the paradigms simply return. Our second finding, from the same survey, is that cheap capture was never sufficient. Only three design-rationale corpora in our survey survived a decade: the RFC, PEP and KEP processes. Each survived because writing the record was a *precondition for landing the change*, not because writing it was cheap. Rust's RFC README states the mechanism without ceremony: submit an implementation PR without an RFC and "it may be closed with a polite request to submit an RFC first."

So the structure is two-stage. Agents make the artifact affordable, and something else has to make it survive. The bulk of this paper is about what that something else is, when it is necessary, and how much of it you can have.

### 1.1 Contributions

- **C0. The revival claim, with a discriminator.** Failed paradigms whose cause of death was labour cost return under agent economics; those whose cause was conceptual or representational do not. We test the discriminator against the historical record and provide an n=1 existence proof from a deployed system.
- **C1. The rot law.** An intent artifact decays at a rate proportional to the arrival of falsifying events *outside its enforcement radius*, where the radius is the product of trigger and enforce, and applies only to the fraction of intent that expression can carry. We show this explains the field's exceptions without special cases.
- **C2. A three-axis design space.** Inline types, `.d.ts` stubs, `CLAUDE.md`, ArchUnit, compiled constraint checkers, and our own system are points in that space rather than rivals.
- **C3. An experimental program.** Its primary result is an *interaction*: the effect of trigger and enforce should scale with claim scope. A null interaction falsifies the mechanism we propose.
- **C4. An instrument.** [System name], deployed across [N] repositories for [M] months, with [K] intent nodes under continuous mechanical checking.

---

## 2. The graveyard and the causes of death

We surveyed eight areas of the software-engineering literature, prioritising peer-reviewed work over recent preprints and instructing two of the eight explicitly to find disconfirming evidence. The full survey, with a ledger of citations we could not verify, accompanies this paper.

**Table 1. Causes of death.**

| Paradigm | Recorded cause of death | Cost class | Survives in agents? |
|---|---|---|---|
| Static architecture conformance | mapping "does not exist, and if it does, is not actively maintained" | labour | ✗ (removed) |
| Design rationale capture | Grudin's disparity: author pays, unknown future reader benefits | labour | ✗ (removed; the writer *is* the reader) |
| Requirements traceability | establish/end-use conflict; "lack of direct perceived benefit to the main development process" | labour | ✗ (removed) |
| Fagan inspection meetings | meeting gain rate ~5% at the highest cost of any phase | labour | ✗ (removed) |
| Heavyweight specification / MDA | "a fairly complete architecture specification must be produced beforehand" | labour + conceptual | partially |
| Waterfall | requirements change | conceptual | ✓ (still fatal) |
| CASE round-tripping | representational, not economic | conceptual | ✓ (still fatal) |

### 2.1 The discriminator

The table's fourth column is the paper's first testable claim:

> **A dead paradigm returns under agent economics if and only if its recorded cause of death was a labour cost.**

This is checkable against the historical record and it is falsifiable in both directions: a paradigm that died of labour cost and *does not* return refutes it, as does one that died of a conceptual problem and does return.

Reflexion models are a near-miss. They died partly of the mapping cost, which agents remove. But the technique's stated purpose was to *"exploit, rather than remove, the drift between design and implementation,"* producing a deliberately approximate, task-scoped artifact. The cost returns; the purpose does not transfer. Citing reflexion models as a precedent for enforcement cites them against their authors' own claim.

### 2.2 Existence proof

`[TO MEASURE]` The strongest available evidence for C0 is a system in which the artifact that killed SACC, the mapping from code to intended structure, is maintained by agents rather than by people. We report, from [N] months of production history across [M] repositories:

- the fraction of governed files carrying a live, correct mapping over time
- the maintenance cost per commit, measured as [metric]
- **targeting precision**: given a diff, does the graph identify the intent node that should have been updated? Reported as precision@k against the node actually updated.
- the growth curve of the acknowledgement/suppression list

The third has not been published, and it bounds the others: an enforcement mechanism's strength is bounded above by its targeting precision. A gate that can only say "update some spec" is satisfiable by updating the wrong one.

**The trigger separation is observational, and must be reported as such.** Manually-run and hook-run instances of the *same* checks over the *same* artifacts differ in exactly one coordinate, which makes them the cleanest available *mechanism* contrast. It does not make them an experiment. Assignment is not random: whether an author chooses to run the check by hand, whether the hook was installed at all, whether it was bypassed through the project's documented escape variable, whether a CI path also fired, and what kind of change was being made all shape exposure.

The design that keeps this honest costs almost nothing and must be fixed before looking at outcomes:

1. **Pre-define the denominator.** The set of eligible spec-governed commits, fixed by a stated rule rather than by what turns out to have data.
2. **Record all three paths per commit**, independently: did the pre-commit hook fire, was the check run manually, did a CI gate evaluate it. Absence of a record is its own category and must not read as "did not fire."
3. **Report bypass explicitly.** The project ships a documented skip variable. Its usage rate is a result in its own right: the suppression-growth measurement the survey identified as the missing health metric for any rules-as-tests system. The same instrumentation yields both.

Framed this way the comparison is a well-characterised observational study with a documented exposure record. Framed carelessly it is a historical correlation reported as a causal effect, which is the failure mode this literature is already full of.

**Threat.** This is n=1 and the authors built the system. It is an existence proof, not a demonstration of generality; generality rests on the discriminator in §2.1, which argues from the literature rather than from measurement.

---

## 3. Three axes

An intent artifact can be a comment, a spec node, a lint rule, or a type. Each can be characterised by three independent design choices, and compared against one property of the claim it carries.

**Trigger.** Does an event bring you into contact with it?

| level | examples | fires? |
|---|---|---|
| ambient | system prompt, `CLAUDE.md`, `AGENTS.md` | no (always present, never fires) |
| on-demand | a skill, a documentation site, a manually-run linter | no (present, must be fetched) |
| event-fired | a pre-commit check, a compiler diagnostic | **yes** |

*Presence in context is not a trigger.* Instruction-following collapses as the number of simultaneous constraints rises, even though every constraint remains in context throughout: joint compliance falls from .94 to .21 over k=1..10 for one frontier model, while per-constraint compliance stays near-flat.

**Enforce.** Can you proceed anyway? None, warning, or blocking. This is the axis the literature converged on, and the one existing agent work has not varied: five delivery surfaces have been compared, all of them soft.

**Expression.** How much of your intent can enter the mechanism at all? Prose → structured prose → controlled natural language → semi-formal DSL → machine-decidable query → executable code → formal specification.

Expression is not independent of enforce: you cannot mechanically enforce prose. Expression gates the maximum achievable enforce. The converse does not hold. A fully machine-decidable artifact with zero enforcement is a real and common configuration, and TypeScript's `.d.ts` declaration files are the cleanest instance. The design space is therefore a cube with a triangular constraint on one face; a naive full factorial has empty cells, and the boundary itself is a finding.

Expression carries a cost the other two do not:

> **The more formal the representation, the higher its decidability, and the less it can say.**

Practitioners typically specify on the order of 22 kinds of quality requirement; industrial conformance tools handle at most three of them. Expressiveness sets that ceiling. Enforcement does not, which is why "enforce everything" is not a strategy.

**Scope.** How far does the claim reach? Local (these lines) → module (this file) → cross-module ("only X may write to Y") → system ("no module may depend on a higher layer"). Scope is *not* a design axis: it is fixed by what you are trying to say. It is the quantity the other three are compared against.

### 3.1 Existing systems as points

| system | trigger | enforce | expression |
|---|---|---|---|
| inline code comment | ambient (local only) | none | prose |
| `CLAUDE.md` / `AGENTS.md` | ambient | none | prose |
| documentation site | on-demand | none | prose |
| `.d.ts` declaration file | on-demand | **none** | machine-decidable |
| inline TypeScript annotation | event-fired (build) | blocking | machine-decidable |
| ArchUnit rule in the test suite | event-fired (CI) | blocking | machine-decidable |
| compiled constraint checker | event-fired | warning | machine-decidable |
| manually-run `spec lint` | **on-demand** | blocking | mixed |
| pre-commit `spec lint` | event-fired | blocking | mixed |

The last two rows differ in exactly one coordinate. They are the same checks over the same artifacts; only the trigger differs. A blocking check nobody runs blocks nothing. That pair is the cleanest available separation of trigger from enforce, and it exists in a deployed system.

---

## 4. The rot law

> An intent artifact decays at a rate proportional to the arrival of falsifying events outside its enforcement radius.
> The radius is the product of trigger and enforce.
> The radius applies only to the fraction of intent that expression can carry; the remainder decays at the unenforced rate regardless.

### 4.1 It explains the exceptions without exceptions

| artifact | falsifier arrival outside radius | observed |
|---|---|---|
| local comment | ≈ 0 (the falsifying edit is in view) | does not rot |
| cross-file comment | ≈ repository change rate | rots, and misleads when it does |
| abstract architecture document | ≈ 0 (*almost nothing falsifies it*) | does not rot, and buys little |
| specification of dead code | 0 | does not rot |
| checked type annotation | 0 (build fails) | 90.1% never edited; 70.4% survive to HEAD |
| unchecked type stub | ≈ repository change rate | wrong in 49 of 54 libraries |

The third row is where the law replaces an existing exception. The best-known finding in this area, that abstract documentation is judged accurate and useful while detailed documentation rots, has been handled by prior work as a special case about abstraction level. Under the law it is not a special case: abstract documents do not rot because they assert too little to be falsified, and the same property is why they help so little. No exception clause is required.

The fourth and fifth rows are a natural control group. `.d.ts` stubs and inline annotations use identical syntax, are written by the same population, in the same ecosystem, with the same tooling. The only difference is whether anything breaks when they are wrong.

So "load-bearing" is not a property of an artifact, a syntax, or a toolchain; it is a property of the gate.

### 4.2 What would falsify it

1. Two claims with identical scope under identical trigger and enforce, decaying at different rates → the law is incomplete.
2. A claim whose falsifiers all arrive outside the radius, which nonetheless stays true → the law is wrong, or the claim is unfalsifiable.
3. Widening the radius, holding everything else fixed, failing to reduce decay → the law is wrong. This is directly testable and is the core of §5.
4. A null scope interaction → the mechanism is wrong even if the direction holds.

---

## 5. Experimental design

`[TO MEASURE]`

### 5.1 The design is additive, not a choice among alternatives

Every enforcement mechanism presupposes that the rule has been stated. A gate that blocks without saying what was violated is not a usable mechanism. Prompt is therefore the baseline rather than an arm:

| condition | |
|---|---|
| prompt | baseline; the rule exists and is stated |
| prompt + on-demand retrieval | a skill the agent may consult |
| prompt + blocking check | enforcement added |
| prompt + retrieval + blocking | both |

This also removes a confound that a four-alternative design would carry: no condition has zero rule text, so no token-matched placebo is needed.

### 5.2 The primary result is an interaction

**Prediction.** The effect of trigger and enforce is small at local scope and large at system scope.

**Rationale.** At local scope the falsifier arrives inside the artifact's natural radius regardless of engineering; there is nothing for a gate to add. At system scope the natural radius is near zero and the engineered radius is the only radius there is.

A null interaction falsifies the mechanism even if the main effects come out in the predicted direction. We consider this the strongest feature of the design: it can distinguish "gates help" (already established) from "gates help *for the reason we claim*" (not established).

### 5.3 Well-formed units

The construction constraint is forced by a failure mode named in the repair-benchmark literature: a test that passes on the *absence* of something is passed by a program that does nothing. Most naive rule checks have exactly this shape.

A (task, rule) pair is well-formed only if:

1. the task requires functionality **F**;
2. the natural implementation of **F** reaches for **X**;
3. the rule forbids **X**;
4. a valid alternative implementation exists.

Then: doing nothing fails the task; default behaviour violates; compliance costs something. All three are required.

This criterion is equivalent to the *against-prior* label used in recent instruction-following work, established there by re-running each task with the rule withheld across nine probe builds. That labelling identifies precisely the pairs where the rule constrains the implementation, and it is the most expensive part of construction.

### 5.4 Verification

- **Deterministic checks only** for the primary metric. Three independent studies report that LLM judges inflate accuracy worst exactly in the high-failure regime; one reports judge-swap agreement of κ = 0.163 while conceding the judge is the dominant source of uncertainty in its own results.
- **Four outcome states** (pass / fail / not-run / skipped). A check that silently stopped running must never read as a pass.
- **Composition holdout.** Visible checks exercise rules in isolation; held-out checks exercise compositions of *the same* rules, every one already mandated. A genuinely compliant artifact scores a zero gap by construction, which removes the "the test was unfairly narrow" confound.
- **Degenerate baselines, published.** A no-op agent and a deletion-only agent. Any check either passes is disqualified. One published repair system that only deleted functionality matched three state-of-the-art tools.
- **Report both per-rule and all-pass rates.** These diverge. In one study the per-requirement metric *rose* as constraint count more than doubled, while joint compliance collapsed. Reporting one alone measures nothing.

### 5.5 Corpus

`[DECISION PENDING]` Two routes, and a cheap measurement decides between them.

**Fork.** Recent instruction-following work over coding agents has released a rule library with an eight-axis taxonomy, five implemented delivery surfaces (our trigger axis), and against-prior labels. It has no enforce axis. That is our contribution, which makes this additive rather than a reconstruction. A second candidate supplies real repositories and rules hand-coded from open-source communities, including the rule class with the largest known effect: rules asking an agent to refuse or hand off sit near zero compliance under *every* soft delivery mode tested.

**Build.** Estimated 2–5 hours per well-formed unit, based on published construction budgets for comparable benchmarks. Amortises within a repository, so few repositories and many tasks per repository.

**The deciding measurements**, both desk work: (i) are the artifacts released; (ii) after reclassifying the rule library by scope and discarding everything not deterministically checkable, how many rules remain per scope level.

### 5.6 Power

`[TO MEASURE]` Variance components must come from a pilot; every number we currently have is assumed. Published guidance gives the sample-size relation and the two structural facts that bound the design: at one repeat per cell the majority of variance is within-task model stochasticity, and there is a floor below which no number of repeats rescues a task set that is too small.

### 5.7 Threats

1. **Degenerate compliance.** An agent that never emits the constrained construct has a zero violation rate. Mandatory co-metrics: task completion, degenerate-compliance rate, and the published no-op baseline.
2. **Prompt realisation.** Conditions differ in text by construction. Mitigation: pre-registered paraphrase sets treated as a crossed random effect; rule text byte-identical across conditions wherever it appears.
3. **Construct validity of the corpus.** Selecting rules a checker can verify selects for rules where mechanical enforcement wins. This is precisely the confound in prior work that compiled constraints into AST queries and then checked them with AST queries. Our expression axis exists to make this visible rather than to avoid it.
4. **Contamination.** The dependent variable is a behaviour rather than a memorisable answer, so the residual risk is repository familiarity. Fresh corpora and a provenance-versus-cutoff table handle it.
5. **Non-determinism.** Temperature zero does not confer determinism; up to three-quarters of code-generation tasks produce no two identical outputs across requests. Repeats, reported variance, and no lowering of temperature to buy variance reduction.

---

## 6. Related work

`[TO WRITE]` Three groups to position against, and the positioning is convergent rather than competitive:

- **Delivery-surface variation in coding agents.** Same rule relocated across ambient and on-demand surfaces, at scale, with an against-prior control. No enforcement arm.
- **Community-rule compliance.** Same clause under native placement, reminder, verbatim quote, and harness feedback, on real repositories. Concludes that control must be placed *outside* the agent, and does not test it. Its measured discovery gap (a policy file opened in 3.5% of runs; the overwhelming majority of violations occurring without it ever being opened) is direct evidence for the trigger axis.
- **Compiled constraint enforcement.** Instruction-file constraints compiled to static queries and runtime interception, reporting a substantial compliance advantage over prompt-only. Occupies a single cell of our cube, with expression and enforce both fixed at their machine-decidable/enforced extremes, and therefore cannot separate which axis produced the gain.

Three groups reached this direction independently, which strengthens it. Our contribution is to separate the axes that produced it, and to supply the enforce arm all three lack.

The classical software-engineering literature is treated in §2 and in the accompanying survey.

---

## 7. Limitations

`[TO WRITE]`

- n=1 on the existence proof; the authors built the instrument.
- The instrument is simultaneously the treatment and the artifact. The design space in §3 is what de-circularises this: the law is a claim about the space, and our system's claim to sit at a good point in it is a derived, falsifiable assertion rather than an assumption.
- Mechanically verifiable rules are a biased sample of the rules practitioners care about. The expression axis measures the bias; it does not remove it.
- **Operational telemetry is not mechanism evidence, and we will not use it as such.** The deployment generates a large volume of fleet observability data: host memory pressure, process health, session lifecycle events. It is tempting because it is free and abundant. It has no treatment group and no task/outcome design, so it cannot support a claim about *why* anything happened. We state this as a standing discipline rather than a passing caveat, because the temptation is real and the failure would be invisible to a reader. Fleet data appears in this paper only as system description, never as evidence for a mechanism.
- Adoption is not downstream of the law. A tool can be correct by the law and still die of the disease that killed SACC. One principle from the survey applies to us: *a compliance artifact survives only where something other than the compliance check itself keeps it alive.* We do not yet have an answer to what that is for our own system, and we state this as an open problem rather than eliding it.

---

## 8. Artifact

`[TO WRITE]` Instrument, corpus, checkers, raw runs, annotations including free-text justifications, harness self-test, and model provenance table with a drift canary.

---

## Notes on how to write this

*Not part of the paper. Guidance for drafting.*

1. **Lead with the graveyard, not with the system.** The revival claim is the interesting one and it is what makes the rot law worth reading. A paper that opens with the tool reads as a tool paper.
2. **Quote the causes of death verbatim.** The force of §2 comes entirely from the fields having diagnosed themselves. Paraphrase weakens it.
3. **Keep the law's three clauses together.** The expression clause is the one readers will drop, and it is the one that explains why "enforce everything" fails.
4. **State the falsifiers early and prominently.** §4.2 and §5.2 are what distinguish this from a position paper. A reader should be able to see, by the end of §4, exactly what result would sink the paper.
5. **Be explicit that the convergence with concurrent work is good news.** Do not defend novelty. Three groups finding the same direction independently strengthens the claim; our contribution is the decomposition, and it should be stated as such without anxiety.
6. **Do not let the system's name appear before §2.2.**
