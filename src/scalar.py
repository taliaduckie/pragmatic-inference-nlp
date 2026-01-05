"""
scalar.py
Detect scalar implicatures using lexical scales.

A scalar implicature arises when a weaker scalar term (e.g. 'some') is used
where a stronger one (e.g. 'all') would also have been true — conversationally
implicating that the stronger term does NOT hold.
"""

import json
from pathlib import Path

SCALES_PATH = Path(__file__).parent.parent / "data" / "scalar_scales.json"

def load_scales():
    with open(SCALES_PATH) as f:
        return json.load(f)

def detect_scalar_implicatures(tokens: list[str]) -> list[dict]:
    """
    Given a list of tokens, return detected scalar implicatures.
    Each result has: {term, scale_type, stronger_terms, implicature}.
    """
    scales = load_scales()
    results = []
    tokens_lower = [t.lower() for t in tokens]

    for scale_type, scale in scales.items():
        for i, term in enumerate(scale[:-1]):  # skip strongest
            if term in tokens_lower:
                stronger = scale[:i]
                results.append({
                    "term": term,
                    "scale_type": scale_type,
                    "stronger_terms": stronger,
                    "implicature": f"Not {stronger[0]!r}" if stronger else None,
                })
    return results
