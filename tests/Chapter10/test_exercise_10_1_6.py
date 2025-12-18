# Test for Exercise 10.1-6 (EN): Verifies queue behavior using two stacks.
# Test do Exercise 10.1-6 (PL): Sprawdza zachowanie kolejki za pomocą dwóch stosów.

import pytest
from src.Chapter10.Exercise_10_1_6 import QueueViaStacks

def test_queue_via_stacks():
    q = QueueViaStacks()
    q.enqueue(10)
    q.enqueue(20)
    assert q.dequeue() == 10
    q.enqueue(30)
    assert q.dequeue() == 20
    assert q.dequeue() == 30
    with pytest.raises(IndexError):
        q.dequeue()
