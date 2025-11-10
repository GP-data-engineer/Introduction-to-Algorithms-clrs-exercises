"""
Problem 8-3 (EN): Sorting variable-length objects (e.g. integers with different digit lengths).
Problem 8-3 (PL): Sortowanie obiektów zmiennej długości (np. liczb całkowitych o różnej liczbie cyfr).
"""

def radix_sort_decimal(arr):
    """
    Sortuje liczby całkowite w czasie O(n), gdzie n to łączna liczba cyfr.
    Używa sortowania pozycyjnego (radix sort) w systemie dziesiętnym.
    """
    if not arr:
        return []

    max_len = len(str(max(arr)))
    for digit in range(max_len):
        buckets = [[] for _ in range(10)]
        for number in arr:
            digit_value = (number // 10**digit) % 10
            buckets[digit_value].append(number)
        arr = [num for bucket in buckets for num in bucket]
    return arr

def radix_sort_binary_strings(arr):
    """
    Sortuje liczby zapisane jako napisy binarne w porządku leksykograficznym.
    """
    return sorted(arr)

if __name__ == "__main__":
    decimal_numbers = [3, 123, 45, 6, 789, 12]
    binary_strings = ["101", "1", "1000", "011", "010"]

    print("Sortowanie dziesiętne (radix sort):")
    print("Wejście:", decimal_numbers)
    print("Wyjście:", radix_sort_decimal(decimal_numbers))

    print("\nSortowanie binarne leksykograficzne:")
    print("Wejście:", binary_strings)
    print("Wyjście:", radix_sort_binary_strings(binary_strings))
