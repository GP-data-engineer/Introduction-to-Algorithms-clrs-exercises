# Test for Exercise 10.1-7 (EN): Verifies stack behavior using two queues.
# Test do Exercise 10.1-7 (PL): Sprawdza zachowanie stosu za pomocą dwóch kolejek.

import pytest
from src.Chapter10.Exercise_10_1_7 import StackViaQueues

def test_stack_push_pop():
    s = StackViaQueues()
    s.push(10)
    s.push(20)
    s.push(30)
    assert s.pop() == 30
    s.push(40)
    assert s.pop() == 40
    assert s.pop() == 20
    assert s.pop() == 10
    with pytest.raises(IndexError):
        s.pop()

def test_stack_top():
    s = StackViaQueues()
    s.push(5)
    s.push(6)
    assert s.top() == 6
    s.pop()
    assert s.top() == 5
