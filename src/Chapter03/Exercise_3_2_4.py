# Exercise 3.2-4
# Check if floor(log n)! and ceil(log n)! are polynomially bounded.

import math

def is_polynomially_bounded_factorial_log(n, floor=True):
    """Check if factorial of floor/ceil(log n) is polynomially bounded."""
    log_val = math.floor(math.log2(n)) if floor else math.ceil(math.log2(n))
    fact_val = math.factorial(log_val)
    # Compare with n^k for some small k (e.g., k=5)
    return fact_val <= n**5

if __name__ == "__main__":
    n = 1024
    print(f"floor(log2({n}))! polynomially bounded?", is_polynomially_bounded_factorial_log(n, floor=True))
    print(f"ceil(log2({n}))! polynomially bounded?", is_polynomially_bounded_factorial_log(n, floor=False))
