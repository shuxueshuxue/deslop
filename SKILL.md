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

**第二种表演，用的是另一种货币：证明写的人是圈内人。**上面那一段说的是证明自己聪明。黑话、
假口语、心照不宣的插话、只有同行才接得住的简写，走的都是另一条路，它们卖的不是智力而是身份。

两者在读者那里的下场不一样，这也是第二种更值得防的原因。端着（`taxonomy.md` E2）听上去像装，
读者当场就听出来。黑话听上去像熟练，读者往往听不出来，所以它在改稿里活得更久，而作者本人几乎
永远发现不了，因为在他自己耳朵里那就是行话说得顺。

这一段的说法来自本仓库作者，照录：

> AI 现在的默认是**愚蠢但狡黠**，而目标是**聪明但幼稚**。真正的聪明绝对不是装成小人。
> 要以童真的初心描写严肃的事情。

狡黠指的是那种心照不宣、见过世面的口气，而底下的内容撑不住这个口气。幼稚在这里不是贬义，
它指的是愿意用普通词，愿意问显然的问题，愿意在读者面前显得不老练。题目越重，越不该靠口气去撑。

**做法上只有一条纪律，叫做憋着一口气。它是一个动作，不是一条规则。**想到一句漂亮的话，
圈内人一看就会心，那就不写。不为了显得是圈内人而放松语言。这条没有办法做成计数指标，
因为被憋回去的那句话根本不会出现在文本里，任何检查都看不见它。它只能发生在写的时候。

**能检查的那一半是 E6 的两条。**这个词有没有一个公认所指，有没有对应的普通词。过了就是术语，
留着；不过就是黑话，换掉。同一条边界也挡住反方向的失误，幼稚不等于外行，把真正的术语铺平会让
文本读起来像外行写的，那比留一个痕迹更糟。

**再往前一步：故意显得笨拙，或者说乐于暴露自己的笨拙。**幼稚是愿意在读者面前显得不老练，
笨拙是主动去选那个不顺的说法。这一条挡的是本文件自己记录在案的一个失败。§4 写着，
限定条件正是让句子变钝的那部分，所以一次以可读性为目标的清理会持续朝着删掉它们的方向使劲。
写的人如果本来就偏爱变钝的那一版，这条路径就窄了。

照着做是四件事：

- 句子读起来磕绊，先问是不是限定条件让它磕绊的。是的话，留着磕绊。
- 有一面没有验，就写"这一面没有验"，不要绕过去。
- 宁可用普通词多写几个字，也不要用更贴切的行话省那几个字。
- 不为了顺，把两件事并进一句。

**边界：笨拙不是邋遢。**它不是把话写不清楚的许可。判据仍然是上面 nofluff 的两条，删掉它信息有没有
少，读者问"具体指什么"答不答得出一个事实。带着限定条件的磕绊句子过得了这两条，什么都不带的
磕绊句子过不了。

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
2. **Protected spans + fact record.** freeze what may not drift, before reading for style (§4).
   **Run the D6 provenance question here, not in the audit** (`taxonomy.md` D6). For every number
   the text leans on, ask whether you read the original record; where the answer is no, or where the
   record carries conditions the sentence needs, mark those words as frozen spans. This is the only
   step whose operator has the provenance knowledge, and the freeze is the output.
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
   **Two questions in this step are not answerable by scanning**, so ask them explicitly rather than
   waiting for a hit to surface. On every compressed term: does the reader have to expand it before
   its referent is fixed (`taxonomy.md` N1)? On every sentence that states a judgement: if this were
   wrong, could a reader see from the sentence where it might be wrong (N2)? Both fail silently,
   because a text with neither handle in it reads well.
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
| `ui-copy` | a label that names the control | standard | `bounded` | `audit-only` | remove a warning the product does not actually handle |

Chinese register anchor, all scenes: **the dubbing register of Japanese film.** Full sentences,
subjects present, two-syllable verbs (`阻断` not `拦`, `承载` not `装`), no slang, no in-group
shorthand, steady but not stiff. Read the result aloud; if it could be a dubbing line, the register
is right. Both failure directions are audible immediately.

English anchor, all document scenes: **Wikipedia, Hacker News technical comments, and good papers.**

**三个锚点，各管一件事。**一个锚点只回答它管得到的问题。把三个并排放，是因为它们管的不是同一件事，
而不是因为多多益善。

| 锚点 | 它决定什么 | 它决定不了什么 |
|---|---|---|
| 日本电影的配音腔 | 句子完不完整，主语在不在位，动词是不是双音节 | 节奏，口气，写给谁看 |
| 百科条目 | 节奏均不均匀，有没有留悬念，分歧写没写成谁的分歧，把握程度标没标出来 | 怎么收尾，以及是不是在对着一小撮人说话 |
| 新闻联播的播报体 | 对谁说，以及怎么停。面向所有人，不假设读者属于哪个圈子，不表个人立场，事情说完就停 | 句法和用词 |

`taxonomy.md` N 对着第二个锚点量。第三个锚点回答的那个问题以前没有锚点管：文本是不是在对着
一小撮人说话。这跟 M2 是同一个方向，M2 问的是读者能不能还原一个指称，这里问的是文本有没有
假设读者属于某个圈子。

第三个也是三个里最容易吃亏的一个，所以按 §2.3 的规矩，先写明要禁掉它自己的什么。播报体带进来的
东西不比它给的少：

- **意义拔高。**`取得了显著成效`，`迈上新台阶`，`开创了新局面`。这是 A1，也是播报体带得最重的一样。
- **口号与四字格堆砌。**为整齐而凑的四字短语，E2 的邻居。
- **泛指的集体主语。**`广大`，`各方`，`有关方面`。它让 D2 无源归属穿着正式的外衣进来。
- **程式化的正面收尾。**A6。

取的是前一半，节奏均匀、面向所有人、说完就停。后一半一样也不要。

**两种自吹自擂，taxonomy 里都已经有位置，不需要新族。**推广文案那种是 A3 促销腔加 A1 意义拔高。
学术那种是 A2 值得性拔高加 A5 自我评价，`§5.2` 里被作者删掉的那句
`We consider this the strongest feature of the design` 就是标本。两者是同一件事的两个场合，
所以判定标准也是同一条，作者在给自己的东西打分，而不是把它写出来。

`code-context` and `ui-copy` have their own file, `references/code-comments.md`, because the
defect there is usually not a phrase. It is text addressed to the reader who watched it being
written (`taxonomy.md` M).

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

### 2.3 用一个人来说明语域，以及这样做的代价

把语域锚点写成**一个人和他日常写的那种文件**，通常比写成形容词更可操作。「写得像百科」是抽象的，
读的人还要自己把它翻译成动作；「你写的是一份要交上去的情况说明」带着一整套具体约束，限定条件要写全，
分歧要写成谁的分歧，没把握的地方不下定论，不留悬念也不抖包袱。这一节把这种写法收进来。

这条来自一次对话里的建议，本仓库还没有拿它跑过对照，所以下面写的是它的形状和边界，不是它的效果。

**代价一：人格会把它自己的语域缺陷一起带进来。** 外交文书有它自己的套话，`关切地注意到`、`重申`、
`敦促各方`，还有名词化堆叠和被动堆叠，正好是 C3 和 C4。换一个人格如果不先说清楚要禁掉什么，
换来的多半是另一种腔，而且因为它听上去更正式，反而更难被自己看见。**所以用人格之前，先把这个人格
自己的毛病列成禁用项。**

**代价二：它只能用来读回去对照，不能用来生成。** `不伪造声音` 在原则层，
`references/provenance.md` 的第 1 条裁决把 `re-voice` 设成默认关，并且要求材料是作者真有的。
让模型「扮演某人来改写」正好是那条裁决拒掉的动作。用同一个人格去问「这一段读起来像不像那种文件」，
则只是把 §2 的锚点说得更具体，没有越界。本文件采用后一种用法。

三个可用的锚点人格，以及各自要先禁掉的东西：

| 人格 | 它带来的 | 先禁掉它自己的 |
|---|---|---|
| 一份提交给理事会的情况说明的起草人 | 限定条件写全，分歧归属清楚，不夸大后果 | 套话（`关切地注意到`、`重申`、`敦促`），名词化堆叠（C3），被动堆叠（C4） |
| 百科条目的撰稿人 | 节奏均匀，不设悬念，有分歧就写明是谁的分歧 | 中立到连有把握的判断也写成争议 |
| 事故报告的撰写人 | 时间线清楚，因果不夸大，不追责，限定条件是正文而不是脚注 | 编号与内部代号（M2），过度被动 |

第三个可能是三个里带进来的毛病最少的，因为事故报告的写作规范本来就要求把不确定的地方标出来。
这句话是推测，没有测过。

**它不动别的轴。** 人格只影响回读时的对照标准，不影响 level、scope、保护片段、Tier，也不给
`re-voice` 开口子。

---

---

## 3. Level × scope

Two independent axes. Confusing them is the most common way this goes wrong.

A length cap is a third instrument and it belongs to the author. **mmastrac** (HN 49389501)
reports it as the strongest single lever there is: comment blocks under 7 words, function names
under 4, user-facing strings under 10. A cap is enforceable in a way a style instruction is not,
which is exactly why it must be *given* rather than inferred. A cap the editor invents is the
−39% failure `references/provenance.md` records, arriving under a new name. Ask for the number,
write it into the output contract, and report the length you actually landed on.

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

## 4. Protected spans, and the record

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
- **Conditions of applicability.** The words that bound where a claim holds: `in a clean-entry
  container`, `a fresh session`, `one model`, `a smoke run`, `n=1`, `autonomously`, `on the training
  split`, `under load`. Freeze them with the numbers they bound, not separately.

  **This class is the one the rest of this file puts at risk**, so it gets its own paragraph.
  The other protected classes have a shape a script can find: a numeral, a backtick, a quotation
  mark, a path. A condition of applicability is ordinary prose and looks like every other clause.
  It is also, precisely, the part that makes a sentence blunt, which means **a pass optimising for
  readability applies steady pressure to remove it.** Compare:

  > 在一个 clean-entry 容器里的一次 smoke 中，一个全新 session 自主采纳为零
  > 一个 agent 通过了全部检查却没用那套工作流

  The second reads better, and the register instincts in this document mostly prefer it. It is also a
  different claim, and no check further down this pipeline reports the difference, because the sentence that
  remains is well formed and correctly attributed. See `taxonomy.md` D6, and mark these spans at
  step 2 before any of the rest runs.

- **In `code-context`:** the described runtime behaviour, applicable conditions, and boundary notes.
  Strip stance words from a comment; keep what it says the code does. A neighbouring line already
  showing a number does not make the sentence redundant.

Alongside the spans, keep a **relations record**. This is where most silent damage happens, and no
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
  `：`, assistant residue, knowledge-cutoff disclaimer, emoji, `-ing` pseudo-analysis tails,
  copula dodges, false ranges, curly quotes in Chinese.
- **CAPPED.** legitimate below a length-normalised cap; only the excess is a finding: signposts,
  editorial stance, lecture tone, exclamation marks, stacked hedges, bold density, inline-title
  list items, the trailing contrastive tail. The caps come from
  natural-talk's 300–500 character reply baseline and are held as a density for longer text.
- **REPORTED. Never gates anything.** Sentence-length CV, conjunction density, nominalisation,
  mixed metaphor fields, rule-of-three candidates, lexicon hits by category.

Four families have no counter, three of them by demotion on evidence, and two more indicators were
demoted from GATED to CAPPED the first time this repository ran its own gates over its own prose
(§5.3). The first two below are printed in every report so nobody quietly re-promotes them:

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

- **Unearned confidence is not counted.** A script can list sentences that assert without hedging,
  and most of them will be ordinary statements of fact, so hits are nowhere near almost-always-real.
  This is a precision problem rather than a scope one (§12.1), which means the script would still
  earn its keep as a candidate lister. None is written yet, and the family is new enough that
  writing one now would fix the wrong shape. `taxonomy.md` N2.

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
whole against 61 cases: currently 100% recall at 97.6% precision, with both false positives coming
from deliberately broad rules (`你` in documents, `请求` under over-catching empathy).

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

### 5.3 Run the gates on your own contract

Anything that states these rules is text, and the rules apply to it. **ziga** (HN 49390469) asked a
model to write the anti-register rules and the first line it produced was "Avoid the stock LLM
register", written in the register it forbade. **dwaltrip** (49395110), reading another tool in this
family: "The readme is filled with slop. Bad sign…"

`python3 tools/selfcheck.py` holds this repository to §5.1: every GATED hit in the 15 files that
speak in deslop's own voice is driven to zero or named in `references/selfcheck.tsv`, with the
reason on the row. An unnamed hit fails the check; so does a reason left behind after its hit is
gone, which is what stops the list becoming a blanket exemption. A CAPPED indicator over its cap
needs a reason too, one per file and indicator rather than per hit, because the size of the excess
moves with the file and only the fact of exceeding the cap is worth a sentence.

The first run demoted two indicators. The trailing contrastive tail (`…, not a style call.`) had six
hits here and one was real; the inline-title list item had eleven and none was, because F4's rule
requires the body to restate the label and no regex can see that. A third pattern was found and
deliberately not acted on: 17 of the 30 hit-level survivors are `、` used as a list separator, which the counter
cannot distinguish from a clause joiner, but marker inventories are the least representative Chinese
prose available and demoting on them would be fitting the rule to the corpus that embarrasses it.
`references/field-reports.md` carries the counts and the condition that would settle it.

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

`python3 tools/measure.py FILE --hits` matches against `references/lexicon.tsv` (625 rows, Chinese
and English, each with a plain replacement, a note where the word is sometimes legitimate, and the
upstream project it came from).

It catches vocabulary and fixed phrases **as candidates**. A hit is not an instruction to rewrite.
It cannot tell whether a quotation is in play, whether `robust` is the statistics term, whether
`harness` names a mechanism, or whether `判据` fits the written register. It is blind to every one of
these: a dramatized closer, a superfluous paragraph-ending summary, an analogy doing no work, a
heading that narrates instead of naming, uniform cadence, a forced triad, a "challenges and future
prospects" section, a generic optimistic ending, and a sentence that fails both nofluff checks.

The whole M family is outside it too, and for a different reason: those defects contain no marker
word at all, so a clean scan says nothing about them. In `code-context` run
`python3 tools/measure.py FILE --comments`, which lists M1 and M2 candidates in comment lines with
line numbers. Like `--metaphor` it produces candidates and never a count, because outside a comment
the same vocabulary is ordinary prose.

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

`references/taxonomy.md` holds the fourteen families. `references/decisions.md` holds the per-hit
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

**Pass B.** Over-correction. Run it as its own pass. Skipping it is the most common way a deslop
run makes text worse.

- Did a written word become a spoken one? (`判据` → `怎么判`, `触发源` → `触发的地方`)
- Did an expansion pad the sentence? Unpacking a clipped term (`taxonomy.md` N1) makes it longer by
  construction, and in a short sentence the added words can carry nothing. Both directions are
  over-correction; only the first one used to be asked about here.
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
4. **the missing-basis notes**, if any claim needed one and did not have it. A number the author
   reached through a paraphrase rather than the original record belongs here even when it has a
   source and a specific attribution. See `taxonomy.md` D6;
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

deslop fixes how a text sounds. **It does not check whether the text is right.**

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

### 11.1 The pass decays while it runs

The rules in this file stop being followed as the session that is applying them gets longer, and the
process enforcing the rule is not exempt from it.

This repository's own evidence is the strongest kind available, because the rule was in view the
whole time: **on every editing round without exception**, Pass B caught em dashes, `、` and
mid-sentence `：` that the pass had just introduced in its own replacement text while removing
others somewhere else. That is not carelessness that more care would fix. It is the reason Pass B is
a separate pass with its own reread rather than a thing to bear in mind.

Seven people in HN 49388752 report the same shape from outside (`references/field-reports.md`):
style rules fade as context grows, the register returns immediately after a compaction, and
comment rules enforced by a hook are still violated a substantial fraction of the time.

What to do about it, in order of how much it buys:

1. **Re-measure. Never assert.** The counted indicators in §5.1 exist because a claim that the
   register is gone is worth nothing and a re-scan is worth something. This is the whole defence and
   the rest is cheaper insurance.
2. **Run Pass B on your replacements, not on the original.** §9 states it. It is the step people
   skip because the replacements feel like the fix rather than new prose.
3. **Take a canary.** **nater5000** (49389776): put one small unmistakable rule in the instructions
   and watch for the moment it stops being obeyed. In a deslop run, `tools/measure.py` on your own
   draft report is the canary: if the report about removing em dashes contains em dashes, the
   session has drifted and the audit needs a fresh read rather than another edit.
4. **Prefer a fresh read to a longer session.** Pass D is a whole-document read, and it is worth
   more when the context that produced the edits is no longer in view.

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
| everything the writer knows, versus what the reader will have | a reader who was not in the room | text that is accurate and unreadable (`taxonomy.md` M) |

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

A third position on the same shape, and the one that hides best: **a relay carries less scope than
the record it came from, and the loss leaves no mark.** A number quoted from a paraphrase has a
source, a specific attribution and an unambiguous value, so every attribution check passes, while the
qualifiers that bounded it are simply not there any more. `taxonomy.md` D6.

Put the three together and the pattern is one sentence with three placements:

| where the mismatch sits | what you end up believing |
|---|---|
| the check sees less than the defect spans | it passed |
| the measurement is taken above the size the decision is made at | the number supports the claim |
| the relay carries less than the record | the citation means what you need it to mean |
| the check carries more context than the reader will | the text is clear |

All four are silent, and silence is the reason each one needs its own gate rather than more care.

The fourth is the same shape with the sign reversed, and it is the hardest to run. The other three
are checks that see too little. This one is a check that sees too much: the author supplies the
missing context for free, every time, without noticing, so the comment reads fine to the only person
in a position to inspect it. **bhelx** (HN 49394255) states it as a fact about the audience, and
**jorl17** (49393580) reports the mitigation and its limit in the same breath: hand it to a reader
with fresh context, and it helps but does not solve it. There is no version of this gate that the
writer can run alone, which is why `taxonomy.md` M is a report to the author rather than an edit.

**What this is and is not.** Three placements sharing a shape is a reason to take the shape
seriously. It is not a demonstration that the shape is right. The study it comes from has not yet
measured its own central prediction, and nothing here measures this one either. Treat it as a
working generalisation that has earned attention by recurring, and keep it separable from the parts
of this file that rest on a count.

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

- `references/taxonomy.md`. The fourteen marker families, merged, with source attribution per family.
- `references/decisions.md`. Per-hit decision procedure, exemption caps, keep conditions, `in-place` alternates.
- `references/titles.md`. Headings: name the content, do not narrate the reading path.
- `references/overcorrection.md`. The false-positive corpus: what looks like a tell and is not.
- `references/provenance.md`. What came from where, every conflict between the four, and the ruling.
- `references/field-reports.md`. What the public complaint threads are worth, attributed, and which parts changed this file.
- `references/code-comments.md`. The `code-context` and `ui-copy` scenes in detail: the survival test, the boundary, the specimens.
- `references/selfcheck.tsv`. Every GATED hit still standing in this repository's own prose, with the reason on the row.
- `references/lexicon.tsv`. 625 candidate rows, zh and en, each with replacement, note, and source project.
- `references/supplement.tsv`. Hand-kept rows only Humanizer-zh and natural-talk carry.
- `tools/measure.py`. Indicators, worksheet, before/after diff. No dependencies beyond python3.
- `tools/build_lexicon.py`. Rebuilds the lexicon from the four upstream checkouts, deduping by match.
- `tools/selfcheck.py`. Runs the gates on this repository's own prose. §5.3.
- `worked-example/`. A full run on a real paper draft: measurements, audit, rewrite, re-measurement.
