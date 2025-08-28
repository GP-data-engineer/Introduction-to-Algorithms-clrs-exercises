import pytest
from src.Chapter02.Exercise_2_2_4 import improve_best_case

def test_improve_best_case():
    suggestion = improve_best_case("linear search")
    assert "early termination" in suggestion.lower()
    assert "best-case" not in suggestion.lower()  # description is generic
