"""
Exercise 6.4-3
English: What is the running time of HEAPSORT for an array already sorted ascending (descending)?
Polish: Jaki jest czas działania HEAPSORT dla tablicy posortowanej rosnąco (malejąco)?
"""

# Polish description:
# Niezależnie od początkowego porządku, HEAPSORT zawsze działa w Θ(n log n).

def heapsort_time_sorted():
    return "Θ(n log n) regardless of ascending or descending input."

if __name__ == "__main__":
    print("Exercise 6.4-3 Result:")
    print(heapsort_time_sorted())
