# test_problem_1_1.py
#
# Unit tests for the Problem_1_1.py module.
# They verify that max_n_for_time returns the largest n whose runtime
# stays within each time limit for the various complexity functions.
#
# How to run:
#   pip install pytest
#   pytest -q
#
# Note: Problem_1_1.py resides in src/Chapter01/, therefore we import it
# using its package path (Chapter01.Problem_1_1).

import math
import pytest

# Direct imports from the source module (no dynamic import).
from Chapter01.Problem_1_1 import max_n_for_time, functions, time_limits


@pytest.mark.parametrize(
    "func_name, limit_key, expected",
    [
        # log n – extremely fast, even a century allows astronomically large n.
        ("log n", "1 second", 2 ** 1_000_000 - 1),
        ("log n", "1 minute", 2 ** (60 * 1_000_000) - 1),

        # sqrt n – grows slower than linear.
        ("sqrt n", "1 second", 1_000_000 ** 2),
        ("sqrt n", "1 hour", (60 * 60 * 1_000_000) ** 2),

        # n – basic linear growth.
        ("n", "1 second", 1_000_000),
        ("n", "1 day", 24 * 60 * 60 * 1_000_000),

        # n log n – slightly slower than pure linear.
        ("n log n", "1 second", 50_000),   # approximate boundary, we check the limit
        ("n log n", "1 minute", 3_000_000),

        # n^2 – quadratic growth.
        ("n^2", "1 second", int(math.isqrt(1_000_000))),
        ("n^2", "1 hour", int(math.isqrt(60 * 60 * 1_000_000))),

        # n^3 – cubic growth.
        ("n^3", "1 second", int(round(1_000_000 ** (1 / 3)))),
        ("n^3", "1 minute", int(round((60 * 1_000_000) ** (1 / 3)))),

        # 2^n – exponential, quickly exceeds limits.
        ("2^n", "1 second", 19),   # 2^19 = 524 288 < 1 000 000 < 2^20
        ("2^n", "1 minute", 25),   # 2^25 = 33 554 432 < 60 000 000 < 2^26

        # n! – factorial, even faster growth than 2^n.
        ("n!", "1 second", 9),     # 9! = 362 880 < 1 000 000 < 10!
        ("n!", "1 minute", 11),    # 11! = 39 916 800 < 60 000 000 < 12!
    ],
)
def test_max_n_for_time(func_name: str, limit_key: str, expected: int):
    """
    Checks whether max_n_for_time returns the expected result.
    For some functions (e.g., log n) the exact value is astronomically large,
    so we only verify that the result satisfies f(n) ≤ limit and that n+1 already exceeds it.
    """
    func = functions[func_name]
    limit = time_limits[limit_key]

    result = max_n_for_time(limit, func)

    # For very large values (log n) we compare only that the result does not exceed the limit
    # and that increasing by 1 would exceed it.
    if func_name == "log n":
        assert func(result) <= limit
        assert func(result + 1) > limit
    else:
        assert result == expected
        # Additional boundary check – the next element should already cross the limit.
        assert func(result + 1) > limit