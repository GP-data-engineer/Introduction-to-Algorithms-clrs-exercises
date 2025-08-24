"""
Exercise 2.2-2 (CLRS) — stub
Example: Merge sort without sentinels (if you choose that problem).

Add a short paraphrase of the task here.
Source of index: MIT Press, "Selected Solutions", pp. 82–83.
PDF: https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/11599/selected-solutions.pdf
"""

from typing import List

def merge_sort_no_sentinels(a: List[int]) -> List[int]:
    """Skeleton for a merge-sort implementation without sentinels.
    Replace with your actual implementation.
    """
    if len(a) <= 1:
        return a[:]
    mid = len(a) // 2
    left = merge_sort_no_sentinels(a[:mid])
    right = merge_sort_no_sentinels(a[mid:])
    return _merge(left, right)

def _merge(left: List[int], right: List[int]) -> List[int]:
    i = j = 0
    out: List[int] = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    # Append the remaining elements (no sentinels)
    out.extend(left[i:])
    out.extend(right[j:])
    return out
