# English markers

The test for any sentence: is it **stating** something, or **performing** it?

Much of this list is catalogued by readers rather than by tooling. The clearest public inventory is the
Hacker News thread on "claudish" ([item 48905248](https://news.ycombinator.com/item?id=48905248)),
where commenters name specific words and sentence shapes. Quotes below are from that thread.

## 1. Fixed vocabulary

> "load bearing, key insight, push back, 'it's not x, it's y'" — user `user3939382`

> Terms like "load-bearing" (meaning structurally essential), "synthesize," "key insight," and
> "genuine" appear repetitively across generated content. — user `lendal`

Also frequent: *delve, leverage, robust, seamless, crucial, nuanced, testament to, at its core,
fundamentally, it's worth noting, that said, the reality is*.

| performing | stating |
|---|---|
| This is the load-bearing constraint. | Removing this constraint breaks X. |
| The key insight is that specs go stale. | Specs go stale. |
| a genuine improvement | 12% fewer false blocks |

## 2. The reversal

> "It's not x, not y, it's z" phrasing persists as reliable identifier — user `kokanee`

Count them. One is a good line. Five is a template.

| performing | stating |
|---|---|
| It's not a documentation problem, it's a feedback problem. | Documentation does not fail here; the missing piece is feedback. |
| Not faster — cheaper. | The cost drops; the latency does not change. |

## 3. Compulsive hedging and self-assessment

Claude models reach for **"honest"** constantly: *honest assessment, honest caveat, the honest
answer, to be honest* (user `lendal`). Same family: *frankly, candidly, I'll be direct, my take is*.

Adjacent tic, parodied in-thread by user `rydtsc`: opening with **"You're absolutely right to
question me"**, then **"But it's not a load-bearing issue"**, then **"my honest take is…"**.

Cut the frame. Say the thing.

## 4. Em dashes

> Em dashes get overused—LLMs favor them excessively in lists and clarifications — user `sheept`

Count them. Then check *where* they land: if most fall at the end of paragraphs, that is a template,
not a voice.

## 5. Latching

> "LLMs seem to get _tragically_ stuck on certain patterns… it will literally just latch onto words
> and repeat them incessantly" — user `jchw`

Count the frequency of any vivid word across the document. Three or more uses of the same metaphor
means replace all but one.

## 6. Personification

Abstract subjects performing human or biological actions: *history reminds you, the test never lies,
state lives on, the cache is warm, the pipeline is healthy, the spec knows*.

Some of these are established terms of art (*warm cache*, *healthy*). See the false-positive rule.

## 7. Elevated diction

A rarer, more "professional"-sounding word where a common one exists. Models reach for the word that
sounds learned; readers hear someone posturing.

| posturing | plain |
|---|---|
| utilize | use |
| leverage | use |
| facilitate | help · let |
| commence | start |
| in order to | to |
| a multitude of | many |
| it is imperative that | X must |

Adjacent habits worth the same pass: **nominalization** (`perform a validation` → `validate`) and
**stacked qualifiers** (`in certain specific circumstances` → `sometimes`).

This does not apply to terms of art. See the last section.

## 8. Dramatized closers

A short assertion parked at the end of a paragraph to leave an aftertaste.

> And nobody noticed.
> That is the whole trick.
> The tests were green.

Delete it and check whether any information was lost. Usually none was.

## 9. Rhythm

Beyond individual words: LLM prose keeps a **uniform cadence**. Every paragraph concedes, then turns,
then lands a summary assertion. Every section is a triad. Reviewers notice the metronome before they
notice any single word. By the third paragraph they can predict the shape of the next one.

Fixing this means varying paragraph length and structure, not swapping words.

## Why it matters beyond taste

> "It just feels lazy. It triggers my 'If you couldn't be bothered to write it, why do you expect me
> to spend my time reading it' allergy" — user `ClikeX`

The cost is not aesthetic. Readers who recognize the register discount the content.

## Do not flatten terms of art

*Drift*, *anchor*, *warm*, *starvation*, *garbage collection*, *back-pressure* are names, not
metaphors, when the field uses them as names. Flattening them makes the text read as though the
author does not know the field, which is worse than leaving a tell.
