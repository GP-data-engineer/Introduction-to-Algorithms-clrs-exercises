#!/usr/bin/env python3
# Exercise_1_2_2.py
"""
Compare insertion sort and merge sort.
Calculate the maximum n for which insertion sort runs faster.
"""

from math import log2
from typing import List

def insertion_faster_range(limit: int = 1000) -> List[int]:
    """
    Returns a list of n values (2..limit) for which insertion sort
    is faster than merge sort based on the given step counts.
    """
    return [n for n in range(2, limit + 1) if 8 * n * n < 64 * n * log2(n)]

def max_n_for_insertion() -> int:
    """
    Finds the largest n for which insertion sort is faster than merge sort.
    """
    n = 2
    last = 0
    while 8 * n * n < 64 * n * log2(n):
        last = n
        n += 1
    return last

if __name__ == "__main__":
    last = max_n_for_insertion()
    print(f"Insertion sort is faster for n in range 2..{last}.")
    print("Sample values:", insertion_faster_range()[:10])
