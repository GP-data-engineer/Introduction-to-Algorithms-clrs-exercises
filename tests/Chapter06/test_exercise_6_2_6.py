import pytest
from src.Chapter06.Exercise_6_2_6 import max_heapify_complexity

def test_max_heapify_complexity():
    assert "Ω(log n)" in max_heapify_complexity()
