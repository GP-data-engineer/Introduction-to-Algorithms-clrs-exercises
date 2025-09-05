import pytest
from src.Chapter03.Exercise_3_1_3 import explain_statement_meaning

def test_explanation_contains_big_o():
    explanation = explain_statement_meaning()
    assert "Big-O" in explanation

def test_explanation_contains_big_omega():
    explanation = explain_statement_meaning()
    assert "Big-Omega" in explanation

def test_explanation_not_empty():
    explanation = explain_statement_meaning()
    assert isinstance(explanation, str)
    assert len(explanation) > 20
