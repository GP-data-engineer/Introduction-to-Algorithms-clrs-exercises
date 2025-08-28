"""
Exercise 2.3-3 (CLRS) — Inductive proof of recurrence solution
"""

import math

def T(n: int) -> int:
    """Rekurencyjna definicja dla n będącego potęgą dwójki."""
    if n == 2:
        return 2
    return 2 * T(n // 2) + n

def formula(n: int) -> int:
    """Zamknięty wzór T(n) = n * log2(n) dla potęg dwójki."""
    return int(n * math.log2(n))

if __name__ == "__main__":
    for k in range(1, 8):
        n = 2 ** k
        val = T(n)
        expected = formula(n)
        print(f"n={n}, T(n)={val}, formula={expected}, match={val == expected}")

