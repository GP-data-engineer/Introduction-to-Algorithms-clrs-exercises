"""
Exercise 2.3-3 (CLRS) — Inductive proof of recurrence solution

Task:
Prove, using mathematical induction, that for n being an exact power of two,
the recurrence
    T(n) = 2, if n = 2
    T(n) = 2T(n/2) + n, if n = 2^k for k > 1
has the solution T(n) = n * lg(n).

This script provides a computational check for small powers of two.
"""

import math

def T(n: int) -> int:
    """Recurrence definition for n being a power of two."""
    if n == 2:
        return 2
    return 2 * T(n // 2) + n

if __name__ == "__main__":
    for k in range(1, 8):
        n = 2 ** k
        val = T(n)
        formula = n * int(math.log2(n))
        print(f"n={n}, T(n)={val}, formula={formula}, match={val == formula}")
