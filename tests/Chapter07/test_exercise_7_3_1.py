from src.Chapter07.Exercise_7_3_1 import explanation

def test_explanation_contains_key_points():
    text = explanation().lower()
    assert "oczekiwany" in text
    assert "pesymistyczny" in text
    assert "n log n" in text
    assert "n²" in text or "n^2" in text
