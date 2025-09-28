"""
Problem 4-2
We analyze the cost of parameter passing in recursive algorithms under three strategies:
1. Passing by pointer: Θ(1)
2. Passing by copying the whole array: Θ(N)
3. Passing by copying only the subarray A[i..j]: Θ(size of subarray)

Tasks:
a) Analyze recursive Binary Search.
b) Analyze Merge-Sort.
"""

# Polish description:
# Ten plik zawiera analizę kosztów przekazywania parametrów dla wyszukiwania binarnego
# i Merge-Sort w trzech strategiach: wskaźnik, kopiowanie całej tablicy, kopiowanie podtablicy.

def binary_search_cost(n: int):
    """
    Returns asymptotic costs for recursive Binary Search under three strategies.
    """
    # Binary Search depth = O(log n)
    return {
        "pointer": "Θ(log n)",          # each call passes pointer, cost Θ(1) per call
        "copy_full": "Θ(n)",            # total cost dominated by n + n/2 + ... ≈ 2n
        "copy_subarray": "Θ(n)"         # similar to full copy, sum of subarray sizes ≈ 2n
    }

def merge_sort_cost(n: int):
    """
    Returns asymptotic costs for Merge-Sort under three strategies.
    """
    # Merge-Sort depth = O(log n), total work = O(n log n)
    return {
        "pointer": "Θ(n log n)",        # normal Merge-Sort complexity
        "copy_full": "Θ(n log^2 n)",    # each level copies O(n), log n levels
        "copy_subarray": "Θ(n log n)"   # each level copies subarrays of total size n
    }

if __name__ == "__main__":
    print("Problem 4-2 Results:")
    print("Binary Search Costs:")
    for k, v in binary_search_cost(16).items():
        print(f"  {k}: {v}")
    print("Merge-Sort Costs:")
    for k, v in merge_sort_cost(16).items():
        print(f"  {k}: {v}")
