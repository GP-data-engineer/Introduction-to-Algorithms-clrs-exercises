# Exercise 11.2-5 tests

import pytest
from src.Chapter11.Exercise_11_2_5 import pigeonhole_collision


def test_pigeonhole_true():
    assert pigeonhole_collision(101, 10, 10)


def test_pigeonhole_false():
    assert not pigeonhole_collision(50, 10, 10)
