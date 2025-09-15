"""
Unit tests for Exercise 4.2-2 (Strassen's algorithm for n x n matrices).
"""

import pytest
from src.Chapter04.Exercise_4_2_2 import strassen


def test_strassen_2x2():
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    expected = [[19, 22], [43, 50]]
    assert strassen(A, B) == expected


def test_strassen_identity():
    A = [[2, 3], [4, 5]]
    I = [[1, 0], [0, 1]]
    assert strassen(A, I) == A
