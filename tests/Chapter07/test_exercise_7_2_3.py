import pytest
from src.Chapter07.Exercise_7_2_3 import quicksort_sorted_input

def test_quicksort_sorted_input():
    assert "Θ(n^2)" in quicksort_sorted_input()
