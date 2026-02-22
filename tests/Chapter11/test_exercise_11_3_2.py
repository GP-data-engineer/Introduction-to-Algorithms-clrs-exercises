import pytest
from src.Chapter11.Exercise_11_3_2 import modular_hash_string


def test_small_string():
    assert modular_hash_string("a", 100) == ord("a") % 100


def test_consistency():
    s = "hello"
    m = 1000
    assert modular_hash_string(s, m) == modular_hash_string(s, m)
