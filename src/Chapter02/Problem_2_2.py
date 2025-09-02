"""
Problem 2.2 (CLRS) — Correctness of Bubble Sort

Task:
Implement the BUBBLESORT procedure as described in the pseudocode.
Prove its correctness using loop invariants.

Algorithm:
- Repeatedly swap adjacent elements if they are out of order.
- After the i-th pass, the i largest elements are in their correct positions at the end of the array.

Time complexity:
- Worst case: O(n^2)
- Best case: O(n) if optimized with a swapped flag (not implemented here).
"""

from typing import List

def bubble_sort(A: List[int]) -> List[int]:
    """
    Sorts the list A in nondecreasing order using the bubble sort algorithm.
    This implementation modifies the list in place and also returns it.
    """
    n = len(A)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if A[j] < A[j - 1]:
                # Swap adjacent elements if they are in the wrong order
                A[j], A[j - 1] = A[j - 1], A[j]
    return A

if __name__ == "__main__":
    # Example usage
    arr = [5, 1, 4, 2, 8]
    print("Original:", arr)
    sorted_arr = bubble_sort(arr)
    print("Sorted:", sorted_arr)
