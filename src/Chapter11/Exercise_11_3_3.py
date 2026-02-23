# Exercise 11.3-3 (CLRS)
# PL:
# Dla m = 2^p - 1 oraz h(k)=k mod m.
# Jeśli x jest permutacją znaków y, to h(x)=h(y).
#
# EN:
# For m = 2^p - 1 and h(k)=k mod m.
# If x is permutation of y then h(x)=h(y).

def mersenne_hash(s: str, p: int) -> int:
    m = 2**p - 1
    total = sum(ord(c) for c in s)
    return total % m


if __name__ == "__main__":
    print(mersenne_hash("abc", 5))
    print(mersenne_hash("cba", 5))
