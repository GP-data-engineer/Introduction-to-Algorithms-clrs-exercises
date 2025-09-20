# Exercise 4.4.7
# Solves the recurrence T(n) = T(n - 1) + T(n - 2) + T(n - 3)
# Asymptotic upper bound: exponential growth, roughly O(3^n)

from functools import lru_cache

@lru_cache(maxsize=None)
def recurrence_4_4_7(n):
    # Base cases
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    # Recursive case: sum of three previous terms
    return recurrence_4_4_7(n - 1) + recurrence_4_4_7(n - 2) + recurrence_4_4_7(n - 3)

if __name__ == "__main__":
    for i in range(1, 10):
        print(f"T({i}) = {recurrence_4_4_7(i)}")
