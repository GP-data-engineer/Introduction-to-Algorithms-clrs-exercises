"""
Problem 2-1

Znajdowanie największego n, które zmieści się w określonym limicie czasu
dla różnych złożoności czasowych algorytmów.
"""

import math

# Funkcje czasowe — skrócone wersje
time_linear      = lambda n: n
time_n_log_n     = lambda n: 0 if n <= 0 else n * math.log2(n)
time_quadratic   = lambda n: n**2
time_cubic       = lambda n: n**3
time_exponential = lambda n: 2**n
time_log_n       = lambda n: 0 if n <= 0 else math.log2(n)
time_factorial   = lambda n: math.factorial(n)

# Słownik funkcji wymagany przez testy
functions = {
    "n": time_linear,
    "n log n": time_n_log_n,
    "n^2": time_quadratic,
    "n^3": time_cubic,
    "2^n": time_exponential,
    "log n": time_log_n,
    "n!": time_factorial
}

# Słownik limitów czasowych w sekundach
time_limits = {
    "1 second":   1,
    "1 minute":   60,
    "1 hour":     60 * 60,
    "1 day":      60 * 60 * 24,
    "1 month":    60 * 60 * 24 * 30,
    "1 year":     60 * 60 * 24 * 365,
    "1 century":  60 * 60 * 24 * 365 * 100
}

def find_max_n(limit_seconds, time_func):
    # Optymalizacja dla log n — liczymy wprost
    if time_func is time_log_n:
        return int(2 ** limit_seconds)

    # Standardowa metoda: podwajanie + wyszukiwanie binarne
    n = 1
    while time_func(n) <= limit_seconds:
        n *= 2
    low, high = n // 2, n
    while low < high:
        mid = (low + high) // 2
        if time_func(mid) <= limit_seconds:
            low = mid + 1
        else:
            high = mid
    return low - 1

# Alias wymagany przez testy
max_n_for_time = find_max_n

if __name__ == "__main__":
    for label, limit in time_limits.items():
        print(f"\nLimit: {label}")
        for name, func in functions.items():
            print(f"{name:<10} -> max n = {max_n_for_time(limit, func)}")
