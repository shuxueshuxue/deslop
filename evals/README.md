# Evaluation set

`cases.json` is the source of truth. Every case contains its input, expected
findings, provenance, and a reason. An empty `findings` list means the text
must not be reported or rewritten.

Two tiers prevent the scanner from claiming a judgment it cannot make:

- `lexicon`: exact, context-independent candidate forms. `run.py` calls
  `scan.py` and reports precision, recall, and F1.
- `judgment`: quotation versus use, audience, terms of art, and Chinese
  register. A reviewer or model must read the sentence. The runner scores an
  independent prediction file against the same metrics.

Run the lexical baseline and the scanner-overreach diagnostic:

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
      "findings": []
    },
    {
      "id": "en-model-jargon-use",
      "findings": [
        {"span": "seamless", "category": "puffery"},
        {"span": "journey", "category": "puffery"}
      ]
    }
  ]
}
```

```sh
python3 evals/run.py --predictions review.json
```

The scanner-on-judgment number is deliberately labeled diagnostic. It measures
how badly a lexical matcher overreaches when asked to decide sentence meaning;
it is not a substitute for model evaluation.
