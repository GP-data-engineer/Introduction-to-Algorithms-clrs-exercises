import pytest
from Exercise_3_2_3 import factorial_greater_than_power_of_two

def test_factorial_vs_power_of_two():
    for n in range(1, 10):
        assert factorial_greater_than_power_of_two(n)
