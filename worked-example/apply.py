#!/usr/bin/env python3
"""Apply the audit's findings to 00-input.md, producing 03-output.md.

Written as explicit (old, new) pairs rather than a hand-retyped document: everything not listed
here stays byte-identical, so the quotations, numbers, placeholders, and table data cannot drift.
Every pair traces to a finding in 02-audit.md.
"""
import sys

EDITS = [
# ---- F1/2 punctuation, F3 stance, F5 bold: status line and abstract -------------------
("Sections 5–8 are structured placeholders marked `[TO MEASURE]` — they state what goes there and what would falsify it, but contain no results.",
 "Sections 5–8 are structured placeholders marked `[TO MEASURE]`. They state what goes there and what would falsify it, but contain no results."),

("We observe that in every case the recorded cause of death is a *human* cost — the effort of maintaining a mapping, of writing down a rationale whose beneficiary is a stranger, of attending a meeting.",
 "We observe that in every case the recorded cause of death is a *human* cost. Someone has to maintain a mapping, write down a rationale whose beneficiary is a stranger, or attend a meeting."),

("But affordability is not survival. Surveying three independent literatures — traceability, design rationale, and executable specification — we find they converge, each as a residual rather than a thesis, on a single variable: whether something stops you when you do not consult the artifact. We formalise this as a rot law over three design axes — **trigger** (does an event bring you into contact), **enforce** (can you proceed anyway), and **expression** (how much of your intent can enter the mechanism at all) — and show that the law explains cases the existing literature handles only by exception. The law makes a falsifiable prediction:",
 "But affordability is not survival. We surveyed three independent literatures: traceability, design rationale, and executable specification. They converge, each as a residual rather than a thesis, on a single variable: whether something stops you when you do not consult the artifact. We formalise this as a rot law over three design axes. **Trigger** asks whether an event brings you into contact, **enforce** asks whether you can proceed anyway, and **expression** asks how much of your intent can enter the mechanism at all. The law explains cases the existing literature handles only by exception, and it makes a falsifiable prediction:"),

# ---- §1 -------------------------------------------------------------------------------
("**Every one of these is a labour cost, and it is a labour cost that a language-model agent does not pay.** An agent maintaining a mapping does not find it tedious. An agent writing down a rationale is not writing for a stranger — with no memory across sessions, it is writing for itself. An agent does not attend meetings.",
 "Every one of these is a labour cost, and it is a labour cost that a language-model agent does not pay. An agent maintaining a mapping does not find it tedious. An agent writing down a rationale has no memory across sessions, so the future reader it is writing for is itself. An agent does not attend meetings."),

("**It does not follow that the paradigms simply return.** Our second finding, from the same survey, is that cheap capture was never sufficient. Every design-rationale corpus that survived a decade — the RFC, PEP and KEP processes are the only ones we found — survived because writing the record was a *precondition for landing the change*, not because writing it was cheap.",
 "It does not follow that the paradigms simply return. Our second finding, from the same survey, is that cheap capture was never sufficient. Only three design-rationale corpora in our survey survived a decade: the RFC, PEP and KEP processes. Each survived because writing the record was a *precondition for landing the change*, not because writing it was cheap."),

("So the structure is two-stage. **Agents make the artifact affordable. Something else has to make it survive.** The bulk",
 "So the structure is two-stage. Agents make the artifact affordable, and something else has to make it survive. The bulk"),

# ---- §1.1 contributions: label dashes -------------------------------------------------
("- **C0 — The revival claim, with a discriminator.**", "- **C0. The revival claim, with a discriminator.**"),
("- **C1 — The rot law.**", "- **C1. The rot law.**"),
("- **C2 — A three-axis design space** in which existing systems — inline types, `.d.ts` stubs, `CLAUDE.md`, ArchUnit, compiled constraint checkers, and our own — are points rather than rivals.",
 "- **C2. A three-axis design space.** Inline types, `.d.ts` stubs, `CLAUDE.md`, ArchUnit, compiled constraint checkers, and our own system are points in that space rather than rivals."),
("- **C3 — An experimental program** whose primary result is an *interaction*: the effect of trigger and enforce should scale with claim scope.",
 "- **C3. An experimental program.** Its primary result is an *interaction*: the effect of trigger and enforce should scale with claim scope."),
("- **C4 — An instrument.**", "- **C4. An instrument.**"),

# ---- Table 1 cell ---------------------------------------------------------------------
("| labour | ✗ (removed — the writer *is* the reader) |", "| labour | ✗ (removed; the writer *is* the reader) |"),

# ---- §2.1 -----------------------------------------------------------------------------
("We note one instructive near-miss. Reflexion models died partly of the mapping cost — which agents remove — but the technique's stated purpose was to",
 "Reflexion models are a near-miss. They died partly of the mapping cost, which agents remove. But the technique's stated purpose was to"),

# ---- §2.2 -----------------------------------------------------------------------------
("`[TO MEASURE]` The strongest available evidence for C0 is a system in which the artifact that killed SACC — the mapping from code to intended structure — is maintained by agents rather than by people.",
 "`[TO MEASURE]` The strongest available evidence for C0 is a system in which the artifact that killed SACC, the mapping from code to intended structure, is maintained by agents rather than by people."),

("The third of these is the one that matters most and the one nobody has published: **an enforcement mechanism's strength is bounded above by its targeting precision.** A gate that can only say \"update some spec\" is satisfiable by updating the wrong one.",
 "The third has not been published, and it bounds the others: an enforcement mechanism's strength is bounded above by its targeting precision. A gate that can only say \"update some spec\" is satisfiable by updating the wrong one."),

("generality rests on the discriminator in §2.1, which is a literature argument, not a measurement.",
 "generality rests on the discriminator in §2.1, which argues from the literature rather than from measurement."),

("1. **Pre-define the denominator** — the set of eligible spec-governed commits, by a stated rule, not by what turns out to have data.",
 "1. **Pre-define the denominator.** The set of eligible spec-governed commits, fixed by a stated rule rather than by what turns out to have data."),

# ---- §3 -------------------------------------------------------------------------------
("An intent artifact — a comment, a spec node, a lint rule, a type — can be characterised by three independent design choices and compared against one property of the claim it carries.",
 "An intent artifact can be a comment, a spec node, a lint rule, or a type. Each can be characterised by three independent design choices, and compared against one property of the claim it carries."),

("**Trigger — does an event bring you into contact with it?**", "**Trigger.** Does an event bring you into contact with it?"),
("| ambient | system prompt, `CLAUDE.md`, `AGENTS.md` | no — always present, never fires |",
 "| ambient | system prompt, `CLAUDE.md`, `AGENTS.md` | no (always present, never fires) |"),
("| on-demand | a skill, a documentation site, a manually-run linter | no — present, must be fetched |",
 "| on-demand | a skill, a documentation site, a manually-run linter | no (present, must be fetched) |"),

("We stress that *presence in context is not a trigger*. The evidence is direct: instruction-following collapses as the number of simultaneous constraints rises even though every constraint remains in context throughout — joint compliance falls from .94 to .21 over k=1..10 for one frontier model while per-constraint compliance stays near-flat. Being available is not being consulted.",
 "*Presence in context is not a trigger.* Instruction-following collapses as the number of simultaneous constraints rises, even though every constraint remains in context throughout: joint compliance falls from .94 to .21 over k=1..10 for one frontier model, while per-constraint compliance stays near-flat."),

("**Enforce — can you proceed anyway?** none / warning / blocking.", "**Enforce.** Can you proceed anyway? None, warning, or blocking."),
("**Expression — how much of your intent can enter the mechanism at all?** prose", "**Expression.** How much of your intent can enter the mechanism at all? Prose"),

("Expression is not independent of enforce: **you cannot mechanically enforce prose.** Expression gates the maximum achievable enforce. The converse does not hold — a fully machine-decidable artifact with zero enforcement is a real and common configuration, of which TypeScript's `.d.ts` declaration files are the cleanest instance.",
 "Expression is not independent of enforce: you cannot mechanically enforce prose. Expression gates the maximum achievable enforce. The converse does not hold. A fully machine-decidable artifact with zero enforcement is a real and common configuration, and TypeScript's `.d.ts` declaration files are the cleanest instance."),

("Practitioners typically specify on the order of 22 kinds of quality requirement; industrial conformance tools handle at most three of them. That is an expressiveness ceiling, not an enforcement ceiling, and it is why \"enforce everything\" is not a strategy.",
 "Practitioners typically specify on the order of 22 kinds of quality requirement; industrial conformance tools handle at most three of them. Expressiveness sets that ceiling. Enforcement does not, which is why \"enforce everything\" is not a strategy."),

("**Scope — how far does the claim reach?** Local", "**Scope.** How far does the claim reach? Local"),

("**A blocking check nobody runs blocks nothing** — this is not a joke but the cleanest available separation of trigger from enforce, and it is available in a deployed system.",
 "A blocking check nobody runs blocks nothing. That pair is the cleanest available separation of trigger from enforce, and it exists in a deployed system."),

# ---- §4 law block: drop doubled emphasis ----------------------------------------------
("> **An intent artifact decays at a rate proportional to the arrival of falsifying events outside its enforcement radius.**\n> **The radius is the product of trigger and enforce.**\n> **The radius applies only to the fraction of intent that expression can carry; the remainder decays at the unenforced rate regardless.**",
 "> An intent artifact decays at a rate proportional to the arrival of falsifying events outside its enforcement radius.\n> The radius is the product of trigger and enforce.\n> The radius applies only to the fraction of intent that expression can carry; the remainder decays at the unenforced rate regardless."),

("| abstract architecture document | ≈ 0 — *almost nothing falsifies it* | does not rot, and buys little |",
 "| abstract architecture document | ≈ 0 (*almost nothing falsifies it*) | does not rot, and buys little |"),

("The third row is the load-bearing one. The best-known finding in this area — that abstract documentation is judged accurate and useful while detailed documentation rots — has been handled by prior work as a special case about abstraction level.",
 "The third row is where the law replaces an existing exception. The best-known finding in this area, that abstract documentation is judged accurate and useful while detailed documentation rots, has been handled by prior work as a special case about abstraction level."),

("This licenses a restatement worth keeping: **\"load-bearing\" is not a property of an artifact, a syntax, or a toolchain. It is a property of the gate.**",
 "So \"load-bearing\" is not a property of an artifact, a syntax, or a toolchain; it is a property of the gate."),

("3. **Widening the radius, holding everything else fixed, failing to reduce decay → the law is wrong.** This is directly testable and is the core of §5.\n4. **A null scope interaction** → the mechanism is wrong even if the direction holds.",
 "3. Widening the radius, holding everything else fixed, failing to reduce decay → the law is wrong. This is directly testable and is the core of §5.\n4. A null scope interaction → the mechanism is wrong even if the direction holds."),

# ---- §5 -------------------------------------------------------------------------------
("Prompt is therefore the **baseline**, not an arm:", "Prompt is therefore the baseline rather than an arm:"),
("| prompt | baseline — the rule exists and is stated |", "| prompt | baseline; the rule exists and is stated |"),

("**A null interaction falsifies the mechanism**",
 "A null interaction falsifies the mechanism"),

("The construction constraint is severe and it is forced by a failure mode named in the repair-benchmark literature:",
 "The construction constraint is forced by a failure mode named in the repair-benchmark literature:"),

("We note that this criterion is equivalent to the *against-prior* label used in recent instruction-following work, established there by re-running each task with the rule withheld across nine probe builds. That labelling identifies precisely the pairs that have bite, and is the most expensive part of construction.",
 "This criterion is equivalent to the *against-prior* label used in recent instruction-following work, established there by re-running each task with the rule withheld across nine probe builds. That labelling identifies precisely the pairs where the rule constrains the implementation, and it is the most expensive part of construction."),

("The precedent is stark: a repair system that only deleted functionality matched three state-of-the-art tools.",
 "One published repair system that only deleted functionality matched three state-of-the-art tools."),

("These diverge sharply — one study's per-requirement metric *rose* as constraint count more than doubled, while joint compliance collapsed.",
 "These diverge. In one study the per-requirement metric *rose* as constraint count more than doubled, while joint compliance collapsed."),

("It has no enforce axis — which is our contribution, making this additive rather than a reconstruction.",
 "It has no enforce axis. That is our contribution, which makes this additive rather than a reconstruction."),

("4. **Contamination.** The dependent variable is not a memorisable answer; the residual risk is repository familiarity, handled by fresh corpora and a provenance-versus-cutoff table.",
 "4. **Contamination.** The dependent variable is a behaviour rather than a memorisable answer, so the residual risk is repository familiarity. Fresh corpora and a provenance-versus-cutoff table handle it."),

# ---- §6 -------------------------------------------------------------------------------
("`[TO WRITE]` Three groups to position against, and the positioning is *convergent*, not competitive:",
 "`[TO WRITE]` Three groups to position against, and the positioning is convergent rather than competitive:"),

("Concludes that control must be placed *outside* the agent — and does not test it.",
 "Concludes that control must be placed *outside* the agent, and does not test it."),

("Occupies a single cell of our cube — expression and enforce both fixed at their machine-decidable/enforced extremes — and therefore cannot separate which axis produced the gain.",
 "Occupies a single cell of our cube, with expression and enforce both fixed at their machine-decidable/enforced extremes, and therefore cannot separate which axis produced the gain."),

("**Three independent groups reaching the same direction is the strongest available evidence that the direction is right.** Our contribution is not to establish it a fourth time; it is to separate the axes that produced it, and to supply the enforce arm all three lack.",
 "Three groups reached this direction independently, which strengthens it. Our contribution is to separate the axes that produced it, and to supply the enforce arm all three lack."),

# ---- §7 -------------------------------------------------------------------------------
("The deployment generates a large volume of fleet observability data — host memory pressure, process health, session lifecycle events.",
 "The deployment generates a large volume of fleet observability data: host memory pressure, process health, session lifecycle events."),

("The survey's strongest single principle applies to us:", "One principle from the survey applies to us:"),

# ---- added after the first after-measurement caught them (see 05-report.md) -------------
("The project ships a documented skip variable; its usage rate is not a nuisance parameter, it is the suppression-growth measurement the survey identified as the missing health metric for any rules-as-tests system.",
 "The project ships a documented skip variable. Its usage rate is a result in its own right: the suppression-growth measurement the survey identified as the missing health metric for any rules-as-tests system."),

("with an against-prior control. **No enforcement arm.**",
 "with an against-prior control. No enforcement arm."),
]


def main():
    text = open("00-input.md", encoding="utf-8").read()
    missed = []
    for old, new in EDITS:
        n = text.count(old)
        if n != 1:
            missed.append((n, old[:70]))
            continue
        text = text.replace(old, new, 1)
    if missed:
        for n, frag in missed:
            print(f"NOT APPLIED (found {n}x): {frag}", file=sys.stderr)
        return 1
    open("03-output.md", "w", encoding="utf-8").write(text)
    print(f"{len(EDITS)} edits applied")
    return 0


if __name__ == "__main__":
    sys.exit(main())
