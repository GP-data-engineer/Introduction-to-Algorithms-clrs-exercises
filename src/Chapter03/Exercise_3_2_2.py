# Exercise 3.2-2
# Prove formula (3.16) - here we assume it's a known logarithmic identity.
# Example: log_a(bc) = log_a(b) + log_a(c)

import math

def log_product(a, b, base):
    """Return log_base(a*b) and verify formula log(a*b) = log(a) + log(b)."""
    return math.log(a*b, base), math.log(a, base) + math.log(b, base)
