# Test for Exercise 9.3-3 (EN): Verifies Quicksort with SELECT pivot runs correctly.
# Test do Exercise 9.3-3 (PL): Sprawdza poprawność Quicksort z pivotem SELECT.

import pytest
from src.Chapter09.Exercise_9_3_3 import quicksort_with_select

def test_sorted_output():
    A = [3, 2, 9, 0, 7, 5, 4, 8, 6, 1]
    assert quicksort_with_select(A) == sorted(A)

def test_empty_array():
    assert quicksort_with_select([]) == []

def test_single_element():
    assert quicksort_with_select([42]) == [42]
