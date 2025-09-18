# Exercise 4.3-6
# Shows that T(n) = 2T(n/2) + n is the exact recurrence for merge sort
# This recurrence models the divide-and-conquer merge sort algorithm

from functools import lru_cache

@lru_cache(maxsize=None)
def merge_sort_recurrence(n):
    # Base case: constant time for n <= 1
    if n <= 1:
        return 1
    # Recursive case: two halves and linear merge cost
    return 2 * merge_sort_recurrence(n // 2) + n

if __name__ == "__main__":
    # Example usage: compute T(16)
    result = merge_sort_recurrence(16)
    print(f"Merge sort recurrence T(16): {result}")
