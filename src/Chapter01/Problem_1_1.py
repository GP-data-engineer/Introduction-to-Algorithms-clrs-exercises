"""
File: Problem_1_1.py
Task: Introduction to Algorithms (CLRS) - Problem 1-1

Description:
------------
This program computes, for various growth-rate functions f(n),
the largest integer n that can be computed within a given time limit.
The time limits range from 1 second to 1 century, and the functions
include logarithmic, polynomial, exponential, and factorial growth.

The goal is to illustrate how quickly different functions grow and
how feasible it is to compute them within realistic time constraints.

Optimizations:
--------------
- Direct mathematical formulas are used where possible to avoid slow iteration.
- Binary search is applied for n log n.
- Factorial is computed iteratively, but n remains small enough to be fast.
- For log n, extremely large results are represented in scientific notation
  in display only, but the actual integer is returned for testing.
- Colored console output for better readability.
"""

import math
from colorama import Fore, Style, init

# Initialize colorama (works on Windows and Linux)
init(autoreset=True)

# Dictionary of growth functions
functions = {
    "log n": lambda n: math.log2(n),
    "sqrt n": lambda n: math.sqrt(n),
    "n": lambda n: n,
    "n log n": lambda n: n * math.log2(n),
    "n^2": lambda n: n**2,
    "n^3": lambda n: n**3,
    "2^n": lambda n: 2**n,
    "n!": lambda n: math.factorial(n)
}

# Time limits in seconds
time_limits = {
    "1 second": 1_000_000,
    "1 minute": 60 * 1_000_000,
    "1 hour": 3_600 * 1_000_000,
    "1 day": 86_400 * 1_000_000,
    "1 month": 2_592_000 * 1_000_000,
    "1 year": 31_536_000 * 1_000_000,
    "1 century": 3_153_600_000 * 1_000_000
}

def max_n_for_time(limit, func):
    """
    Given a time limit (in seconds) and a growth function f(n),
    return the largest integer n such that f(n) <= limit.
    Always returns an int for compatibility with tests.
    """
    if func == functions["log n"]:
        # Return actual integer so tests can check it
        return int(2 ** limit)
    elif func == functions["√n"]:
        return int(limit**2)
    elif func == functions["n"]:
        return int(limit)
    elif func == functions["n log n"]:
        # Solve n log2(n) <= limit using binary search
        low, high = 1, int(limit)
        while low < high:
            mid = (low + high + 1) // 2
            if mid * math.log2(mid) <= limit:
                low = mid
            else:
                high = mid - 1
        return low
    elif func == functions["n^2"]:
        return int(math.isqrt(limit))
    elif func == functions["n^3"]:
        return int(round(limit ** (1/3)))
    elif func == functions["2^n"]:
        return int(math.log2(limit))
    elif func == functions["n!"]:
        n, fact = 1, 1
        while fact <= limit:
            n += 1
            fact *= n
        return n - 1

def main():
    # Print table header
    print(Fore.CYAN + Style.BRIGHT + f"{'f(n)':<10}", end="")
    for t in time_limits:
        print(Fore.YELLOW + f"{t:>12}", end="")
    print(Style.RESET_ALL)

    # Separator
    print(Fore.MAGENTA + "-" * (10 + 12 * len(time_limits)))

    # Print table rows
    for name, func in functions.items():
        print(Fore.CYAN + f"{name:<10}", end="")
        for t in time_limits.values():
            val = max_n_for_time(t, func)
            # For huge log n values, display scientific notation instead of printing billions of digits
            if func == functions["log n"] and t > 1000:
                exp = t * math.log10(2)
                display_val = f"~10^{exp:.2f}"
                color = Fore.BLUE
            else:
                display_val = str(val)
                color = Fore.GREEN if isinstance(val, int) and val < 1000 else Fore.RED
            print(color + f"{display_val:>12}", end="")
        print(Style.RESET_ALL)

if __name__ == "__main__":
    main()
