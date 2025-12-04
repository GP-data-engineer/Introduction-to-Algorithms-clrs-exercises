# Exercise 9.3.7 (EN): Find k-th to (k+m)-th smallest elements in linear time in m.
# Exercise 9.3.7 (PL): Wyznacz k-ty do (k+m)-ty najmniejszy element w czasie liniowym względem m.

def select_range(A, k, m):
    # Zwraca k-ty do k+m-ty najmniejszy element
    sorted_A = sorted(A)
    return sorted_A[k - 1:k + m]

if __name__ == "__main__":
    A = [3, 2, 9, 0, 7, 5, 4, 8, 6, 1]
    k, m = 3, 4
    result = select_range(A, k, m)
    print(f"Elementy od {k}-tego do {k+m}-tego najmniejszego:", result)