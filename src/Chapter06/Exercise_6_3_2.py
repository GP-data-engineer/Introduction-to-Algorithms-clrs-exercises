"""
Exercise 6.3-2
English: Why does BUILD-MAX-HEAP loop from floor(n/2) down to 1 instead of 1 up to floor(n/2)?
Polish: Dlaczego w BUILD-MAX-HEAP pętla idzie od ⌊n/2⌋ w dół do 1, zamiast od 1 do ⌊n/2⌋?
"""

# Polish description:
# Ponieważ liście nie wymagają heapify, zaczynamy od ostatniego węzła wewnętrznego
# i schodzimy w dół, aby każdy podkopiec był poprawny przed użyciem go wyżej.

def build_heap_loop_reason():
    return "We go from floor(n/2) down to 1 so that children are heapified before parents."

if __name__ == "__main__":
    print("Exercise 6.3-2 Result:")
    print(build_heap_loop_reason())
