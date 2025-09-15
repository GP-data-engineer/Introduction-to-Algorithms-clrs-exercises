"""
Exercise 4.2-1
Use Strassen's algorithm to multiply two 2x2 matrices.
"""

from typing import List


def strassen_2x2(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    """
    Performs Strassen's multiplication for 2x2 matrices.
    """
    a, b, c, d = A[0][0], A[0][1], A[1][0], A[1][1]
    e, f, g, h = B[0][0], B[0][1], B[1][0], B[1][1]

    # Strassen's formulas
    p1 = a * (f - h)
    p2 = (a + b) * h
    p3 = (c + d) * e
    p4 = d * (g - e)
    p5 = (a + d) * (e + h)
    p6 = (b - d) * (g + h)
    p7 = (a - c) * (e + f)

    # Result matrix
    return [
        [p5 + p4 - p2 + p6, p1 + p2],
        [p3 + p4, p1 + p5 - p3 - p7]
    ]


if __name__ == "__main__":
    A = [[13, 5], [75, 42]]
    B = [[8, 4], [7, 6]]
    result = strassen_2x2(A, B)
    print("Result of Strassen 2x2 multiplication:", result)
