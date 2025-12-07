# Exercise 9.3.9 (EN): Find median of two sorted arrays of size n in O(log n).
# Exercise 9.3.9 (PL): Wyznacz medianę dwóch posortowanych tablic o rozmiarze n w czasie O(log n).

def find_median_sorted_arrays(X, Y):
    # Zakładamy X i Y są posortowane i mają ten sam rozmiar
    def helper(x, y):
        if len(x) == 1:
            return min(max(x[0], y[0]), max(x[0], y[-1]))
        mid = len(x) // 2
        if x[mid] < y[mid]:
            return helper(x[mid:], y[:len(y)-mid])
        else:
            return helper(x[:len(x)-mid], y[mid:])
    return helper(X, Y)

if __name__ == "__main__":
    X = [1, 3, 5, 7, 9]
    Y = [2, 4, 6, 8, 10]
    median = find_median_sorted_arrays(X, Y)
    print("Mediana dwóch tablic:", median)