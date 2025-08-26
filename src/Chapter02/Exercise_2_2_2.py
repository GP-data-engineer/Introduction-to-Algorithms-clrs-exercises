"""
Exercise 2.2-2 (CLRS) — Merge without sentinels

Task:
Rewrite the MERGE procedure so that it does not use sentinels.
Modify MERGE-SORT to use your MERGE.

Notes:
- Stable merge: keep relative order of equal elements.
- No sentinels: explicitly check subarray exhaustion.
- Time: O(n log n), Space: O(n) due to temporary arrays.

This file implements a functional (out-of-place) merge sort that
adheres to the “no sentinels” requirement in the merge step.
Comments and task text are in English by design.
"""

from typing import List, TypeVar, Sequence

T = TypeVar("T")

def merge_sort_no_sentinels(a: Sequence[T]) -> List[T]:
    # Return a sorted copy of sequence a using merge sort without sentinels.
    n = len(a)
    if n <= 1:
        return list(a)
    mid = n // 2
    left = merge_sort_no_sentinels(a[:mid])
    right = merge_sort_no_sentinels(a[mid:])
    return _merge(left, right)

def _merge(left: List[T], right: List[T]) -> List[T]:
    # Merge two sorted lists into a new sorted list without using sentinels.
    i = 0  # index into left
    j = 0  # index into right
    out: List[T] = []
    out_extend = out.extend  # minor micro-optimization for tail copy

    # While both lists have remaining elements, pick the smaller (stable on ties).
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1

    # Append the remainder from the non-exhausted list (no sentinels needed).
    if i < len(left):
        out_extend(left[i:])
    elif j < len(right):
        out_extend(right[j:])
    return out

if __name__ == "__main__":
    # Simple self-checks
    samples = [
        [],
        [1],
        [2, 1],
        [3, 2, 1],
        [5, 1, 4, 2, 8, 5, 2],
        [0, -1, -1, 3, 2, 2, 2, 1],
    ]
    for s in samples:
        got = merge_sort_no_sentinels(s)
        assert got == sorted(s), f"Failed on {s}: got {got}"
    print("All self-checks passed.")

