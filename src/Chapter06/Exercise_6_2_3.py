"""
Exercise 6.2-3
English: What happens if MAX-HEAPIFY(A, i) is called when A[i] is larger than its children?
Polish: Jaki jest skutek wywołania MAX-HEAPIFY(A, i), gdy A[i] jest większy niż jego synowie?
"""

def max_heapify_no_change():
    return "No change, heap property already satisfied."

if __name__ == "__main__":
    print("Exercise 6.2-3 Result:")
    print(max_heapify_no_change())
