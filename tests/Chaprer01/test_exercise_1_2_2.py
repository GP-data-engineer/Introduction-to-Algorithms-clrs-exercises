#!/usr/bin/env python3
# test_exercise_1_2_2.py
"""
Tests for Exercise_1_2_2.py
"""

import Exercise_1_2_2 as ex

def test_insertion_faster_range_small():
    result = ex.insertion_faster_range(20)
    assert all(2 <= n <= 20 for n in result)
    assert all(8 * n * n < 64 * n * ex.log2(n) for n in result)

def test_max_n_for_insertion():
    assert isinstance(ex.max_n_for_insertion(), int)
    assert ex.max_n_for_insertion() > 0
