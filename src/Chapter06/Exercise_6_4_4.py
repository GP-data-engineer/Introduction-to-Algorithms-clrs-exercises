"""
Exercise 6.4-4
English: Show that worst-case running time of HEAPSORT is Ω(n log n).
Polish: Pokaż, że czas działania HEAPSORT w przypadku pesymistycznym wynosi Ω(n log n).
"""

def heapsort_worst_case():
    return "Worst-case time is Ω(n log n), since each of n extract-max operations costs O(log n)."

if __name__ == "__main__":
    print("Exercise 6.4-4 Result:")
    print(heapsort_worst_case())
