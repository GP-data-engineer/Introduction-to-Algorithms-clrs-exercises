import pytest
from src.Chapter06.Exercise_6_4_4 import heapsort_worst_case

def test_heapsort_worst_case():
    assert "Ω(n log n)" in heapsort_worst_case()
