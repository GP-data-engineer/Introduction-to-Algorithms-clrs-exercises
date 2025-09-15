"""
Unit tests for Exercise 4.2-5 (Strassen's time complexity verification).
"""

import pytest
from src.Chapter04.Exercise_4_2_5 import time_for_2n, verify_strassen_time


def test_time_for_2n():
    result = time_for_2n(100, 4, 2)
    assert result == 7 * 100 + 2 * (4 ** 2)


def test_verify_strassen_time():
    from math import log2
    a = 1
    n = 4
    expected = a * ((2 * n) ** (log2(7)))
    assert verify_strassen_time(a, n) == expected
