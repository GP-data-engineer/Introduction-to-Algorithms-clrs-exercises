"""
Problem 4-3
We are asked to provide asymptotic upper and lower bounds for each recurrence.
Assume T(n) is constant for sufficiently small n. The solutions are derived using
the Master Theorem, recursion tree analysis, or iterative expansion.
"""

# Polish description:
# Ten plik zawiera rozwiązania rekurencji z problemu 4-3.
# Każda funkcja zwraca asymptotyczne oszacowanie Θ(...) dla danej rekurencji.

def recurrence_a():
    # T(n) = 4T(n/3) + n log n
    # log_b a = log_3 4 ≈ 1.26, f(n) = n log n = O(n^(1+ε)), dominuje n^(1.26)
    return "Θ(n^log_3 4) ≈ Θ(n^1.26)"

def recurrence_b():
    # T(n) = 4T(n/3) + n^2
    # log_3 4 ≈ 1.26, f(n) = n^2 dominates -> Θ(n^2)
    return "Θ(n^2)"

def recurrence_c():
    # T(n) = 4T(n/3) + n^2 / log n
    # f(n) slightly smaller than n^2, still dominates -> Θ(n^2)
    return "Θ(n^2)"

def recurrence_d():
    # T(n) = 4T(n/3) + n^2 / ln n
    # Same reasoning as (c) -> Θ(n^2)
    return "Θ(n^2)"

def recurrence_e():
    # T(n) = 4T(n/3) + n^2 + n
    # n^2 dominates -> Θ(n^2)
    return "Θ(n^2)"

def recurrence_f():
    # T(n) = 4T(n/3) + n^2 + T(n/8) + n
    # Extra T(n/8) does not change asymptotics -> Θ(n^2)
    return "Θ(n^2)"

def recurrence_g():
    # T(n) = 4T(n/3) + n^2 + T(n/8)
    # Same as (f) -> Θ(n^2)
    return "Θ(n^2)"

def recurrence_h():
    # T(n) = T(n-1) + 1 -> Θ(n)
    return "Θ(n)"

def recurrence_i():
    # T(n) = T(n-1) + n -> Θ(n^2)
    return "Θ(n^2)"

def recurrence_j():
    # T(n) = T(n-1) + n^2 -> Θ(n^3)
    return "Θ(n^3)"

def recurrence_k():
    # T(n) = T(n-1) + n log n -> Θ(n^2 log n)
    return "Θ(n^2 log n)"

def recurrence_l():
    # T(n) = √n T(√n) + n
    # Expansion shows Θ(n log log n)
    return "Θ(n log log n)"


if __name__ == "__main__":
    print("Problem 4-3 Results:")
    print("a:", recurrence_a())
    print("b:", recurrence_b())
    print("c:", recurrence_c())
    print("d:", recurrence_d())
    print("e:", recurrence_e())
    print("f:", recurrence_f())
    print("g:", recurrence_g())
    print("h:", recurrence_h())
    print("i:", recurrence_i())
    print("j:", recurrence_j())
    print("k:", recurrence_k())
    print("l:", recurrence_l())
