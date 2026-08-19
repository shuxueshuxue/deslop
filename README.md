<div align="center">

# deslop

**检查并改写技术文档里的模型腔。**

这是一个供 [Claude Code](https://claude.ai/code) 使用的中英文写作检查 skill。

中文（默认） | [English](./README.en.md)

</div>

---

LLM 写过的文字会反复出现某些句式和用词。`deslop` 按照标记分类检查文档，逐行列出问题和替换方案。修改后再测量一次，前后的指标可以直接比较。

## 判断标准

`deslop` 删除没有增加信息的修辞，并把没有必要的生僻词换成常用词。平实而谨慎的原句可以保留。

## 修改的默认规则

默认重写每句话。确认原句语气合适时才保留。模型文字的问题常分布在全文，局部替换无法统一语气。

可以修改全文，但修改后的语气应保持平实。删去冗余时不得减少信息。

## 句子去留

1. **删掉这句话，信息有没有减少？** 没有就删除。
2. **读者问「具体是什么意思」时，能不能用事实回答？** 不能就继续改写。

本仓库对这两条规则的说明见 [`references/nofluff.md`](references/nofluff.md)。分类表用于定位问题，两条检查用于决定句子去留。

## 检查项目

| 类型 | 示例 |
|---|---|
| **动作类比** | `接住每个事件` → `为每个事件创建一条记录` |
| **拟人** | `状态活不过一次调用` → `调用结束即失效` |
| **对偶反转** | `不是 X，是 Y` → 直接陈述结论 |
| **顿号和冒号** | 顿号连接本应成列的内容，句中冒号引出本应独立成句的说明 |
| **第二人称翻译腔** | 中文技术文档里密集出现的「你」 |
| **戏剧性收尾** | 段尾短句重复前文，没有提供新信息 |
| **作者自评** | `Naur 说得对` → `与 Naur 的结论一致` |
| **破折号** | 统计数量和出现位置，检查是否用来代替完整句子 |
| **词语重复** | 同一个比喻词在全文反复出现 |
| **不必要的生僻词** | `判据` → `判定规则` |
| **圈内黑话** | `抓手` → `办法` |

## 安装

```sh
git clone https://github.com/shuxueshuxue/deslop.git ~/.claude/skills/deslop
```

然后在 Claude Code 中使用：

```
/deslop  README
/deslop  slides/talk.html，面向中文会议听众
```

也可以直接说「这段文字有 AI 味，帮我改掉」。Skill 的描述会匹配这类请求。

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

`references/lexicon.tsv` 中的每个词条都带有普通替代词。扫描器只报告候选，不会自动改写。有些词在特定上下文中可以保留，词条备注会说明原因。

顿号连接三项以上内容时，应改为列表。冒号后的说明可以独立成立时，应拆成新句或小节。

脚本只能检查词汇和固定句式。以下问题仍需人工审查：

- 戏剧性收尾
- 重复段意
- 删除后不损失信息的类比
- 只描述阅读路径的标题

## 工作流程

1. **提取正文。** 排除 Markdown 和 HTML 标记。
2. **运行扫描器。** 得到候选词以及四项标点和句式计数。
3. **逐行审查。** 由未参与改写的 subagent 审查，避免沿用改写时的判断。
4. **统计指标。** 记录扫描器输出的四项计数。拟人用法由人工记录。
5. **应用修改。** 按照字面含义改写，不要用新的动作类比替换旧的动作类比。
6. **重新测量。** 报告修改前后的指标，例如 `reversals 12 → 0`。主观感受不能代替计数。

## 范围

**检查表达方式。** 检查结果说明文字是否符合本项目的写作规则，不评价作者的观点。

**保留术语。** 普通词不能准确表达时保留原术语，例如 *spec drift*。常见例子还包括 *anchor* 和 *garbage collection*。*back-pressure* 同样保留。

**不改变论点。** 工具只重写表达论点的句子。重排章节和删除段落需要作者确认。

**不核对事实。** 文字改得平实之后，仍可能存在悬空指代或前后矛盾，引用内容也可能不准确。审查示例见 [`references/worked-example.md`](references/worked-example.md)。

## 文件说明

```
SKILL.md                        skill 的完整规则
scan.py                         扫描器（仅依赖 Python 3）
references/lexicon.tsv          中英文候选词及其替代词和误报备注
references/markers-zh.md        中文标记分类，共八类
references/markers-en.md        英文标记，来源为 HN 48905248
references/titles.md            标题规则，要求标题直接命名内容
references/nofluff.md           nofluff 的两个检查和补充规则
references/worked-example.md    含 45 项问题和修改前后指标的审查示例
```

## 致谢

本项目由 [linux.do](https://linux.do/) 社区推广。

## 资料来源

两个快速检查和四条规则来自 [nofluff](https://nofluff.0x01.me/nofluff.txt) 写作标准。

英文标记列表参考 Hacker News 上整理「claudish」特征的讨论（[48905248](https://news.ycombinator.com/item?id=48905248)）。引用和出处见 [`references/markers-en.md`](references/markers-en.md)。

词汇表包含四类来源：

- **测量结果。** Kobak 等分析了 1400 万篇 PubMed 摘要，论文发表于 [Science Advances 11(27), 2025](https://www.science.org/doi/10.1126/sciadv.adt3813)。另一项来源是 Juzek 与 Ward 的 [*Why Does ChatGPT "Delve" So Much?*](https://arxiv.org/abs/2412.11385)。
- **有引用的整理。** Wikipedia 的 [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)（WP:AIVOCAB）。
- **实践者整理。** [ninehills/public-skills](https://github.com/ninehills/public-skills)（MIT，经 [nmhjklnm/skills](https://github.com/nmhjklnm/skills)）。
- **审查新增。** 审查中新增的词条会在备注列注明来源。

## 许可

MIT
