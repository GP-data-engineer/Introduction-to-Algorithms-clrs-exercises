"""
Exercise 5.3-3
English: Does PERMUTE-WITH-ALL generate a uniform random permutation?
Polish: Czy PERMUTE-WITH-ALL generuje losową permutację z równym prawdopodobieństwem?
"""

# Polish description:
# PERMUTE-WITH-ALL nie generuje równomiernie wszystkich permutacji.
# Odpowiedź: False.

def permute_with_all_uniform():
    return False

if __name__ == "__main__":
    print("Exercise 5.3-3 Result:")
    print("Is it uniform?", permute_with_all_uniform())
