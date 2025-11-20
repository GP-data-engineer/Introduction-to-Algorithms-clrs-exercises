# Exercise 9.2-3 (EN): Implement an iterative version of the RANDOMIZED-SELECT algorithm.
# Exercise 9.2-3 (PL): Zaimplementuj iteracyjną wersję algorytmu RANDOMIZED-SELECT.

import random

def randomized_partition(A, low, high):
    # Losowy wybór pivota i podział tablicy
    pivot_index = random.randint(low, high)
    A[pivot_index], A[high] = A[high], A[pivot_index]
    pivot = A[high]
    i = low - 1
    for j in range(low, high):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[high] = A[high], A[i + 1]
    return i + 1

def randomized_select_iterative(A, i):
    # Iteracyjna wersja RANDOMIZED-SELECT
    low = 0
    high = len(A) - 1
    while low <= high:
        q = randomized_partition(A, low, high)
        k = q - low + 1
        if i == k:
            return A[q]
        elif i < k:
            high = q - 1
        else:
            low = q + 1
            i -= k

if __name__ == "__main__":
    A = [3, 2, 9, 0, 7, 5, 4, 8, 6, 1]
    i = 1
    result = randomized_select_iterative(A.copy(), i)
    print(f"{i}-ty najmniejszy element to:", result)
