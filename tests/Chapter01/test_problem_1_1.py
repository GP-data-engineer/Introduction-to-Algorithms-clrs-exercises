import math
import pytest
from Chapter01.Problem_1_1 import max_n_for_time, functions, time_limits

# Dane testowe – dla "log n" expected ustawiamy na None, bo i tak sprawdzamy warunek graniczny
params = [
    ("log n", "1 second", None),
    ("log n", "1 minute", None),

    ("sqrt n", "1 second", 1_000_000 ** 2),
    ("sqrt n", "1 hour", (60 * 60 * 1_000_000) ** 2),

    ("n", "1 second", 1_000_000),
    ("n", "1 day", 24 * 60 * 60 * 1_000_000),

    ("n log n", "1 second", 50_000),
    ("n log n", "1 minute", 3_000_000),

    ("n^2", "1 second", int(math.isqrt(1_000_000))),
    ("n^2", "1 hour", int(math.isqrt(60 * 60 * 1_000_000))),

    ("n^3", "1 second", int(round(1_000_000 ** (1 / 3)))),
    ("n^3", "1 minute", int(round((60 * 1_000_000) ** (1 / 3)))),

    ("2^n", "1 second", 19),
    ("2^n", "1 minute", 25),

    ("n!", "1 second", 9),
    ("n!", "1 minute", 11),
]

# Własne ID dla każdego zestawu parametrów – unikamy konwersji gigantycznych intów
ids = [f"{fn} - {lk}" for fn, lk, _ in params]

@pytest.mark.parametrize("func_name, limit_key, expected", params, ids=ids)
def test_max_n_for_time(func_name: str, limit_key: str, expected: int):
    func = functions[func_name]
    limit = time_limits[limit_key]

    result = max_n_for_time(limit, func)

    if func_name == "log n":
        # Sprawdzamy tylko warunek graniczny
        assert func(result) <= limit
        assert func(result + 1) > limit
    else:
        assert result == expected
        assert func(result + 1) > limit
