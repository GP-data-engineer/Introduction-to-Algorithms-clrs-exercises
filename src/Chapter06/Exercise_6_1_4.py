"""
Exercise 6.1-4
English: Where is the minimum element in a max-heap (all elements distinct)?
Polish: Gdzie w kopcu typu max można znaleźć element najmniejszy (przy różnych elementach)?
"""

# Polish description:
# Najmniejszy element w max-heapie musi znajdować się w liściach.

def min_in_max_heap_location():
    return "Leaves"

if __name__ == "__main__":
    print("Exercise 6.1-4 Result:")
    print("Minimum element is in:", min_in_max_heap_location())
