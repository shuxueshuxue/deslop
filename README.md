<div align="center">

# deslop

**Strip the LLM tells out of prose.**

A [Claude Code](https://claude.ai/code) skill. Chinese and English.

</div>

---

LLM-written or LLM-polished prose carries tells. They are learnable, countable, and removable.

`deslop` audits a document against a marker taxonomy, produces a per-line kill list with plain
replacements, applies them, and re-measures three countable indicators — so the result is verifiable
rather than asserted.

## The thing most people get wrong

**AI flavor is not "plain, careful wording." Plain, careful wording is the target.**

AI flavor is the writer showing you how clever they are. Every marker below is one form of it — the
vivid analogy, the staged reversal, the punchy closer, the word picked because it sounds learned. They
all do the same job: prove the author is smart. It reads well line by line, which is exactly why it
survives editing.

The test for any sentence:

> Is this **saying the thing**, or **being clever**?

Humble and plain is the target. Sly and clever is the defect.

An editor who mistakes plainness for the problem sands the text into mush and misses every real tell.
The models to aim at are Wikipedia, Hacker News technical comments, and academic papers.

## What it catches

| | |
|---|---|
| **Action metaphor** | `接住每个事件` → `对每个事件创建一条记录` · `costs collapsed` → `costs fell` |
| **Personification** | `状态活不过一次调用` → `调用结束即失效` · `history reminds you` → `history does not indicate` |
| **Staged reversal** | `不是 X，是 Y` · `it's not x, it's y` — the single most reliable tell |
| **Dramatized closer** | a short assertion parked at a paragraph's end to leave an aftertaste |
| **Self-assessment** | `Naur 说得对` → `与 Naur 的结论一致` · `my honest take` → *(cut)* |
| **Em dashes** | counted, and checked for where they land |
| **Latching** | one vivid word reused across a document |
| **Elevated diction** | a rarer, more "professional"-sounding word where a common one exists — 判据 → 判定规则 · utilize → use |
| **Jargon** | 赛道 / 闭环 / 抓手 · load-bearing / key insight / synthesize |

## Install

```sh
git clone https://github.com/shuxueshuxue/deslop.git ~/.claude/skills/deslop
```

Then, in Claude Code:

```
/deslop  the README
/deslop  slides/talk.html — Chinese, conference audience
```

Or just say *"this sounds like AI, fix it"* — the skill's description matches that.

## How it works

1. **Extract** the prose so the audit sees what a reader sees, not the markup.
2. **Audit** line by line, in a **fresh-context subagent**. Self-auditing prose you just wrote does
   not work: you re-read your own intent instead of the words on the page.
3. **Count** three indicators — staged reversals, em dashes, personification.
4. **Apply** the literal denotation. Never swap one vivid word for another vivid word.
5. **Re-measure** and report both numbers.

`reversals 12 → 0` is evidence. *"now it reads naturally"* is not.

## What it will not do

**It does not flatten terms of art.** If a mechanism is literally named *drift*, then "spec drift" is
the term, not a metaphor. Same for *anchor*, *warm cache*, *starvation*, *back-pressure*. Flattening
those makes text read as though the author does not know the field — worse than leaving a tell.

**It does not edit arguments.** It restates sentences. Restructuring, cutting sections, and changing
claims need the author's sign-off.

**It does not check whether the text is right.** Register and comprehension are different defects. A
document can be perfectly plain and still contain a dangling pronoun, a contradiction between two
pages, or a misread citation. See [`references/worked-example.md`](references/worked-example.md) for a
case where all three existed alongside the register problems.

## Files

```
SKILL.md                        the skill
references/markers-zh.md        Chinese taxonomy, eight categories
references/markers-en.md        English markers, sourced to HN 48905248
references/worked-example.md    a real audit: 45 findings, 12/10/14 → 0/0/0
```

## Credit

The English marker list draws on the Hacker News thread cataloguing "claudish"
([48905248](https://news.ycombinator.com/item?id=48905248)), where readers named the specific words
and sentence shapes. Quotes are attributed in `references/markers-en.md`.

## License

MIT
