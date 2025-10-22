# Exercise_7_4_5.py
# PL: Zadanie 7.4-5 - Hybrydowy algorytm: quicksort + insertion for subarrays of size < k.
#     Pokaż, że oczekiwany czas działania to O(n k + n log(n/k)).
# EN: Exercise 7.4-5 - Hybrid algorithm: quicksort but stop recursing for subarrays of size < k,
#     then finish with insertion sort. Show expected time O(n k + n log(n/k)).
#
# Implementation:
# - simulate expected comparisons cost: model quicksort cost down to size k (treat partitions randomized and balanced in expectation)
# - compute cost formula: cost_quicksort_levels ≈ c * n * log2(n/k)
# - insertion pass cost ≈ O(n*k) (each of n elements moved at most k positions in worst case of that approach)
# - provide function hybrid_cost_estimate(n,k) giving O(...) estimate and a simple simulation that runs randomized quicksort but stops at k then insertion sort.

import random
import math
from typing import List, Tuple

def hybrid_cost_estimate(n: int, k: int, c_quick: float = 1.0, c_insert: float = 1.0) -> float:
    """
    Return estimated cost ~ c_quick * n * log2(n/k) + c_insert * n * k
    as the theoretical bound O(n k + n log(n/k)).
    """
    if k <= 0:
        raise ValueError("k must be >= 1")
    if n <= k:
        return c_insert * n * n  # insertion sort cost ~ n^2 if full
    return c_quick * n * math.log2(max(2, n // k)) + c_insert * n * k

# Implement hybrid algorithm on concrete array (randomized quicksort but stop recursing at size < k)
def insertion_sort(A: List[int]) -> Tuple[List[int], dict]:
    A = list(A)
    counters = {'comparisons': 0, 'shifts': 0}
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0:
            counters['comparisons'] += 1
            if A[i] > key:
                A[i+1] = A[i]
                counters['shifts'] += 1
                i -= 1
            else:
                break
        A[i+1] = key
    return A, counters

def hybrid_sort(A: List[int], k: int, seed: int = 0) -> Tuple[List[int], dict]:
    """
    Perform randomized quicksort but do not recurse into subarrays of size < k.
    After quicksort stage, perform insertion sort on entire array to finish sorting.
    Return counts of operations.
    """
    random.seed(seed)
    A = list(A)
    counters = {'random_calls': 0, 'comparisons_quick': 0, 'partitions': 0}
    def _partial_qs(lo: int, hi: int):
        if hi - lo + 1 < k:
            return
        # choose random pivot index and partition (count comparisons ~ n)
        counters['random_calls'] += 1
        pivot_index = random.randint(lo, hi)
        pivot = A[pivot_index]
        # Lomuto-like partition but stable for counting
        i = lo - 1
        for j in range(lo, hi + 1):
            counters['comparisons_quick'] += 1
            if A[j] <= pivot:
                i += 1
                A[i], A[j] = A[j], A[i]
        counters['partitions'] += 1
        p = i
        _partial_qs(lo, p - 1)
        _partial_qs(p + 1, hi)
    _partial_qs(0, len(A) - 1)
    # finish with insertion sort
    _, ins_c = insertion_sort(A)
    # merge counters
    counters['ins_comparisons'] = ins_c['comparisons']
    counters['ins_shifts'] = ins_c['shifts']
    return A, counters

if __name__ == "__main__":
    import random
    random.seed(1)
    n = 500
    for k in [5, 10, 50]:
        arr = list(range(n))
        random.shuffle(arr)
        est = hybrid_cost_estimate(n, k)
        _, counters = hybrid_sort(arr, k, seed=1)
        print(f"n={n}, k={k}: estimate~{est:.1f}, quick_calls={counters['random_calls']}, ins_comp={counters['ins_comparisons']}")
