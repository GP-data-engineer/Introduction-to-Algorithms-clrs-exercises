"""
Unit tests for Exercise 4.2-1 (Strassen's 2x2 multiplication).
"""

import pytest
from src.Chapter04.Exercise_4_2_1 import strassen_2x2


def test_strassen_2x2_given_problem():
    # Given matrices from the exercise prompt
    A = [[13, 5], [75, 42]]
    B = [[8, 4], [7, 6]]
    expected = [[139, 82], [894, 552]]
    assert strassen_2x2(A, B) == expected


def test_strassen_2x2_identity_left():
    # Multiplication by identity (left) should return the same matrix
    I = [[1, 0], [0, 1]]
    A = [[2, -3], [4, 5]]
    assert strassen_2x2(I, A) == A


def test_strassen_2x2_identity_right():
    # Multiplication by identity (right) should return the same matrix
    I = [[1, 0], [0, 1]]
    A = [[7, 8], [9, 10]]
    assert strassen_2x2(A, I) == A
