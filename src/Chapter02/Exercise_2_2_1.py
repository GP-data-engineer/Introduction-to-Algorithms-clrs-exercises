"""
Exercise 2.2-1

Express the function n³ / 1000 – 100n² – 100n + 3 using Θ-notation.
Also, prove it formally using the definition of Θ.
"""
def analyze_function(n: int) -> float:
    return (n**3) / 1000 - 100*(n**2) - 100*n + 3


def prove_theta():
    """
    Formal proof that f(n) ∈ Θ(n³):

    By definition:
    f(n) ∈ Θ(g(n)) if there exist positive constants c1, c2, and n0
    such that for all n ≥ n0:  c1*g(n) ≤ f(n) ≤ c2*g(n).

    Let g(n) = n³.

    Lower bound:
    For large n, negative terms become insignificant compared to n³/1000.
    Choose c1 = 1/2000, n0 large enough so that f(n) ≥ c1*n³.

    Upper bound:
    Absolute value of f(n) is less than (n³/1000 + 100n² + 100n + 3).
    For large n, that is ≤ (1/1000 + 1)*n³ for some constant.
    Choose c2 = 2 for n ≥ n0.

    Conclusion: f(n) is bounded above and below by constant multiples of n³
    for all n ≥ n0, therefore f(n) ∈ Θ(n³).
    """
    print("Formal proof by definition is explained in the docstring above.")


if __name__ == "__main__":
    for n in [10, 100, 1000, 10000]:
        value = analyze_function(n)
        print(f"n = {n:<6}  f(n) = {value:<20}  Dominant term: n^3")
    prove_theta()
    # Final asymptotic classification:
    # f(n) ∈ Θ(n³)

