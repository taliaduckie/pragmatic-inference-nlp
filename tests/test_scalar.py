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

def test_some_implicature_content():
    results = detect_scalar_implicatures(["Some", "students", "passed"])
    some = next(r for r in results if r["term"] == "some")
    assert some["implicature"] == "Not 'all'"
    assert some["stronger_terms"] == ["all", "most", "many"]

def test_negative_scalars_not_flagged():
    results = detect_scalar_implicatures(["Few", "students", "ever", "fail"])
    assert results == []
