# Test for Exercise 10.1-5 (EN): Verifies deque operations and structure.
# Test do Exercise 10.1-5 (PL): Sprawdza operacje deque i strukturę tablicy.

import pytest
from src.Chapter10.Exercise_10_1_5 import Deque

def test_deque_operations():
    d = Deque(4)
    d.push_back(1)
    d.push_front(2)
    d.push_back(3)
    assert d.pop_front() == 2
    assert d.pop_back() == 3
    assert d.pop_front() == 1
    with pytest.raises(IndexError):
        d.pop_back()
