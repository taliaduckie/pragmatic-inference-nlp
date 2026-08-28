from src.speech_acts import detect_indirect_speech_acts


def test_can_you_is_request():
    results = detect_indirect_speech_acts(["Can", "you", "pass", "the", "salt", "?"])
    assert len(results) == 1
    assert results[0]["indirect_force"] == "request"


def test_would_you_mind_matches_once():
    results = detect_indirect_speech_acts(
        ["Would", "you", "mind", "closing", "the", "window", "?"]
    )
    assert len(results) == 1
    assert results[0]["pattern"] == "Would you mind"


def test_why_dont_you_spacy_tokenization():
    results = detect_indirect_speech_acts(["Why", "do", "n't", "you", "try", "again", "?"])
    assert any(r["indirect_force"] == "suggestion" for r in results)


def test_declarative_modal_not_matched():
    results = detect_indirect_speech_acts(["You", "can", "swim", "well"])
    assert results == []
