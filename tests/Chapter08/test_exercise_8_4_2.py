import pytest 
from src.Chapter08.Exercise_8_4_2 import bucket_sort_with_merge

def test_bucket_sort_merge():
    A = [0.99, 0.98, 0.97, 0.96, 0.95, 0.94]
    expected = sorted(A)
    assert bucket_sort_with_merge(A) == pytest.approx(expected)
