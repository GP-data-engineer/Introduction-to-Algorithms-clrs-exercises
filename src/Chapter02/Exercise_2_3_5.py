"""
Exercise 2.3-5 (CLRS) — Binary search recurrence

Task:
Given a sorted array A, binary search compares the target to the middle element:
    - If equal, stop.
    - If smaller, search left half.
    - If larger, search right half.
Write the recurrence for the worst-case running time and solve T(n).

Worst-case recurrence:
    T(n) = T(n/2) + Θ(1)
Solution:
    T(n) = Θ(log n)
"""

from typing import List

def binary_search(A: List[int], target: int) -> int:
    """Iterative binary search returning index or -1."""
    low, high = 0, len(A) - 1
    while low <= high:
        mid = (low + high) // 2
        if A[mid] == target:
            return mid
        elif A[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13]
    print("Index of 7:", binary_search(arr, 7))
    print("Index of 2:", binary_search(arr, 2))
