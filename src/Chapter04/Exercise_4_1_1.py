"""
Exercise 4.1-1
Determine what FIND-MAXIMUM-SUBARRAY returns when all elements of array A are negative.
"""

from typing import List, Tuple


def find_maximum_subarray_all_negative(arr: List[int]) -> Tuple[int, int, int]:
    """
    Returns the maximum subarray for an array with all negative numbers.
    In this case, the maximum subarray is the single element with the largest value.
    """
    if not arr:
        raise ValueError("Array must not be empty")

    max_value = arr[0]
    max_index = 0
    for i, val in enumerate(arr):
        if val > max_value:
            max_value = val
            max_index = i
    return max_index, max_index, max_value


if __name__ == "__main__":
    # Example demonstration
    example_array = [-5, -9, -3, -8]
    result = find_maximum_subarray_all_negative(example_array)
    print(f"Array: {example_array}")
    print(f"Max subarray (start, end, sum): {result}")
