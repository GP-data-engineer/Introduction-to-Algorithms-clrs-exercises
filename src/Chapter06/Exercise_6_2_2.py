"""
Exercise 6.2-2
English: Write MIN-HEAPIFY(A, i) based on MAX-HEAPIFY. Compare running times.
Polish: Napisz MIN-HEAPIFY(A, i) na podstawie MAX-HEAPIFY. Porównaj czasy działania.
"""

def min_heapify(A, i, n):
    l = 2*i+1
    r = 2*i+2
    smallest = i
    if l < n and A[l] < A[smallest]:
        smallest = l
    if r < n and A[r] < A[smallest]:
        smallest = r
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        min_heapify(A, smallest, n)
    return A

def time_complexity():
    return "O(log n) same as MAX-HEAPIFY"

if __name__ == "__main__":
    arr = [3, 5, 4, 10, 8]
    print("Exercise 6.2-2 Result:")
    print(min_heapify(arr, 0, len(arr)))
    print(time_complexity())
