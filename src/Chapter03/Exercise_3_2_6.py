# Exercise 3.2-6
# Prove that n! = ω(2^n) and n! = o(n^n).

import math

def compare_factorial_growth(n):
    """Return comparison results for n! vs 2^n and n^n."""
    fact = math.factorial(n)
    return fact > 2**n, fact < n**n

if __name__ == "__main__":
    for n in range(3, 8):
        greater, smaller = compare_factorial_growth(n)
        print(f"n={n}: n! > 2^n? {greater}, n! < n^n? {smaller}")
