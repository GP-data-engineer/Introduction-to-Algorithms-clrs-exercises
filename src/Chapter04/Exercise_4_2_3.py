"""
Exercise 4.2-3
Modify Strassen's algorithm to handle n not being a power of 2 by padding matrices.
"""

from typing import List
from src.Chapter04.Exercise_4_2_2 import strassen


def pad_matrix(A: List[List[int]], size: int) -> List[List[int]]:
    """
    Pad a square matrix with zeros to reach the given size.
    """
    n = len(A)
    padded = []
    for i in range(size):
        if i < n:
            padded.append(A[i] + [0] * (size - n))
        else:
            padded.append([0] * size)
    return padded


def strassen_with_padding(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    """
    Strassen's algorithm with zero-padding for non-power-of-2 sizes.
    Works for square matrices of the same size.
    """
    if len(A) != len(B) or any(len(row) != len(A) for row in A) or any(len(row) != len(B) for row in B):
        raise ValueError("Both matrices must be square and of the same size")

    n = len(A)
    # Find the next power of 2 greater than or equal to n
    m = 1
    while m < n:
        m *= 2

    # If already power of 2, no need to pad
    if m == n:
        return strassen(A, B)

    # Pad matrices
    A_pad = pad_matrix(A, m)
    B_pad = pad_matrix(B, m)

    # Multiply using Strassen
    C_pad = strassen(A_pad, B_pad)

    # Remove padding
    return [row[:n] for row in C_pad[:n]]


if __name__ == "__main__":
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    print("Strassen with padding result:", strassen_with_padding(A, B))
