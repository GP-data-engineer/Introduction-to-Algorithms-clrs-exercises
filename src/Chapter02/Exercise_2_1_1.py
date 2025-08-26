"""
Exercise 2.1-1 (CLRS) — stub

Add a short paraphrase of the task here.
Source of index: MIT Press, "Selected Solutions", pp. 82–83.
PDF: https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/11599/selected-solutions.pdf
"""

"""
Exercise 2.1-1 (CLRS)
Implementation of INSERTION-SORT for an array A = (31, 41, 59, 26, 41, 58)
"""

def solve():
    A = [31, 41, 59, 26, 41, 58]
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
    return A

if __name__ == "__main__":
    print(solve())
