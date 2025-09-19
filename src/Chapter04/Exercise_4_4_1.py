# Exercise 4.4.1
# Solves the recurrence T(n) = 3T(⌊n/2⌋) + n using recursion
# Demonstrates asymptotic upper bound via recursion tree: O(n log n)

from functools import lru_cache

@lru_cache(maxsize=None)
def recurrence_4_4_1(n):
    # Base case: constant time for n <= 1
    if n <= 1:
        return 1
    # Recursive case: three subproblems of size floor(n/2) plus linear cost
    return 3 * recurrence_4_4_1(n // 2) + n

if __name__ == "__main__":
    # Example usage
    for i in [1, 2, 4, 8, 16]:
        print(f"T({i}) = {recurrence_4_4_1(i)}")
