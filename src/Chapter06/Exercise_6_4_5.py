"""
Exercise 6.4-5
English: Show that if all elements are distinct, the optimistic case of HEAPSORT is still Ω(n log n).
Polish: Pokaż, że jeśli wszystkie elementy są różne, to czas działania HEAPSORT w przypadku optymistycznym wynosi Ω(n log n).
"""

def heapsort_best_case():
    return "Even in best case with distinct elements, HEAPSORT is Ω(n log n) due to repeated heapify calls."

if __name__ == "__main__":
    print("Exercise 6.4-5 Result:")
    print(heapsort_best_case())
