# Exercise 9.3-1 (EN): Analyze whether SELECT runs in linear time with groups of 7 or 3 elements.
# Exercise 9.3-1 (PL): Przeanalizuj, czy SELECT działa w czasie liniowym dla grup 7 lub 3 elementów.

def select_group_size_analysis(n, group_size):
    """
    Analizuje czy algorytm SELECT działa w czasie liniowym dla danego rozmiaru grupy.
    Zwraca szacunkowy rozmiar podproblemu w rekurencji.
    """
    groups = n // group_size
    median_of_medians = groups // 2
    guaranteed_partition = n - median_of_medians
    return {
        "n": n,
        "group_size": group_size,
        "median_of_medians": median_of_medians,
        "guaranteed_partition_size": guaranteed_partition
    }

if __name__ == "__main__":
    print("Analiza dla grupy 7:")
    print(select_group_size_analysis(140, 7))
    print("\nAnaliza dla grupy 3:")
    print(select_group_size_analysis(140, 3))
