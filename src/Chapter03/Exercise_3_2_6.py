"""
Exercise 3.2-6
Functions to compare factorial growth with exponential growth
and to analyze asymptotic relationships between two functions.
"""

import math
from typing import Callable, List


def compare_factorial_growth(n: int) -> tuple[bool, bool]:
    """
    Compare n! with 2^n for a given n.
    Returns:
        greater (bool): True if n! > 2^n
        smaller (bool): True if n! < 2^n
    """
    factorial_val = math.factorial(n)  # Compute n!
    power_val = 2 ** n                  # Compute 2^n
    return factorial_val > power_val, factorial_val < power_val


def analyze_pair(f: Callable[[int], float],
                 g: Callable[[int], float],
                 n_values: List[int]) -> dict:
    """
    Analyze the asymptotic relationship between f and g over given n_values.
    Returns a dict with keys: "O", "o", "Ω", "ω", "Θ".
    """
    result = {"O": False, "o": False, "Ω": False, "ω": False, "Θ": False}

    # Compute ratios f(n)/g(n) for all n
    ratios = []
    for n in n_values:
        gv = g(n)
        if gv == 0:
            ratios.append(math.inf)
        else:
            ratios.append(f(n) / gv)

    max_ratio = max(ratios)
    min_ratio = min(ratios)

    # Big O: ratio is bounded above
    result["O"] = math.isfinite(max_ratio) and max_ratio < 1e6

    # little o: ratio tends to 0
    tail = ratios[-3:] if len(ratios) >= 3 else ratios
    result["o"] = all(abs(r) < 1e-6 for r in tail)

    # Big Omega: ratio is bounded below by positive constant
    result["Ω"] = min_ratio > 1e-6 and math.isfinite(min_ratio)

    # little omega: ratio tends to infinity
    result["ω"] = all(r > 1e6 for r in tail if math.isfinite(r))

    # Theta: both O and Ω
    result["Θ"] = result["O"] and result["Ω"]

    return result


if __name__ == "__main__":
    print("=== Demonstration of Exercise 3.2-6 functions ===\n")

    # Demonstrate compare_factorial_growth
    for n in range(3, 10):
        greater, smaller = compare_factorial_growth(n)
        print(f"n = {n}: n! = {math.factorial(n)}, 2^n = {2**n}, "
              f"greater? {greater}, smaller? {smaller}")

    print("\n--- Asymptotic analysis example: n vs n^2 ---")
    n_vals = [10**k for k in range(2, 6)]
    result = analyze_pair(lambda n: n, lambda n: n**2, n_vals)
    print(f"n values: {n_vals}")
    print("Analysis result:", result)

    print("\n=== End of demonstration ===")
