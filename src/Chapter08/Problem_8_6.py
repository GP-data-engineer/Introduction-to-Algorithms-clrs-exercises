"""
Problem 8.6 (EN): Analyze the lower bound for merging two sorted lists of size n using comparisons.
Problem 8.6 (PL): Analiza dolnej granicy dla scalania dwóch posortowanych list o rozmiarze n za pomocą porównań.
"""

from math import comb, log2

def merge_sorted_lists(A, B):
    """
    Scala dwie posortowane listy A i B w jedną listę C.
    Zlicza liczbę porównań wykonanych podczas scalania.
    """
    i = j = 0
    comparisons = 0
    C = []

    while i < len(A) and j < len(B):
        comparisons += 1
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1

    C.extend(A[i:])
    C.extend(B[j:])
    return C, comparisons

def theoretical_lower_bound(n):
    """
    Oblicza dolną granicę liczby porównań potrzebnych do scalenia dwóch list o rozmiarze n.
    Bazuje na liczbie możliwych podziałów: (2n choose n).
    """
    return log2(comb(2 * n, n))

if __name__ == "__main__":
    A = [1, 3, 5, 7]
    B = [2, 4, 6, 8]
    merged, cmp = merge_sorted_lists(A, B)
    print("Scalona lista:", merged)
    print("Liczba porównań:", cmp)
    print("Teoretyczna dolna granica:", round(theoretical_lower_bound(len(A)), 2))
