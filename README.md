<div align="center">

# deslop

**去掉技术文案里的模型腔。**

这是一个供 [Claude Code](https://claude.ai/code) 使用的 skill，支持中文和英文。

中文（默认） | [English](./README.en.md)

</div>

---

LLM 写的或润色过的文字通常会留下固定的句式和用词。它们可以被识别、统计，也可以被改掉。

`deslop` 按照标记分类检查文档，逐行列出需要删除或改写的内容，应用修改后再测量机械指标和拟人化用法。结果有可复核的数字，不只是一句“读起来更自然”。

## 最容易弄错的地方

**平实、谨慎的文字不是问题，正是目标。**

模型腔的问题在于，作者在展示自己有多聪明。生动的类比、刻意的反转、段尾的漂亮收束，以及听起来更专业的词，都在做同一件事：让作者显得聪明。逐句看它们往往没有语法问题，所以更容易被留下。

检查每句话时只问一件事：

> 这句话是在陈述事实，还是在表演？

目标是谦逊、平实、具体的技术文档。可以参考 Wikipedia、Hacker News 上的技术评论和学术论文。

## 修改的默认规则

不要假定原句可以保留。模型文字通常是整篇文字的语域偏离目标，不能只改掉少数最明显的句子。

保留一句话需要理由，改写一句话不需要。这里的“激进”只表示修改范围大，不表示让结果更响亮。改完的文字仍应平实，并且比原文更短或信息更密。

## 两个快速检查

1. **删掉这句话，信息有没有减少？** 没有就删掉。
2. **读者问“具体是什么意思”时，能不能用事实回答？** 不能就继续改写。

这两条来自 [nofluff](https://nofluff.0x01.me/nofluff.txt) 标准，完整内容见 [`references/nofluff.md`](references/nofluff.md)。分类表告诉你去哪里找问题；这两条决定一句话是否应该存在。

## 能检查什么

| 类型 | 示例 |
|---|---|
| **动作类比** | `接住每个事件` → `为每个事件创建一条记录`；`costs collapsed` → `costs fell` |
| **拟人** | `状态活不过一次调用` → `调用结束即失效`；`history reminds you` → `history does not indicate` |
| **对偶反转** | `不是 X，是 Y`；`it's not X, it's Y`。这是最稳定的模型腔标记之一 |
| **压缩标点** | `——`、`、`、`：` 把多个想法塞进一句话；检查会统计它们，并要求把结构拆开 |
| **翻译过来的第二人称** | 中文技术文档里密集出现的“你”，通常是英文文档语气的遗留 |
| **戏剧性收尾** | 段尾追加一句短断言，制造余味却没有增加信息 |
| **作者自评** | `Naur 说得对` → `与 Naur 的结论一致`；`my honest take` → 删除 |
| **破折号** | 统计数量和出现位置，检查是否用来代替完整句子 |
| **词语复读** | 同一个生动词在全文反复出现 |
| **抬高的用词** | `判据` → `判定规则`；`utilize` → `use` |
| **圈内黑话** | 赛道、闭环、抓手；`load-bearing`、`key insight`、`synthesize` |

标准术语不会被强行改成普通词。如果机制的正式名称就是 *drift*、*anchor*、*garbage collection* 或 *back-pressure*，就保留术语；只有在存在准确的普通替代词时才改写。

## 安装

```sh
git clone https://github.com/shuxueshuxue/deslop.git ~/.claude/skills/deslop
```

然后在 Claude Code 中使用：

```
/deslop  README
/deslop  slides/talk.html —— 面向中文会议听众
```

也可以直接说“这段文字有 AI 味，帮我改掉”。Skill 的描述已经覆盖这类请求。

## 扫描器

```sh
python3 scan.py --strip draft.md          # 按出现频率列出候选
python3 scan.py --strip --lines draft.md  # 每个命中显示行号
python3 scan.py --lang zh draft.md        # 只检查中文
```

输出示例：

```
count   term            category   replacement          note
5       leverage        vocab      use
1       不是历史，是     shape      （只保留后半句）       对偶反转，计入指标

# lexicon hits: 7  (2.9 per 1000 chars)
# staged reversal: 1
# em dash: 1
# 顿号: 14
# 句中冒号: 3
```

`references/lexicon.tsv` 中的每个中文或英文词条都带有普通替代词。扫描器只报告候选，不会自动改写；有些词在特定上下文中完全正确，词条备注会说明这一点。

顿号和句中冒号通常一开始很多。这些标点本身没有错，但文档常用一个句子代替本应分开的结构。改写时应拆分句子，把行内枚举改成真正的列表，必要时把冒号后的说明改成标题。

词汇选择只是脚本能处理的一半。戏剧性收尾、重复段意的句子、没有实际作用的类比，以及描述阅读路径而不是内容的标题，都需要人工审查。

## 工作流程

1. **提取正文。** 去掉 Markdown 和 HTML 标记，只检查读者真正看到的文字。
2. **运行扫描器。** 先得到词汇候选和机械指标。
3. **逐行审查。** 在全新的上下文中检查句子，避免只按自己刚才的意图阅读。
4. **统计指标。** 机械统计对偶反转和破折号；在审查表中单独统计拟人。
5. **应用修改。** 使用字面含义，不要用另一个生动词替换原来的生动词。
6. **重新测量。** 报告修改前后的数字。

`reversals 12 → 0` 是证据，“现在读起来很自然”不是。

## 不负责什么

**不抹平术语。** 术语有明确含义且没有普通替代词时会保留。把 *spec drift* 改成生硬的中文，反而会让文档失去准确性。

**不修改论点。** 工具可以重写表达论点的句子，但不会改变论点本身。重排章节和删除段落需要作者确认。

**不检查事实正确性。** 语域和事实是两类问题。文字可以很平实，但仍然存在悬空指代、自相矛盾或错误引用。完整示例见 [`references/worked-example.md`](references/worked-example.md)。

## 文件说明

```
SKILL.md                        skill 的完整规则
scan.py                         扫描器（仅依赖 Python 3）
references/lexicon.tsv          中英文候选词、替代词和误报备注
references/markers-zh.md        中文标记分类，共八类
references/markers-en.md        英文标记，来源为 HN 48905248
references/titles.md            标题规则：命名内容，不叙述阅读路径
references/nofluff.md           nofluff 的两个检查和补充规则
references/worked-example.md    完整审查示例：45 个问题，12/10/14 → 0/0/0
```

## 致谢与来源

两个快速检查和四条规则来自 [nofluff](https://nofluff.0x01.me/nofluff.txt) 写作标准。

英文标记列表参考 Hacker News 上整理 “claudish” 特征的讨论（[48905248](https://news.ycombinator.com/item?id=48905248)），引用和出处见 [`references/markers-en.md`](references/markers-en.md)。

词汇表包含四类来源：

- **测量结果。** Kobak、González-Márquez、Horvát 和 Lause 对 1400 万篇 PubMed 摘要的研究：[Science Advances 11(27), 2025](https://www.science.org/doi/10.1126/sciadv.adt3813)；以及 Juzek 与 Ward 的 [*Why Does ChatGPT “Delve” So Much?*](https://arxiv.org/abs/2412.11385)。
- **有引用的整理。** Wikipedia 的 [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)（WP:AIVOCAB）。
- **实践者整理。** [ninehills/public-skills](https://github.com/ninehills/public-skills)（MIT，经 [nmhjklnm/skills](https://github.com/nmhjklnm/skills)）。
- **实际审查。** 来自真实审查的新词条，会在备注列标明。

## License

MIT
