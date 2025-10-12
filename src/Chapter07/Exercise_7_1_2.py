"""
Exercise 7.1-2
English: What value q does PARTITION return if all elements are equal?
Modify PARTITION so that q = floor((p+r)/2) in this case.
Polish: Jaką wartość q zwraca PARTITION, gdy wszystkie elementy są równe?
Zmodyfikuj PARTITION tak, aby q = ⌊(p+r)/2⌋ w tym przypadku.
"""

def partition_equal(A, p, r):
    if all(A[i] == A[p] for i in range(p, r+1)):
        return (p + r) // 2, A
    # fallback to normal partition
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1, A

if __name__ == "__main__":
    arr = [5, 5, 5, 5]
    q, result = partition_equal(arr, 0, len(arr)-1)
    print("Exercise 7.1-2 Result:")
    print("Partition index:", q)
