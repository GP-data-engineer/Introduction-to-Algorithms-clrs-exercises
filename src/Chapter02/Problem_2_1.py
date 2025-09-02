"""
Problem 2-1 (CLRS) — stub

Add a short paraphrase of the task here.
Source of index: MIT Press, "Selected Solutions", pp. 82–83.
PDF: https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/11599/selected-solutions.pdf
"""
import math

time_limits = {
    "1 second": 1,
    "1 minute": 60,
    "1 hour": 60 * 60,
    "1 day": 60 * 60 * 24,
    "1 month": 60 * 60 * 24 * 30,
    "1 year": 60 * 60 * 24 * 365,
    "1 century": 60 * 60 * 24 * 365 * 100,
}

functions = {
    "n^2": lambda n: n**2,
    "log n": lambda n: math.log2(n),
    "n!": lambda n: math.factorial(n),
    "n": lambda n: n,
    "n log n": lambda n: n * math.log2(n),
    "2^n": lambda n: 2**n,
}

def max_n_for_time(time_limit: float, f) -> int:
    n = 1
    while f(n) <= time_limit:
        n += 1
    return n - 1


