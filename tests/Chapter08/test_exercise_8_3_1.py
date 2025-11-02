# test_exercise_8_3_1.py
import pytest
from src.Chapter06 import Exercise_8_3_1 as ex

def test_radix_sort_strings_example():
    words = ["COW","DOG","SEA","RUG","ROW","MOB","BOX","TAB","BAR","EAR","TAR","DIG","BIG","TEA","NOW","FOX"]
    alphabet = ''.join(sorted({ch for w in words for ch in w}))
    sorted_words, snaps = ex.radix_sort_strings_lsd(words, alphabet)
    # result should be lexicographic by characters (since all same length)
    assert sorted_words == sorted(words)
    # number of snapshots equals word length (3)
    assert len(snaps) == 3
    # snapshots should show progressive sorting by positions
    # last snapshot should equal final output
    assert snaps[-1][1] == sorted_words
