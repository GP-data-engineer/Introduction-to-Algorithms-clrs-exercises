"""
Exercise 6.4-1 / Zadanie 6.4-1
---------------------------------
EN: Illustrate the operation of the HEAPSORT procedure for the array 
A = [5, 13, 2, 25, 7, 17, 20, 8, 4].

PL: Zilustruj działanie procedury HEAPSORT dla tablicy 
A = [5, 13, 2, 25, 7, 17, 20, 8, 4].
"""

def heapify(arr, n, i):
    """Ensure subtree rooted at index i satisfies max-heap property."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def build_max_heap(arr):
    """Build max heap from array."""
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

def heapsort(arr):
    """Perform heapsort."""
    n = len(arr)
    build_max_heap(arr)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr

if __name__ == "__main__":
    A = [5, 13, 2, 25, 7, 17, 20, 8, 4]
    print("Original:", A)
    print("Sorted:", heapsort(A))
