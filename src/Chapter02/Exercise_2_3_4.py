"""
Exercise 2.3-4 (CLRS) — Recursive insertion sort recurrence

Task:
Express insertion sort recursively:
    - Sort A[1..n-1] recursively
    - Insert A[n] into the sorted subarray A[1..n-1]
Write the recurrence for the worst-case running time.

This script implements recursive insertion sort and counts comparisons.
"""

from typing import List, Tuple

def recursive_insertion_sort(A: List[int], n: int) -> Tuple[List[int], int]:
    """Sort first n elements of A recursively and count comparisons."""
    if n <= 1:
        return A, 0
    A, comps = recursive_insertion_sort(A, n - 1)
    key = A[n - 1]
    i = n - 2
    while i >= 0 and A[i] > key:
        A[i + 1] = A[i]
        i -= 1
        comps += 1
    A[i + 1] = key
    comps += 1  # final comparison
    return A, comps

if __name__ == "__main__":
    arr = [5, 2, 4, 6, 1, 3]
    sorted_arr, comparisons = recursive_insertion_sort(arr, len(arr))
    print("Sorted:", sorted_arr)
    print("Comparisons (worst-case recurrence T(n) = T(n-1) + Θ(n)):", comparisons)
