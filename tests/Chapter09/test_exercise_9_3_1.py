# Test for Exercise 9.3-1 (EN): Verifies partition size estimation for SELECT with group sizes.
# Test do Exercise 9.3-1 (PL): Sprawdza szacowanie rozmiaru podziału dla SELECT z różnymi grupami.

import pytest
from src.Chapter09.Exercise_9_3_1 import select_group_size_analysis

def test_group_7_partition():
    result = select_group_size_analysis(140, 7)
    assert result["guaranteed_partition_size"] >= 140 - 10  # median_of_medians ≈ 10

def test_group_3_partition():
    result = select_group_size_analysis(140, 3)
    assert result["guaranteed_partition_size"] < 140 - 20  # median_of_medians ≈ 23
