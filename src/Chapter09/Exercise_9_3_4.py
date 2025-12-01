# Exercise 9.3-4 (EN): After finding the i-th smallest element, extract i−1 smallest and n−i largest without extra comparisons.
# Exercise 9.3-4 (PL): Po znalezieniu i-tego najmniejszego elementu, wyznacz i−1 najmniejszych i n−i największych bez dodatkowych porównań.

def extract_extremes_given_ith(A, ith_value):
    # Dzieli tablicę względem znanego i-tego najmniejszego elementu
    smaller = [x for x in A if x < ith_value]
    equal = [x for x in A if x == ith_value]
    greater = [x for x in A if x > ith_value]
    return smaller, equal, greater

if __name__ == "__main__":
    A = [3, 2, 9, 0, 7, 5, 4, 8, 6, 1]
    i = 5
    ith_value = sorted(A)[i - 1]
    smaller, equal, greater = extract_extremes_given_ith(A, ith_value)
    print(f"{i}-ty najmniejszy element to: {ith_value}")
    print("i−1 najmniejszych:", smaller)
    print("n−i największych:", greater)
