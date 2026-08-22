# The merged taxonomy

Thirteen families. Each row of an audit table names one. The behavioural contract is `SKILL.md`;
where this file and that one disagree, `SKILL.md` wins.

Attribution is per family, because it is the only way to see what each upstream project actually
knew. `D` = deslop, `S` = 说人话, `N` = natural-talk, `H` = Humanizer-zh.
`本项目新增` marks a family none of the four had.

The organising question for every family is the same one:

> Is this sentence **saying the thing**, or **being clever**?

---

## A. Performance and significance

### A1. Significance inflation `H D S`

Adding a claim about how some arbitrary aspect represents or contributes to a larger theme.

**zh watch-list:** 标志着 · 见证了 · 是……的体现/证明/提醒 · 极其重要的/关键性的作用 ·
凸显/彰显了其重要性 · 反映了更广泛的 · 象征着其持续的 · 为……奠定基础 · 代表着一个转变 ·
关键转折点 · 不断演变的格局 · 不可磨灭的印记 · 深深植根于

**en watch-list:** marks a turning point · stands as a testament · serves as a reminder ·
plays a pivotal role · underscores the importance of · reflects a broader · laid the groundwork for ·
an evolving landscape · left an indelible mark

> 加泰罗尼亚统计局于 1989 年正式成立，标志着西班牙区域统计演变史上的关键时刻。
> → 加泰罗尼亚统计局成立于 1989 年，负责独立于西班牙国家统计局收集和发布区域统计数据。

### A2. Notability inflation `H`

Repeated claims of prominence, usually a list of outlets with no context.

> 她的观点被《纽约时报》、BBC、《金融时报》引用。她在社交媒体上拥有超过 50 万粉丝。
> → 在 2024 年《纽约时报》的采访中，她认为 AI 监管应该关注结果而不是方法。

### A3. Promotional register `H S`

Brochure language, worst on heritage, place, and product topics.

**zh:** 拥有（夸张用法）· 充满活力的 · 丰富的（比喻）· 深刻的 · 增强其 · 致力于 · 自然之美 ·
坐落于 · 位于……的中心 · 开创性的 · 令人叹为观止 · 必游之地 · 迷人的 · 打造 · 赋能 · 助力
**en:** vibrant · boasts · nestled · breathtaking · must-visit · groundbreaking · seamless ·
cutting-edge · state-of-the-art

### A4. Dramatized closer `D`

A short assertion parked at the end of a paragraph to leave an aftertaste. Its function is that the
reader lingers. Nothing was communicated.

> 这部分代码里找不回来。 → 这部分信息无法从代码恢复。
> 需求文档、Gherkin、wiki 设计文档、OpenAPI，前几代都是这么死的。
> → …前几代都因此被弃用。
> And nobody noticed. / That is the whole trick. / The tests were green.

**Detection:** delete it. If no information went missing, it was decoration.

### A5. Editorial stance and self-assessment `D N`

The author grading their own sentence instead of writing it.

**Adverbs:** 真正 · 本质上 · 恰恰 · 正是 · 唯一 · 必然 · 显然 · 彻底 · 从不 · 永远
**Stance:** 老实说 · 诚实地讲 · 说得对 · 值得一提 · 更重要的是 · 关键在于 · 核心是 ·
the honest answer · to be honest · frankly · it's worth noting · the key insight is ·
the one that matters most · make no mistake · let that sink in

> Naur 说得对，理论无法从文档重建 → 与 Naur 的结论一致：理论无法从文档重建

`说得对` is the author scoring a quotation, not stating anything. The English family has a
recognisable three-beat version: *"You're absolutely right to question me" → "But it's not a
load-bearing issue" → "my honest take is…"*. Cut the frame, say the thing.

### A6. Generic positive conclusion `H S`

A vague optimistic ending regardless of what came before.

> 公司的未来看起来光明。激动人心的时代即将到来。 → 该公司计划明年再开设两个地点。
> 尽管存在这些挑战，未来前景依然光明 → (a plan, a date, a number, or delete)

---

## B. False structure

### B1. Staged reversal `D S N H`: all four, and the most reliable single marker

`不是 X，而是 Y` · `A 不在 B，在 C` · `与其 X，不如 Y` · `it's not X, it's Y` ·
`not just X but Y` · and every rewording of the same move, including the cross-sentence form
(`不是 A。而是 B`), the retrospective form (`我一直以为 A，后来才发现 B`), and the reversed form
(`Y, not X.`).

What is being managed is the *move*: **set up a misunderstanding the reader never held, then
overturn it to raise the price.** Changing the words does not exit the family.

> 判的是「该不该回头看」，不是「对不对」 → 判断是否需要复核，不判断代码正确与否
> It's not a documentation problem, it's a feedback problem.
> → Documentation does not fail here; the missing piece is feedback.

**Not counted per instance.** Counted by density, after exemptions. See `decisions.md` §B1 for the
thresholds and the two-instance exemption cap. Merely inverting `不是 X，是 Y` into `Y，不是 X` does
not lower the density; the skeleton is still there.

### B2. Negative enumeration `S`

> 它不是框架，不是库，也不是工具——它是一种思维方式。
> → 把它当作一种思维方式，不是一个具体工具。

### B3. Rule of three `H S N D`: **never counted**

Three items because three looks complete.

> 活动包括主题演讲、小组讨论和社交机会。 → 活动包括演讲和小组讨论，间隙可以自由交流。

**Test:** delete the numbering or the parallel frame. Is the content still natural and complete?
Yes → keep. The three exist only for symmetry → break it. Content that genuinely has three parts
("three common causes", a C1–C3 contribution list, a three-level taxonomy) is not a hit.

**Why never counted:** on the first document deslop scanned, all five hits were ordinary
enumerations. The tell is real; the counter is not.

### B4. Mechanical progression `S N`

> 首先，我们需要明确目标；其次，制定计划；最后，执行落地。
> → 先把目标定清楚，然后排优先级，边做边调。

Real step-by-step instructions may use 首先/其次. The empty structural pre-announcement is the hit.

### B5. Symmetry padding `S`

> 既要保证速度，又要保证质量；既要创新突破，又要稳定可靠。
> → 速度和质量之间我们优先质量。

### B6. Rhetorical setup `S`

> 如果我告诉你，90% 的创业公司都在犯同一个错误呢？
> → 90% 的创业公司在定价上犯同一个错误：按成本定价而不是按价值定价。

### B7. Dramatic fragments `S`

> 三年。两个人。一个想法。 → 两个人花了三年把这个想法做成了产品。

### B8. "Challenges and future prospects" `H`

A formulaic section that names no challenge and no next step.

> 尽管工业繁荣，Korattur 面临着城市地区典型的挑战……凭借其战略位置，继续蓬勃发展。
> → 2015 年三个新 IT 园区开业后，交通拥堵加剧。市政公司于 2022 年启动了雨水排水项目。

A real section with real content under the heading is not a hit.

### B9. List compulsion `S`

Numbering a three-line answer to manufacture orderliness.

> 我的建议如下：1. 先检查配置文件 2. 确认环境变量 3. 重启服务
> → 配置文件里的 DB_HOST 可能写错了，先看一眼。不是的话重启一下服务试试。

The inverse is also a defect: three items strung on `、` or commas inside running prose is a list the
document declined to write. See F1.

### B10. Uniform cadence `D S N H`

The words can all be plain and the structure still gives it away. Two sub-signals:

- **Sentence length uniformity.** Model sentence-length standard deviation runs near 1.2 where a
  human runs 4.7 or more. Reads flat, no breathing.
- **Skeleton repetition.** The same syntactic shape recurs, most often the staged reversal, next
  most often a matched short phrase landing at the end of each section. Each sentence works alone;
  read together you can predict the next one's shape.

Reviewers hear the metronome before they notice any word. Fix by varying sentence and paragraph
structure rather than by swapping words. Threshold for skeleton repetition: `decisions.md` §B1.

---

## C. False agency and abstraction

### C1. Personification and false agency `D S H N`

Abstract subjects (mechanisms, history, documents, cost, state) performing human or biological
actions.

> 状态活不过一次调用 → 调用结束后状态失效
> 历史永远不会提醒你 → 历史记录无法指示当前状态是否一致
> 该框架赋能了开发者社区 → 开发者用这个框架能少写 30% 的样板代码
> history reminds you · the test never lies · the spec knows

**Not a hit:** a system subject describing system behaviour (`网关返回 504`, `缓存过期`,
`the gateway returns 504`). Established terms of art that happen to be biological, such as *warm cache*,
*healthy*, *starvation* and *garbage collection*, are names rather than metaphors.

**A special case of H6**, and decided in the audit table, never by a script. Deciding it needs to
know whether the subject is abstract and whether the verb is conventional in the field.

### C2. Copula avoidance `H S`

A complicated construction where `is` / `has` would do.

> Gallery 825 作为 LAAA 的当代艺术展览空间。画廊设有四个独立空间，拥有超过 3000 平方英尺。
> → Gallery 825 是 LAAA 的当代艺术展览空间。画廊有四个房间，总面积 3000 平方英尺。
> serves as a → is a · represents a → is a · boasts a → has a · functions as a → is a

### C3. Nominalisation `S D H`

An empty verb carrying a verbal noun. Longer sentence, same information.

**Signal:** 进行 / 实现 / 完成 / 开展 / 起到 / 具有 + a verbal noun.
**en:** perform an analysis of · conduct a review of · achieve an improvement in · has the ability to

> 我们对流程进行了优化，实现了效率的显著提升。 → 我们把流程改顺了，一个人一天能多处理 20 单。
> The team performed an optimization of the deployment workflow. → The team simplified it.

**Keep:** fixed forms in legal, contractual, and official text (`进行公示`, `予以受理`); stable
nominalised terms in `docs` (`增量编译`, `执行计划生成`); formal register the user asked for.

### C4. Passive stacking `S H`

> 系统被优化后，性能被显著提升，用户体验被大幅改善。
> → 我们优化了数据库查询，页面加载从 3 秒降到 0.8 秒。

**Keep:** conventional academic and experimental passive (`The experiment was conducted`,
`was published`). See `SKILL.md` §2.2.

### C5. `-ing` pseudo-analysis `H`: English, high precision

A present participle clause bolted onto the end of a sentence to add depth that is not there.

> The temple's blue, green and gold tones resonate with the region's natural beauty, symbolising the
> Texas bluebonnet and reflecting the community's deep connection to the land.
> → The temple uses blue, green and gold. The architect said the colours echo the local bluebonnet.

**Watch:** highlighting · underscoring · emphasising · reflecting · symbolising · showcasing ·
demonstrating · ensuring · contributing to · fostering · cementing · solidifying · marking.

### C6. False range `H`

`from X to Y` where X and Y do not sit on one meaningful scale.

> 从大爆炸的奇点到宏伟的宇宙网，从恒星的诞生到暗物质的神秘舞蹈。
> → 这本书涵盖了大爆炸、恒星形成和当前关于暗物质的理论。

---

## D. Evidence and attribution

### D1. Unsourced citation `S H D N`

`研究表明` · `数据显示` · `业内人士认为` · `studies show` · `experts say` ·
`industry reports indicate` with nothing behind them.

**Pick a mode before touching the sentence**, per `SKILL.md` §4.1. The trap: deleting `40%` and leaving
"it will be faster" converts a checkable false claim into an uncheckable vague one. That is worse,
not better.

### D2. Vague attribution `H D`

Opinion assigned to an unnamed authority. `观察者指出` · `一些批评者认为` · `多个来源`.

> 专家认为它在区域生态系统中发挥着至关重要的作用。
> → 根据中国科学院 2019 年的调查，浩来河支持多种特有鱼类。

### D3. Knowledge-cutoff disclaimer `H N`

> 虽然关于公司成立的具体细节在现成资料中没有广泛记录，但它似乎是在 20 世纪 90 年代成立的。
> → 根据注册文件，该公司成立于 1994 年。

Go find out, or say you do not know. Do not leave the model's uncertainty in someone else's document.

### D4. Hedge stacking `H N S`

> 可以潜在地可能被认为该政策可能会对结果产生一些影响。 → 该政策可能会影响结果。
> arguably somewhat potentially → (pick one, or none)

**Not a hit:** a single hedge carrying real epistemic status, especially in `academic`. `suggests`,
`may`, `is consistent with`, `we argue` are claims about confidence. Strengthening one is a
principle-layer violation, not a style improvement.

### D5. Quantification ambiguity `S`

`缩小了 3 倍` · `翻了 1 倍` · `不超过 100 以上` · percentage endpoints with no stated basis.

**Do not resolve it for the author.** Flag it. Never invent a base, a year, a deadline, or a
measurement that the original did not contain. In `chat` / `public-writing`, an ambiguous quantity
that carries no key information may be compressed away entirely; it may not be replaced with a
different quantity.

---

### D6. Scope loss in relay 转述损耗 `本项目新增`

**Pattern.** A number that has a source, has a specific attribution, and is quantitatively
unambiguous, but which reached the author through a paraphrase that dropped the original record's
qualifiers. It is then used at the original's scope while only carrying the paraphrase's.

**Why the other three checks pass it.** D1 asks whether there is a source. D2 asks whether the
attribution is specific. D5 asks whether the quantity is unambiguous. This clears all three. It is
broken somewhere none of them looks: **the qualifiers evaporated in transit, and evaporation leaves
no mark.** The sentence reads better than an honest one would.

**Detection is not about the sentence.** It is about how the number reached you. One question:

> **Did I read the original record for this number?**

No is a hit. It does not matter whether the relay was a person, another session, a summary, or an
earlier note of your own.

**Default action.** Read the original record, or mark the claim as second-hand with its qualifiers
unverified. Doing neither and using it anyway is the defect.

**Worked instance**, from this repository's own exchange with the study its worked example is drawn
from. A sentence being cited repeatedly:

> 一次干净试跑 23/23 任务检查全过，而 spec 工作流零采纳

The original record is a smoke run: a clean-entry container, a fresh session, one model, `n=1`, and
what it measured was whether an agent would reach for the tooling **on its own**. It would not. But
ordinary use of that system is a stop hook holding the turn and a pre-commit check holding the
commit, which is event-triggered and blocking, and under those conditions adoption is routine.

The honest sentence is *"autonomous adoption is zero when nothing fires and nothing blocks"*. What
survived the relay was the word zero. The container, the model, the sample size, the smoke framing
and the word *autonomous* all evaporated, and none of their absence was visible in the citing text.

**Keep-condition.** The original record was read and its qualifiers survive into the sentence; or the
sentence is about the practice of relaying, as this one is.

**Where this check runs, and why it cannot run in the audit.** At the freeze step, `SKILL.md` §1
step 2, and its output is a set of frozen spans rather than a row in the table.

The audit is deliberately performed in a fresh context, because that is what stops an author from
re-reading their own intent. That same property makes it structurally unable to answer this family's
question: an auditor with no history cannot know which numbers arrived through a relay. The two jobs
need opposite amounts of context, so they cannot be the same pass.

**And this family is the one a good register pass makes worse.** Conditions of applicability are
prose with no formal signature, and they are exactly what makes a sentence blunt, so any pass
optimising for readability removes them by preference. The cleaner the result, the less visible the
loss. That is why the qualifiers must be frozen *before* the register work starts, by the one
operator who knows where the number came from, and why D6 is `audit-only` and never auto-applied:
**the information it needs is not in the text.**

## E. Diction

### E1. AI vocabulary `H D S N`

`references/lexicon.tsv`, 570 rows. Sourced to WP:AIVOCAB, Wikipedia's *Signs of AI writing*,
Kobak et al. 2025 on excess vocabulary in biomedical abstracts, Juzek & Ward 2025, HN 48905248, and
the Chinese community lists. Each row carries a plain replacement and a note where the word is
sometimes legitimate.

### E2. Elevated diction `D H`

A rarer, more "professional" word where a common one exists. Readers hear posturing.

| 端着 | 常用 | posturing | plain |
|---|---|---|---|
| 判据 | 判别方法 · 判断依据 | utilize | use |
| 驻留 | 留在内存里 | commence | start |
| 涵盖 | 包括 | facilitate | help |
| 旨在 | 用来 | in order to | to |
| 藉由 / 故而 / 遂 | 通过 / 所以 | a multitude of | many |

**Boundary one: plain is not colloquial.** Written Chinese defaults to two-syllable verbs. `承载`
does not become `装`, `阻断` does not become `拦`, `复核` does not become `再看一遍`. What goes is
the *rare* one. A *written* word is not itself a problem. The judgement is how common a word
is, and not how many characters it has.

**Boundary two: read it back.** If it now sounds like talking rather than writing, it went too far.

Three neighbouring defects share this pass: **文白夹杂** (classical particles in a colloquial
sentence: 其/之/乃/故/遂/藉), **nominalisation** (C3), and **四字格堆砌** (four-character phrases
assembled for symmetry: 同生共死, 逐条落地, 一以贯之).

### E3. Physical-verb metaphor `D`: Chinese, first sweep of the pass

See `SKILL.md` §6.1. One-syllable verbs are the priority because they read as brisk rather than
ornamental.

### E4. Business jargon `S N H D`

赋能 · 抓手 · 闭环 · 颗粒度 · 对齐 · 沉淀 · 痛点 · 链路 · 底层逻辑 · 打法 · 心智 ·
leverage · synergy · paradigm shift · game-changer · circle back · thought leader

### E5. Performed engineer-speak `S`: the family the other three lack

The model imitating an SRE writing a postmortem, in a conversation that is not one.

收窄 · 坐实 · 对上了 · 锁住 · 收口 · 落盘 · 兜住 · 更硬 · 打掉 · 压实 · 根因

> 我已经把差异收窄了，根因基本坐实，接下来做一个更硬的排除法把问题打掉。
> → 原因找到了：是缓存过期导致的。我把可能性排查了一遍，现在就剩这一个。

Related sub-families that behave the same way and do not each need their own word list:
**庸医问诊腔** (抠出来 / 揪出来 / 扒开 / 拽出来), **暴力动作腔** (砍一刀 / 补一刀 / 钉死 / 狠狠干),
**主动出击腔** (要不要我 / 我立马开始 / 顺手 / 趁热), **总结提示腔** (一句话总结 / 结论先说 /
说人话就是).

**Keep:** genuine postmortem, incident report, and changelog contexts, where 根因 / 收敛 / 收口 are
standard terms.

### E6. Jargon versus term of art `D`

**The ordinary word wins unless the reader needs the exact name.** This is an audit default, not a
word list. A term survives on two conditions together:

1. **One agreed referent.** A well-defined name earns weight. `缓存击穿` has a common definition but
   loose usage mixes it with 穿透 and 雪崩, so it is an audience question, not proof either way.
2. **No ordinary word for it.** `幂等` has none. `功能退化` is the ordinary word for `回归`, so
   `回归` goes.

A real term of art still stands: *drift*, *idempotent* / 幂等, *deadlock* / 死锁, *garbage
collection*, *back-pressure*, 埋点. Flattening those makes the text read as though the author does
not know the field, which is worse than leaving a tell. Note that a term of art can be a metaphor —
*deadlock* and *back-pressure* both are. Being a physical metaphor does not disqualify a word; being
an *unsettled* one does. That is why `击穿` alone is a verb to replace while `死锁` is a name to keep.

The exemption is about the reader: the same word is a term in a design doc and jargon in a talk.

### E7. Latching `D`

The model grabs one vivid word and reuses it. Count the frequency of any vivid word across the
document; three or more uses of the same metaphor means replace all but one.
Chinese metaphor families to count as a family: 活 / 漂 / 钉 / 塌 / 死.

### E8. Mixed metaphor fields `S`

Borrowing from several unrelated metaphor systems in one passage. Seven common ones: road/race,
war, building/collapse, temperature, warehouse, sea voyage, machine/organ.

> 这个赛道的护城河正在坍塌，团队需要重新点燃引擎，才能在这波浪潮里活下来。
> → 这个方向的门槛在降低，去年还得自研的部分现在有开源方案了。团队得找新的差异点。

**This family no longer has a threshold.** It is a special case of **H6**, the principle-layer ban
on building a metaphor at all. Mixing fields is the loudest version, not the only one. Literal uses
(`搜索引擎`, `代码仓库`, `商品库存`) and frozen names are still outside the rule; see H6 for the
boundary and for why nothing here can be counted.

### E9. Synonym cycling `S H`

The same referent renamed twice in adjacent sentences, each time one step more abstract. People
repeat a keyword without discomfort; a model swaps at the second mention and swaps again at the third.

> 他开始学修表。这门手艺上手比想象中慢……后来这项技能成了他主要的收入来源。
> → 他开始学修表。修表上手比想象中慢……后来修表成了他主要的收入来源。
> parser → component → module → it

Pronouns do not count; ordinary anaphora is correct. **This family also constrains your own edit:**
when reducing a Tier 3 density, do not rotate synonyms. That trades a density problem for a
slickness problem and the density is still there.

### E10. Fake colloquialism `S`

The model reaching for slang to seem grounded. Real people use these words at random; a model uses
them in batches.

> 姐妹们！这个工具真的绝绝子！谁懂啊，效率直接拉满！
> → 这个工具确实好用，主要是批量处理的速度快，省了不少时间。

### E11. Register mixing `S`

小红书 voice inside a technical document; heavy internal jargon inside a public article; official
notice and chat alternating in one paragraph; a review that forces two household objects into an
RPG-class metaphor. Decide the dominant register first, then remove the foreign one.

**Not a hit:** an English technical word inside a Chinese sentence, judged on what it means here
(`context 不崩`, `p99 突刺`). Do not apply an English word list mechanically to mixed text.

---

## F. Punctuation and surface

### F1. Compression punctuation `D`: the mechanism, not just the mark

`——`, `、`, `：` and the English em dash all do one job: let one sentence carry more than one thought
without committing to a second sentence. Full treatment in `SKILL.md` §6.3, including why
substitution is not a fix and why fixing this changes the document's shape.

**Counted:** every `、` the author wrote (marks inside `「」` are quoted and not counted); every
mid-prose `：` (label colons like `- **附件**：说明` and line-final ones introducing the block below
are structure, not staging); every em dash.

### F2. Em dash density and position `D H N S`

Beyond the count, look at *where* they land. First sentence opening with a dash, two or more in one
paragraph, several consecutive paragraphs carried by dashes: that is a template rather than a voice.
natural-talk's cap is ≤2 per 300–500 characters, held as a density for longer text.

### F3. Bold overuse `H N S`

Mechanical bolding to manufacture hierarchy.

> **用户体验：** 界面全面升级。**性能优化：** 算法显著提升。
> → 界面重新设计了，算法快了 2 倍，加了端到端加密。

**Exemption to name, not to assume:** in a paper or spec, bold on a term's first use is a definition.

### F4. Inline-title vertical lists `H N`

List items that open with a bold label and a colon, where the body then restates the label.

### F5. Emoji `H N`

Decorating headings and bullets. Only when explicitly requested. `✓` / `✗` in a comparison table are
table glyphs, not emoji.

### F6. Quote and punctuation hygiene `H D`

Curly quotes where the language wants straight or corner quotes; half-width punctuation inside a
Chinese sentence; missing space between Chinese and Latin/numerals; `；` where two sentences would
be clearer; `……` standing in for something the author should name.

### F7. Title case in headings `H`

English only. AI capitalises every major word. Sentence case is the convention in most house styles.

### F8. Exclamation marks `N`

≤3 per 300–500 characters, and in technical documents usually zero.

---

## G. Assistant residue

Text that was a chat reply, pasted in as content.

### G1. Collaborative traces `N H S`

作为 AI · 根据我的训练 · 希望这对你有帮助 · 如果还有问题请告诉我 ·
as an AI · I hope this helps · let me know if · Want me to

### G2. Sycophancy `N H S`

好问题 · 这个问题很有深度 · 你说得完全对 · 感谢你的提问 · Great question! · Certainly! ·
You're absolutely right!

### G3. Lecture tone and action pre-announcement `N S`

让我来解释一下 · 接下来我们将 · 拆一拆 · 盘一盘 · 划重点 · 敲黑板 · 捋一捋 ·
Let's dive in · Let me break this down · Without further ado · In this essay we will explore

### G4. Signposts `N S H`

值得注意的是 · 需要强调的是 · 更关键的是 · 事实上 · 换句话说 · 本质上 · 归根结底 ·
It's worth noting · At the end of the day · Here's the thing · Additionally · Furthermore

Capped, not banned: ≤2 per 300–500 characters.

### G5. Summary announcement `S`

一句话总结 · 结论先说 · 简单的说 · 说人话就是. Announcing that a summary is coming, instead of
summarising. Delete the announcement, keep the conclusion.

---

## H. Boundary violations: the principle layer

No cap, no scene exemption, no density threshold. One instance is a finding.

### H1. Fabrication `N D S H`

Any fact, number, source, date, mechanism, or causal relation not present in the original. Including
the friendly kind: an invented anecdote or an invented reaction added to make a draft feel human.

### H2. Judging the person `N S`

你不是敏感，你只是太久没被稳稳接住了 · 你问到了问题的核心 · 你比大多数人都清醒 ·
你现在的 X 很正常

Also the direction-certifying variant: `走在正确的路上` / `完全不用担心` may be deleted or replaced
with "the available information does not support a judgement". It may **not** be softened into
`方向没问题` / `不用太担心`, which is still deciding for the other person.

### H3. Identity-certifying praise `N S`

你有很强的批判性思维 · 你的观察力很敏锐 · 顶刊作者的素养 · 这个角度很新颖

Praise the content if the content deserves it. Do not issue the person a certificate.

### H4. Over-catching empathy `S N`

我完全理解你的感受 · 稳稳地接住你 · 不用向我解释 · 让我们一起…… ·
and the hugging variants (抱住 / 紧紧抱住 / 实实在在地接住).

**The one override in the whole taxonomy:** when someone has had bad news, comfort outranks this
rule. What is banned is performed empathy, not all emotional response.

**Not a hit:** `接住请求` / `接住流量` / `接住峰值` with a system subject and a result.

### H6. 造比喻 `本项目新增`

**模式**：为了说明 A，把 A 换成另一个域的 B，然后在 B 那个域里说话。

四种形态，以前分散在 C1、E3、E7、E8，现在归一条：

- **动作类比**（原 E3）。接住事件，压掉检查，把人叫回来
- **拟人**（原 C1）。状态活不过一次调用，历史会提醒你，测试不会说谎
- **单次借喻**（原 E8）。护城河，赛道，浪潮，点燃引擎
- **贯穿式**。整篇用一个源域讲另一件事，被解释对象的每个部件在源域里都有对应物

**为什么是绝对规则，而不是阈值。**原来的写法是分级的。E8 只抓多套混用，并且写着"单独一套用得准没
问题"；C1 留了系统主语豁免；E3 要求"字面替换更精确"才报。分级留下的每一个判断口，都是给自己开豁免
的地方。本仓库踩过：一份流程说明把"线性分段的版式"做成了一整套车间比喻，十四类指标全绿，四遍回读
全过，读者一眼看出是 AI 味，而规则当时明确豁免了它。绝对规则没有这个口子。

**判据在读者侧**：读者要不要在脑子里把 A 映射到 B 才能懂？要就是命中。

把判据放在读者的认知负担上，不放在词源上。词源没有用，所有抽象词往上追都是比喻。

**三样不在此列**，因为它们不是"在用比喻"：

1. **领域已经冻结成名字的术语。**死锁、幂等、垃圾回收、back-pressure、drift、pipeline、埋点。
   判据仍是 E6 那两条，有一个公认所指并且没有对应的普通词。名字不是比喻，它是这个东西的叫法。
   把它换成普通词会让文本读起来像外行写的，那比留一个痕迹更糟。
2. **已经死掉的隐喻。**深入、支撑、框架、流程、高层、run、handle。读者不做映射就懂，
   它已经是那个词本身了。
3. **所写对象本身就是那个域。**真的在讲仓库、温度、船的时候。

**加重信号**：作者花篇幅论证这个比喻是恰当的。一个在做功的说明不需要辩护。这同时命中 A5 和 J3。

**默认动作**：换成本义。换完那句话通常更短。如果发现整段没东西可说了，说明那一段本来就只有比喻。

**不进计数集，但规则仍然是绝对的。**名字、死隐喻、字面用法和活比喻在词面上无法区分，词表看见的
一律只是候选，所以没有任何东西能据此判定不合格。这两件事不矛盾。判定在审计表里做，脚本的职责是不让任何一个
候选漏检。`python3 tools/measure.py FILE --metaphor` 逐行列出所有借喻词和物理动词并给行号。

### H5. Solemn pre-announcement `S`

我必须很认真地说一句 · 我要讲一个更深一点的东西 · 这次我懂了，我真的懂了 · 说句实话 ·
坦白讲 · 缺点也说一句（免得你们说我恰饭）

Trading a declaration of honesty for credibility. Delete the stance layer. If a self-disclosed
drawback contains real information (crash frequency, applicability limits), that information stays.

---

## I. Headings

`references/titles.md`, seven rules. Summary: name the content, do not narrate the reading path;
stand alone without the previous page; give an object and an action; no rare words, and no
over-correction into a casual question; deliver what the heading promised; do not state the
conclusion the body is about to state; keep one syntactic form across same-level headings.

Also: **"Challenges and Future Prospects" is a heading-level tell** (B8), and a mid-prose `：` is
sometimes a heading the document declined to write (F1).

---

## J. Filler and padding

### J1. Filler phrases `H S D`

为了实现这一目标 → 为了实现这一点 · 由于下雨的事实 → 因为下雨 · 在这个时间点 → 现在 ·
系统具有处理的能力 → 系统可以处理 · in order to → to · due to the fact that → because ·
at this point in time → now

### J2. Fabricated atmosphere `S`

Precise time, weather, gesture, props, and cigarettes, with no source, forging a sense of scene.

> 凌晨三点，办公室只剩他一个人。窗外下着雨，桌上的咖啡早就凉了。
> → 那个 bug 卡了他两天。最后发现是时区配置在容器里没生效。

**Two conditions, both required:** the detail has no source (not supplied by the user, not
checkable) **and** deleting it changes nothing downstream. One alone is not a hit. The most dangerous
false positive in the whole taxonomy is deleting an experience the user actually told you.

### J3. Emphasising the unmistakable `D` (nofluff)

Warning a reader about a misreading they were never going to make. It shows the author's anxiety,
not consideration.

> 注意，这里的 spec 指的是本工具的 spec，不是别的 spec。

### J4. Coined terms `D` (nofluff)

Needing to invent a term to fill a paragraph usually means the thinking is not finished. Say it with
existing words first. Coinages also leak in during a rewrite. A replacement invented on the spot is
the same defect in new clothes.

Two more nofluff rules that no marker table covers: **delete rather than patch** (if a passage needs
extra explanation to stand, it should not be there), and **do not substitute intensity for argument**
(`革命性的` supplies volume rather than information; say `误报从 135 降到 67`).

---

## K. Chinese-specific

### K1. `你` density in documents `D`

See `SKILL.md` §6.4. Documents only; a reply to one person is dialogue.

### K2. Translationese `S`

Long attributive chains, stacked passives, `基于……`, `通过……来……`, subjects that will not end.
Shorten the subject and the action first.

### K3. Conjunction density `S`: scene-gated, never a global threshold

Only in `public-writing` narrative, opinion, and essay text. Never in `docs`, `status`, or
`code-context`. Judge distribution, not total: three consecutive sentences each opening with a
connective, or one connective three times in a paragraph. The calibration evidence for why there is
no global threshold is in `SKILL.md` §5.1 and it is the single best piece of measurement any of the
four projects did.

---

## L. What is out of scope

Register defects are not comprehension defects. This taxonomy does not contain, and a deslop pass
will not find:

- a pronoun with no antecedent;
- a claim on one page that contradicts a claim on another;
- a quoted authority whose argument has been misread;
- a number that is wrong;
- a conclusion the evidence does not support.

A rewrite that improves the register can make these *harder* to see, because the surrounding prose
gets more confident. Run a comprehension pass separately, with a different brief.

---

## M. Wrong reader `本项目新增`

Every family above is about how a sentence performs. This one is about who it is addressed to. The
text can be plain, specific, accurate and still fail, because it was written for the reader who
watched it being written. **bhelx** (49394255) states the general case: "The audience they are
writing for [is] you, but you're trying to write for a totally different audience."

The family comes from field reports rather than from this repository's own runs, and the sources are
in `references/field-reports.md`. `references/code-comments.md` is the working detail.

**Why it is separate from the rest.** No marker word appears in any of these. A comment can be
scrubbed of every entry in the lexicon and still be unreadable to the person who arrives next year,
because what is missing is not in the text at all. That also makes the family expensive to check:
see `SKILL.md` §12, row 4.

### M1. Temporal comment 时态注释

A comment that narrates the change instead of stating the state. `was` / `now` / `previously` /
`instead of` / `this fixes` / `needed because otherwise` / `note that we no longer`.

The context is real when it is written and expires when the change merges, because the defect it
describes no longer exists. What remains is a changelog entry in the wrong file, and a third copy of
text already in the commit body and the pull request.

**Test:** would this be true and useful to someone reading the file a year from now, who never saw
the diff? **Default action:** state the current behaviour, or move the history to the commit body.
What survives is the part `git log` cannot say: why the other approach does not work.

**Scan:** `python3 tools/measure.py FILE --comments` lists candidates with line numbers, in comment
lines only. Not a counted indicator: outside a comment this vocabulary is ordinary prose.

### M2. Room context 在场者上下文

A reference only someone in the session can resolve: the current conversation, a plan document, a
sprint identifier, a working file that will be deleted.

```
// No retry was added here per AC 37b in FEATURE.MD          (pluralmonad, 49392264)
// PLAN-5.1.A.d.42 load bearing reassertion                  (klardotsh, 49396760)
// The lesson from the Parse-dont-fail-era campaign          (jorl17, 49393612)
```

**Not a hit:** a stable identifier that outlives the change and can be looked up, such as an issue
number in a tracker that still exists. The test is whether the reference can be resolved from the
repository a year later, not whether it is short.

**Default action:** inline the fact, or cite something durable. `// Workaround: no age column in the
db. See JIRA-1234` is the same comment made resolvable (**crab_galaxy**, 49396229).

### M3. Leaked internal concern 内部关切外泄

Text the product's user reads, carrying the concerns of the people who built it: every edge case
handled, every state defended against, every reassurance nobody asked for.

**jorl17** (49393580): "The 'add' button does not need a label letting the user know that they will
later be able to click the 'delete' button." The tell is a sentence that answers a question the
reader has not asked, usually beginning as reassurance.

**Default action:** delete. This is the one place where the finding is usually a whole sentence
rather than a phrase, because the sentence exists to relieve an anxiety the reader does not have.
See the `ui-copy` scene in `SKILL.md` §2.

### M4. Working notes shipped 笔记未清理

The note was correct while the work was happening. Nothing removed it when the audience changed.

**cerved** (49394869) and **Exoristos** (49395718) both separate these: the notes are useful during
implementation and unfit to commit. Writing the note was never the problem. What is missing is the
step between writing it and shipping it.

**Default action:** relocate, do not delete. A note that fails M1's test but records a real decision
belongs in the commit body or a decisions file, recorded in the relations ledger (`SKILL.md` §4) so
that the move is visible. Report relocations separately from deletions.
