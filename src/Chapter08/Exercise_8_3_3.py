# Exercise_8_3_3.py
# PL:
# Zadanie 8.3-3:
# Udowodnij przez indukcję poprawność sortowania pozycyjnego (radix sort) korzystając ze stabilnego sortowania pomocniczego.
# W którym miejscu dowodu potrzebne jest założenie, że pomocniczy algorytm sortowania jest stabilny?
#
# EN:
# Exercise 8.3-3:
# Prove by induction the correctness of positional (radix) sorting when using a stable sort as a subroutine.
# Identify the step where stability is required.
#
# Implementacja:
# - provide a textual proof string (PL/EN) and a small verifier that demonstrates correctness for random examples
#   by comparing radix sort (LSD) using a stable counting sort with Python's sorted (lexicographic).
# - verify_stability_dependency: returns True if changing stable->unstable helper can break correctness on a crafted input.
#
# Note: this is a computational illustration of the induction argument, and a demonstration that stability is necessary.

from typing import List, Tuple
import random

def proof_text() -> str:
    return (
        "Proof (sketch, EN):\n"
        "LSD radix sort applies a stable sort on the least significant digit, "
        "then on the next, and so on up to the most significant digit. "
        "Induction on number of digits m:\n"
        "Base m=1: stable sort by single digit yields correct ordering.\n"
        "Inductive step: assume LSD on m-1 digits yields array sorted by last m-1 digits. "
        "When we stably sort by the m-th (next) digit, items with equal m-th digit keep relative order "
        "established by previous passes (sorted by lower-order digits). Thus after this pass the array "
        "is sorted by m digits. Stability is used exactly at this step: to preserve order among equal keys.\n"
        "\nPL (sketch):\n"
        "Sortowanie LSD stosuje stabilne sortowanie po kolejnych pozycjach od najmniej znaczącej do najbardziej. "
        "Indukcyjnie: dla m=1 OK. Jeśli dla m-1 działa, to stabilne posortowanie po m-tej pozycji zachowa porządek "
        "dla elementów mających tę samą m-tą cyfrę, a więc całość będzie posortowana. Założenie stabilności jest "
        "użyte przy przejściu indukcyjnym, przy ostatnim sortowaniu — aby nie zniszczyć porządku według niższych pozycji."
    )

def radix_lsd_with_stable_counting(nums: List[int], base: int, width: int) -> List[int]:
    """
    Generic LSD radix for integers represented in 'width' digits base 'base'.
    Uses stable counting sort for each digit (implemented stably).
    """
    A = list(nums)
    for d in range(width):
        # stable counting sort by digit d (0=least significant)
        buckets = [[] for _ in range(base)]
        for x in A:
            digit = (x // (base ** d)) % base
            buckets[digit].append(x)  # append preserves previous order -> stable
        A = [x for bucket in buckets for x in bucket]
    return A

def verify_random_examples(trials: int = 100):
    """
    Verify that radix_lsd_with_stable_counting matches Python's sorted for random lists
    formatted as base^width numbers -> compare lexicographic on digit tuples.
    """
    random.seed(0)
    for _ in range(trials):
        base = random.randint(2, 10)
        width = random.randint(1, 4)
        n = random.randint(0, 50)
        max_val = base ** width - 1
        arr = [random.randint(0, max_val) for _ in range(n)]
        sorted_by_radix = radix_lsd_with_stable_counting(arr, base, width)
        # sort by tuple of digits (most significant first) to simulate natural number order
        def key_num(x):
            return tuple((x // (base ** d)) % base for d in reversed(range(width)))
        assert sorted_by_radix == sorted(arr, key=key_num)
    return True

def verify_stability_dependency_example() -> bool:
    """
    Construct small example where unstable sorting on a digit would break correctness.
    We'll simulate an unstable 'counting' by reversing placement order.
    """
    # craft base=10 width=2 numbers where instability will swap lower-order order
    # Example: numbers with digits: [ (1,0,a), (1,0,b) ] where a,b are lower-order sorts; if unstable on higher digit, can break
    nums = [10 + 1, 10 + 2, 20 + 1, 20 + 2]  # digits: (1,1),(1,2),(2,1),(2,2)
    # stable radix gives [11,12,21,22]
    ok_stable = radix_lsd_with_stable_counting(nums, base=10, width=2)
    # simulate unstable pass on most significant digit: emulate a counting sort that places elements left-to-right but uses last-to-first placement reversed
    A = nums.copy()
    # first pass by least significant digit (stable)
    buckets = [[] for _ in range(10)]
    for x in A:
        buckets[(x // 1) % 10].append(x)
    A = [x for b in buckets for x in b]
    # now unstable "most significant" pass: instead of appending to buckets in order, we prepend to bucket (unstable)
    buckets2 = [[] for _ in range(10)]
    for x in A:
        idx = (x // 10) % 10
        buckets2[idx].insert(0, x)  # PREPEND -> reverses relative order, unstable
    A_unstable = [x for b in buckets2 for x in b]
    return ok_stable != A_unstable  # True if instability changed result

if __name__ == "__main__":
    print(proof_text())
    print("Running random verification (should return True):", verify_random_examples(50))
    print("Stability dependency example shows instability can break correctness:", verify_stability_dependency_example())
