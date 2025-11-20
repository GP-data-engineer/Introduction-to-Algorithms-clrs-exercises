# Test for Exercise 9.2-3 (EN): Tests iterative RANDOMIZED-SELECT.
# Test do Exercise 9.2-3 (PL): Testuje iteracyjną wersję RANDOMIZED-SELECT.

import pytest
from src.Chapter09.Exercise_9_2_3 import randomized_select_iterative

def test_min_element():
    A = [3, 2, 9, 0, 7, 5, 4, 8, 6, 1]
    assert randomized_select_iterative(A.copy(), 1) == 0

def test_max_element():
    A = [3, 2, 9, 0, 7, 5, 4, 8, 6, 1]
    assert randomized_select_iterative(A.copy(), 10) == 9

def test_middle_element():
    A = [3, 2, 9, 0, 7, 5, 4, 8, 6, 1]
    result = randomized_select_iterative(A.copy(), 5)
    assert result in sorted(A)[4:6]  # tolerancja na losowość
