# Per-hit decision procedure

The taxonomy says what a thing is. This file says what to do about it. Behavioural contract is
`SKILL.md`; where this file and that one disagree, `SKILL.md` wins.

## The procedure, for every candidate

Run in order. The first step that fires decides it.

```
candidate
  ├─ inside a protected span?              → keep, unchanged. Do not gamble.
  ├─ inside quoted material?               → keep. Mark it. It is not yours to rewrite.
  ├─ is the word itself the subject?       → keep. A style guide quotes slop to name it.
  ├─ principle-layer family (H1..H6)?      → act. No cap, no scene exemption, no threshold.
  │     H6 is the metaphor ban: a frozen name and a literal use are outside it, nothing else is.
  │     Fill the audit table's source-domain column, then aggregate it. Two hits from one
  │     domain is a sustained metaphor, and no single row would have shown you that.
  ├─ fails nofluff check 1 or 2?           → delete or rewrite, whatever the tables say.
  │     1. delete it — is any information lost?
  │     2. "what specifically does this mean" — can you answer with a fact?
  ├─ Tier 1?                               → replace by default, subject to keep-conditions below.
  ├─ Tier 2?                               → a finding only when clustered: short paragraph 2+,
  │                                           long paragraph 3+. Keep the best one, rewrite the rest.
  ├─ Tier 3?                               → a finding only above document density: <200 same word
  │                                           3+; 200-1000 5+; >1000 above 0.5%. Delete the surplus
  │                                           or replace some with concrete information.
  │                                           NEVER rotate synonyms to lower the density.
  └─ otherwise                             → report as `?`. Over-report; do not drop it silently.
```

Then apply the scope filter:

```
action requires deleting a whole sentence
  ├─ structural  → delete it
  ├─ bounded     → does it meet all three list conditions?
  │                  yes → proposed-deletion list, with "why deleting loses nothing"
  │                  no  → clean inside the sentence only
  └─ in-place    → keep the sentence, annotate it, never soften it into a different empty sentence
```

## Exemption caps

Some families allow named survivors. The cap exists because of what the alternative looks like:
"each of these carries the argument", repeated eight times, is itself the evidence that the shape is
doing the work.

**Exempt instances are not counted toward density and are not flattened.** Only the remainder above
the threshold gets handled. This matters: it means running the rules again on your own output does
not produce a second round of hits.

| family | cap | what qualifies |
|---|---|---|
| B1 staged reversal | **2 per document** | one term definition (`X 不是 A，是 B`, correcting a misreading of what X is, usually in the opening or a positioning sentence) + one argument the following text depends on (the first half is a misconception the reader genuinely holds, and deleting it costs the following data or conclusion its basis). "It reads weaker without it" does not qualify. |
| E7 latching | 1 use of any vivid word | the rest get replaced |
| E8 mixed metaphor fields | 1 field | used accurately, and literal uses do not count at all |
| F2 em dash | driven toward zero, every survivor named | a genuine parenthetical, one per paragraph at most |
| F3 bold | first use of a defined term | in a paper or spec; name the exemption, do not assume it |
| B3 rule of three | uncapped | never counted; judged per instance |

## B1 staged reversal: the density thresholds

Remove exemptions first, then count what is left.

- **In one paragraph:** two or more consecutive instances, including mixed with value-inflation
  skeletons.
- **Across the document,** normalised by length (Chinese by characters, English by words; a code
  fragment, path, command, or version counts as 1; punctuation and whitespace count as 0):
  - under 300: more than 2
  - 300–1000: more than 3
  - over 1000: more than one per 300 on average
- **When you can predict the shape of the next sentence**, the threshold has already been passed.

Variants count. `不像 A，像 B` · `要的是 X，不是 Y` · `X 不行，Y 才行` · `不是 A。而是 B` ·
`与其说 A，毋宁说 B` · `你以为 A，其实 B` · `我一直以为 A，后来才发现 B` · `答案恰恰相反` ·
`Y, not X.` · `not just X but Y` · consecutive list items or table rows all ending in a negation.

**Default action:** replace the excess with a neutral connective or a direct statement
(`X 不够，Y 更重要`, `相比 X，Y 更能说明问题`, `Documentation does not fail here; the missing piece is
feedback`). Both sides' information survives. Inverting to `Y，不是 X` does not count as fixing it.
Do not kill on sight, and do not flatten the exempt instances into the same shape as everything else.

## Self-assessment: which ones stay

A5 covers two different things that look identical, and cutting both is an over-correction that costs
a claim. The separator, established on a real paper draft:

> **Keep a self-assessment that the following clause justifies. Cut one that nothing follows from.**

- Keep: `We consider this the strongest feature of the design: it can distinguish X from Y.` The
  superlative is followed by what the feature does, and it is hedged (`We consider`). Removing the
  hedge would strengthen a claim, which is a principle-layer violation.
- Keep: `The strongest available evidence for C0 is a system in which…` It grades the evidence, which
  is a methodological statement an author defends, and not a grade on their own sentence.
- Cut: `The survey's strongest single principle applies to us:` The principle applies regardless of
  its rank; the superlative does no work.
- Cut: `the one that matters most`, `this is not a joke but`, `a restatement worth keeping`,
  `We note one instructive near-miss`, `We stress that`. Pure flourish, nothing turns on them.

When the same sentence carries both a grade and a claim, cut the grade and keep the claim verbatim.
`The third of these is the one that matters most and the one nobody has published:` loses the first
half and keeps the second: `The third has not been published, and it bounds the others:`.

## Keep-conditions by family

A Tier 1 hit still stays when one of these holds. This is the misfire-protection layer, and it is
what separates an edit from a massacre.

1. **Quoted material.** Someone else's words, verbatim, including inside a document about slop.
2. **Term definition.** The word itself is what the sentence is about (`什么是赋能`).
3. **Code and configuration.** Technical names, variables, APIs, fields, paths.
4. **Industry-standard sense.** `杠杆` in finance is leverage. `navigate` in graph, network, and
   routing contexts is literal.
5. **System subject in technical description.** `网关返回 504`, `缓存过期`, `the gateway returns 504`.
   A non-human subject describing system behaviour is correct, not personification.
6. **Engineering terms in engineering reports.** In a postmortem, incident report, or changelog,
   `根因` / `收敛` / `收口` are standard.
7. **Real internet voice with real detail.** A blogger writing `踩坑` after describing the specific
   pit is not AI register. Specifics are the evidence.
8. **Conventional academic passive and hedging.** `was conducted`, `was published`, `suggests`,
   `may`, `is consistent with`. See `SKILL.md` §2.2.
9. **A real debug conversation with evidence.** Parameters, operations, durations, observations
   present → `root cause` and `打满` are technical speech.
10. **English words inside Chinese sentences**, judged by what they mean in that sentence, not by an
    English word list. `这次 refactor 的 leverage 点在缓存` is business jargon; `用 10 倍 leverage
    做空` is a finance term.
11. **Project style guide and glossary.** The user's current instruction and the project's existing
    terminology outrank every default here. A stable team term is not rewritten because it matched a
    generic list.
12. **Rhythm-bearing repetition and transitions**, in long-form text. A repeated phrase can be
    carrying a pause, an emphasis, or a hand-off. Delete it only after checking that the paragraph
    still joins.

## `in-place` alternates

Under `in-place` nothing is deleted, so each family needs a within-sentence move. These are the ones
that work; anything not listed here has no `in-place` action and gets an annotation instead.

| family | in-place move |
|---|---|
| B1 staged reversal | compress the skeleton to a connective: `X 不够，Y 更重要`. If the first half is only a lead-in, delete the lead-in phrase and check that what remains stands alone. |
| A6 / G4 empty summary | delete the leading phrase (`归根到底`, `本质上`, `In conclusion`). If a readable judgement remains, the sentence stays. If nothing remains, annotate `[空总结，建议人工确认是否删除]`. |
| A1 / B-value inflation | `这不仅仅是 X，更是 Y` → `这是 Y`, provided Y carries information. `真正的 X 不是 A，而是 B` → `X 更看 B`. A promise-shaped closer (`看完就懂了`) becomes a low-commitment description. |
| C3 nominalisation | restore the verb inside the sentence. The character count will drop; that is normal and is not the deletion the length floor guards against. If restoring would lose the claimed effect type, keep the predicate direction and compress around it. |
| E5 performed engineer-speak | swap the stance verb for a plain one: 确认 / 解决 / 核对 / 缩小范围. |
| K3 conjunctions | connectives are sentence-internal; removing them is not deleting a sentence, so this runs normally under `in-place`. |
| E8 metaphor fields | restore the literal sense in place. If the sentence is then empty, it had only the metaphor: annotate, do not invent content. |
| J2 fabricated atmosphere | if the detail is a modifier, delete the modifier and keep the clause. If it fills the whole sentence, annotate `[无来源细节，建议人工确认是否删除]`. |
| D5 quantification ambiguity | compress the quantity away only if the sentence stays complete and the number carries nothing. Otherwise keep the sentence and annotate `[量化关系有歧义，待确认]`. |
| F1 compression punctuation | **no `in-place` move exists.** Decompressing means writing a second sentence, which `in-place` forbids. Under `in-place`, punctuation work is limited to substitution, and substitution is not the fix. Record it as deferred and say so. |

`in-place` also has a phrase-level precondition: after deleting a phrase, what remains must still be a
complete, readable statement with no dangling reference. If not, substitute inside the sentence
instead of deleting.

## Length checks under `bounded` and `in-place`

- Every information point in the original must be traceable in the output. This is a hard check,
  not a preference.
- `in-place`: output below 85% of the original length means go back and look for a deleted sentence,
  a merge, or a compressed paragraph. `in-place` should not delete any sentence at all.
- `bounded`: length falls because empty sentences went on the list, so there is no floor. Instead
  verify that every line on the list is genuinely empty, with no substantive sentence and no
  rhythm-bearing repetition smuggled in.
- Either scope: a sentence-count change past about 10% means checking whether unapproved structural
  work happened.

## When the sentence lands nowhere

After the stance layer is gone, some sentences have nothing left. Three cases, in priority order:

1. The original has a number, an action, an object, or a definite conclusion → strip the rendering
   words and keep those.
2. The original has no concrete metric or fact → the output is allowed to be shorter and plainer.
   **Do not fill the gap** with `能提效` / `有改进` / `降低了延迟` / `faces challenges` /
   `it improves things`. Do not swap one exhortation for another (`值得尝试`, `继续学习`).
3. `status` / `docs` / `academic` where the claim needs a basis the original never gave → write
   "original gives no basis". Do not supply a number, a feature, a source, or a technology choice.

If deleting a sentence leaves a paragraph without a landing, rebuild one **from information already
in the original**. If the original has nothing to rebuild from, let the paragraph be shorter.
