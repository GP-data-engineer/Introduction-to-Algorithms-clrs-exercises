"""
Problem 2.4 — Counting Inversions

Definition:
An inversion in an array A[0..n-1] is a pair (i, j) such that i < j and A[i] > A[j].

This implementation counts the number of inversions in O(n log n) time
by modifying the merge sort algorithm.
"""

from typing import List, Tuple

def count_inversions(arr: List[int]) -> int:
    """
    Counts the number of inversions in the given list using a modified merge sort.

    Parameters:
    arr (List[int]): List of distinct integers.

    Returns:
    int: The number of inversions in the list.
    """
    _, inv_count = _merge_sort_and_count(list(arr))  # Use a copy to avoid modifying the original
    return inv_count

def _merge_sort_and_count(arr: List[int]) -> Tuple[List[int], int]:
    """
    Recursively sorts the array and counts inversions.

    Returns:
    Tuple[List[int], int]: A tuple containing the sorted array and the inversion count.
    """
    n = len(arr)
    if n <= 1:
        return arr, 0

    mid = n // 2
    left, left_inv = _merge_sort_and_count(arr[:mid])
    right, right_inv = _merge_sort_and_count(arr[mid:])
    merged, split_inv = _merge_and_count(left, right)

    return merged, left_inv + right_inv + split_inv

def _merge_and_count(left: List[int], right: List[int]) -> Tuple[List[int], int]:
    """
    Merges two sorted lists and counts split inversions.

    A split inversion occurs when an element from the left half is greater
    than an element from the right half.
    """
    merged = []
    i = j = inv_count = 0
    len_left = len(left)

    while i < len_left and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            # All remaining elements in left[i:] are greater than right[j]
            inv_count += len_left - i

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inv_count

if __name__ == "__main__":
    # Example usage
    example = [2, 3, 8, 6, 1]
    print("Array:", example)
    print("Number of inversions:", count_inversions(example))
