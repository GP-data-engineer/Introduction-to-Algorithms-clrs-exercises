"""
Exercise 4.1-3
Compare brute-force and recursive maximum subarray algorithms and find crossover point n0.
"""

from typing import List, Tuple
import random
import time


def brute_force_maximum_subarray(arr: List[int]) -> Tuple[int, int, int]:
    """Brute-force O(n^2) maximum subarray."""
    max_sum = arr[0]
    start = end = 0
    n = len(arr)
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            if current_sum > max_sum:
                max_sum = current_sum
                start, end = i, j
    return start, end, max_sum


def find_max_crossing_subarray(arr: List[int], low: int, mid: int, high: int) -> Tuple[int, int, int]:
    """Find max subarray crossing the midpoint."""
    left_sum = float('-inf')
    total = 0
    max_left = mid
    for i in range(mid, low - 1, -1):
        total += arr[i]
        if total > left_sum:
            left_sum = total
            max_left = i

    right_sum = float('-inf')
    total = 0
    max_right = mid + 1
    for j in range(mid + 1, high + 1):
        total += arr[j]
        if total > right_sum:
            right_sum = total
            max_right = j

    return max_left, max_right, left_sum + right_sum


def recursive_maximum_subarray(arr: List[int], low: int, high: int) -> Tuple[int, int, int]:
    """Recursive divide-and-conquer maximum subarray."""
    if low == high:
        return low, high, arr[low]
    mid = (low + high) // 2
    left_low, left_high, left_sum = recursive_maximum_subarray(arr, low, mid)
    right_low, right_high, right_sum = recursive_maximum_subarray(arr, mid + 1, high)
    cross_low, cross_high, cross_sum = find_max_crossing_subarray(arr, low, mid, high)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum


def find_crossover_point(max_n: int = 200) -> int:
    """
    Find n0 where recursive algorithm becomes faster than brute-force.
    """
    for n in range(2, max_n + 1):
        arr = [random.randint(-100, 100) for _ in range(n)]
        start_b = time.perf_counter()
        brute_force_maximum_subarray(arr)
        time_b = time.perf_counter() - start_b

        start_r = time.perf_counter()
        recursive_maximum_subarray(arr, 0, len(arr) - 1)
        time_r = time.perf_counter() - start_r

        if time_r < time_b:
            return n
    return -1  # not found within range


if __name__ == "__main__":
    n0 = find_crossover_point(200)
    print(f"Crossover point n0: {n0}")
