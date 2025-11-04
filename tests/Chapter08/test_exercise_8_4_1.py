import pytest 
from src.Chapter06.Exercise_8_4_1 import bucket_sort

def test_bucket_sort_basic():
    A = [0.79, 0.13, 0.16, 0.64, 0.39, 0.20, 0.89, 0.53, 0.71, 0.42]
    expected = sorted(A)
    assert bucket_sort(A) == pytest.approx(expected)
