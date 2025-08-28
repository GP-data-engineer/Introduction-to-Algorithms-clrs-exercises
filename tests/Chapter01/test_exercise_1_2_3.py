#!/usr/bin/env python3
# test_exercise_1_2_3.py
"""
Tests for Exercise_1_2_3.py
"""

import Chapter01.Exercise_1_2_3 as ex

def test_smallest_n_condition():
    n = ex.smallest_n()
    assert 100 * n * n < (1 << n)
    assert 100 * (n - 1) * (n - 1) >= (1 << (n - 1))
