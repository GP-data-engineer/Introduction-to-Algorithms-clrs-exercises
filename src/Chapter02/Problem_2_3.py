"""
Problem 2.3 — Correctness of Horner's Scheme

Horner's method evaluates a polynomial:
P(x) = a0 + a1*x + a2*x^2 + ... + an*x^n
in O(n) time using a nested multiplication approach.

Algorithm:
- Start from the highest degree coefficient and iterate downwards.
- At each step, multiply the current result by x and add the next coefficient.
"""

from typing import List

def horner_evaluate(coefficients: List[float], x: float) -> float:
    """
    Evaluates the polynomial with given coefficients at value x
    using Horner's method.

    Parameters:
    coefficients (List[float]): List of coefficients [a0, a1, ..., an]
                                where a0 is the constant term.
    x (float): The value at which to evaluate the polynomial.

    Returns:
    float: The value of the polynomial at x.
    """
    n = len(coefficients)
    y = 0.0
    # Iterate from the highest degree term down to the constant term
    for i in range(n - 1, -1, -1):
        y = coefficients[i] + x * y
    return y

if __name__ == "__main__":
    # Example usage
    coeffs = [2, -6, 2, -1]  # Represents 2 - 6x + 2x^2 - x^3
    val = 3
    print(f"P({val}) =", horner_evaluate(coeffs, val))
