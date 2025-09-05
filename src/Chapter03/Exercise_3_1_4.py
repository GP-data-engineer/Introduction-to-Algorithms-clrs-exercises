"""
Explanation (in Polish):

Zadanie:
1. Czy C_{XY} * 2^{n+1} = O(2^n)?
2. Czy C_{XY} * 2^n = O(2^{2^n})?

Analiza:
1. 2^{n+1} = 2 * 2^n, więc C_{XY} * 2^{n+1} = (2 * C_{XY}) * 2^n.
   Stała nie wpływa na klasę złożoności, więc TAK — jest to O(2^n).

2. 2^n rośnie znacznie wolniej niż 2^{2^n}, ponieważ 2^{2^n} jest funkcją
   wykładniczą o wykładniku wykładniczym (double exponential).
   Zatem C_{XY} * 2^n = O(2^{2^n}) również jest prawdziwe.

W obu przypadkach odpowiedź brzmi: TAK.
"""

def is_big_o_of(expr_func, bound_func, n_values):
    """
    Checks if expr_func(n) = O(bound_func(n)) using the definition of Big-O.
    This means there exist constants c > 0 and n0 such that:
        expr_func(n) <= c * bound_func(n) for all n >= n0.
    """
    ratios = []
    for n in n_values:
        bound_val = bound_func(n)
        expr_val = expr_func(n)
        if bound_val == 0:
            continue
        ratios.append(expr_val / bound_val)

    if not ratios:
        return False

    c = max(ratios)
    return c < float('inf')

# Example functions for the given problem
def expr1(n, C=1):
    return C * (2 ** (n + 1))

def bound1(n):
    return 2 ** n

def expr2(n, C=1):
    return C * (2 ** n)

def bound2(n):
    return 2 ** (2 ** n)

if __name__ == "__main__":
    # Demonstration
    n_values_demo = range(1, 10)
    print("Check if C*2^(n+1) = O(2^n):", is_big_o_of(lambda n: expr1(n, 3), bound1, n_values_demo))
    print("Check if C*2^n = O(2^(2^n)):", is_big_o_of(lambda n: expr2(n, 5), bound2, n_values_demo))
