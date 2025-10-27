# test_exercise_8_1_4.py
import pytest
from src.Chapter06 import Exercise_8_1_4 as ex

def test_lower_bound_basic():
    n, k = 100, 5
    lb = ex.lower_bound_n_lgk(n, k)
    # Expect lb to be comparable to n*log2(k)
    approx = n * (math.log2(k) if hasattr(__import__('math'),'log2') else (__import__('math').log(k,2)))
    assert lb > 0
    assert lb > 0.5 * approx  # constant factor: lb is Theta(n log k), so > 0.5 n log k for these params

def test_n_not_divisible_raises():
    with pytest.raises(ValueError):
        ex.lower_bound_n_lgk(100, 3)  # 100 not divisible by 3
