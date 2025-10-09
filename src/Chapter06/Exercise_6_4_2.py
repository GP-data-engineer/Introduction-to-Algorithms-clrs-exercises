"""
Exercise 6.4-2 / Zadanie 6.4-2
---------------------------------
EN: Justify the correctness of HEAPSORT using the loop invariant:
At the beginning of each iteration of the for loop, the subarray A[0..i]
is a max-heap containing the i smallest elements of A[0..n], and the
subarray A[i+1..n] contains the sorted n - i largest elements.

PL: Uzasadnij poprawność procedury HEAPSORT korzystając z niezmiennika pętli:
Na początku każdej iteracji pętli for podtablica A[0..i] jest kopcem typu max
zawierającym i najmniejszych elementów, a A[i+1..n] zawiera posortowane
n - i największych elementów.
"""

from src.Chapter06.Exercise_6_4_1 import heapify, build_max_heap

def verify_heap_property(arr):
    """Check if array satisfies max-heap property."""
    n = len(arr)
    for i in range(n // 2):
        left, right = 2 * i + 1, 2 * i + 2
        if left < n and arr[i] < arr[left]:
            return False
        if right < n and arr[i] < arr[right]:
            return False
    return True

def heapsort_with_invariant(arr):
    """Heapsort that verifies invariant at each step."""
    n = len(arr)
    build_max_heap(arr)
    assert verify_heap_property(arr), "Invariant failed: not a max-heap"
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
        assert verify_heap_property(arr[:i]), f"Invariant failed at i={i}"
    return arr

if __name__ == "__main__":
    A = [5, 13, 2, 25, 7, 17, 20, 8, 4]
    print("Sorted with invariant check:", heapsort_with_invariant(A))
