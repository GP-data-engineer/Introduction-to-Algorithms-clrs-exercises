import pytest 
from src.Chapter06.Exercise_6_4_2 import heapsort_correctness

def test_heapsort_correctness():
    assert "loop invariant" in heapsort_correctness()
