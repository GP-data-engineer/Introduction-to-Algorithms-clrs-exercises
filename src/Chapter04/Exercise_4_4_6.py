# Exercise 4.4.6
# Solves the recurrence T(n) = T(n - 1) + 1/n using recursion
# Asymptotic upper bound: O(log n)

from functools import lru_cache

@lru_cache(maxsize=None)
def recurrence_4_4_6(n):
    # Base case: constant time for n <= 1
    if n <= 1:
        return 1
    # Recursive case: one subproblem of size n-1 plus harmonic cost
    return recurrence_4_4_6(n - 1) + 1 / n

if __name__ == "__main__":
    for i in [1, 2, 4, 8, 16]:
        print(f"T({i}) = {recurrence_4_4_6(i):.6f}")
