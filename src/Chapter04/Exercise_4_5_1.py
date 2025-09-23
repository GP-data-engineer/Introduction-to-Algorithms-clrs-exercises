"""
Exercise 4.5-1
Solve the given recurrences using the Master Theorem (universal recurrence method).
We provide functions that compute asymptotic complexity results for each case.
"""

# Polish description:
# Ten plik zawiera rozwiązania rekurencji z zadania 4.5-1 przy użyciu twierdzenia uniwersalnego.
# Funkcje zwracają oszacowania asymptotyczne w postaci stringów.

def recurrence_a():
    # T(n) = 2T(n/4) + n -> Θ(n)
    return "Θ(n)"

def recurrence_b():
    # T(n) = 2T(n/4) + √n -> Θ(√n log n)
    return "Θ(√n log n)"

def recurrence_c():
    # T(n) = 2T(n/4) + n² -> Θ(n²)
    return "Θ(n²)"

def recurrence_d():
    # T(n) = 2T(n/4) + n² log n -> Θ(n² log n)
    return "Θ(n² log n)"

def recurrence_e():
    # T(n) = 2T(n/4) + n³ -> Θ(n³)
    return "Θ(n³)"


if __name__ == "__main__":
    print("Exercise 4.5-1 Results:")
    print("a:", recurrence_a())
    print("b:", recurrence_b())
    print("c:", recurrence_c())
    print("d:", recurrence_d())
    print("e:", recurrence_e())
