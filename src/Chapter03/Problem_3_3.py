"""
Ordering by the magnitude of functions (in English):

Part (a):
We sort the given functions g1, g2, ..., g30 by their asymptotic growth rate.
We also group them into equivalence classes where f(n) = Θ(g(n)).

Part (b):
We provide an example of a non-negative function f(n) such that for all g3(n)
from part (a), f(n) is neither O(g3(n)) nor Ω(g3(n)).

This module contains:
- A predefined ordering of the functions according to their growth rate.
- A function to return the equivalence classes.
- An example function for part (b).
"""

import math

def get_ordered_functions():
    """
    Return the list of functions sorted from fastest-growing to slowest-growing,
    grouped into Θ-equivalence classes.
    Each element is a tuple: (description, callable).
    """
    funcs = [
        ("2^(2^n)", lambda n: 2 ** (2 ** n)),
        ("n^n", lambda n: n ** n),
        ("(n/2)!", lambda n: math.factorial(n // 2)),
        ("n!", lambda n: math.factorial(n)),
        ("2^(n^2)", lambda n: 2 ** (n ** 2)),
        ("2^(sqrt(n))", lambda n: 2 ** math.sqrt(n)),
        ("2^n", lambda n: 2 ** n),
        ("n^5", lambda n: n ** 5),
        ("n^4", lambda n: n ** 4),
        ("n^3", lambda n: n ** 3),
        ("n^2", lambda n: n ** 2),
        ("n lg n", lambda n: n * math.log(n, 2)),
        ("n ln n", lambda n: n * math.log(n)),
        ("n", lambda n: n),
        ("n / lg n", lambda n: n / math.log(n, 2)),
        ("n / ln n", lambda n: n / math.log(n)),
        ("sqrt(n)", lambda n: math.sqrt(n)),
        ("lg^2 n", lambda n: math.log(n, 2) ** 2),
        ("ln^2 n", lambda n: math.log(n) ** 2),
        ("lg n", lambda n: math.log(n, 2)),
        ("ln n", lambda n: math.log(n)),
        ("lg lg n", lambda n: math.log(math.log(n, 2), 2)),
        ("ln ln n", lambda n: math.log(math.log(n))),
    ]
    return funcs

def get_equivalence_classes():
    """
    Return a list of Θ-equivalence classes based on known asymptotic identities.
    Each class is a list of descriptions of equivalent functions.
    """
    return [
        ["n lg n", "n ln n"],  # differ by constant factor
        ["lg n", "ln n", "lg(n^2 + 1)", "ln(n^2 + 1)"],  # constant factor
        ["lg lg n", "ln ln n"],  # constant factor
        ["lg^2 n", "ln^2 n"],  # constant factor
    ]

def example_function_part_b():
    """
    Example of a function that is neither O(g(n)) nor Ω(g(n)) for any g(n) from part (a).
    We can use an oscillating function that alternates between very small and very large values.
    """
    def f(n):
        if n % 2 == 0:
            return n
        else:
            return 2 ** n
    return f

if __name__ == "__main__":
    print("=== Problem 3-3 ===")
    print("\n(a) Ordered functions by growth rate:\n")
    for desc, _ in get_ordered_functions():
        print(" -", desc)

    print("\nΘ-equivalence classes:\n")
    for eq_class in get_equivalence_classes():
        print("   {" + ", ".join(eq_class) + "}")

    print("\n(b) Example function f(n) alternating growth:\n")
    f = example_function_part_b()
    for n in range(2, 12):
        print(f"f({n}) = {f(n)}")