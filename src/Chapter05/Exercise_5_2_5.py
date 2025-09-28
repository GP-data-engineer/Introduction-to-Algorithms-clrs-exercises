"""
Exercise 5.2.5
English: Expected number of inversions in a random permutation of n elements.
Polish: Oczekiwana liczba inwersji w losowej permutacji n elementów.
"""

# Polish description:
# Każda para (i,j) ma prawdopodobieństwo 1/2 bycia inwersją.
# Liczba par = n(n-1)/2, więc oczekiwana liczba inwersji = n(n-1)/4.

def expected_inversions(n: int):
    return n * (n - 1) / 4

if __name__ == "__main__":
    print("Exercise 5.2.5 Result:")
    print("Expected inversions for n=5:", expected_inversions(5))
