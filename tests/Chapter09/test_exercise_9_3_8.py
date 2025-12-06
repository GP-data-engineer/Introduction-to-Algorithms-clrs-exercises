# Exercise 9.3.8 (EN): Compute k-quantiles in linear time in k.
# Exercise 9.3.8 (PL): Wyznacz k-kwantyle w czasie liniowym względem k.

def compute_k_quantiles(A, k):
    # Zwraca k−1 kwantyli dzielących zbiór na k części
    A_sorted = sorted(A)
    n = len(A)
    quantiles = []
    for i in range(1, k):
        index = (i * n) // k
        quantiles.append(A_sorted[index])
    return quantiles

if __name__ == "__main__":
    A = [3, 2, 9, 0, 7, 5, 4, 8, 6, 1]
    k = 4
    result = compute_k_quantiles(A, k)
    print(f"{k}-kwantyle:", result)