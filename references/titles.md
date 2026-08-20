# Headings

Headings are the most-read and most easily wrecked part of a document. Slide decks make it obvious:
the audience reads the heading, then decides whether to listen to the body.

## 1. Name the content, do not narrate the reading path

Narration describes the route, not the destination. Anything containing 上一页 / 接下来 / 先看 /
下面讲 / 我们来看 / 具体来说 / 落到 X 上, or *Next up* / *Let's look at* / *Moving on to*, is narration.

| narration | naming |
|---|---|
| 上一页那个「项目级」，拆开是三层 | 项目级 harness 的三层架构 |
| SpexCode：先看一个 spec 节点 | 一个 spec 节点 |
| 落到工程上，我关心三件事 | 工程上的三个问题 |

Narration also carries a hidden cost: **it makes the heading depend on order.** Read out of sequence,
screenshotted alone, or quoted by someone else, it breaks.

## 2. A heading must stand alone

Anything with 那个 / 这一层 / 上面说的 / *the above* / *this one* stops working the moment it leaves
its context. Use the thing's own name.

## 3. A noun phrase needs an object and an action

Piled nouns with no action leave the reader unsure what the section does.

| empty | concrete |
|---|---|
| 该由项目持有的那层状态 | 编排软件本身的生命周期 |
| 关于测量的一些考虑 | 怎么测一个场景 |

Do not force a verb in the other direction either. The verb has to match what the section actually does.

## 4. No posturing words in a heading

Headings are short, so a rare word is magnified. See `taxonomy.md` E2.

| posturing | common |
|---|---|
| drift 判据 | drift 检查的判别方法 |
| 意图承载体的选型 | 意图写在哪 |

**But do not over-correct.** `drift 判据` → `drift 检查怎么判` falls into speech: in a heading, a
colloquial question is more jarring than a rare word, and it is a different form from the noun-phrase
headings around it (rule 7). Headings sit further toward written register than the body.

## 5. Deliver what the heading promised

If the heading says "orchestration lifecycle" and the body discusses where state is stored, the
reader feels the drift. Change the heading or connect them. Do not leave it.

## 6. Do not let the heading state the body's conclusion

If the heading concludes and the body concludes again, the same thing was said twice. The heading
gives the object; the body gives the conclusion.

## 7. One syntactic form per level

Within a document, same-level headings are all noun phrases or all short sentences, never mixed.
Mixing signals to the reader that some sections outrank others.

## Two heading-level tells from the taxonomy

- **"Challenges and Future Prospects"** and its Chinese equivalents are a formulaic section, not a
  heading choice (`taxonomy.md` B8). A real section with real content under it is fine.
- **A mid-prose colon is sometimes a heading the document declined to write** (`taxonomy.md` F1).
  When decompressing punctuation, watch for the sections that were hiding behind a `：`.

## Self-check

Read the heading, then ask three questions:

1. Does it tell me what this section is about, rather than where it sits in the document?
2. Pulled out on its own, does it still stand?
3. After reading the body, did the heading deliver what it promised?
