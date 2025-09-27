"""
Exercise 4.5-5
We need to provide an example of constants a ≥ 1, b > 1, and a function f(n)
that satisfies all conditions of Case 3 of the Master Theorem,
except the regularity condition: a f(n/b) ≤ c f(n) for some c < 1.

Example:
- a = 2
- b = 2
- f(n) = n^2 / log n

This function grows faster than n^(log_b a + ε) = n^(1+ε), so it fits Case 3.
But the regularity condition fails because:
a f(n/b) = 2 * ( (n/2)^2 / log(n/2) ) ≈ n^2 / (2 log n),
which is not ≤ c * (n^2 / log n) for any c < 1.
"""

# Polish description:
# Wybieramy a=2, b=2, f(n)=n^2/log n. Funkcja spełnia warunki przypadku 3,
# ale nie spełnia warunku regularności, bo stosunek a f(n/b) / f(n) dąży do 1/2,
# a nie do wartości < 1 dla stałej c.

def example_case():
    a = 2
    b = 2
    f = "n^2 / log n"
    return a, b, f

if __name__ == "__main__":
    a, b, f = example_case()
    print("Exercise 4.5-5 Example:")
    print(f"a = {a}, b = {b}, f(n) = {f}")
    print("This satisfies Case 3 except the regularity condition.")
"""
Exercise 4.5-5
We need to provide an example of constants a ≥ 1, b > 1, and a function f(n)
that satisfies all conditions of Case 3 of the Master Theorem,
except the regularity condition: a f(n/b) ≤ c f(n) for some c < 1.

Example:
- a = 2
- b = 2
- f(n) = n^2 / log n

This function grows faster than n^(log_b a + ε) = n^(1+ε), so it fits Case 3.
But the regularity condition fails because:
a f(n/b) = 2 * ( (n/2)^2 / log(n/2) ) ≈ n^2 / (2 log n),
which is not ≤ c * (n^2 / log n) for any c < 1.
"""

# Polish description:
# Wybieramy a=2, b=2, f(n)=n^2/log n. Funkcja spełnia warunki przypadku 3,
# ale nie spełnia warunku regularności, bo stosunek a f(n/b) / f(n) dąży do 1/2,
# a nie do wartości < 1 dla stałej c.

def example_case():
    a = 2
    b = 2
    f = "n^2 / log n"
    return a, b, f

if __name__ == "__main__":
    a, b, f = example_case()
    print("Exercise 4.5-5 Example:")
    print(f"a = {a}, b = {b}, f(n) = {f}")
    print("This satisfies Case 3 except the regularity condition.")
