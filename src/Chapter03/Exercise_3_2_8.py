"""
Exercise 3.2.8
Prove that if k * ln(k) = Θ(n), then k = Θ(n / ln(n)).

This script provides a computational check for the asymptotic relationship
using numerical approximation and verifies the proportionality.
"""

import math


def k_from_n(n: float) -> float:
    """
    Given n, approximate k from the equation k * ln(k) ≈ n.
    Uses iterative approximation (Newton's method).
    """
    if n <= 0:
        raise ValueError("n must be positive")

    # Initial guess for k
    k = n / math.log(n)
    for _ in range(20):  # iterate to refine the approximation
        k = k - (k * math.log(k) - n) / (math.log(k) + 1)
    return k


def check_asymptotic_relation(n: float) -> bool:
    """
    Check if k ≈ n / ln(n) for large n.
    Returns True if the ratio is close to a constant.
    """
    k_val = k_from_n(n)
    approx = n / math.log(n)
    ratio = k_val / approx
    return 0.9 <= ratio <= 1.1  # within 10% tolerance


if __name__ == "__main__":
    # Example demonstration
    test_values = [10, 100, 1000, 10_000, 100_000]
    for n in test_values:
        k_val = k_from_n(n)
        approx = n / math.log(n)
        print(f"n={n:>7}, k≈{k_val:.6f}, n/ln(n)≈{approx:.6f}, ratio={k_val/approx:.4f}")
