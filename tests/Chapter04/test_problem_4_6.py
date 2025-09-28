"""
Tests for Problem 4-6
We check Monge array properties and explanations.
"""

import pytest
from src.Chapter04.Problem_4_6 import (
    is_monge_matrix, part_a_explanation, part_b_example,
    part_c_explanation, part_d_explanation, part_e_explanation
)

def test_part_a_explanation():
    assert "Monge" in part_a_explanation()

def test_is_monge_matrix_true():
    matrix = [
        [1, 2, 3],
        [2, 3, 4],
        [3, 4, 5]
    ]
    assert is_monge_matrix(matrix) is True

def test_is_monge_matrix_false():
    matrix = [
        [10, 17, 13, 28, 23],
        [17, 22, 16, 29, 23],
        [24, 28, 22, 34, 24],
        [11, 13, 6, 17, 7]
    ]
    # This matrix is not Monge (one element breaks the rule)
    assert part_b_example(matrix) is False

def test_part_c_explanation():
    assert "non-decreasing" in part_c_explanation()

def test_part_d_explanation():
    assert "m+n" in part_d_explanation()

def test_part_e_explanation():
    assert "O(m + n log m)" in part_e_explanation()
