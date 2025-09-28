"""
Problem 4-6
Monge arrays.

Tasks:
(a) Prove that a matrix is a Monge array if and only if the inequality
    A[i,j] + A[i+1,j+1] <= A[i,j+1] + A[i+1,j] holds for all valid i,j.
(b) Verify if a given matrix is a Monge array.
(c) Show that the column indices of leftmost minima in each row are non-decreasing.
(d) Explain how to compute leftmost minima in odd rows using only m+n comparisons.
(e) Provide recurrence for the divide-and-conquer algorithm and solve it: O(m + n log m).
"""

# Polish description:
# Ten plik zawiera implementację sprawdzania tablicy Monge’a oraz pomocnicze funkcje
# do analizy własności (a)-(e). Funkcje zwracają wyniki w postaci stringów lub wartości logicznych.

from typing import List

def is_monge_matrix(matrix: List[List[int]]) -> bool:
    """Check if a matrix is a Monge array using the local condition (a)."""
    m, n = len(matrix), len(matrix[0])
    for i in range(m - 1):
        for j in range(n - 1):
            if matrix[i][j] + matrix[i+1][j+1] > matrix[i][j+1] + matrix[i+1][j]:
                return False
    return True

def part_a_explanation():
    return "A matrix is Monge iff local 2x2 condition holds for all i,j."

def part_b_example(matrix: List[List[int]]):
    return is_monge_matrix(matrix)

def part_c_explanation():
    return "In a Monge array, leftmost minima indices are non-decreasing across rows."

def part_d_explanation():
    return "Odd-row minima can be found using m+n comparisons by restricting search to neighbor columns."

def part_e_explanation():
    return "Recurrence: T(m,n) = T(m/2,n) + O(m+n). Solution: O(m + n log m)."

if __name__ == "__main__":
    example_matrix = [
        [10, 17, 13, 28, 23],
        [17, 22, 16, 29, 23],
        [24, 28, 22, 34, 24],
        [11, 13, 6, 17, 7]
    ]
    print("Problem 4-6 Results:")
    print("a:", part_a_explanation())
    print("b: Example matrix is Monge?", part_b_example(example_matrix))
    print("c:", part_c_explanation())
    print("d:", part_d_explanation())
    print("e:", part_e_explanation())
