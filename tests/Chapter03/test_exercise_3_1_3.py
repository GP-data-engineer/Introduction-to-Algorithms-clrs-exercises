import pytest
from src.Chapter03.Exercise_3_1_3 import explain_statement_meaning

def test_explanation_contains_big_o():
    """
    Checks that the explanation mentions Big-O notation.
    This ensures the function addresses the concept of upper bound.
    """
    explanation = explain_statement_meaning()
    assert "Big-O" in explanation

def test_explanation_contains_big_omega():
    """
    Checks that the explanation mentions Big-Omega notation.
    This ensures the function addresses the concept of lower bound.
    """
    explanation = explain_statement_meaning()
    assert "Big-Omega" in explanation

def test_explanation_not_empty():
    """
    Ensures the explanation is a non-empty string with sufficient length.
    """
    explanation = explain_statement_meaning()
    assert isinstance(explanation, str)
    assert len(explanation) > 20
