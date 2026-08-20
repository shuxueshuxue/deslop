# The false-positive corpus

Everything here looks like a tell and is not. Read this before the first pass, not after the damage.

A deslop pass that removes too much fails twice: it loses information, and it produces the flat,
voiceless text that Humanizer-zh correctly identifies as its own kind of tell. **Over-correction is
not a lesser failure than under-correction.**

## The six classic misjudgements

From natural-talk, which has the best material on this of the four.

### 1. "Delete every 首先 / 其次"

**Wrong:** any step-ordering word is lecture tone.

**Right:** real step-by-step instructions may use them.

> 首先备份数据，其次关闭服务，最后执行迁移。   ← operations. Keep.
> 首先我们需要理解背景，其次分析问题，最后给出方案。   ← empty scaffolding. Cut.

**Test:** delete the ordering words. Are the steps still there? Then they were steps.

### 2. "Every 实际上 is a violation"

**Wrong:** the signpost cap is 2, so drive all of them to 2 regardless of length.

**Right:** the cap is a sparseness signal at a 300–500 character baseline, held as a density for
longer text. Two in a medium reply is fine. Four `实际上` plus a `本质上` in one paragraph is not.

### 3. "Three points must be broken up"

**Wrong:** any list of three is the rule-of-three tell.

**Right:**

> 常见的一般有三种情况：1. 端口被占用 2. 镜像拉不下来 3. 权限不够   ← there are three. Keep.
> 这个问题的本质体现在三个核心维度：技术层面 / 业务层面 / 战略层面   ← cut into three. Break it.

**Test:** delete the numbering. Is the content still natural and complete?

In `academic`, a C1–C4 contribution list, a three-part falsifier list, and a three-level taxonomy are
all content. This is never a counted indicator anywhere.

### 4. "No closing sentence at all"

**Wrong:** the last line must be a cold fact.

**Right:**

> 大概率是这两个之一，日志贴全一点我能看得更准。 / 你看情况决定。 / 先这样。   ← natural. Keep.
> 希望这能帮助你解决问题！如果还有疑问请随时告诉我。   ← ceremony. Cut.

### 5. "Long replies are not direct"

**Wrong:** direct means short.

**Right:** direct means zero throat-clearing and zero pre-announcement. "Explain MySQL indexing in
detail" wants 500–1000 words. Using "be direct" as cover for a thin answer is the actual failure.

### 6. "Emotion is not allowed"

**Wrong:** natural means cold.

**Right:** performed empathy is banned; emotional response is not.

> 听到这个消息很难过。失去至亲是很重的痛。   ← real. Keep.
> 我完全理解你的感受。让我们一起度过这个困难时期。   ← performance. Cut.

**When someone has had bad news, comfort outranks every rule in this repository.**

## The misfire-protection list

From shuorenhua. A Tier 1 hit still stays when any of these holds. Full list with examples in
`decisions.md`; the ones that get missed most often:

- **The system subject.** `网关返回 504` is not personification. Non-human subjects describing
  system behaviour are correct.
- **Engineering terms in engineering reports.** 根因 / 收敛 / 收口 are standard in a postmortem. The
  tell is those words in a conversation that is not one.
- **Real internet voice with real detail.** `踩坑` after describing the actual pit is a person. The
  specifics are the evidence.
- **Literal technical verbs in English.** `navigate` / `traverse` / `route` in graph, network, and
  path-finding contexts.
- **Conventional academic passive.** `was conducted`, `was published`, `were sampled`.
- **Mixed-script judgement.** An English word inside a Chinese sentence is judged by what it means
  there. `这次 refactor 的 leverage 点在缓存` is jargon; `用 10 倍 leverage 做空` is finance.
- **User-supplied experience.** The single most dangerous deletion in the taxonomy is treating
  something the user actually told you as fabricated atmosphere. When in doubt, it stays.

## The over-correction pass itself

From deslop. Run it as a separate pass, not as a thing to keep in mind. Skipping it is the most
common way a deslop run makes text worse.

1. **Did a written word become a spoken one?** `判据` → `怎么判`. `触发源` → `触发的地方`.
2. **Did a two-syllable verb become one syllable?** Written Chinese prefers two. `承载` does not
   become `装`; `阻断` does not become `拦`; `复核` does not become `再看一遍`. What goes is the
   *rare* word, not the *written* one.
3. **Did a heading become a casual question?** Headings sit further toward written register than the
   body. `drift 判据` → `drift 检查的判别方法` is right; → `drift 怎么判` is over-corrected.
4. **Did a term of art get flattened?** *drift*, *anchor*, *warm cache*, *starvation*, *garbage
   collection*, *back-pressure*, *idempotent* / 幂等, *deadlock* / 死锁, 埋点. Flattening these makes
   the text read as though the author does not know the field, which is worse than leaving a tell.
5. **In `academic`: did a hedge get stronger?** `suggests` → `shows`, `may` → `does`, `is consistent
   with` → `proves`. Did a limitation get shorter? Either is a principle-layer violation, not a
   style call.
6. **Re-run the taxonomy on the words you just wrote.** A replacement is new prose and carries the
   same defect. This happens constantly: `砍掉` swapped for `压掉`, then `击穿` swapped for `打穿` —
   one physical verb on an abstract object traded for another, twice, by someone who had just
   written the rule against it. Coinages leak the same way (`自扫` for "scan the document against
   itself"). Read your replacements as if a stranger wrote them.

**If a sentence now sounds like conversation rather than a document, put it back and pick a common
word instead of a spoken one. The target is common, not casual.**

## The pass that has nothing to do with words

From deslop, and it is the one people skip because it feels redundant.

Read the whole document straight through, once, at the end. The line-by-line passes and the scanner
both work item by item, and there is a class of damage they structurally cannot see: **the boundary
between two items.** An edit that swallowed the heading between two paragraphs leaves both paragraphs
correct on their own and the seam between them nonsense.

Resolving to be more careful does not help here. Care does not produce a second reading. A different
kind of pass does.

## Three fast tests, when nothing else resolves it

1. **Delete test.** Remove the word or sentence. Is any information lost? No → remove it.
2. **Specificity test.** A reader asks "what specifically does this mean". Can you answer with a
   fact? No → it is filler.
3. **Register test.** Read it aloud against the scene's anchor (`SKILL.md` §2). Chinese: could this
   be a dubbing line? English document: could this be a Wikipedia sentence, or a good paper's?
   Chat: would you say this to a friend?

The rules exist to make text more natural. They do not exist to turn you into a deletion machine.
