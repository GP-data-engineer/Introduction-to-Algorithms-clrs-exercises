"""
Exercise 6.1-6
English: Is the sequence <23, 17, 14, 6, 13, 10, 1, 5, 7, 12> a max-heap?
Polish: Czy ciąg <23, 17, 14, 6, 13, 10, 1, 5, 7, 12> jest kopcem typu max?
"""

def is_max_heap(arr):
    n = len(arr)
    for i in range(n//2):
        left = 2*i+1
        right = 2*i+2
        if left < n and arr[i] < arr[left]:
            return False
        if right < n and arr[i] < arr[right]:
            return False
    return True

if __name__ == "__main__":
    seq = [23, 17, 14, 6, 13, 10, 1, 5, 7, 12]
    print("Exercise 6.1-6 Result:")
    print("Is sequence a max-heap?", is_max_heap(seq))
