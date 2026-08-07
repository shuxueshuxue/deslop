#!/usr/bin/env python3
"""Score deslop's lexical and context-dependent evaluation cases.

    python3 evals/run.py
    python3 evals/run.py --predictions path/to/model-output.json

The lexical score runs scan.py. The judgment score requires a model or human
prediction file because the scanner deliberately cannot decide use versus
mention, quotation, audience, or terms of art.
"""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import scan  # noqa: E402

CASES = Path(__file__).with_name("cases.json")


def signature(finding):
    return finding["span"], finding["category"]


def load_cases(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema") != 1 or not isinstance(data.get("cases"), list):
        raise ValueError(f"{path}: expected schema 1 with a cases list")
    ids = set()
    for case in data["cases"]:
        required = {"id", "tier", "source", "input", "findings", "reason"}
        missing = required - case.keys()
        if missing:
            raise ValueError(f"{case.get('id', '<unknown>')}: missing {sorted(missing)}")
        if case["tier"] not in {"lexicon", "judgment"}:
            raise ValueError(f"{case['id']}: invalid tier {case['tier']!r}")
        if case["id"] in ids:
            raise ValueError(f"duplicate id: {case['id']}")
        ids.add(case["id"])
        for finding in case["findings"]:
            if not isinstance(finding.get("span"), str) or not isinstance(finding.get("category"), str):
                raise ValueError(f"{case['id']}: each finding needs span and category")
    return data["cases"]


def scanner_findings(case, lexicon):
    hits = scan.scan(case["input"], lexicon, set())
    findings = []
    for (_, _, category, _, _), occurrences in hits.items():
        findings.extend({"span": matched, "category": category} for _, matched, _ in occurrences)
    return findings


def score(cases, predicted_by_id):
    expected = set()
    predicted = set()
    for case in cases:
        expected.update((case["id"], *signature(f)) for f in case["findings"])
        predicted.update((case["id"], *signature(f)) for f in predicted_by_id.get(case["id"], []))
    true_positive = len(expected & predicted)
    false_positive = len(predicted - expected)
    false_negative = len(expected - predicted)
    precision = true_positive / (true_positive + false_positive) if true_positive + false_positive else 1.0
    recall = true_positive / (true_positive + false_negative) if true_positive + false_negative else 1.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return true_positive, false_positive, false_negative, precision, recall, f1


def print_score(label, cases, predicted_by_id):
    tp, fp, fn, precision, recall, f1 = score(cases, predicted_by_id)
    clean = sum(not case["findings"] for case in cases)
    print(f"{label}: {len(cases)} cases, {sum(len(c['findings']) for c in cases)} expected findings, {clean} clean cases")
    print(f"  TP {tp}  FP {fp}  FN {fn}  precision {precision:.1%}  recall {recall:.1%}  F1 {f1:.1%}")


def load_predictions(path, known_ids):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if data.get("schema") != 1 or not isinstance(data.get("predictions"), list):
        raise ValueError(f"{path}: expected {{\"schema\": 1, \"predictions\": [...]}}")
    results = {}
    for row in data["predictions"]:
        case_id = row.get("id")
        if case_id not in known_ids:
            raise ValueError(f"{path}: unknown case id {case_id!r}")
        if case_id in results:
            raise ValueError(f"{path}: duplicate prediction for {case_id}")
        findings = row.get("findings")
        if not isinstance(findings, list):
            raise ValueError(f"{path}: {case_id} needs a findings list")
        results[case_id] = findings
    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cases", type=Path, default=CASES)
    parser.add_argument("--predictions", type=Path,
                        help="JSON predictions for judgment-tier cases")
    args = parser.parse_args()

    cases = load_cases(args.cases)
    lexicon = scan.load_lexicon(scan.LEXICON)
    lexical = [case for case in cases if case["tier"] == "lexicon"]
    judgment = [case for case in cases if case["tier"] == "judgment"]

    print_score("lexicon", lexical, {case["id"]: scanner_findings(case, lexicon) for case in lexical})
    print_score("scanner on judgment tier (diagnostic, not a model)", judgment,
                {case["id"]: scanner_findings(case, lexicon) for case in judgment})

    if args.predictions:
        predictions = load_predictions(args.predictions, {case["id"] for case in judgment})
        missing = [case["id"] for case in judgment if case["id"] not in predictions]
        if missing:
            raise ValueError(f"{args.predictions}: missing {len(missing)} judgment cases")
        print_score("model judgment", judgment, predictions)
    else:
        print("model judgment: not scored; pass --predictions with one decision per judgment case")


if __name__ == "__main__":
    main()
