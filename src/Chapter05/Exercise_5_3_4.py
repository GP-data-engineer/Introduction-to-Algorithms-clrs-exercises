"""
Exercise 5.3-4
English: Why does PERMUTE-BY-CYCLIC not generate a uniform random permutation?
Polish: Dlaczego PERMUTE-BY-CYCLIC nie generuje równomiernie losowej permutacji?
"""

# Polish description:
# PERMUTE-BY-CYCLIC generuje tylko przesunięcia cykliczne tablicy.
# Każdy element ma prawdopodobieństwo 1/n bycia na swojej pozycji,
# ale nie wszystkie permutacje są osiągalne.

def permute_by_cyclic_uniform():
    return False

if __name__ == "__main__":
    print("Exercise 5.3-4 Result:")
    print("Is it uniform?", permute_by_cyclic_uniform())
