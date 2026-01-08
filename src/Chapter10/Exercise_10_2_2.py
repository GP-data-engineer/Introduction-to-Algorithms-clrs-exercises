import pytest
from src.Chapter08.Exercise_10_2_2 import Stack

def test_stack_push_pop():
    s = Stack()
    s.push(10)
    s.push(20)
    assert s.pop() == 20
    assert s.pop() == 10
    assert s.is_empty()

def test_stack_empty_pop():
    s = Stack()
    with pytest.raises(IndexError):
        s.pop()
