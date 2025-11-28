# Exercise 9.3-3 (EN): Implement Quicksort using SELECT to guarantee worst-case O(n log n).
# Exercise 9.3-3 (PL): Zaimplementuj Quicksort z użyciem SELECT, aby zagwarantować pesymistyczny czas O(n log n).

def deterministic_select(A, i):
    """
    Deterministyczna wersja SELECT (median-of-medians).
    """
    if len(A) <= 5:
        return sorted(A)[i - 1]
    groups = [sorted(A[j:j+5]) for j in range(0, len(A), 5)]
    medians = [group[len(group)//2] for group in groups]
    pivot = deterministic_select(medians, len(medians)//2 + 1)
    lows = [x for x in A if x < pivot]
    highs = [x for x in A if x > pivot]
    k = len(lows) + 1
    if i == k:
        return pivot
    elif i < k:
        return deterministic_select(lows, i)
    else:
        return deterministic_select(highs, i - k)

def quicksort_with_select(A):
    """
    Quicksort z deterministycznym wyborem pivota przez SELECT.
    """
    if len(A) <= 1:
        return A
    pivot = deterministic_select(A, len(A)//2 + 1)
    left = [x for x in A if x < pivot]
    right = [x for x in A if x > pivot]
    middle = [x for x in A if x == pivot]
    return quicksort_with_select(left) + middle + quicksort_with_select(right)

if __name__ == "__main__":
    A = [3, 2, 9, 0, 7, 5, 4, 8, 6, 1]
    sorted_A = quicksort_with_select(A)
    print("Posortowana tablica:", sorted_A)
