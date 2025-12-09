# Test for Exercise 10.1-2 (EN): Verifies dual stack operations.
# Test do Exercise 10.1-2 (PL): Sprawdza operacje dwóch stosów w jednej tablicy.

import pytest
from src.Chapter10.Exercise_10_1_2 import DualStack

def test_dual_stack_push_pop():
    ds = DualStack(6)
    ds.push1(1)
    ds.push2(9)
    ds.push1(2)
    ds.push2(8)
    assert ds.pop1() == 2
    assert ds.pop2() == 8
