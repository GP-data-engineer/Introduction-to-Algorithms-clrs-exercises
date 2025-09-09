# Exercise 3.2-7
# Prove that for positive constant c, n^c is asymptotically smaller than 2^n.

def compare_polynomial_vs_exponential(n, c):
    """Return True if n^c < 2^n."""
    return (n**c) < (2**n)

if __name__ == "__main__":
    c = 3
    for n in range(5, 15):
        print(f"n={n}, n^{c} < 2^n? {compare_polynomial_vs_exponential(n, c)}")
