
# Test for Exercise 9.3.8 (EN): Verifies k-quantile computation.
# Test do Exercise 9.3.8 (PL): Sprawdza wyznaczanie k-kwantyli.

import pytest
from src.Chapter09.Exercise_9_3_8 import compute_k_quantiles

def test_quantiles():
    A = [3, 2, 9, 0, 7, 5, 4, 8, 6, 1]
    result = compute_k_quantiles(A, 4)
    assert result == [2, 5, 7]