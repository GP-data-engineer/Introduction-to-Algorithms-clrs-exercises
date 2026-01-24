import pytest
from src.Chapter08.Exercise_10_3_2 import MemoryManager

def test_allocate_and_free():
    mm = MemoryManager(3)
    i1 = mm.allocate_object()
    i2 = mm.allocate_object()
    mm.free_object(i1)
    i3 = mm.allocate_object()
    assert i3 == i1
