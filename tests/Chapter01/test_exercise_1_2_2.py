#!/usr/bin/env python3
# test_exercise_1_2_2.py
"""
Tests for Exercise_1_2_2.py
"""

import pytest
from math import log2
import Chapter01.Exercise_1_2_2 as ex

def test_insertion_faster_range_small():
    result = ex.insertion_faster_range(20)
    # All values should be within the given range
    assert all(2 <= n <= 20 for n in result)
    # All values should satisfy the condition for insertion sort being faster
    assert all(8 * n * n < 64 * n * log2(n) for n in result)

def test_max_n_for_insertion():
    max_n = ex.max_n_for_insertion()
    assert isinstance(max_n, int)
    assert max_n > 0
    # For max_n the condition should hold
    assert 8 * max_n * max_n < 64 * max_n * log2(max_n)
    # For max_n + 1 the condition should fail
    assert not (8 * (max_n + 1) ** 2 < 64 * (max_n + 1) * log2(max_n + 1))
