import pytest
from src.Chapter06.Exercise_6_4_3 import heapsort_time_sorted

def test_heapsort_time_sorted():
    assert "Θ(n log n)" in heapsort_time_sorted()
