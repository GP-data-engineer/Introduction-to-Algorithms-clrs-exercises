"""
Problem 3-3
Ordering functions by growth rate and providing an oscillating example function.
Optimized for speed and overflow safety.
"""

import math
from functools import lru_cache

def fast_factorial(n: int) -> float:
    """Approximate factorial for large n using Stirling's formula."""
    if n < 20:
        return math.factorial(n)
    return math.sqrt(2 * math.pi * n) * (n / math.e) ** n

@lru_cache(maxsize=None)
def safe_log_value(desc: str, n: int) -> float:
    """
    Return log(f(n)) safely, using formulas to avoid huge computations.
    This ensures sorting is fast and avoids overflow.
    """
    if desc == "2^(2^n)":
        return (2 ** n) * math.log(2)
    if desc == "2^(n^2)":
        return (n ** 2) * math.log(2)
    if desc == "n^n":
        return n * math.log(n)
    if desc == "n!":
        return n * math.log(n) - n  # Stirling's approximation (log)
    if desc == "(n/2)!":
        half = n // 2
        return half * math.log(half) - half
    if desc == "n*2^n":
        return math.log(n) + n * math.log(2)
    if desc == "2^n":
        return n * math.log(2)
    if desc == "n^(lg n)":
        return math.log(n) * math.log(n, 2)
    if desc.startswith("n^"):
        power = float(desc[2:])
        return power * math.log(n)
    if desc == "n lg n":
        return math.log(n) + math.log(math.log(n, 2))
    if desc == "n ln n":
        return math.log(n) + math.log(math.log(n))
    if desc == "n":
        return math.log(n)
    if desc == "n / lg n":
        return math.log(n) - math.log(math.log(n, 2))
    if desc == "n / ln n":
        return math.log(n) - math.log(math.log(n))
    if desc == "sqrt(n)":
        return 0.5 * math.log(n)
    if desc.startswith("lg^"):
        power = float(desc[3:-2])
        return power * math.log(math.log(n, 2))
    if desc.startswith("ln^"):
        power = float(desc[3:-2])
        return power * math.log(math.log(n))
    if desc == "lg n":
        return math.log(math.log(n, 2))
    if desc == "ln n":
        return math.log(math.log(n))
    if desc.startswith("lg(") or desc.startswith("ln("):
        return math.log(math.log(n))  # approximation
    if desc == "lg lg n" or desc == "ln ln n":
        return math.log(math.log(math.log(n)))
    if desc == "1":
        return 0.0
    return 0.0

@lru_cache(maxsize=None)
def safe_value(desc: str, n: int) -> float:
    """Return f(n) safely, using exp(log) to avoid overflow."""
    logv = safe_log_value(desc, n)
    if logv > 700:  # exp(>700) overflows double
        return float('inf')
    return math.exp(logv)

FUNCTIONS = [
    "2^(2^n)", "2^(n^2)", "n!", "n^n", "(n/2)!", "n*2^n", "2^n", "n^(lg n)",
    "n^5", "n^4", "n^3", "n^2", "n lg n", "n ln n", "n", "n / lg n", "n / ln n",
    "sqrt(n)", "lg^4 n", "lg^3 n", "lg^2 n", "ln^2 n", "lg n", "ln n",
    "lg(n^2 + 1)", "ln(n^2 + 1)", "lg lg n", "ln ln n", "1"
]

def get_ordered_functions():
    """Return functions sorted by growth rate for n=50."""
    n_test = 50
    return sorted(
        [(desc, lambda nn, d=desc: safe_value(d, nn)) for desc in FUNCTIONS],
        key=lambda item: safe_log_value(item[0], n_test),
        reverse=True
    )

def get_equivalence_classes():
    """Return Θ-equivalence classes."""
    return [
        ["n lg n", "n ln n"],
        ["lg n", "ln n", "lg(n^2 + 1)", "ln(n^2 + 1)"],
        ["lg lg n", "ln ln n"],
        ["lg^2 n", "ln^2 n"],
    ]

def example_function_part_b():
    """
    Oscillating function: very small for even n, extremely large for odd n.
    Ensures that for any monotonic g(n) from part (a), there are both smaller and larger cases.
    """
    def f(n):
        if n % 2 == 0:
            return 0.5  # very small for even n
        else:
            return float('inf')  # huge for odd n
    return f



if __name__ == "__main__":
    print("=== Problem 3-3 ===")
    print("\n(a) Ordered functions by growth rate for n=50:\n")
    for desc, func in get_ordered_functions():
        print(f" - {desc}: {safe_value(desc, 50)}")

    print("\nΘ-equivalence classes:\n")
    for eq_class in get_equivalence_classes():
        print("   {" + ", ".join(eq_class) + "}")

    print("\n(b) Example function f(n) alternating growth:\n")
    f = example_function_part_b()
    for n in range(10, 20):
        print(f"f({n}) = {f(n)}")
