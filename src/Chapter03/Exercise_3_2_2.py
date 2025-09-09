# Exercise 3.2-2
# Prove formula (3.16) - here we assume it's a known logarithmic identity.
# Example: log_a(bc) = log_a(b) + log_a(c)

import math

def log_product(a, b, base):
    """Return log_base(a*b) and verify formula log(a*b) = log(a) + log(b)."""
    return math.log(a*b, base), math.log(a, base) + math.log(b, base)

if __name__ == "__main__":
    a, b, base = 4, 8, 2
    val1, val2 = log_product(a, b, base)
    print(f"log_{base}({a*b}) = {val1}")
    print(f"log_{base}({a}) + log_{base}({b}) = {val2}")
    print("Equal?", abs(val1 - val2) < 1e-9)
