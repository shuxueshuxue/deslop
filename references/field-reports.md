# Field reports

What people outside this repository say the register does to them, what they built against it, and
which parts of that changed the contract. Every claim below is attributed. Nothing here is measured
by us; the measured claims live in `evals/` and in the worked example.

## The source

Hacker News item 49388752, 2026-08-21, 275 points, about 230 comments, submitted on
`adnanakil/nobuzz`, a Claude Code skill (`/debuzz`) that pipes a reply through a second model.
Three sibling tools are named in the thread: `zachahn/vomit`, `gvzdv/claudish-to-english`,
`yn/claude-output-styles`. `references/markers-en.md` already cites the older thread 48905248.

**What this is as evidence.** A self-selected sample of people annoyed enough to post. It shows what
gets noticed and by whom. It does not show how often anything occurs, and no rate in this file was
counted by anyone. Two things it does establish well: which surface forms are recognisable to
strangers, and which mitigations people tried and abandoned.

## The counter-sample, read first

Four commenters argue against the whole enterprise, and one of them states this repository's main
risk better than `references/overcorrection.md` did:

- **colordrops** (49396578): "When I do stop yelling at Claude to be more concise and actually read
  what it wrote it's often valuable complexity and subtlety that I could use to better understand
  what it did and steer it, rather than Claude just papering over important details like it did
  before."
- **cortesoft** (49394350): "I find it slightly amusing when I even notice at all, normally I am so
  focused on the content of what I am working on that I don't really pay attention to the prose."
- **ed_mercer** (49396529): the register at least tells you "what meaning it's assigning to certain
  situations."
- **Exoristos** (49395718): "I appreciate Claude's comments during implementation, but they won't do
  to commit."

Read together they say the register is not uniformly waste: some of it is the writer's working state
made visible, and deleting it deletes the state. That is a claim about **where** to remove, not
whether. It is why the M family below removes at a boundary rather than at the source, and it
belongs in the over-correction pass.

## What changed here

| finding | where it landed |
|---|---|
| Comments that narrate the change instead of stating the state | `taxonomy.md` M1 |
| Text written for the reader who was in the room | `taxonomy.md` M2, `SKILL.md` §12 row 4 |
| Internal concerns leaked into user-visible strings | `taxonomy.md` M3, `SKILL.md` §2 `ui-copy` |
| Working notes shipped because nobody cleaned them at the boundary | `taxonomy.md` M4 |
| A comment ruleset that survived contact with a real repository | `references/code-comments.md` |
| Style instructions decay as a session grows | `SKILL.md` §11.1 |
| A word cap is a different instrument from level and scope | `SKILL.md` §3 |
| Hand the text to a second model instead | ruled on below |
| Run the tool's gates on the tool's own prose | `tools/selfcheck.py`, two demotions below |
| Phrases with a public citation | `references/lexicon.tsv`, source `hn-49388752` |

## Running the gates on this repository

**dwaltrip** (49395110), on another tool in the same family: "The readme is filled with slop. Bad
sign…" That is a test, it costs nothing to run, and this repository had never run it. `tools/selfcheck.py`
now does, over the 15 files that speak in deslop's own voice, and holds them to the rule §5.1 states
for everyone else: drive the gates to zero, or name every survivor in `references/selfcheck.tsv`.

The first run found two indicators whose hits here were almost all false, and both lost their GATED
place under §5.1's own standard:

- **The trailing contrastive tail** (`…, not a style call.`), a branch of the staged-reversal regex.
  Six hits, one real. The other five are ordinary contrastive predicates in two languages
  (`Narration describes the route, not the destination.`). The staged move the branch was added for
  is already caught by the `不是X而是Y`, `not just X but Y` and `isn't X, it's Y` branches. Now CAPPED.
- **The inline-title list item** (F4). Eleven hits, zero real. F4's own definition is "a bold label
  and a colon, **where the body then restates the label**", and the regex cannot see the second half,
  so it reports every glossary entry in the repository. Now CAPPED, where density still catches the
  page made entirely of label bullets.

A third pattern showed up and was **not** acted on. Of the 30 hit-level ledger rows, 17 say the same thing about
`、`: it separated items in one list, so it replaced a comma rather than a full stop, which is
exactly the test F1 states. The counter cannot see the difference. Demoting it on this evidence
would be wrong, because these files are marker inventories and inventories are list-heavy in a way
ordinary Chinese prose is not; the corpus that produced the reason is the least representative one
available. What would settle it is a count on Chinese prose that is not an inventory, separating
list-separator uses from clause-joining ones. Until then `、` stays GATED and the survivors stay named.

## The explanations offered, and why none of them is used

Seven mechanisms were proposed in the thread for why the register exists. None is verified, one was
rebutted in the thread itself, and this repository depends on none of them:

| claim | who |
|---|---|
| The output is a compressed thought trace, dense because tokens are scarce | YuriNiyazov (49390537) |
| A persona choice, so the model plays a character rather than answering | the_sleaze_ (49389639) |
| Longer output bills more | fmbb (49389859) |
| Reinforcement learning aimed at code, with prose as an unattended side effect | gste (49397001), janalsncm (49395067) |
| Social-media engagement text fed back into training | nrmitchi (49392343) |
| Human feedback from raters with a shared style | jayers (49389681), nozzlegear (49390192) |
| Watermarking | cryptonector (49393297); rebutted by IshKebab (49394818) and thorian1828i03 (49396231), who notes another model watermarks without the same symptoms |

The rewrite is the same under all seven. A rule that only makes sense once you accept a cause is a
rule with an unverified premise inside it, so the taxonomy states surface forms and the tests that
decide them, and leaves the cause alone.

One of the seven does converge with something this repository derived independently. `taxonomy.md`
F1 treats `——`, `、`, `：` and the em dash as one compression mechanism, with the test *did it
replace a full stop, or a line break?* YuriNiyazov's compressed-thought-trace account predicts
exactly that, from the other direction, and **3371** (49397048) states the same thing about the
model's channels: "the difference between 'thoughts' and 'words' is very weak." Two derivations
agreeing is a reason to keep the family, not evidence that either account is right.

## The route not taken: hand it to a second model

Four tools in the thread share one architecture. The original model's own rewrite reintroduces the
register, so the text goes to a different model whose only job is to say it plainly, and the result
is printed **verbatim**. nobuzz's README puts the argument in one sentence: letting the first model
"tidy up" the translation "reintroduces exactly the voice being removed."

They differ in where they sit:

- **nobuzz / `debuzz`**. A skill, invoked explicitly, with three audience modes (`colleague`,
  `manager`, `director`) and the second model reached through a CLI. Fails loudly: on error it shows
  the error, and offers the first model's rewrite only as a labelled fallback.
- **vomit**. A hook plus a side channel, local model, no network. Its README states the cost
  plainly: the rewriter sees only the text, not the actions or files, "so it hallucinates a bit."
- **claudish-to-english**. A display hook, and display-only: the transcript and the model's own
  reasoning keep the original, and only what is on screen changes. Every hook **fails open**, so a
  provider outage shows the original rather than eating it.
- **claude-output-styles**. No second model at all. Instead of forbidding the register it
  separates the channels: keep it in notes and memory, translate on the way out to a person.

**The ruling: deslop stays an in-place editor, and does not adopt the second-model route.** The
reason is the fidelity contract. §4's protected spans and the relations ledger exist because a free
rewrite loses which number modifies which object and which actor holds which goal, and a model that
cannot see the source material cannot preserve what it cannot check. vomit says this about itself.
**amumu** (49396731) adds a measurement in the same direction: across several local rewriters, the
best one was the one that "added bad behavior back in less than any others I tested". The editor
slops too, and the question is only by how much.

Two things from that family are adopted anyway, because they are about custody and not about who
writes:

1. **Display-only, original retained.** claudish-to-english's design is the strongest form of §3's
   `in-place` scope: the rewrite never destroys its input. `tools/freeze.py` already enforces the
   hash; the reading is that a pass which cannot show you the original is not `in-place`.
2. **Fail open, and say so.** When the pass cannot run, the original stands and the failure is
   visible. Never a silent substitution, which is also `SKILL.md` §4.1's rule for citations.

Where the second-model route is genuinely better: when there is no fidelity requirement at all.
Somebody wants a reply said plainly on screen, once, and the source is one paragraph up. deslop is
the wrong size of tool for that.

## Instruction decay, reported by seven people

The most repeated operational claim in the thread, and the one that bears on how a deslop pass is
run rather than what it contains:

- **vrosas** (49389574): as context grows the rules are forgotten; a ban in the global file, the
  local file **and** a hook, and some still get through.
- **ianjbutler** (49392471): with hooks enforcing them, comment rules are still violated "about 25%
  of the time."
- **troupo** (49390575): the verbose style returns immediately after compaction, and also
  immediately after re-reading the style instructions.
- **strbean / troupo** (49392307, 49393012): the post-compaction hook is the obvious fix and is
  reported not to hold.
- **nater5000** (49389776): the canary. Put one small unmistakable rule in the instructions, his
  being "start every sentence with my name". When the model stops obeying it, the session is too
  long to trust. A cheap staleness signal that needs no tooling.
- **boc** (49394950), **jen729w** (49395049): work under a fraction of the window and hand off to a
  fresh session rather than compacting.
- **adastra22** (49389920): compaction is worse than starting over; **enraged_camel** (49393493)
  disagrees from long orchestrator sessions, so this one is contested.

This repository has a matching observation from its own runs, and it is the strongest single reason
Pass B exists: on every editing round without exception, re-running the taxonomy over the
replacement text caught em dashes, `、` and mid-sentence `：` that the pass had just introduced while
removing others. The rule was in view. It was violated anyway, by the process enforcing it.

`SKILL.md` §11.1 states what to do about it.

## Word caps

**mmastrac** (49389501), the most-endorsed practical comment in the thread: "Comment blocks are
<= 7 words, function names <= 4 words. User-facing message strings should be <= 10 words. Use an
active voice, no stage performances, and pick the most common word when choosing among
alternatives." And: "Limiting the number of words is the strongest factor in cleaning up the output,
IMO." Others report the same shape at other sizes: **kanzure** (49390088) asks for one sentence or
ten words; **lubujackson** (49396108) caps a whole implementation at a line count.

Three of those are already here: active voice, no performance, and the plain-word preference as
E2's test. The cap is not, and it is a different kind of instrument. `SKILL.md` §3 records the ruling: a
cap set by the author is a legitimate third control, a cap the editor invents is the −39% failure
`references/provenance.md` documents.

## The register in the wild

Phrases below entered `references/lexicon.tsv` with source `hn-49388752`. Some are quoted as
specimens by people describing the register, some are parodies, and one is a real reply somebody
pasted. All are recognisable to strangers, which is the property the lexicon selects for.

- `load-bearing`, already present from thread 48905248, and the single most-repeated word here.
  Six different commenters use it as shorthand for the whole register.
- "Let me ground my answer so I'm not just guessing" · "The blast radius of this change is
  significant and requires careful surgery to get right" · "it cuts more deeply than you thought"
  (collingreen, 49389652, parody).
- "And honestly? That changes the game." (jasongill, 49394371, parody).
- "this isn't just necessary, it's mandatory. that's the difference." (zengid, 49389340), a parody
  of the negation-parallelism move already counted as B1.
- "That's a sharp insight, and it reveals something core to … that I otherwise wouldn't have
  considered" (FiddlyPack, 49396771, parody).
- "Say the word and I'll do the joinery" (gste, 49397018, quoting a real reply).
- "Still pending: … — your call on whether to start one now or deploy tonight's campaign to surface
  any wrinkles the spec drifted on" (jorl17, 49394209), a parody of the offer-closer.
- "the third one is the most instructive" · "here's the kicker", the two nobuzz's README is built
  around.

One entry is about the tool class rather than the register. **ziga** (49390469) asked the model to
write the anti-register rules, and the first line it produced was "Avoid the stock LLM register."
The instruction was itself written in the register it forbade. That is `tools/selfcheck.py`'s reason
for existing, stated as a joke by someone who was not building anything.
