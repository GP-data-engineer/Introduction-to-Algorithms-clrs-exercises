import pytest
from src.Chapter11.Exercise_11_3_6 import polynomial_hash


def test_polynomial_hash_basic():
    assert polynomial_hash([1,2,3], 5, 13) == (
        (1*1 + 2*5 + 3*25) % 13
    )


def test_mod_property():
    assert polynomial_hash([0,0,0], 7, 17) == 0