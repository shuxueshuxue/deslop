# Comments, and the reader who was not in the room

The `code-context` scene was one table row until the largest cluster in thread 49388752 turned out
to be about comments. This file is that scene's detail. `references/field-reports.md` has the
sources; the marker forms are `taxonomy.md` M1 to M4.

## What deslop is and is not doing here

deslop edits text. It is not a comment policy, and it does not decide whether a file should have
comments. In `code-context` the default scope is `in-place`: strip the register from a comment,
keep what it says the code does, and report anything in the M family as a finding for the author.
Deleting a comment changes what the file tells the next reader, so it is a `structural` action and
needs the author's word, exactly like deleting a sentence from a document.

The one case where deslop deletes without asking is register with no content underneath: a comment
that only grades the code (`this elegant solution`, `the critical piece here`) says nothing that
survives its own removal.

## The survival test

One question decides most comments. **easyascake** (49394683) names the failure and **nrmitchi**
(49392261) writes the test:

> would this still be true and useful to someone reading this file a year from now, who never saw
> the diff?

A comment that only makes sense beside the diff is a changelog entry in the wrong file. It is also
a third copy of text that already exists in the commit body and the pull request. easyascake states
what replaces it: "It doesn't matter why funcA was added then later refactored to funcB. That much
can be ascertained from git history. What does matter is why approach A doesn't work, but B does."

## The rules

Adapted from nrmitchi's published set, which was itself written by a model and then kept because it
held. Their numbering is preserved so the source stays checkable.

- **CC-1.** No comment describing a change, a fix, a defect, its cause, or what the code used to do.
  No `was` / `now` / `previously` / `instead of`, no `this fixes`, no `needed because otherwise`, no
  `note that we no longer`.
- **CC-2.** Apply the survival test above before writing the comment, not after.
- **CC-3.** Default to zero. Declarative configuration describes itself: a resource named
  `dmarc-example-com` does not need a comment saying it is the DMARC record.
- **CC-4.** Comment when a future editor would break something without it: an external constraint
  that is not visible here, a required manual step, an invariant the surrounding code cannot show.
  One line. A paragraph belongs in a document.
- **CC-5.** Before committing, re-read the comment lines you added.
  `git diff --cached | grep '^+' | grep -E '#|//|/\*'` lists them. Each one has to pass CC-2 on its
  own, and deleting is always an acceptable outcome. nrmitchi's closing clause is the part that does
  the work: *"I already wrote it", "it is only one line", and "this one is genuinely useful" are not
  exemptions, and the last one is the exact thought that precedes every violation.*
- **CC-6.** The rules cover comments you edit as well as ones you add. When a change invalidates a
  comment, the default action is to delete it rather than rewrite it into a narrative.

**Where deslop departs.** CC-3's "default to zero" is a house style, and deslop does not import
house styles: `references/overcorrection.md` treats deleting a comment that carries a real external
constraint as a false positive, whatever the default says. CC-1 and CC-2 are different, and they
transfer whole, because they are about whether the text addresses the reader who will actually
arrive.

## The boundary, which is where the defect actually is

Two people in the thread make the same distinction and it changes what gets removed:

- **cerved** (49394869): the model writes these as notes while working, which is fine in itself; the
  problem is that they are never cleaned up before the commit.
- **Exoristos** (49395718): "I appreciate Claude's comments during implementation, but they won't do
  to commit." They keep some by moving them into a decisions document.

So the failure is not that the notes exist. It is that nothing removes them at the point where the
audience changes. That has three consequences for a deslop pass:

1. Run at the boundary, not during the work. A `code-context` pass over a branch about to merge is
   worth more than one over a working tree.
2. Prefer relocation to deletion. A comment that fails the survival test but records a real
   decision goes into the commit body or a decisions file. The relations record in `SKILL.md` §4 is
   where that move gets recorded, so nothing quietly disappears.
3. Report the count of comments moved separately from the count deleted. They are different
   outcomes for the author.

## Text the user reads

The same defect, further from the room and with more readers. **jorl17** (49393580) describes it
exactly:

> Claude loves to write up tooltips and other labels that leak everything to the end user. Every
> single concern we have, every edge case we've meticulously made our code handle, it passes on to
> the user, so they don't "need to worry". But no sane user would think of these things.

The rule that follows: a label says what the control does. It does not enumerate what was handled,
warn about a case the product already handles, or explain a state the user cannot reach. **mmastrac**
(49389501) puts a number on it that is worth borrowing as a default, not as a gate: user-facing
message strings under about ten words.

This is the `ui-copy` scene in `SKILL.md` §2. It is the one scene where the usual deslop finding is
not a phrase to replace but a sentence to remove entirely, because the sentence exists to relieve an
anxiety the reader does not have.

## Specimens

Real and parodied, from the thread. Each one is an M-family hit and none contains a marker word, so
no lexicon entry would find them:

```
// No retry was added here per AC 37b in FEATURE.MD          (pluralmonad, 49392264)   M2
// PLAN-5.1.A.d.42 load bearing reassertion                  (klardotsh, 49396760)     M2
// The lesson from the Parse-dont-fail-era campaign          (jorl17, 49393612)        M2
// Judged on merit from computed properties during the cursor saga                     M2
// Chop 6ms due to lenience and lax-constraints vs 18ms baseline April perf            M1
```

The last one is instructive: every fact in it is specific, and it is still unreadable to anyone who
was not in that session. Specificity is not the test. The reader is.
