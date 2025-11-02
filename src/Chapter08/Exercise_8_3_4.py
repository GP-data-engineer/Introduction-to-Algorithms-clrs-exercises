# Exercise_8_3_4.py
# PL:
# Zadanie 8.3-4:
# Skonstruuj algorytm, który pozwala posortować n liczb całkowitych z przedziału
# 0 .. n^3 - 1 w czasie O(n).
#
# EN:
# Exercise 8.3-4:
# Construct an algorithm to sort n integers in 0..n^3-1 in O(n) time.
#
# Idea / Implementacja:
# Use radix sort with base = n. Each number < n^3 has at most 3 digits in base-n.
# Perform 3 passes of counting sort with k = n (counts array size n) and each pass runs Theta(n + k) = Theta(n).
# Total Theta(3n) = Theta(n).
#
# We'll implement counting sort for digits and the full radix procedure.

from typing import List

def counting_sort_by_digit_base_n(A: List[int], digit_pos: int, base: int) -> List[int]:
    """
    Stable counting sort by digit at position digit_pos (0 = least significant) in base 'base'.
    """
    n = len(A)
    k = base
    C = [0] * k
    for x in A:
        d = (x // (base ** digit_pos)) % base
        C[d] += 1
    for i in range(1, k):
        C[i] += C[i - 1]
    B = [0] * n
    for j in range(n - 1, -1, -1):
        d = (A[j] // (base ** digit_pos)) % base
        C[d] -= 1
        B[C[d]] = A[j]
    return B

def sort_numbers_0_to_n3_minus1(A: List[int]) -> List[int]:
    """
    Sort numbers in 0..n^3 - 1 in Theta(n) time using base = n radix (3 passes).
    """
    n = len(A)
    if n == 0:
        return []
    base = n
    max_val = n**3 - 1
    # Validate inputs are in range
    for x in A:
        if x < 0 or x > max_val:
            raise ValueError("All numbers must be in range 0..n^3-1")
    B = list(A)
    # 3 digit passes: 0,1,2
    for pos in range(3):
        B = counting_sort_by_digit_base_n(B, pos, base)
    return B

if __name__ == "__main__":
    # Demo: create n numbers in range 0..n^3-1, unsort and sort
    n = 50
    import random
    random.seed(0)
    A = [random.randint(0, n**3 - 1) for _ in range(n)]
    sorted_A = sort_numbers_0_to_n3_minus1(A)
    print("n=", n, "sorted correctly?", sorted_A == sorted(A))
