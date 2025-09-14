"""
Exercise 4.1-2
Brute-force algorithm for the maximum subarray problem with Θ(n^2) complexity.
"""

from typing import List, Tuple


def brute_force_maximum_subarray(arr: List[int]) -> Tuple[int, int, int]:
    """
    Finds the maximum subarray using a brute-force O(n^2) approach.
    Returns (start_index, end_index, max_sum).
    """
    if not arr:
        raise ValueError("Array must not be empty")

    max_sum = arr[0]
    start = end = 0
    n = len(arr)

    # Check all possible subarrays
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            if current_sum > max_sum:
                max_sum = current_sum
                start, end = i, j
    return start, end, max_sum


if __name__ == "__main__":
    # Example demonstration
    example_array = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    result = brute_force_maximum_subarray(example_array)
    print(f"Array: {example_array}")
    print(f"Max subarray (start, end, sum): {result}")
