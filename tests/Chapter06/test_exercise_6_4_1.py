import pytest 
from src.Chapter06.Exercise_6_4_1 import heapsort

def test_heapsort_basic():
    arr = [5, 13, 2, 25, 7, 17, 20, 8, 4]
    assert heapsort(arr.copy()) == sorted(arr)

def test_heapsort_empty():
    assert heapsort([]) == []

def test_heapsort_single():
    assert heapsort([10]) == [10]
