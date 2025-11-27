# Test for Exercise 9.3-2 (EN): Verifies lower bound of ⌈n/4⌉ for SELECT partition.
# Test do Exercise 9.3-2 (PL): Sprawdza dolną granicę ⌈n/4⌉ dla podziału SELECT.

import pytest
from src.Chapter09.Exercise_9_3_2 import lower_bound_partition

def test_bound_for_large_n():
    assert lower_bound_partition(200) == 50

def test_none_for_small_n():
    assert lower_bound_partition(100) is None
