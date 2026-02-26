# Exercise 11.3-6 (CLRS)
# PL:
# h_b(a0,...,a_{r-1}) = (sum a_i b^i) mod p
#
# EN:
# Polynomial hash over Z_p

def polynomial_hash(vector, b, p):
    result = 0
    power = 1
    for a in vector:
        result = (result + a * power) % p
        power = (power * b) % p
    return result


if __name__ == "__main__":
    print(polynomial_hash([1,2,3], 5, 13))