# Exercise_8_3_1.py
# PL:
# Zadanie 8.3-1: Zilustruj działanie procedury RADIX-SORT dla następującego ciągu
# angielskich słów (treat as fixed-length 3-letter words):
# COW, DOG, SEA, RUG, ROW, MOB, BOX, TAB, BAR, EAR, TAR, DIG, BIG, TEA, NOW, FOX.
#
# EN:
# Exercise 8.3-1: Illustrate RADIX-SORT operation for the following fixed-length 3-letter words:
# COW, DOG, SEA, RUG, ROW, MOB, BOX, TAB, BAR, EAR, TAR, DIG, BIG, TEA, NOW, FOX.
#
# Implementacja:
# - radix_sort_strings_lsd(words, alphabet): LSD radix sort over characters with counting sort as stable subroutine
# - demonstration prints intermediate buckets / steps

from typing import List, Tuple
import string

def char_to_index(c: str, alphabet: str) -> int:
    return alphabet.index(c)

def counting_sort_by_char(words: List[str], pos: int, alphabet: str) -> List[str]:
    """
    Stable counting-sort of words by character at position pos (0-based),
    assumes all words length > pos and alphabet provides index mapping.
    """
    k = len(alphabet)
    n = len(words)
    C = [0] * (k + 1)
    for w in words:
        idx = char_to_index(w[pos], alphabet)
        C[idx] += 1
    # prefix sums
    for i in range(1, k):
        C[i] += C[i - 1]
    B = [None] * n
    # place right-to-left for stability
    for j in range(n - 1, -1, -1):
        idx = char_to_index(words[j][pos], alphabet)
        C[idx] -= 1
        B[C[idx]] = words[j]
    return B

def radix_sort_strings_lsd(words: List[str], alphabet: str) -> Tuple[List[str], List[List[str]]]:
    """
    LSD radix sort for fixed-length strings.
    Returns sorted words and list of snapshots after each digit pass (from least significant to most).
    """
    if not words:
        return [], []
    m = len(words[0])
    for w in words:
        if len(w) != m:
            raise ValueError("All words must have same length for this LSD demo")
    snapshots = []
    A = list(words)
    # iterate from last position to first (LSD -> MSD)
    for pos in range(m - 1, -1, -1):
        A = counting_sort_by_char(A, pos, alphabet)
        snapshots.append((pos, A.copy()))
    return A, snapshots

if __name__ == "__main__":
    words = ["COW","DOG","SEA","RUG","ROW","MOB","BOX","TAB","BAR","EAR","TAR","DIG","BIG","TEA","NOW","FOX"]
    # Use uppercase English letters A-Z as alphabet
    alphabet = "".join(sorted({ch for w in words for ch in w}))
    # Ensure deterministic alphabet order (A..Z) but reduce to used letters for compactness
    alphabet = ''.join(sorted(alphabet))
    sorted_words, snaps = radix_sort_strings_lsd(words, alphabet)
    print("Input words:")
    print(words)
    print("\nAlphabet used:", alphabet)
    print("\nSnapshots (after each LSD pass):")
    for pos, arr in snaps:
        print(f"pos={pos}: {arr}")
    print("\nFinal sorted words:", sorted_words)
