"""
Exercise 5.3-6
English: Explain how to implement PERMUTE-BY-SORTING so that it handles duplicate priorities
and still produces a uniform random permutation.
Polish: Wyjaśnij, jak zaimplementować PERMUTE-BY-SORTING tak, aby radził sobie z powtarzającymi się
priorytetami i nadal generował losową permutację zgodnie z rozkładem jednostajnym.
"""

# Polish description:
# Standardowy PERMUTE-BY-SORTING losuje priorytety i sortuje tablicę.
# Jeśli priorytety się powtarzają, trzeba rozstrzygać remisy losowo.
# Dzięki temu każda permutacja ma jednakowe prawdopodobieństwo.

import random

def permute_by_sorting(A):
    n = len(A)
    # Assign random priorities
    priorities = [(random.random(), i) for i in range(n)]
    # Sort by priority, break ties randomly by index
    priorities.sort(key=lambda x: (x[0], random.random()))
    return [A[i] for (_, i) in priorities]

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print("Exercise 5.3-6 Result:")
    print("Random permutation:", permute_by_sorting(arr))
