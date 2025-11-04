# Exercise 8.4-1 (CLRS)
# English: Illustrate the operation of the BUCKET-SORT procedure for A = [0.79, 0.13, 0.16, 0.64, 0.39, 0.20, 0.89, 0.53, 0.71, 0.42].
# Polish: Zilustruj działanie procedury BUCKET-SORT dla tablicy A = [0.79, 0.13, 0.16, 0.64, 0.39, 0.20, 0.89, 0.53, 0.71, 0.42].

def insertion_sort(bucket):
    """Helper function: sorts a bucket using insertion sort."""
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key
    return bucket

def bucket_sort(A):
    """Implementation of the Bucket Sort algorithm for floating-point numbers in [0, 1)."""
    n = len(A)
    B = [[] for _ in range(n)]  # Create n empty buckets
    for x in A:
        index = int(n * x)  # Determine bucket index
        B[index].append(x)
    for i in range(n):
        B[i] = insertion_sort(B[i])
    return [x for bucket in B for x in bucket]  # Concatenate buckets

if __name__ == "__main__":
    A = [0.79, 0.13, 0.16, 0.64, 0.39, 0.20, 0.89, 0.53, 0.71, 0.42]
    print("Original array:", A)
    sorted_A = bucket_sort(A)
    print("Sorted array:", sorted_A)
