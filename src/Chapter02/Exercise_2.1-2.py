"""
Exercise 2.1-2 from "Introduction to Algorithms" (CLRS)
------------------------------------------------------
Task:
Modify the INSERTION-SORT procedure to sort into nonincreasing (descending) order.
"""

def insertion_sort_descending(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] < key:  # odwrócony warunek
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
    return arr


if __name__ == "__main__":
    data = [5, 2, 4, 6, 1, 3]
    print("Original:", data)
    print("Sorted (descending):", insertion_sort_descending(data.copy()))
