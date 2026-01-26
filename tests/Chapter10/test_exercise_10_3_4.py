import pytest
from src.Chapter10.Exercise_10_3_4 import CompactAllocator

def test_compact_allocate_free():
    a = CompactAllocator(2)
    i1 = a.allocate(1)
    i2 = a.allocate(2)
    a.free(i1)
    i3 = a.allocate(3)
    assert i3 == i1
