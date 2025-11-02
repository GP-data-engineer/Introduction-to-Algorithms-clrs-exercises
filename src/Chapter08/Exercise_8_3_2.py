# Exercise_8_3_2.py
# PL:
# Zadanie 8.3-2:
# Które z następujących algorytmów sortowania są stabilne:
# - insertion sort, merge sort, heap sort, quicksort?
# Podaj metodę, która z dowolnego algorytmu sortującego za pomocą porównań
# tworzy stabilny algorytm sortujący. Ile dodatkowej pamięci i czasu wymaga zastosowanie Twojej metody?
#
# EN:
# Exercise 8.3-2:
# Which sorting algorithms are stable: insertion sort, merge sort, heap sort, quicksort?
# Give a method that turns any comparison sort into a stable sort, and state extra memory/time cost.
#
# Implementacja:
# - answers() returns stability booleans and explanation
# - make_stable_by_index(A): decorate-sort-undecorate method (stable) using any underlying comparison sort (here Python's Timsort is stable)
#   shows additional memory O(n) and time overhead O(n).
# - small demo in __main__.

from typing import List, Tuple

def answers() -> dict:
    """
    Return stability answers for the named algorithms.
    insertion sort: stable
    merge sort: stable (if implemented stably)
    heap sort: not stable (typical implementations)
    quicksort: not stable (typical implementations)
    """
    return {
        "insertion_sort": True,
        "merge_sort": True,
        "heap_sort": False,
        "quicksort": False,
        "method": "decorate-with-original-index (stable decorate-sort-undecorate)",
        "extra_memory": "O(n)",
        "extra_time": "O(n) overhead (for decorating/undecorating) + cost of underlying sort"
    }

def make_stable_by_index(A: List[Tuple[object, object]]) -> List[Tuple[object, object]]:
    """
    Generic method: if input is list of keys (or pairs), we decorate each key with its original index,
    sort by (key, original_index) using any comparison sort (Python's sorted is stable),
    then remove indices. This ensures equal keys are ordered by original indices -> stability.
    Returns list of original items sorted stably by their key (first component)
    Expect input as list of (key, payload) or simple keys — we handle both.
    """
    decorated = []
    for idx, item in enumerate(A):
        # interpret item: if it's a pair (key,payload) keep as is, else treat item as key and payload None
        if isinstance(item, tuple) and len(item) >= 1:
            key = item[0]
            payload = item[1] if len(item) > 1 else None
            decorated.append((key, idx, payload))
        else:
            key = item
            decorated.append((key, idx, None))
    # sort by (key, index) — Python sort is stable but index ensures order among equal keys
    decorated.sort(key=lambda x: (x[0], x[1]))
    # undecorate to original format: (key, payload) if payload not None else key
    result = []
    for key, orig_idx, payload in decorated:
        if payload is None:
            result.append(key)
        else:
            result.append((key, payload))
    return result

if __name__ == "__main__":
    print("Stability answers:", answers())
    arr = [(2,'a'), (1,'b'), (2,'c'), (1,'d')]
    stable_sorted = make_stable_by_index(arr)
    print("Original:", arr)
    print("Stable sorted by key:", stable_sorted)
