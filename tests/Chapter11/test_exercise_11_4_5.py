import pytest
from src.Chapter11.Exercise_11_4_5 import good_alpha

def test_good_alpha():
    alphas = good_alpha()
    assert all(a < 0.5 for a in alphas)
