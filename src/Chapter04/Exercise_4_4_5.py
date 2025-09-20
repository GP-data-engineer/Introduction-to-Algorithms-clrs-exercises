# Exercise 4.4.5
# Solves the recurrence T(n) = T(n - 2) + n^2 using recursion
# Asymptotic upper bound via recursion tree: O(n^3)

from functools import lru_cache

@lru_cache(maxsize=None)
def recurrence_4_4_5(n):
    # Base case: constant time for n <= 1
    if n <= 1:
        return 1
    # Recursive case: one subproblem of size n-2 plus quadratic cost
    return recurrence_4_4_5(n - 2) + n ** 2

if __name__ == "__main__":
    for i in [1, 2, 4, 6, 8]:
        print(f"T({i}) = {recurrence_4_4_5(i)}")
