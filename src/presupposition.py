"""
presupposition.py
Identify presupposition triggers in text.

Trigger classes implemented:
- Factive verbs (know, realize, regret, manage)
- Implicative verbs (manage, forget, bother)
- Iteratives (again, return, restore)
- Definite descriptions (the + NP)
"""

FACTIVE_VERBS = {"know", "realize", "regret", "discover", "notice", "forget"}
IMPLICATIVE_VERBS = {"manage", "bother", "remember", "dare"}
ITERATIVES = {"again", "return", "restore", "resume", "retry"}


def detect_presuppositions(tokens: list[str]) -> list[dict]:
    results = []
    tokens_lower = [t.lower() for t in tokens]

    for tok in tokens_lower:
        if tok in FACTIVE_VERBS:
            results.append({"trigger": tok, "type": "factive", "presupposition": "complement clause is true"})
        if tok in IMPLICATIVE_VERBS:
            results.append({"trigger": tok, "type": "implicative", "presupposition": "attempt was made"})
        if tok in ITERATIVES:
            results.append({"trigger": tok, "type": "iterative", "presupposition": "event occurred before"})

    for i, tok in enumerate(tokens_lower[:-1]):
        if tok == "the":
            results.append({"trigger": f"the {tokens[i+1]}", "type": "definite_description",
                            "presupposition": f"a unique referent for '{tokens[i+1]}' exists"})

    return results
