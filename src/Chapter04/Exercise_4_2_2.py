"""
Exercise 4.2-2
Pseudocode implementation of Strassen's algorithm for n x n matrices (n is a power of 2).
"""

from typing import List


def add_matrix(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    """Add two matrices."""
    return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]


def sub_matrix(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    """Subtract two matrices."""
    return [[A[i][j] - B[i][j] for j in range(len(A))] for i in range(len(A))]


def strassen(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    """Recursive Strassen's algorithm."""
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2
    # Split matrices into quadrants
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    # Strassen's formulas
    M1 = strassen(add_matrix(A11, A22), add_matrix(B11, B22))
    M2 = strassen(add_matrix(A21, A22), B11)
    M3 = strassen(A11, sub_matrix(B12, B22))
    M4 = strassen(A22, sub_matrix(B21, B11))
    M5 = strassen(add_matrix(A11, A12), B22)
    M6 = strassen(sub_matrix(A21, A11), add_matrix(B11, B12))
    M7 = strassen(sub_matrix(A12, A22), add_matrix(B21, B22))

    # Combine results
    C11 = add_matrix(sub_matrix(add_matrix(M1, M4), M5), M7)
    C12 = add_matrix(M3, M5)
    C21 = add_matrix(M2, M4)
    C22 = add_matrix(sub_matrix(add_matrix(M1, M3), M2), M6)

    # Merge quadrants
    C = [C11[i] + C12[i] for i in range(mid)] + [C21[i] + C22[i] for i in range(mid)]
    return C


if __name__ == "__main__":
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    print("Strassen multiplication result:", strassen(A, B))
