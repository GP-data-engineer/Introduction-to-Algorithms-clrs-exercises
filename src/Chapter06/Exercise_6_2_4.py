"""
Exercise 6.2-4
English: What happens if MAX-HEAPIFY(A, i) is called for i > A.heap-size/2?
Polish: Jaki jest skutek wywołania MAX-HEAPIFY(A, i) dla i > A.heap-size/2?
"""

def max_heapify_on_leaf():
    return "No effect, since i is a leaf."

if __name__ == "__main__":
    print("Exercise 6.2-4 Result:")
    print(max_heapify_on_leaf())
