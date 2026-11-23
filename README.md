# Pragmatic Inference NLP Tool

A small, rule-based Python prototype for exploring pragmatic inference. It
flags candidate readings from token patterns rather than deciding what a speaker
meant in context.

- **Scalar terms**: look up alternatives on a fixed scale. For example,
  `some` can suggest `not all`, but that inference can be canceled.
- **Indirect requests and suggestions**: match conventional forms such as
  `could you` and `why don't you`. The same words can also occur in a literal
  question.
- **Presupposition triggers**: flag lexical patterns such as `retry` and simple
  definite descriptions. A flag is a prompt to inspect the sentence, not a
  judgment that the presupposition holds.

The rules take a single utterance, without its preceding discourse. Use the
output as a starting point for hand annotation, not as validated labels.

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

Record the spaCy version and
`en_core_web_sm` model version alongside any reported output (both are shown
by `python -m spacy info`). The offline rule tests do not require a spaCy model:
`python -m pip install -r requirements-dev.txt && python -m pytest -q`.
