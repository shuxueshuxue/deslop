# Evaluation set

`cases.json` is the source of truth. Every case contains its input, provenance,
and a reason. It records two different expectations:

- `candidate_findings`: what the word-list scanner must report. A candidate is
  not an edit instruction.
- `judgments`: the review result for the candidate: `keep` or `rewrite`.

For backward-compatible compact cases, `findings` means both a candidate and a
`rewrite` judgment. Cases that need a distinct contract set both explicit
fields.

The two layers prevent the scanner from claiming a judgment it cannot make:

- Candidate detection: `run.py` calls `scan.py` and scores whether expected
  candidate forms were reported. Terms of art and quoted examples stay here.
- Judgment: a reviewer or model reads the sentence and labels each candidate
  `keep` or `rewrite`. This covers quotation versus use, audience, terms of
  art, and Chinese register.

`tier: lexicon` contains direct word-list fixtures. `tier: judgment` contains
the context-sensitive fixtures used for the candidate-only and model metrics;
both tiers still contribute to candidate detection.

Candidate precision/recall measures lexical coverage only. Do not use it as a
claim that all reported text should be changed; the judgment score measures
that separate editorial decision.

Run candidate detection and the candidate-only rewrite diagnostic:

```sh
python3 evals/run.py
```

To score a model or human review, provide all judgment case IDs:

```json
{
  "schema": 1,
  "predictions": [
    {
      "id": "en-quote-lexicon-example",
      "judgments": [
        {"span": "load-bearing", "category": "jargon", "verdict": "keep"},
        {"span": "key insight", "category": "jargon", "verdict": "keep"}
      ]
    },
    {
      "id": "en-model-jargon-use",
      "judgments": [
        {"span": "seamless", "category": "puffery", "verdict": "rewrite"},
        {"span": "journey", "category": "puffery", "verdict": "rewrite"}
      ]
    }
  ]
}
```

The JSON above is an excerpt; a scored file must contain every reviewed case
ID.

```sh
python3 evals/run.py --predictions review.json
```

The candidate-only rewrite number is deliberately labeled diagnostic. It
measures how badly a lexical matcher overreaches when every candidate is treated
as an edit; it is not a substitute for model evaluation.
