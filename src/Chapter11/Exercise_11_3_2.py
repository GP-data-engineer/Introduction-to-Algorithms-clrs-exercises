# Exercise 11.3-2 (CLRS)
# PL:
# Obliczanie k mod m dla bardzo długiego napisu (podstawa 128)
# używając stałej dodatkowej pamięci.
#
# EN:
# Compute k mod m for very long string (base 128 representation)
# using constant additional memory.

def modular_hash_string(s: str, m: int) -> int:
    result = 0
    for char in s:
        result = (result * 128 + ord(char)) % m
    return result


if __name__ == "__main__":
    print("Hash:", modular_hash_string("abcd", 1000))
