import pytest 
from src.Chapter07.Exercise_7_2_2 import quicksort_equal_elements

def test_quicksort_equal_elements():
    assert "Θ(n^2)" in quicksort_equal_elements()
