import pytest
from src.Chapter12.Exercise_12_2_4 import bunyan_counterexample

def test_contains_counterexample():
    text = bunyan_counterexample()
    assert "Kontrprzykład" in text
