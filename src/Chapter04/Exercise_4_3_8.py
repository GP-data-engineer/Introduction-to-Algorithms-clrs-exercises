# Exercise 4.3-8
# Solves the recurrence T(n) = 4T(n/2) + n
# This recurrence results in Θ(n^2) due to the dominance of recursive branching

from functools import lru_cache

@lru_cache(maxsize=None)
def recurrence_4_3_8(n):
    # Base case: constant time for n <= 1
    if n <= 1:
        return 1
    # Recursive case: four subproblems of size n/2 plus linear cost
    return 4 * recurrence_4_3_8(n // 2) + n

if __name__ == "__main__":
    # Example usage: compute T(16)
    result = recurrence_4_3_8(16)
    print(f"Result for T(16): {result}")
