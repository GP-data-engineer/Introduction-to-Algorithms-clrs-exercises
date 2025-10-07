"""
Exercise 6.2-1
English: Illustrate the operation of MAX-HEAPIFY(A, 3) for array 
A = <27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0>.
Polish: Zilustruj działanie MAX-HEAPIFY(A, 3) dla tablicy
A = <27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0>.
"""

# Polish description:
# MAX-HEAPIFY porównuje węzeł z dziećmi i zamienia go z największym.
# Tutaj A[3]=3, dzieci to 16 i 13, więc zamiana z 16, potem dalsze poprawki.

def max_heapify_example():
    A = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
    # Po MAX-HEAPIFY(A,3) wynik:
    return [27, 17, 16, 7, 13, 10, 1, 5, 3, 12, 4, 8, 9, 0]

if __name__ == "__main__":
    print("Exercise 6.2-1 Result:")
    print(max_heapify_example())
