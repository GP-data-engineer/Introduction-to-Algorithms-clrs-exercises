import pytest
from src.Chapter06.Exercise_6_4_5 import heapsort_best_case

def test_heapsort_best_case():
    assert "Ω(n log n)" in heapsort_best_case()
