# Exercise_7_4_2.py
# PL: Zadanie 7.4-2 - Pokaż, że czas działania quicksort w przypadku optymistycznym wynosi Ω(n lg n).
# EN: Exercise 7.4-2 - Show that quicksort running time in optimistic case is Ω(n log n).
#
# Implementation:
# - We'll argue via recurrence: if at each partition we split at most constant fraction (balanced),
#   recurrence gives T(n) = Ω(n log n). To demonstrate, implement balanced quicksort and count comparisons.
# - balanced_quicksort_count simulates balanced partitions by always choosing median pivot (perfect split).
# - Count comparisons and show growth ~ n log n.

from typing import List, Tuple
import math

def balanced_quicksort_count(A: List[int]) -> Tuple[List[int], dict]:
    """
    Simulate best/optimistic scenario by always partitioning evenly (median pivot).
    Count comparisons as if partition inspects each element once per partition call -> Θ(n) per level.
    The total comparisons ~ c * n * depth ~ Theta(n log n).
    """
    counters = {'comparisons': 0}
    A_copy = list(A)
    def _simulate(n: int):
        if n <= 1:
            return
        # one partition step touches n-1 elements => n comparisons approx
        counters['comparisons'] += n - 1
        left = n // 2
        right = n - left - 1
        _simulate(left)
        _simulate(right)
    _simulate(len(A_copy))
    return A_copy, counters

if __name__ == "__main__":
    for n in [16, 64, 256]:
        _, counters = balanced_quicksort_count(list(range(n)))
        comps = counters['comparisons']
        print(f"n={n}, comparisons≈{comps}, comps / (n * log2 n) ≈ {comps / (n * math.log2(n)):.3f}")
