# test_exercise_8_3_3.py 
import pytest
from src.Chapter08 import Exercise_8_3_3 as ex

def test_proof_text_contains_stability_keyword():
    txt = ex.proof_text().lower()
    assert "stable" in txt or "stabil" in txt  # English or Polish mention

def test_verify_random_examples_runs():
    assert ex.verify_random_examples(trials=30) is True

def test_verify_stability_dependency_example():
    # verify that unstable variant can change the result compared to stable variant
    assert ex.verify_stability_dependency_example() is True
