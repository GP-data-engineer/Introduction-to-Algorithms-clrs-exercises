"""
Exercise 2.3-6 (CLRS)

Question:
In INSERTION-SORT, the inner while-loop (lines 5–7 in CLRS pseudocode) performs a
linear search backward over the already-sorted prefix A[1..j-1]. Could we use
binary search to reduce the running time of insertion sort to Θ(n log n)?

Answer:
Using binary search to find the insertion position reduces the number of key
comparisons from Θ(n^2) to Θ(n log n). However, insertion sort still needs to
shift elements to make room for the inserted key. Those shifts cost Θ(n^2) in
the worst case, so the overall time remains Θ(n^2).

Below is a stable insertion sort that uses binary search to locate the insertion
index inside the sorted prefix. It accepts an optional `key` function and
sorts the list in-place, returning the same list for convenience.
"""

from typing import Callable, List, Optional, TypeVar

T = TypeVar("T")


def _upper_bound(a: List[T], x: T, hi: int, key: Callable[[T], T]) -> int:
    """
    Return the index in a[0:hi] where x should be inserted to keep the order,
    placing x AFTER any existing elements that compare equal (upper bound).
    """
    lo = 0
    kx = key(x)
    while lo < hi:
        mid = (lo + hi) // 2
        if key(a[mid]) <= kx:
            lo = mid + 1
        else:
            hi = mid
    return lo


def binary_insertion_sort(a: List[T], key: Optional[Callable[[T], T]] = None) -> List[T]:
    """
    Stable insertion sort using binary search to find the insertion position.
    """
    if key is None:
        def key(x):  # type: ignore
            return x

    n = len(a)
    for j in range(1, n):
        x = a[j]
        pos = _upper_bound(a, x, j, key)
        if pos != j:
            a[pos + 1 : j + 1] = a[pos : j]
            a[pos] = x
    return a


if __name__ == "__main__":
    # Example usage
    data = [5, 2, 4, 6, 1, 3]
    print("Before sorting:", data)
    binary_insertion_sort(data)
    print("After sorting: ", data)

    # Another example with duplicates
    data2 = [3, 1, 2, 3, 2, 1, 3]
    print("\nBefore sorting:", data2)
    binary_insertion_sort(data2)
    print("After sorting: ", data2)
