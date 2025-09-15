"""
Unit tests for Exercise 4.2-3 (Strassen's algorithm with padding for non-power-of-2 sizes).
"""

import pytest
from src.Chapter04.Exercise_4_2_3 import strassen_with_padding


def test_strassen_with_padding_3x3():
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    expected = [
        [30, 24, 18],
        [84, 69, 54],
        [138, 114, 90]
    ]
    assert strassen_with_padding(A, B) == expected


def test_strassen_with_padding_identity():
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    I = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    assert strassen_with_padding(A, I) == A


def test_power_of_two_matrix_no_padding():
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    expected = [[19, 22], [43, 50]]
    assert strassen_with_padding(A, B) == expected


def test_invalid_dimensions():
    A = [[1, 2], [3, 4]]
    B = [[1, 2, 3], [4, 5, 6]]
    with pytest.raises(ValueError):
        strassen_with_padding(A, B)
