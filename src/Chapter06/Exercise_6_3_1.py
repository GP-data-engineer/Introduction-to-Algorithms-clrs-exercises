"""
Exercise 6.3-1
English: Illustrate the operation of BUILD-MAX-HEAP for array 
A = <5, 3, 17, 10, 84, 19, 6, 22, 9>.
Polish: Zilustruj działanie BUILD-MAX-HEAP dla tablicy
A = <5, 3, 17, 10, 84, 19, 6, 22, 9>.
"""

# Polish description:
# BUILD-MAX-HEAP wywołuje MAX-HEAPIFY od połowy tablicy w dół.
# Wynik to poprawny max-heap.

def build_max_heap(A):
    n = len(A)
    # Iteracyjna wersja heapify
    def max_heapify(A, i, n):
        while True:
            l = 2*i+1
            r = 2*i+2
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

    for i in range(n//2 - 1, -1, -1):
        max_heapify(A, i, n)
    return A

if __name__ == "__main__":
    arr = [5, 3, 17, 10, 84, 19, 6, 22, 9]
    print("Exercise 6.3-1 Result:")
    print(build_max_heap(arr))
