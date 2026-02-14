# Exercise 11.2-1 tests

import pytest
from src.Chapter11.Exercise_11_2_1 import expected_collisions


def test_expected_collisions_basic():
    assert expected_collisions(2, 1) == 1.0


def test_expected_collisions_zero():
    assert expected_collisions(1, 10) == 0.0


def test_expected_collisions_general():
    assert expected_collisions(4, 2) == 3.0
