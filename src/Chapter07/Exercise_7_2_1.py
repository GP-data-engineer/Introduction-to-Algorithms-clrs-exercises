# Exercise_7_2_1.py
# PL: Zadanie 7.2-1 (CLRS) - Dowód przez podstawianie, że T(n) = T(n-1) + Theta(n) => T(n) = Theta(n^2).
# EN: Exercise 7.2-1 (CLRS) - By substitution show T(n)=T(n-1)+Theta(n) implies T(n)=Theta(n^2).
#
# Implementation:
# - compute_recurrence(n): computes exact T(n) assuming T(1)=c and cost per level = a*n + b (Theta(n)).
# - compare_to_quadratic(n): returns T(n) and n^2 coefficient estimate to illustrate Theta(n^2).
#
# Small demonstration in __main__.

from typing import Tuple

def compute_recurrence(n: int, c: float = 1.0, a: float = 1.0, b: float = 0.0) -> float:
    """
    Compute T(n) by recurrence T(1)=c, T(n)=T(n-1) + (a*n + b).
    Returns exact T(n) = c + sum_{k=2..n} (a*k + b).
    """
    if n <= 1:
        return c
    # Sum a*(2+...+n) + b*(n-1) + c
    sum_k = (n * (n + 1) // 2) - 1  # sum 2..n
    total = c + a * sum_k + b * (n - 1)
    return float(total)

def compare_to_quadratic(n: int, c: float = 1.0, a: float = 1.0, b: float = 0.0) -> Tuple[float, float]:
    """
    Returns (T(n), ratio = T(n)/n^2) to show Theta(n^2) behaviour.
    """
    Tn = compute_recurrence(n, c=c, a=a, b=b)
    ratio = Tn / (n ** 2) if n > 0 else float('inf')
    return Tn, ratio

if __name__ == "__main__":
    # Demo prints to illustrate growth
    for n in [10, 100, 500]:
        Tn, ratio = compare_to_quadratic(n)
        print(f"n={n:4d} T(n)={Tn:10.1f} T(n)/n^2={ratio:.6f}")
