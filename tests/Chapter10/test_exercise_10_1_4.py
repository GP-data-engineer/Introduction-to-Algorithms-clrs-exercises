# Test for Exercise 10.1-4 (EN): Verifies overflow and underflow detection in queue.
# Test do Exercise 10.1-4 (PL): Sprawdza wykrywanie przepełnienia i niedomiaru w kolejce.

import pytest
from src.Chapter10.Exercise_10_1_4 import SafeQueue

def test_overflow():
    q = SafeQueue(2)
    q.enqueue(1)
    q.enqueue(2)
    with pytest.raises(OverflowError):
        q.enqueue(3)

def test_underflow():
    q = SafeQueue(2)
    with pytest.raises(IndexError):
        q.dequeue()

def test_normal_behavior():
    q = SafeQueue(3)
    q.enqueue(5)
    q.enqueue(6)
    assert q.dequeue() == 5
    assert q.dequeue() == 6
