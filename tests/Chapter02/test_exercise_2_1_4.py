import pytest
from src.Chapter02.Exercise_2_1_4 import add_binary_integers

def test_add_binary_no_carry():
    A = [0, 1, 0, 1]  # 5
    B = [0, 0, 1, 1]  # 3
    assert add_binary_integers(A, B) == [0, 1, 0, 0, 0]  # 8

def test_add_binary_with_carry():
    A = [1, 1, 1, 1]  # 15
    B = [0, 0, 0, 1]  # 1
    assert add_binary_integers(A, B) == [1, 0, 0, 0, 0]  # 16

def test_add_binary_different_bits():
    A = [1, 0, 1, 0]  # 10
    B = [1, 1, 0, 1]  # 13
    assert add_binary_integers(A, B) == [1, 0, 1, 1, 1]  # 23
