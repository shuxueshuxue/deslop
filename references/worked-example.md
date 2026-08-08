# Worked example

A conference talk deck, Chinese, ~1,700 characters on screen, audience of software-engineering
researchers. The author had already rewritten it several times and still judged it "too AI".

A fresh-context subagent audited the extracted prose against `markers-zh.md` and returned 45 findings
plus three counts. All 45 were applied.

## Indicators

| | before | after |
|---|---|---|
| staged reversals (`不是 X，是 Y`) | 12 | 0 |
| em dashes (`——`) | 10 | 0 |
| personification | 14 | 0 |

Same word count (1,682 → 1,678). Nothing was cut; sentences were restated.

## Selected pairs

**Action metaphor**

> 接住每个 MR 的每一版，我们给它开一个自己的 review session
> → 对每个 MR 的每个版本，创建一个 review session

> 写和读的成本都塌了
> → 写和读的成本都大幅下降

> pre-commit 会当场拦下这次提交
> → pre-commit 会拒绝这次提交

**Personification**

> 状态活不过一次调用 / 状态活不过一个会话 / 状态活得和项目一样久
> → 调用结束即失效 / 会话结束即失效 / 与项目同生命周期

Three lines had used the same biological metaphor in sequence. The parallelism also hid a category
error: the first two describe lifetime, the third describes ownership. Flattening exposed it.

> 但历史记得再全，也有一件事做不到：它不会过期，所以它永远不会提醒你。
> → 但无论历史记录多完整，都有一个固有限制：历史不会失效，因此无法指示当前代码是否仍与其一致。

**Staged reversal**

> 判的是「该不该回头看」，不是「对不对」
> → 这个检查判断是否需要复核，不判断代码正确与否

**Dramatized closer**

> 需求文档、Gherkin、wiki 设计文档、OpenAPI，前几代都是这么死的。
> → 需求文档、Gherkin、wiki 设计文档、OpenAPI，前几代都因此被弃用。

> 这部分代码里找不回来。
> → 这部分信息无法从代码恢复。

**Self-assessment**

> Naur 说得对，程序背后那套理论没法从文档里重建。
> → 与 Naur 的结论一致：程序背后的理论无法从文档重建。

The reviewer's note on this one is the sharpest in the audit: *「说得对」是作者在给引文打分，不是陈述。*

**Jargon**

> 同赛道都在把记录做细 → 相关工作都在提高记录粒度
> 测试也绿 → 测试通过
> 踩过的坑 → 已知的失败案例

## What the audit could not do

Two earlier rounds of review, by subagents with different briefs, had found problems the marker
taxonomy does not cover: a dangling pronoun with no antecedent, a claim on one page that contradicted
a claim on another, and a quoted authority whose argument had been subtly misread. Those are
comprehension defects, not register defects.

`deslop` fixes how the text sounds. It does not check whether the text is right.
