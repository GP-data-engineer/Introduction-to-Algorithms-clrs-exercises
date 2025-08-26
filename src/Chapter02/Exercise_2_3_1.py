"""
Exercise 2.3-1 (CLRS) — Illustrating merge sort

Task:
Illustrate (similar to Figure 2.4 in the book) the operation of the merge sort
algorithm for the array A = (3, 41, 52, 26, 38, 57, 9, 49).

Requirements:
- Show the recursive division of the array into subarrays.
- Show the merging steps until the array is sorted.
- Output should clearly indicate each merge step.

Note:
This is primarily a tracing/illustration exercise, not an optimization task.
"""

from typing import List

def merge_sort_trace(a: List[int], depth: int = 0) -> List[int]:
    """Perform merge sort and print the splitting/merging steps."""
    indent = "  " * depth
    print(f"{indent}Splitting: {a}")
    if len(a) <= 1:
        return a[:]
    mid = len(a) // 2
    left = merge_sort_trace(a[:mid], depth + 1)
    right = merge_sort_trace(a[mid:], depth + 1)
    merged = _merge(left, right)
    print(f"{indent}Merging: {merged}")
    return merged

def _merge(left: List[int], right: List[int]) -> List[int]:
    """Merge two sorted lists without sentinels."""
    i = j = 0
    out: List[int] = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    out.extend(left[i:])
    out.extend(right[j:])
    return out

if __name__ == "__main__":
    A = [3, 41, 52, 26, 38, 57, 9, 49]
    print("Initial array:", A)
    sorted_A = merge_sort_trace(A)
    print("Sorted array:", sorted_A)
