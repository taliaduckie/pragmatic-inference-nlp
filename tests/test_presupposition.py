from src.presupposition import detect_presuppositions


def test_iterative_trigger_is_case_insensitive():
    assert detect_presuppositions(["Retry"]) == [
        {
            "trigger": "retry",
            "type": "iterative",
            "presupposition": "event occurred before",
        }
    ]


def test_trailing_determiner_does_not_create_trigger():
    assert detect_presuppositions(["the"]) == []
