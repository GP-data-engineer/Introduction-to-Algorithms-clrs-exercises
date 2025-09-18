# Exercise 4.3-7
# Solves the recurrence T(n) = 4T(n/2) + n^2
# This recurrence grows faster than linear or log-linear, and results in Θ(n^2 log n)

from functools import lru_cache

@lru_cache(maxsize=None)
def recurrence_4_3_7(n):
    # Base case: constant time for n <= 1
    if n <= 1:
        return 1
    # Recursive case: four subproblems of size n/2 plus quadratic cost
    return 4 * recurrence_4_3_7(n // 2) + n ** 2

if __name__ == "__main__":
    # Example usage: compute T(16)
    result = recurrence_4_3_7(16)
    print(f"Result for T(16): {result}")
