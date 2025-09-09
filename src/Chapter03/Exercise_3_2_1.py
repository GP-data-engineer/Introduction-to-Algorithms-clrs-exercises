# Exercise 3.2-1
# Prove that if f(n) and g(n) are monotonically increasing functions,
# then f(n) + g(n) and f(n) * g(n) are also monotonically increasing.
# If f(n) and g(n) are additionally non-negative, then f(n) * g(n) is monotonically increasing.

def is_monotonic_increasing(seq):
    """Check if a sequence is monotonically increasing."""
    return all(seq[i] <= seq[i+1] for i in range(len(seq)-1))

def sum_of_functions(f, g, n_values):
    """Return list of f(n) + g(n) for given n values."""
    return [f(n) + g(n) for n in n_values]

def product_of_functions(f, g, n_values):
    """Return list of f(n) * g(n) for given n values."""
    return [f(n) * g(n) for n in n_values]
