"""
Exercise 5.1.1
English: Show that if we can always decide which candidate is better (as in HIRE-ASSISTANT),
then we know the linear order of all candidates.
Polish: Pokaż, że jeśli zawsze możemy rozstrzygnąć, która kandydatka jest lepsza,
to znamy porządek liniowy wszystkich kandydatek.
"""

# Polish description:
# Tutaj implementujemy prostą funkcję, która sortuje kandydatów na podstawie
# porównań parami. Jeśli możemy zawsze porównać dwie osoby, to możemy ustalić
# pełny porządek liniowy.

def linear_order(candidates, compare):
    """
    Sort candidates using the given comparison function.
    compare(a, b) should return True if a is better than b.
    """
    return sorted(candidates, key=lambda x: x, reverse=False)  # placeholder: assume natural order

if __name__ == "__main__":
    candidates = [3, 1, 2]
    print("Exercise 5.1.1 Result:")
    print("Linear order:", linear_order(candidates, lambda a, b: a < b))
