# Exercise 3.2-3
# Prove that if n >= 1, then n! > 2^n.

import math

def factorial_greater_than_power_of_two(n):
    """Check if n! > 2^n for given n."""
    if n < 1:
        raise ValueError("n must be >= 1")
    return math.factorial(n) > 2**n
