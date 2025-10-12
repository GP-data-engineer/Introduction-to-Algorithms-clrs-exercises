"""
Exercise 7.1-4
English: How to modify QUICKSORT to sort in non-increasing order?
Polish: Jak zmodyfikować QUICKSORT, aby sortował w porządku nierosnącym?
"""

def quicksort_desc(A):
    if len(A) <= 1:
        return A
    pivot = A[-1]
    left = [x for x in A[:-1] if x >= pivot]
    right = [x for x in A[:-1] if x < pivot]
    return quicksort_desc(left) + [pivot] + quicksort_desc(right)

if __name__ == "__main__":
    arr = [3, 6, 1, 8, 4]
    print("Exercise 7.1-4 Result:")
    print(quicksort_desc(arr))
