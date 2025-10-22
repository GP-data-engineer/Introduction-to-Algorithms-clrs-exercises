# Exercise_7_4_4.py
# PL: Zadanie 7.4-4 - Pokaż, że oczekiwany czas działania RANDOMIZED-QUICKSORT wynosi Ω(n lg n).
# EN: Exercise 7.4-4 - Show expected running time of randomized-quicksort is Ω(n log n).
#
# Implementation:
# - Provide a numeric demonstration: compute expected number of comparisons using
#   known identity: expected number of comparisons = 2 * sum_{i<j} Pr{(i,j) compared} = 2 * sum_{i<j} 2/(j-i+1) ~ Θ(n log n).
# - We will compute exact expected comparisons for small n and show growth ~ n log n.

import math
from typing import List

def expected_comparisons_exact(n: int) -> float:
    """
    Compute expected number of comparisons of randomized quicksort exactly
    using formula: E[C] = 2 * sum_{1 <= i < j <= n} 1/(j-i+1)
    (Equivalent forms exist; here we use direct sum.)
    """
    total = 0.0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            total += 2.0 / (j - i + 1)
    return total

if __name__ == "__main__":
    for n in [8, 16, 32, 64]:
        e = expected_comparisons_exact(n)
        print(f"n={n}, E[comparisons]={e:.3f}, E/(n*log2 n)={e/(n*math.log2(n)):.3f}")
