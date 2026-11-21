# Pragmatic Inference NLP Tool

A Python toolkit for detecting and classifying pragmatic inference phenomena
in natural language: scalar implicature, indirect speech acts, and
presupposition triggers.

Grounded in Gricean maxims and neo-Gricean theory (Horn, Levinson).
Designed as a research-grade annotation aid, not a black-box classifier.

## What it detects
- **Scalar implicature** — "some" → not all, "possible" → not certain
- **Indirect speech acts** — "Can you pass the salt?" as a request, not a question
- **Presupposition triggers** — factive verbs, definite descriptions, iteratives

## Setup
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python src/analyze.py --text "Some students will retry."
```

## Example output
```
Input: "Some students will retry."
Scalar implicatures:
  · 'some' [quantifier] → implicates Not 'all'

Presupposition triggers:
  · 'retry' (iterative) → presupposes event occurred before
Indirect speech acts: none detected
```

## Project Structure
```
pragmatic-inference-nlp/
├── src/
│   ├── scalar.py         # scalar implicature detection
│   ├── speech_acts.py    # indirect speech act classification
│   ├── presupposition.py # presupposition trigger identification
│   └── analyze.py        # unified CLI entry point
├── data/
│   └── scalar_scales.json
└── tests/
    ├── test_scalar.py
    ├── test_speech_acts.py
    └── test_presupposition.py
```

## Testing

This is a rule-based prototype. Record the spaCy version and
`en_core_web_sm` model version alongside any reported output (both are shown
by `python -m spacy info`). The offline rule tests do not require a spaCy model:
`python -m pip install -r requirements-dev.txt && python -m pytest -q`.
