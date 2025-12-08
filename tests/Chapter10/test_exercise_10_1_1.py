# Test for Exercise 10.1-1 (EN): Verifies stack state after operations.
# Test do Exercise 10.1-1 (PL): Sprawdza stan stosu po operacjach.

import pytest
from src.Chapter10.Exercise_10_1_1 import Stack

def test_stack_sequence():
    s = Stack(6)
    s.push(4)
    s.push(1)
    s.push(3)
    s.pop()
    s.push(8)
    s.pop()
    assert s.state()[:s.top+1] == [4, 1]
