# Exercise 11.3-4 (CLRS)
# PL:
# Metoda mnożeniowa: h(k)=floor(m*(kA mod 1))
#
# EN:
# Multiplication method: h(k)=floor(m*(kA mod 1))

import math

def multiplication_hash(k: int, m: int):
    A = (math.sqrt(5) - 1) / 2
    return int(m * ((k * A) % 1))


if __name__ == "__main__":
    m = 1000
    for k in [61, 62, 63, 64, 65]:
        print(k, multiplication_hash(k, m))