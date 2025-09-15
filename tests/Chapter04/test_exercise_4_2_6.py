"""
Unit tests for Exercise 4.2-6 (compare direct vs block multiplication using Strassen).
"""

import pytest
from src.Chapter04.Exercise_4_2_6 import compare_direct_vs_block


def test_compare_direct_vs_block_true_case():
    # Parameters chosen so that block method is faster
    # For small k and large n, block method should be faster
    assert compare_direct_vs_block(2, 128, 1.0) is True


def test_compare_direct_vs_block_false_case():
    # Parameters chosen so that direct method is faster
    # For large k and small n, direct method should be faster
    assert compare_direct_vs_block(8, 2, 1.0) is False


def test_compare_direct_vs_block_equal_case():
    # Artificial case where times are equal
    # This happens when k^3 * n^(log2(7)) == (k*n)^(log2(7))
    from math import log2, isclose
    k = 4
    n = 4
    a = 1.0
    direct_time = a * ((k * n) ** (log2(7)))
    block_time = (k ** 3) * (a * (n ** (log2(7))))
    assert isclose(direct_time, block_time)
    # In this case, function should return False (not faster)
    assert compare_direct_vs_block(k, n, a) is False


def test_compare_direct_vs_block_type():
    # Ensure the function always returns a boolean
    result = compare_direct_vs_block(3, 8, 1.0)
    assert isinstance(result, bool)
