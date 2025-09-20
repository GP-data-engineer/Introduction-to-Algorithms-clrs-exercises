# Exercise 4.4.8
# Solves the recurrence T(n) = T(n - 1) + log n using recursion
# Asymptotic upper bound: O(n log n)

from functools import lru_cache
from math import log

@lru_cache(maxsize=None)
def recurrence_4_4_8(n):
    # Base case
    if n <= 1:
        return 1
    # Recursive case: one subproblem of size n-1 plus logarithmic cost
    return recurrence_4_4_8(n - 1) + log(n)

if __name__ == "__main__":
    for i in [1, 2, 4, 8, 16]:
        print(f"T({i}) = {recurrence_4_4_8(i):.4f}")
