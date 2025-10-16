# Exercise_7_2_4.py
# PL: Zadanie 7.2-4 - Banki i sortowanie prawie posortowanych danych: uzasadnij, że Insertion-Sort lepiej niż Quicksort nadaje się do rozwiązania tego problemu.
# EN: Exercise 7.2-4 - Banks record transactions nearly sorted: show Insertion Sort is better than Quicksort for nearly-sorted data.
#
# Implementation:
# - insertion_sort_count: counts shifts/comparisons.
# - quicksort_count (Lomuto) reused from other exercises (local minimal copy).
# - generator for nearly-sorted arrays: start sorted then perform k random swaps.
# - comparison function compares counts for both algorithms.

from typing import List, Tuple
import random

def insertion_sort_count(A: List[int]) -> Tuple[List[int], dict]:
    A_copy = list(A)
    n = len(A_copy)
    counters = {'comparisons': 0, 'shifts': 0}
    for j in range(1, n):
        key = A_copy[j]
        i = j - 1
        # compare at least once in while test
        while i >= 0:
            counters['comparisons'] += 1
            if A_copy[i] > key:
                A_copy[i+1] = A_copy[i]
                counters['shifts'] += 1
                i -= 1
            else:
                break
        A_copy[i+1] = key
    return A_copy, counters

# Minimal Lomuto quicksort for comparison
def lomuto_partition(A: List[int], lo: int, hi: int, counters: dict) -> int:
    pivot = A[hi]
    i = lo - 1
    for j in range(lo, hi):
        counters['comparisons'] += 1
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
            counters['swaps'] = counters.get('swaps', 0) + 1
    A[i+1], A[hi] = A[hi], A[i+1]
    counters['swaps'] = counters.get('swaps', 0) + 1
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

def generate_nearly_sorted(n: int, k_swaps: int) -> List[int]:
    arr = list(range(n))
    # perform k random swaps to make it nearly sorted
    for _ in range(k_swaps):
        i = random.randrange(n)
        j = random.randrange(n)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

if __name__ == "__main__":
    import statistics
    random.seed(0)
    n = 200
    k = 5  # small number of swaps -> nearly-sorted
    arr = generate_nearly_sorted(n, k)
    _, ins_c = insertion_sort_count(arr)
    _, qs_c = quicksort_count(arr)
    print(f"n={n}, k_swaps={k}, insertion comparisons={ins_c['comparisons']}, shifts={ins_c['shifts']}")
    print(f"n={n}, quicksort comparisons={qs_c['comparisons']}, swaps={qs_c['swaps']}")
    print("Insertion sort should cost ~ O(n + #inversions) - small for nearly-sorted data.")
