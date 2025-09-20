# Exercise 4.4.3
# Solves the recurrence T(n) = 4T(n/2) + n using recursion
# Asymptotic upper bound via recursion tree: O(n log n)

from functools import lru_cache

@lru_cache(maxsize=None)
def recurrence_4_4_3(n):
    # Base case: constant time for n <= 1
    if n <= 1:
        return 1
    # Recursive case: four subproblems of size n/2 plus linear cost
    return 4 * recurrence_4_4_3(n // 2) + n

if __name__ == "__main__":
    for i in [1, 2, 4, 8, 16]:
        print(f"T({i}) = {recurrence_4_4_3(i)}")
