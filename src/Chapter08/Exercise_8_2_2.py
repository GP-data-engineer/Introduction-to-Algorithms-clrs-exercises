# Exercise_8_2_2.py
# PL:
# Zadanie 8.2-2: Udowodnij, że procedura COUNTING-SORT sortuje stabilnie.
#
# EN:
# Exercise 8.2-2: Prove that COUNTING-SORT is stable.
#
# Implementacja:
# - counting_sort_stable(A, k): stabilna implementacja COUNTING-SORT, pracuje na parach (key, value).
# - is_stable: test stabilności na przykładzie listy par (key, original_index).
#   Jeśli stable, sort zachowuje porządek elementów o tych samych kluczach.

from typing import List, Tuple

def counting_sort_stable(A: List[Tuple[int, object]], k: int) -> List[Tuple[int, object]]:
    """
    Stable counting sort for list of pairs (key, payload).
    Preserves relative order of equal keys.
    """
    n = len(A)
    C = [0] * (k + 1)
    # Count keys
    for key, _ in A:
        C[key] += 1
    # Prefix sums
    for i in range(1, k + 1):
        C[i] += C[i - 1]
    B = [None] * n
    # Place elements right-to-left to preserve stability (CLRS)
    for j in range(n - 1, -1, -1):
        key, payload = A[j]
        C[key] -= 1
        B[C[key]] = (key, payload)
    return B

def is_stable_counting_sort(A_keys: List[int], k: int) -> bool:
    """
    Build list of (key, original_index), sort with counting_sort_stable and
    verify that for equal keys indices are nondecreasing in output.
    """
    A = [(key, idx) for idx, key in enumerate(A_keys)]
    B = counting_sort_stable(A, k)
    # For output, extract for each key the list of original indices
    from collections import defaultdict
    groups = defaultdict(list)
    for key, idx in B:
        groups[key].append(idx)
    # check monotonicity of indices per key
    for key, idxs in groups.items():
        if idxs != sorted(idxs):
            return False
    return True

if __name__ == "__main__":
    # Example demonstrating stability
    keys = [2, 5, 3, 2, 3, 5, 2]
    k = max(keys)
    print("Input keys with indices:", list(enumerate(keys)))
    print("Stable sort preserves original order among equal keys:",
          is_stable_counting_sort(keys, k))
