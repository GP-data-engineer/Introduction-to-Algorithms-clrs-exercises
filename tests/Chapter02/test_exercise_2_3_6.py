import random
import pytest
from src.Chapter02.Exercise_2_3_6 import binary_insertion_sort

def test_empty_list():
    data = []
    assert binary_insertion_sort(data) == []

def test_single_element():
    data = [42]
    assert binary_insertion_sort(data) == [42]

def test_sorted_list():
    data = [1, 2, 3, 4, 5]
    assert binary_insertion_sort(data.copy()) == sorted(data)

def test_reverse_sorted_list():
    data = [5, 4, 3, 2, 1]
    assert binary_insertion_sort(data.copy()) == sorted(data)

def test_with_duplicates():
    data = [3, 1, 2, 3, 2, 1, 3]
    assert binary_insertion_sort(data.copy()) == sorted(data)

def test_random_lists():
    rng = random.Random(0)
    for _ in range(20):
        data = [rng.randint(-50, 50) for _ in range(15)]
        assert binary_insertion_sort(data.copy()) == sorted(data)

def test_stability():
    # Pary (klucz, identyfikator)
    pairs = [(2, "a"), (1, "x"), (2, "b"), (1, "y"), (2, "c")]
    sorted_pairs = binary_insertion_sort(pairs.copy(), key=lambda p: p[0])
    # Klucze posortowane rosnąco
    assert [k for k, _ in sorted_pairs] == [1, 1, 2, 2, 2]
    # Kolejność elementów o tym samym kluczu zachowana
    assert [tag for _, tag in sorted_pairs] == ["x", "y", "a", "b", "c"]
