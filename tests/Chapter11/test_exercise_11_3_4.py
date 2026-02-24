import pytest
from src.Chapter11.Exercise_11_3_4 import multiplication_hash


def test_positions():
    m = 1000
    results = [multiplication_hash(k, m) for k in [61,62,63,64,65]]
    assert len(results) == 5
    assert all(0 <= r < m for r in results)