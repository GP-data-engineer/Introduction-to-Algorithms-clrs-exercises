"""
Exercise 2.3-2 (CLRS) — Merge procedure without sentinels

Task:
Modify the MERGE procedure so that it does not use sentinel values.
Instead, the algorithm should:
1. Stop when all elements from one of the subarrays (L or R) have been copied.
2. Copy the remaining elements from the other subarray into A.

This implementation assumes that the input subarrays are already sorted.
"""

from typing import List

def merge_no_sentinels(A: List[int], p: int, q: int, r: int) -> None:
    """
    Merge two sorted subarrays A[p:q+1] and A[q+1:r+1] into a single sorted subarray in place.
    This version does not use sentinel values.
    """
    # Create copies of the subarrays
    L = A[p:q+1]
    R = A[q+1:r+1]

    i = 0  # index for L
    j = 0  # index for R
    k = p  # index for merged array A

    # Merge until one subarray is exhausted
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    # Copy any remaining elements from L
    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1

    # Copy any remaining elements from R
    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1

def merge_sort_no_sentinels(A: List[int], p: int, r: int) -> None:
    """Recursive merge sort using merge_no_sentinels."""
    if p < r:
        q = (p + r) // 2
        merge_sort_no_sentinels(A, p, q)
        merge_sort_no_sentinels(A, q + 1, r)
        merge_no_sentinels(A, p, q, r)

if __name__ == "__main__":
    A = [3, 41, 52, 26, 38, 57, 9, 49]
    print("Initial array:", A)
    merge_sort_no_sentinels(A, 0, len(A) - 1)
    print("Sorted array:", A)
