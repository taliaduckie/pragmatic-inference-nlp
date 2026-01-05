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
python src/analyze.py --text "She managed to finish the paper."
```

## Example output
```
Input: "She managed to finish the paper."
Presupposition trigger: 'managed' (factive implicative — implies prior difficulty)
Scalar implicature: none detected
Indirect speech act: none detected
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
    └── test_scalar.py
```
