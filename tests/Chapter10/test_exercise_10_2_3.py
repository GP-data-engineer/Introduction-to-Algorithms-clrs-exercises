import pytest
from src.Chapter10.Exercise_10_2_3 import Queue

def test_queue_enqueue_dequeue():
    q = Queue()
    q.enqueue(5)
    q.enqueue(10)
    assert q.dequeue() == 5
    assert q.dequeue() == 10
    assert q.is_empty()

def test_queue_empty_dequeue():
    q = Queue()
    with pytest.raises(IndexError):
        q.dequeue()
