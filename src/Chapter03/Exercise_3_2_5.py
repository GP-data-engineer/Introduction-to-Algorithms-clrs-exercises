# Exercise 3.2-5
# Prove that log(n!) = Θ(n log n).

import math

def log_factorial(n):
    """Return log2(n!) and compare with n log2 n."""
    return math.log2(math.factorial(n)), n * math.log2(n)

if __name__ == "__main__":
    for n in range(2, 8):
        log_fact, nlogn = log_factorial(n)
        print(f"n={n}, log2(n!)={log_fact:.4f}, n log2 n={nlogn:.4f}")
