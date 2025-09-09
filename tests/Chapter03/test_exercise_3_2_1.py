import pytest
from src.Chapter03.Exercise_3_2_1 import is_monotonic_increasing, sum_of_functions, product_of_functions

def test_sum_and_product_monotonic():
    f = lambda n: n
    g = lambda n: n**2
    n_values = list(range(1, 10))
    assert is_monotonic_increasing(sum_of_functions(f, g, n_values))
    assert is_monotonic_increasing(product_of_functions(f, g, n_values))
