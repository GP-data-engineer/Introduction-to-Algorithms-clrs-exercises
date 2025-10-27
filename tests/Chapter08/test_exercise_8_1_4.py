# corrected test_exercise_8_1_4.py with import math
import pytest
import math
from src.Chapter06 import Exercise_8_1_4 as ex

def test_lower_bound_basic():
    n, k = 100, 5
    lb = ex.lower_bound_n_lgk(n, k)
    approx = n * math.log2(k)
    assert lb > 0
    assert lb > 0.5 * approx

def test_n_not_divisible_raises():
    with pytest.raises(ValueError):
        ex.lower_bound_n_lgk(100, 3)
