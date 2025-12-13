# Test for Exercise 10.1-3 (EN): Verifies queue state after operations.
# Test do Exercise 10.1-3 (PL): Sprawdza stan kolejki po operacjach.

import pytest
from src.Chapter10.Exercise_10_1_3 import Queue

def test_queue_sequence():
    q = Queue(6)
    q.enqueue(4)
    q.enqueue(1)
    q.enqueue(3)
    q.dequeue()
    q.enqueue(8)
    q.dequeue()
    assert q.state().count(None) == 2
    assert q.state()[q.head] == 3
