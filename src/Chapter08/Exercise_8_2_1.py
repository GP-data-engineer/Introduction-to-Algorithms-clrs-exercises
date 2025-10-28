# Exercise_8_2_1.py
# PL:
# Zadanie 8.2-1: Zilustruj działanie procedury COUNTING-SORT dla tablicy
# A = <6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2>.
#
# EN:
# Exercise 8.2-1: Illustrate the operation of COUNTING-SORT on array
# A = <6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2>.
#
# Implementacja:
# - counting_sort_with_trace(A, k) zwraca (B, C, trace) gdzie:
#   B = posortowana tablica,
#   C = tablica zliczeń (prefix sums),
#   trace = lista snapshotów (C oraz B) w kluczowych krokach (użyteczna do ilustracji).
# - Funkcja demonstracyjna w __main__ drukuje kroki.

from typing import List, Tuple

def counting_sort_with_trace(A: List[int], k: int) -> Tuple[List[int], List[int], List[Tuple[List[int], List[int]]]]:
    """
    Counting sort with trace for illustration.
    A: input list of integers in range 0..k
    k: maximum value
    Returns:
      B: sorted output list
      C: count prefix-sum array (length k+1)
      trace: snapshots capturing C and B at important moments
    """
    n = len(A)
    C = [0] * (k + 1)
    trace = []

    # 1) Count occurrences
    for a in A:
        C[a] += 1
    trace.append((C.copy(), []))  # after counting, before prefix

    # 2) Compute prefix sums
    total = 0
    for i in range(k + 1):
        total += C[i]
        C[i] = total
    trace.append((C.copy(), []))  # after prefix sums

    # 3) Build output array B (iterate right-to-left as in CLRS)
    B = [0] * n
    for j in range(n - 1, -1, -1):
        v = A[j]
        C[v] -= 1
        B[C[v]] = v
        # record snapshot occasionally (each placement)
        trace.append((C.copy(), B.copy()))
    return B, C, trace

if __name__ == "__main__":
    A = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
    k = max(A)
    B, C, trace = counting_sort_with_trace(A, k)
    print("Input A:", A)
    print("Final sorted B:", B)
    print("Final counts C (prefix sums):", C)
    print("\nTrace snapshots (showing some steps):")
    # print only first 2 and last 3 snapshots for readability
    for idx, (c_snapshot, b_snapshot) in enumerate(trace[:2] + trace[-3:]):
        print(f"Step {idx+1}: C={c_snapshot}, B={b_snapshot}")
