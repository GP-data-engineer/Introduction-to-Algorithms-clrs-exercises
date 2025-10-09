"""
Exercise 6.4-1
English: Illustrate the operation of HEAPSORT for array A = (5, 13, 2, 25, 7, 17, 20, 8, 4).
Polish: Zilustruj działanie HEAPSORT dla tablicy A = (5, 13, 2, 25, 7, 17, 20, 8, 4).
"""

# Polish description:
# HEAPSORT działa w dwóch krokach: (1) budowa kopca max, (2) wielokrotne usuwanie maksimum.
# Wynik to tablica posortowana rosnąco.

def heapsort(A):
    def max_heapify(A, i, n):
        while True:
            l, r = 2*i+1, 2*i+2
            largest = i
            if l < n and A[l] > A[largest]:
                largest = l
            if r < n and A[r] > A[largest]:
                largest = r
            if largest != i:
                A[i], A[largest] = A[largest], A[i]
                i = largest
            else:
                break

    def build_max_heap(A):
        n = len(A)
        for i in range(n//2 - 1, -1, -1):
            max_heapify(A, i, n)

    n = len(A)
    build_max_heap(A)
    for i in range(n-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        max_heapify(A, 0, i)
    return A

if __name__ == "__main__":
    arr = [5, 13, 2, 25, 7, 17, 20, 8, 4]
    print("Exercise 6.4-1 Result:")
    print(heapsort(arr))
