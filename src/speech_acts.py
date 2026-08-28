"""
speech_acts.py
Classify indirect speech acts via conventionalized surface forms.

An indirect speech act (Searle 1975) performs one illocutionary act by way
of another: "Can you pass the salt?" is literally a question about ability
but conventionally functions as a request. Detection here targets
conventionalized forms only — non-conventional indirection ("It's cold in
here" as a request to close the window) requires discourse context beyond
the sentence and is out of scope.

Note on tokenization: patterns include both spaCy-style contraction splits
("do", "n't") and unsplit forms ("don't") so the detector works on either.
"""

# (token sequence, literal illocutionary force, conventional indirect force)
PATTERNS = [
    (("would", "you", "mind"), "question about hearer's objection", "request"),
    (("why", "do", "n't", "you"), "negative why-question", "suggestion"),
    (("why", "don't", "you"), "negative why-question", "suggestion"),
    (("i", "was", "wondering", "if"), "report of speaker's mental state", "request"),
    (("i", "need", "you", "to"), "assertion of speaker's need", "request"),
    (("you", "might", "want", "to"), "assertion about hearer's preferences", "suggestion"),
    (("can", "you"), "question about hearer's ability", "request"),
    (("could", "you"), "question about hearer's ability", "request"),
    (("would", "you"), "question about hearer's willingness", "request"),
    (("will", "you"), "question about hearer's future action", "request"),
]


def detect_indirect_speech_acts(tokens: list[str]) -> list[dict]:
    """
    Given a list of tokens, return detected indirect speech acts.
    Each result has: {pattern, literal_force, indirect_force}.

    Longer patterns are matched first and consume their tokens, so
    "would you mind" does not also fire the bare "would you" rule.
    """
    tokens_lower = [t.lower() for t in tokens]
    consumed: set[int] = set()
    matches = []

    for pattern, literal, indirect in sorted(PATTERNS, key=lambda p: -len(p[0])):
        n = len(pattern)
        for i in range(len(tokens_lower) - n + 1):
            span = range(i, i + n)
            if tuple(tokens_lower[i:i + n]) == pattern and not any(j in consumed for j in span):
                consumed.update(span)
                matches.append((i, {
                    "pattern": " ".join(tokens[i:i + n]).replace(" n't", "n't"),
                    "literal_force": literal,
                    "indirect_force": indirect,
                }))

    return [m for _, m in sorted(matches, key=lambda m: m[0])]
