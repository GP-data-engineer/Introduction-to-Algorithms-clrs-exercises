"""
Exercise 2.1-3 (CLRS) Linear Search

Given:
    A sequence of n numbers A = ⟨a1, a2, ..., an⟩ and a value v.
Goal:
    Return an index i such that v = A[i], or None (NIL) if v does not appear in A.

Loop Invariant Proof:
Invariant: Before each iteration of the loop with index i (0-based in Python),
           v does not appear in the prefix A[0..i-1].

1. Initialization:
   Before the first iteration (i = 0), the prefix A[0..-1] is empty,
   so v is not present — the invariant holds.

2. Maintenance:
   If A[i] != v, then after incrementing i the invariant still holds.
   If A[i] == v, the algorithm returns i — a correct result.

3. Termination:
   After scanning the entire array (i = n), the invariant implies that v
   is not in A, so returning None (NIL) is correct.
"""

from typing import List, Optional

def linear_search(array: List[int], target: int) -> Optional[int]:
    """
    Returns the 0-based index of the first occurrence of target in array,
    or None if target is not found.

    Time complexity: O(n)
    Space complexity: O(1)
    """
    for index, value in enumerate(array):
        if value == target:
            return index
    return None

if __name__ == "__main__":
    # Example array
    array = [31, 41, 59, 26, 41, 58]
    test_values = [31, 41, 58, 100]

    for target in test_values:
        result_index = linear_search(array, target)
        print(f"array={array}, target={target} -> index={result_index if result_index is not None else 'NIL'}")
