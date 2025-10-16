"""
Exercise 7.2-3
English: Show that QUICKSORT runs in Θ(n^2) if input is already sorted ascending.
Polish: Pokaż, że QUICKSORT działa w Θ(n^2), gdy dane wejściowe są już posortowane rosnąco.
"""

def quicksort_sorted_input():
    return "Θ(n^2) when pivot is always first/last element on sorted input."

if __name__ == "__main__":
    print("Exercise 7.2-3 Result:", quicksort_sorted_input())
