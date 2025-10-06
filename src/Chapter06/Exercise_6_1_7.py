"""
Exercise 6.1-7
English: Show that in array representation of an n-element heap,
the leaves are at indices floor(n/2)+1 ... n.
Polish: Pokaż, że w tablicowej reprezentacji kopca n-elementowego liście są na pozycjach
⌊n/2⌋+1 ... n.
"""

def leaf_indices(n: int):
    return list(range(n//2 + 1, n+1))

if __name__ == "__main__":
    print("Exercise 6.1-7 Result:")
    print("Leaf indices for n=10:", leaf_indices(10))
