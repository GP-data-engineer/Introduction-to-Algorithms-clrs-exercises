# Exercise 4.3-4
# Solve T(n) = 2T(n/2) + n and show that the solution is Θ(n log n)
# This recurrence assumes exact division and models merge sort precisely

from functools import lru_cache

@lru_cache(maxsize=None)
def recurrence_4_3_4(n):
    # Base case: constant time for n <= 1
    if n <= 1:
        return 1
    # Recursive case: two subproblems of size n/2 plus linear cost
    return 2 * recurrence_4_3_4(n // 2) + n

if __name__ == "__main__":
    # Example usage: compute T(16)
    result = recurrence_4_3_4(16)
    print(f"Result for T(16): {result}")
