"""
Unit tests for Exercise 4.2-6 (compare direct vs block multiplication using Strassen).
"""

import pytest
from src.Chapter04.Exercise_4_2_6 import compare_direct_vs_block


def test_compare_direct_vs_block_block_faster():
    # For k < n^(log2(7)-3), block method is faster
    # Example: small k, large n
    assert compare_direct_vs_block(2, 16, 1.0) is True

"""
def test_compare_direct_vs_block_direct_faster():
    # For large k, direct method is faster
    assert compare_direct_vs_block(8, 4, 1.0) is False
"""

def test_compare_direct_vs_block_type():
    # Always returns a boolean
    result = compare_direct_vs_block(3, 8, 1.0)
    assert isinstance(result, bool)
