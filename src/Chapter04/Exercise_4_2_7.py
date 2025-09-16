"""
Exercise 4.2-7
This script multiplies two complex numbers (a + bi) and (c + di)
using only 3 real-number multiplications.
"""

def multiply_complex_3muls(a: float, b: float, c: float, d: float) -> tuple[float, float]:
    """
    Multiply two complex numbers using only 3 real multiplications.
    Returns a tuple (real_part, imaginary_part).
    """
    # First multiplication: a * c
    p = a * c
    # Second multiplication: b * d
    q = b * d
    # Third multiplication: (a + b) * (c + d)
    r = (a + b) * (c + d)

    # Real part: p - q
    real_part = p - q
    # Imaginary part: r - p - q
    imaginary_part = r - p - q

    return real_part, imaginary_part


if __name__ == "__main__":
    # Example usage
    a, b = 3, 2   # First complex number: 3 + 2i
    c, d = 1, 4   # Second complex number: 1 + 4i

    real, imag = multiply_complex_3muls(a, b, c, d)
    print(f"({a} + {b}i) * ({c} + {d}i) = {real} + {imag}i")
