# Exercise 9.3.6 (EN): After finding the i-th smallest element, extract i−1 smallest and n−i largest without extra comparisons.
# Exercise 9.3.6 (PL): Po znalezieniu i-tego najmniejszego elementu, wyznacz i−1 najmniejszych i n−i największych bez dodatkowych porównań.

def partition_by_known_element(A, pivot):
    # Dzieli tablicę względem znanego elementu pivot
    smaller = [x for x in A if x < pivot]
    equal = [x for x in A if x == pivot]
    greater = [x for x in A if x > pivot]
    return smaller, equal, greater

if __name__ == "__main__":
    A = [3, 2, 9, 0, 7, 5, 4, 8, 6, 1]
    i = 5
    pivot = sorted(A)[i - 1]
    smaller, equal, greater = partition_by_known_element(A, pivot)
    print(f"{i}-ty najmniejszy element to: {pivot}")
    print("i−1 najmniejszych:", smaller)
    print("n−i największych:", greater)