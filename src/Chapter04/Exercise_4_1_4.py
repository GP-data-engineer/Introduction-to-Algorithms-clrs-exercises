"""
Exercise 4.1-4
Modify the maximum subarray algorithm to allow an empty subarray with sum 0.
"""

from typing import List, Tuple


def max_subarray_allow_empty(arr: List[int]) -> Tuple[int, int, int]:
    """
    Returns the maximum subarray allowing an empty subarray with sum 0.
    If all numbers are negative, returns an empty subarray (start=end=-1, sum=0).
    """
    if not arr:
        return -1, -1, 0  # empty array case

    max_sum = 0
    start = end = -1
    current_sum = 0
    temp_start = 0

    for i, val in enumerate(arr):
        current_sum += val
        if current_sum > max_sum:
            max_sum = current_sum
            start, end = temp_start, i
        if current_sum < 0:
            current_sum = 0
            temp_start = i + 1

    return start, end, max_sum


if __name__ == "__main__":
    # Example demonstration
    example_array = [-5, -1, -8]
    result = max_subarray_allow_empty(example_array)
    print(f"Array: {example_array}")
    print(f"Max subarray (start, end, sum): {result}")
