"""
Exercise 6.1-1
English: Give the maximum and minimum number of elements in a heap of height h.
Polish: Podaj największą i najmniejszą możliwą liczbę elementów w kopcu o wysokości h.
"""

# Polish description:
# Minimalna liczba elementów w kopcu wysokości h = 2^h.
# Maksymalna liczba elementów = 2^(h+1) - 1.

def heap_elements_range(h: int):
    min_elems = 2**h
    max_elems = 2**(h+1) - 1
    return min_elems, max_elems

if __name__ == "__main__":
    print("Exercise 6.1-1 Result:")
    print("Range for h=3:", heap_elements_range(3))
