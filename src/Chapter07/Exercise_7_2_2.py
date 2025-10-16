"""
Exercise 7.2-2
English: Running time of QUICKSORT when all elements are equal.
Polish: Czas działania QUICKSORT, gdy wszystkie elementy są równe.
"""

def quicksort_equal_elements():
    return "Θ(n^2), because partitioning is always unbalanced."

if __name__ == "__main__":
    print("Exercise 7.2-2 Result:", quicksort_equal_elements())
