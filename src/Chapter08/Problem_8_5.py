"""
Problem 8.5 (EN): k-sorting an array based on average comparisons and segment constraints.
Problem 8.5 (PL): k-sortowanie tablicy na podstawie porównań średnich i ograniczeń segmentowych.
"""

import heapq

def k_sort(arr, k):
    """
    Sortuje tablicę tak, aby była k-posortowana.
    Działa w czasie O(n log(n/k)) przy użyciu kopca.
    """
    n = len(arr)
    result = []
    heap = []

    for i in range(k):
        if i < n:
            heapq.heappush(heap, arr[i])

    for i in range(k, n):
        result.append(heapq.heappop(heap))
        heapq.heappush(heap, arr[i])

    while heap:
        result.append(heapq.heappop(heap))

    return result

def is_k_sorted(arr, k):
    """
    Sprawdza czy tablica jest k-posortowana.
    """
    for i in range(len(arr) - k):
        if arr[i] > arr[i + k]:
            return False
    return True

if __name__ == "__main__":
    A = [9, 1, 3, 7, 5, 2, 6, 4, 8]
    k = 3
    sorted_k = k_sort(A, k)
    print(f"Tablica wejściowa: {A}")
    print(f"{k}-posortowana tablica: {sorted_k}")
    print(f"Czy jest {k}-posortowana? {is_k_sorted(sorted_k, k)}")
