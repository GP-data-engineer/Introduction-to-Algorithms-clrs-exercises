"""
Exercise 6.2-5
English: Write an iterative version of MAX-HEAPIFY.
Polish: Napisz iteracyjną wersję MAX-HEAPIFY.
"""

def max_heapify_iter(A, i, n):
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
    return A

if __name__ == "__main__":
    arr = [3, 17, 10, 1, 5]
    print("Exercise 6.2-5 Result:")
    print(max_heapify_iter(arr, 0, len(arr)))
