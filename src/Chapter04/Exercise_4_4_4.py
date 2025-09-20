# Exercise 4.4.4
# Solves the recurrence T(n) = 2T(n/4) + sqrt(n) using recursion
# Asymptotic upper bound via recursion tree: O(sqrt(n) log n)

from functools import lru_cache
from math import sqrt

@lru_cache(maxsize=None)
def recurrence_4_4_4(n):
    # Base case: constant time for n <= 1
    if n <= 1:
        return 1
    # Recursive case: two subproblems of size n/4 plus square root cost
    return 2 * recurrence_4_4_4(n // 4) + sqrt(n)

if __name__ == "__main__":
    for i in [1, 4, 16, 64, 256]:
        print(f"T({i}) = {recurrence_4_4_4(i):.4f}")
