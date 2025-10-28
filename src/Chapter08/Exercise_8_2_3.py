# Exercise_8_2_3.py
# PL:
# Zadanie 8.2-3:
# Zmodyfikujmy pętlę for w wierszu 10 procedury COUNTING-SORT w następujący sposób:
#   for j = 1 to A.length
# Pokaż, że algorytm nadal działa poprawnie. Czy nowa wersja zapewnia stabilność?
#
# EN:
# Exercise 8.2-3:
# Modify the for loop in line 10 of COUNTING-SORT to iterate j = 1 to A.length (left-to-right).
# Show the algorithm still produces a correct permutation, and investigate stability.
#
# Implementacja:
# - counting_sort_left_to_right: version that iterates left-to-right when placing elements.
# - is_stable_left_to_right: test whether that version is stable (it won't be).

from typing import List, Tuple

def counting_sort_left_to_right(A: List[int], k: int) -> List[int]:
    """
    Counting sort placing elements by iterating j from 0..n-1 (left-to-right).
    This still produces a correct sorted permutation but is NOT stable.
    """
    n = len(A)
    C = [0] * (k + 1)
    for a in A:
        C[a] += 1
    # prefix sums
    for i in range(1, k + 1):
        C[i] += C[i - 1]
    B = [None] * n
    # left-to-right placement: for j from 0 to n-1
    for j in range(0, n):
        v = A[j]
        C[v] -= 1
        B[C[v]] = v
    return B

def is_stable_left_to_right(A_keys: List[int], k: int) -> bool:
    """
    Check stability of left-to-right variant using (key, original_index) pairs.
    """
    A = [(key, idx) for idx, key in enumerate(A_keys)]
    # strip payload during sort
    keys = [key for key, _ in A]
    B_vals = counting_sort_left_to_right(keys, k)
    # Now we need to reconstruct which original indices ended up for each equal key.
    # left-to-right variant loses payload, so to test stability we simulate mapping:
    # We emulate placing with copies of original indices using same left-to-right routine.
    # Build C and simulate placements of indices
    n = len(A)
    C = [0] * (k + 1)
    for key, _ in A:
        C[key] += 1
    for i in range(1, k + 1):
        C[i] += C[i - 1]
    positions = [None] * n
    # iterate left-to-right placing original indices
    for key, idx in A:
        C[key] -= 1
        positions[C[key]] = (key, idx)
    # Now for each key check if indices are nondecreasing (stability property)
    from collections import defaultdict
    groups = defaultdict(list)
    for key, idx in positions:
        groups[key].append(idx)
    for idxs in groups.values():
        if idxs != sorted(idxs):
            return False
    return True

if __name__ == "__main__":
    keys = [2, 1, 2, 0, 2, 1]
    k = max(keys)
    B = counting_sort_left_to_right(keys, k)
    print("Input keys:", keys)
    print("Sorted with left-to-right variant:", B)
    print("Is stable (left-to-right)?", is_stable_left_to_right(keys, k))
