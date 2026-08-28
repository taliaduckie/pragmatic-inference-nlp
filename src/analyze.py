"""
analyze.py
Unified CLI for pragmatic inference analysis.

Usage:
    python analyze.py --text "She managed to finish the paper."
"""

import argparse
import spacy
from scalar import detect_scalar_implicatures
from presupposition import detect_presuppositions
from speech_acts import detect_indirect_speech_acts

nlp = spacy.load("en_core_web_sm")


def analyze(text: str):
    doc = nlp(text)
    tokens = [tok.text for tok in doc]

    print(f"\nInput: {text!r}\n")

    scalars = detect_scalar_implicatures(tokens)
    if scalars:
        print("Scalar implicatures:")
        for s in scalars:
            print(f"  · '{s['term']}' [{s['scale_type']}] → implicates {s['implicature']}")
    else:
        print("Scalar implicatures: none detected")

    presups = detect_presuppositions(tokens)
    if presups:
        print("\nPresupposition triggers:")
        for p in presups:
            print(f"  · '{p['trigger']}' ({p['type']}) → presupposes {p['presupposition']}")
    else:
        print("\nPresupposition triggers: none detected")

    speech_acts = detect_indirect_speech_acts(tokens)
    if speech_acts:
        print("\nIndirect speech acts:")
        for a in speech_acts:
            print(f"  · '{a['pattern']}' — literally {a['literal_force']}, "
                  f"conventionally a {a['indirect_force']}")
    else:
        print("\nIndirect speech acts: none detected")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", required=True)
    args = parser.parse_args()
    analyze(args.text)
