"""
Zadanie 8.4.5 (PL): Sortuj n zmiennych losowych zgodnie z jednostajnym rozkładem o ciągłej dystrybuancie P(x), którą można obliczyć w czasie Θ(1). Algorytm powinien działać w czasie średnim Θ(n).

Exercise 8.4.5 (EN): Sort n random variables drawn from a uniform distribution with continuous CDF P(x), computable in Θ(1). The algorithm should run in average-case Θ(n) time.
"""

def bucket_sort_uniform(values):
    """
    Sortowanie zmiennych losowych z jednostajnego rozkładu [0,1] w czasie liniowym.
    """
    n = len(values)
    buckets = [[] for _ in range(n)]

    for x in values:
        index = min(n - 1, int(x * n))  # Skalowanie do koszyka
        buckets[index].append(x)

    sorted_values = []
    for bucket in buckets:
        sorted_values.extend(sorted(bucket))

    return sorted_values

if __name__ == "__main__":
    import random
    random.seed(123)
    values = [random.uniform(0, 1) for _ in range(20)]
    sorted_vals = bucket_sort_uniform(values)
    print("Posortowane wartości zmiennych losowych:")
    print(sorted_vals)
