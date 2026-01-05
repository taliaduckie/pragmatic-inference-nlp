from src.scalar import detect_scalar_implicatures

def test_some_implicates_not_all():
    results = detect_scalar_implicatures(["Some", "students", "passed"])
    assert any(r["term"] == "some" for r in results)

def test_all_no_implicature():
    results = detect_scalar_implicatures(["All", "students", "passed"])
    assert not any(r["term"] == "all" for r in results)

def test_possible_scale():
    results = detect_scalar_implicatures(["It", "is", "possible"])
    assert any(r["scale_type"] == "epistemic" for r in results)
