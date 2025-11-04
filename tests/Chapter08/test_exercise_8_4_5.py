"""  
Testy do zadania 8.4.5 (PL): Sprawdzamy poprawność sortowania zmiennych losowych z jednostajnego rozkładu.

Tests for Exercise 8.4.5 (EN): Verifies correct sorting of random variables from uniform distribution.
"""

import pytest
from src.Chapter08.Exercise_8_4_5 import bucket_sort_uniform

def test_sorted_uniform_values():
    values = [0.3, 0.1, 0.9, 0.5]
    sorted_vals = bucket_sort_uniform(values)
    assert sorted_vals == sorted(values)

def test_preserves_all_values():
    values = [0.2, 0.4, 0.6, 0.8]
    sorted_vals = bucket_sort_uniform(values)
    assert set(sorted_vals) == set(values)
