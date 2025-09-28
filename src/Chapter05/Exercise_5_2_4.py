"""
Exercise 5.2.4
English: Random permutation hat-check problem. Expected number of people
who get their own hat back.
Polish: Problem roztargnionego szatniarza. Oczekiwana liczba osób,
które odzyskają swój kapelusz.
"""

# Polish description:
# Każda osoba ma prawdopodobieństwo 1/n odzyskania swojego kapelusza.
# Oczekiwana liczba = 1.

def expected_fixed_points(n: int):
    return 1

if __name__ == "__main__":
    print("Exercise 5.2.4 Result:")
    print("Expected number of fixed points (n=10):", expected_fixed_points(10))
