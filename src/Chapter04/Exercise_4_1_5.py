"""
Exercise 4.1-5
Non-recursive linear-time algorithm for the maximum subarray problem (Kadane's algorithm).
"""

from typing import List, Tuple


def kadane_maximum_subarray(arr: List[int]) -> Tuple[int, int, int]:
    """
    Finds the maximum subarray in O(n) time using Kadane's algorithm.
    Returns (start_index, end_index, max_sum).
    """
    if not arr:
        raise ValueError("Array must not be empty")

    max_sum = arr[0]
    current_sum = arr[0]
    start = end = 0
    temp_start = 0

    for i in range(1, len(arr)):
        # Decide whether to extend the current subarray or start a new one
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            temp_start = i
        else:
            current_sum += arr[i]

        # Update max_sum if needed
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    return start, end, max_sum


if __name__ == "__main__":
    # Example demonstration
    example_array = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    result = kadane_maximum_subarray(example_array)
    print(f"Array: {example_array}")
    print(f"Max subarray (start, end, sum): {result}")
