import pytest
from src.Chapter03.Exercise_3_2_2 import log_product

def test_log_product_identity():
    val1, val2 = log_product(4, 8, 2)
    assert pytest.approx(val1, 0.0001) == val2
