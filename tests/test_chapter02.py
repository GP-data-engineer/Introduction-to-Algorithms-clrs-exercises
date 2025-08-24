import pytest
from src.Chapter02.Exercise_2.2-2 import merge_sort_no_sentinels  # type: ignore # noqa: E402,F401

def test_merge_sort_no_sentinels_basic():
    assert merge_sort_no_sentinels([3, 1, 2]) == [1, 2, 3]

def test_merge_sort_no_sentinels_empty():
    assert merge_sort_no_sentinels([]) == []

def test_merge_sort_no_sentinels_duplicates():
    assert merge_sort_no_sentinels([2, 2, 1]) == [1, 2, 2]
