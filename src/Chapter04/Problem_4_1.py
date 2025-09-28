"""
Problem 4-1
We are asked to provide asymptotic upper and lower bounds for several recurrences.
Assume T(n) is constant for n ≤ 2. The solutions are derived using the Master Theorem
and recursion tree analysis.
"""

# Polish description:
# Ten plik zawiera rozwiązania rekurencji z problemu 4-1.
# Każda funkcja zwraca asymptotyczne oszacowanie Θ(...) dla danej rekurencji.

def recurrence_a():
    # T(n) = 2T(n/2) + n^4 -> Θ(n^4)
    return "Θ(n^4)"

def recurrence_b():
    # T(n) = 2T(n/2) + n -> Θ(n log n)
    return "Θ(n log n)"

def recurrence_c():
    # T(n) = 16T(n/4) + n^2
    # log_b a = log_4 16 = 2, f(n) = n^2 -> Θ(n^2 log n)
    return "Θ(n^2 log n)"

def recurrence_d():
    # T(n) = 7T(n/2) + n^3
    # log_b a = log_2 7 ≈ 2.81, f(n) = n^3 dominates -> Θ(n^3)
    return "Θ(n^3)"

def recurrence_e():
    # T(n) = 2T(n/4) + √n
    # log_b a = log_4 2 = 0.5, f(n) = n^0.5 -> Θ(√n log n)
    return "Θ(√n log n)"

def recurrence_f():
    # T(n) = T(n/2) + T(n/4) + n
    # Equivalent to a=1.25, b≈2, dominates by n log n
    return "Θ(n log n)"

def recurrence_g():
    # T(n) = T(n/2) + n^2 + 2n -> dominated by n^2
    return "Θ(n^2)"

if __name__ == "__main__":
    print("Problem 4-1 Results:")
    print("a:", recurrence_a())
    print("b:", recurrence_b())
    print("c:", recurrence_c())
    print("d:", recurrence_d())
    print("e:", recurrence_e())
    print("f:", recurrence_f())
    print("g:", recurrence_g())
