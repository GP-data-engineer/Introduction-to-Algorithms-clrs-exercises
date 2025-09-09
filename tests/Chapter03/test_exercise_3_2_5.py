import pytest
from Exercise_3_2_5 import log_factorial

def test_log_factorial_growth():
    for n in range(2, 20):
        log_fact, nlogn = log_factorial(n)
        assert 0.5 * nlogn <= log_fact <= 2 * nlogn
