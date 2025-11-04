# Exercise 8.4-2 (CLRS)
# English: Explain why the worst-case running time of bucket sort is Θ(n²). How can it be modified so that its average case remains linear, but the worst-case becomes O(n log n)?
# Polish: Wyjaśnij, dlaczego pesymistyczny czas działania sortowania kubełkowego to Θ(n²). Jak można go zmodyfikować, aby średni czas pozostał liniowy, a pesymistyczny wynosił O(n log n)?

from src.Chapter06.Exercise_8_4_1 import bucket_sort

def bucket_sort_with_merge(A):
    """Modified bucket sort using Merge Sort inside each bucket for better worst-case time."""
    def merge_sort(lst):
        if len(lst) <= 1:
            return lst
        mid = len(lst)//2
        left = merge_sort(lst[:mid])
        right = merge_sort(lst[mid:])
        return merge(left, right)

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result

    n = len(A)
    B = [[] for _ in range(n)]
    for x in A:
        index = int(n * x)
        B[index].append(x)
    for i in range(n):
        B[i] = merge_sort(B[i])
    return [x for bucket in B for x in bucket]

if __name__ == "__main__":
    A = [0.99, 0.98, 0.97, 0.96, 0.95, 0.94]
    print("Original array:", A)
    print("Sorted array with merge:", bucket_sort_with_merge(A))
