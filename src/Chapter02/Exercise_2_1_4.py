"""
Exercise 2.1-4

Task:
Given two n-bit binary integers stored in two n-element arrays A and B,
compute their sum and store the result in an (n+1)-element array C.

Each element of A and B contains a single bit (0 or 1), with the most
significant bit at index 0.

Write a procedure in pseudocode and implement it in Python.
"""

from typing import List

def add_binary_integers(A: List[int], B: List[int]) -> List[int]:
    """
    Adds two n-bit binary integers represented as lists of bits.

    Args:
        A (List[int]): First binary number as a list of bits (MSB at index 0).
        B (List[int]): Second binary number as a list of bits (MSB at index 0).

    Returns:
        List[int]: (n+1)-element list representing the binary sum.
    """
    n = len(A)
    C = [0] * (n + 1)
    carry = 0

    for i in range(n - 1, -1, -1):
        total = A[i] + B[i] + carry
        C[i + 1] = total % 2
        carry = total // 2

    C[0] = carry
    return C
