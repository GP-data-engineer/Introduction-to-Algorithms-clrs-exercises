import pytest
from src.Chapter08.Exercise_10_3_2 import ObjectPool

def test_allocate_and_free():
    pool = ObjectPool(3)
    idx1 = pool.allocate_object(10)
    idx2 = pool.allocate_object(20)
    pool.free_object(idx1)
    idx3 = pool.allocate_object(30)
    assert idx3 == idx1
