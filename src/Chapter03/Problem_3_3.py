import math

def fast_factorial(n: int) -> float:
    """Approximate factorial for large n using Stirling's formula for speed."""
    if n < 20:
        return math.factorial(n)
    return math.sqrt(2 * math.pi * n) * (n / math.e) ** n

def get_ordered_functions():
    """
    Return the list of functions sorted from fastest-growing to slowest-growing for large n.
    Uses safe approximations for huge values to avoid OverflowError.
    """
    HUGE = 1e308
    funcs = [
        ("2^(2^n)", lambda n: HUGE),
        ("n^n", lambda n: HUGE / 2),
        ("2^(n^2)", lambda n: HUGE / 4),
        ("n!", lambda n: fast_factorial(n)),
        ("(n/2)!", lambda n: fast_factorial(n // 2)),
        ("2^n", lambda n: 2 ** n),
        ("2^(sqrt(n))", lambda n: 2 ** math.sqrt(n)),
        ("n^5", lambda n: n ** 5),
        ("n^4", lambda n: n ** 4),
        ("n^3", lambda n: n ** 3),
        ("n^2", lambda n: n ** 2),
        ("n lg n", lambda n: n * math.log(n, 2)),
        ("n ln n", lambda n: n * math.log(n)),
        ("n", lambda n: n),
        ("n / lg n", lambda n: n / math.log(n, 2)),
        ("n / ln n", lambda n: n / math.log(n)),
        ("sqrt(n)", lambda n: math.sqrt(n)),
        ("lg^2 n", lambda n: math.log(n, 2) ** 2),
        ("ln^2 n", lambda n: math.log(n) ** 2),
        ("lg n", lambda n: math.log(n, 2)),
        ("ln n", lambda n: math.log(n)),
        ("lg(n^2 + 1)", lambda n: math.log(n**2 + 1, 2)),
        ("ln(n^2 + 1)", lambda n: math.log(n**2 + 1)),
        ("lg lg n", lambda n: math.log(math.log(n, 2), 2)),
        ("ln ln n", lambda n: math.log(math.log(n))),
    ]
    return funcs

def get_equivalence_classes():
    return [
        ["n lg n", "n ln n"],
        ["lg n", "ln n", "lg(n^2 + 1)", "ln(n^2 + 1)"],
        ["lg lg n", "ln ln n"],
        ["lg^2 n", "ln^2 n"],
    ]

def example_function_part_b():
    """
    Oscillating function: small for even n, large for odd n.
    Large value chosen so that for some g(n) it's bigger, for others smaller.
    """
    def f(n):
        if n % 2 == 0:
            return n
        else:
            return n ** 6  # większe niż wielomiany, mniejsze niż potęgi wykładnicze
    return f

if __name__ == "__main__":
    print("=== Problem 3-3 ===")
    print("\n(a) Ordered functions by growth rate:\n")
    for desc, func in get_ordered_functions():
        print(f" - {desc}: value for n=10 → {func(10)}")

    print("\nΘ-equivalence classes:\n")
    for eq_class in get_equivalence_classes():
        print("   {" + ", ".join(eq_class) + "}")

    print("\n(b) Example function f(n) alternating growth:\n")
    f = example_function_part_b()
    for n in range(2, 12):
        print(f"f({n}) = {f(n)}")
