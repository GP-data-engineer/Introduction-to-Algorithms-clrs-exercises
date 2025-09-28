"""
Exercise 5.2.3
English: Use indicator random variables to compute expected number of hires.
Polish: Zastosuj zmienne losowe wskaźnikowe do obliczenia wartości oczekiwanej liczby zatrudnionych osób.
"""

# Polish description:
# Oczekiwana liczba zatrudnionych = H_n (n-ta liczba harmoniczna).

def expected_hires(n: int):
    return sum(1 / k for k in range(1, n+1))

if __name__ == "__main__":
    print("Exercise 5.2.3 Result:")
    print("Expected hires for n=5:", expected_hires(5))
