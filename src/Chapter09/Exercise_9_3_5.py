# Exercise 9.3-5 (EN): Use a black-box median algorithm to find any order statistic in linear time.
# Exercise 9.3-5 (PL): Użyj algorytmu mediany jako czarnej skrzynki, aby wyznaczyć dowolną statystykę pozycyjną w czasie liniowym.

def black_box_median(A):
    # Symulowana czarna skrzynka — mediana w czasie liniowym
    return sorted(A)[len(A) // 2]

def order_statistic_via_median_box(A, k):
    # Wyznacza k-tą statystykę pozycyjną używając czarnej skrzynki mediany
    if len(A) <= 5:
        return sorted(A)[k - 1]
    pivot = black_box_median(A)
    lows = [x for x in A if x < pivot]
    highs = [x for x in A if x > pivot]
    equals = [x for x in A if x == pivot]
    if k <= len(lows):
        return order_statistic_via_median_box(lows, k)
    elif k <= len(lows) + len(equals):
        return pivot
    else:
        return order_statistic_via_median_box(highs, k - len(lows) - len(equals))

if __name__ == "__main__":
    A = [3, 2, 9, 0, 7, 5, 4, 8, 6, 1]
    k = 4
    result = order_statistic_via_median_box(A, k)
    print(f"{k}-ta statystyka pozycyjna to:", result)
