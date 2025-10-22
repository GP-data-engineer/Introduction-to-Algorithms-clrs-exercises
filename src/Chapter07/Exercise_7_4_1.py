# Exercise_7_4_1.py
# PL: Zadanie 7.4-1 (CLRS) - Pokaż, że rozwiązaniem rekurencji
#     T(n) = max_{0 <= q <= n-1} ( T(q) + T(n-q-1) ) + Θ(n) jest T(n) = Ω(n^2).
# EN: Exercise 7.4-1 - Show that solution of recurrence
#     T(n) = max_{0<=q<=n-1} ( T(q) + T(n-q-1) ) + Θ(n) is T(n) = Ω(n^2).
#
# Implementation:
# - compute_lower_bound(n): compute explicit lower bound by choosing q = n-1 (or q = 0),
#   which yields T(n) >= T(n-1) + Theta(n), so gives Omega(n^2).
# - simulate_recurrence(n): compute exact recurrence using max over q with base T(0)=T(1)=c,
#   using simple Theta(n) = a*n + b to show numeric growth.

from typing import List

def compute_lower_bound(n: int, c: float = 1.0, a: float = 1.0, b: float = 0.0) -> float:
    """
    Using q = n-1 we get recurrence T(n) >= T(n-1) + (a*n + b).
    Compute that closed-form lower bound (sum of linear terms) -> Theta(n^2).
    """
    if n <= 1:
        return c
    # same formula as sum of k from 2..n
    sum_k = (n * (n + 1) // 2) - 1
    return float(c + a * sum_k + b * (n - 1))

def simulate_recurrence(n: int, c: float = 1.0, a: float = 1.0, b: float = 0.0) -> float:
    """
    Compute T(n) exactly for this 'max' recurrence using dynamic programming:
    T(0)=T(1)=c. For each n compute T(n) = max_q (T(q) + T(n-q-1)) + (a*n+b).
    Returns numeric T(n).
    """
    if n <= 1:
        return c
    T: List[float] = [0.0] * (n + 1)
    T[0] = c
    T[1] = c
    for m in range(2, n + 1):
        best = -float('inf')
        for q in range(0, m):
            val = T[q] + T[m - q - 1]
            if val > best:
                best = val
        T[m] = best + (a * m + b)
    return T[n]

if __name__ == "__main__":
    for n in [5, 10, 20]:
        lb = compute_lower_bound(n)
        sim = simulate_recurrence(n)
        print(f"n={n}: lower_bound≈{lb:.1f}, simulated T(n)={sim:.1f}  -> shows Ω(n^2)")
