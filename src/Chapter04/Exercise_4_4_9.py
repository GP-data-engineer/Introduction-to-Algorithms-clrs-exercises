# Exercise 4.4.9
# Solves the recurrence T(n) = T(n - 1) + T(n/2) + n using recursion
# Asymptotic upper bound: superlinear, roughly O(n log n)

from functools import lru_cache

@lru_cache(maxsize=None)
def recurrence_4_4_9(n):
    # Base case
    if n <= 1:
        return 1
    # Recursive case: one linear term plus two recursive calls
    return recurrence_4_4_9(n - 1) + recurrence_4_4_9(n // 2) + n

if __name__ == "__main__":
    for i in [1, 2, 4, 8, 16]:
        print(f"T({i}) = {recurrence_4_4_9(i)}")
