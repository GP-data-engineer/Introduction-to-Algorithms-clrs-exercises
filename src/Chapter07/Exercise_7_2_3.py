# Exercise_7_2_3.py
# PL: Zadanie 7.2-3 - Pokaż, że Quicksort działa w Theta(n^2), gdy wszystkie elementy są różne i ustawione w kolejności malejącej.
# EN: Exercise 7.2-3 - Show Quicksort is Theta(n^2) when elements are distinct and in decreasing order.
#
# Implementation:
# - instrumented quicksort (Lomuto) counting comparisons; decreasing input triggers worst-case.

from typing import List, Tuple

def lomuto_partition(A: List[int], lo: int, hi: int, counters: dict) -> int:
    pivot = A[hi]
    i = lo - 1
    for j in range(lo, hi):
        counters['comparisons'] += 1
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
            counters['swaps'] += 1
    A[i+1], A[hi] = A[hi], A[i+1]
    counters['swaps'] += 1
    return i + 1

def quicksort_count(A: List[int]) -> Tuple[List[int], dict]:
    counters = {'comparisons': 0, 'swaps': 0}
    A_copy = list(A)
    def _qs(lo: int, hi: int):
        if lo < hi:
            q = lomuto_partition(A_copy, lo, hi, counters)
            _qs(lo, q - 1)
            _qs(q + 1, hi)
    _qs(0, len(A_copy) - 1)
    return A_copy, counters

if __name__ == "__main__":
    # Demo: decreasing array
    n = 30
    arr = list(range(n, 0, -1))
    _, counters = quicksort_count(arr)
    print(f"decreasing input n={n}, comparisons={counters['comparisons']}, swaps={counters['swaps']}")
    print("Expect quadratic number of comparisons for classical Lomuto quicksort on decreasing array.")
