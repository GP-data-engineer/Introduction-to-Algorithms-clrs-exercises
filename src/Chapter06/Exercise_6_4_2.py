"""
Exercise 6.4-2
English: Justify correctness of HEAPSORT using the loop invariant:
At the start of each iteration of the for loop, A[1..i] is a max-heap containing i smallest elements.
Polish: Uzasadnij poprawność HEAPSORT, korzystając z niezmiennika pętli:
Na początku każdej iteracji pętli for, A[1..i] jest kopcem max zawierającym i najmniejszych elementów.
"""

def heapsort_correctness():
    return "Correctness follows from loop invariant: each iteration maintains max-heap property and places next largest element at the end."

if __name__ == "__main__":
    print("Exercise 6.4-2 Result:")
    print(heapsort_correctness())
