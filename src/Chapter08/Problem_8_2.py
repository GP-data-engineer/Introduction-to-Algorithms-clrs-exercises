"""
Problem 8-2 (EN): In-place linear-time sorting of records with keys 0 or 1.
Problem 8-2 (PL): Sortowanie w miejscu w czasie liniowym rekordów o kluczach 0 lub 1.
"""

def in_place_binary_sort(arr):
    """
    Sortuje tablicę zawierającą tylko 0 i 1 w miejscu i w czasie O(n).
    """
    left = 0
    for right in range(len(arr)):
        if arr[right] == 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
    return arr

if __name__ == "__main__":
    example = [1, 0, 1, 0, 0, 1, 1, 0]
    print("Wejściowa tablica:", example)
    sorted_arr = in_place_binary_sort(example)
    print("Posortowana tablica:", sorted_arr)
