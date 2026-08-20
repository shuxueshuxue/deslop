# Worked example

One full pass over a real academic draft: *The Graveyard Reopens*, a paper skeleton on why failed
software-engineering paradigms become viable under agent economics.

Read in this order.

| file | what it is |
|---|---|
| `00-input.md` | the frozen input. sha256 `021e54a9…2c2eb8`, from `spexcode-base` commit `f07c9ac`. The live file has moved since. |
| `01-before.json` / `.txt` | indicators before |
| `02-audit.md` | the frame, the protected spans, 52 findings, and **the Pass B and Pass D corrections at the end**, which are the most useful part |
| `apply.py` | the rewrite, as 50 explicit (old, new) pairs. Everything not listed stays byte-identical, so quotations, numbers, placeholders and table data cannot drift. |
| `03-output.md` | the result |
| `04-after.json` / `.txt` / `04-diff.md` | indicators after |
| `05-report.md` | the output contract: before/after table, every named survivor, missing-basis notes, caveats |

Headline: em dashes 38 to 0, staged reversals 7 to 1, editorial stance 7 to 2, with every survivor
named. Prose words 3462 to 3385, sentences 227 to 242. **More sentences and fewer words** is the
signature of decompression rather than deletion.

The rewrite is a proposal. The source file belongs to a live session that is still writing the paper,
so nothing was edited in place.

Reproduce:

```
python3 ../tools/measure.py 00-input.md  --scene academic --json > 01-before.json
python3 apply.py
python3 ../tools/measure.py 03-output.md --scene academic --json > 04-after.json
python3 ../tools/measure.py --diff 01-before.json 04-after.json
```
