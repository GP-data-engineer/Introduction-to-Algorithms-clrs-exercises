"""
Exercise 7.1-1
English: Illustrate the operation of PARTITION for array 
A = (13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11).
Polish: Zilustruj działanie PARTITION dla tablicy
A = (13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11).
"""

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1, A

if __name__ == "__main__":
    arr = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
    q, result = partition(arr, 0, len(arr)-1)
    print("Exercise 7.1-1 Result:")
    print("Partition index:", q)
    print("Array after partition:", result)
