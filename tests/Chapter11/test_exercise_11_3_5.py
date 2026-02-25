import pytest
from src.Chapter11.Exercise_11_3_5 import epsilon_lower_bound


def test_lower_bound():
    assert epsilon_lower_bound(100, 10) == 1/10 - 1/100