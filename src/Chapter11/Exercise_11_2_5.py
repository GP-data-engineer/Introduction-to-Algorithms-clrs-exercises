# Exercise 11.2-5 (CLRS)
# PL:
# Jeśli |U| > n*m, istnieje podzbiór n kluczy haszujących się do tej samej pozycji.
#
# EN:
# If |U| > n*m then there exists subset of n keys mapping to same slot.

def pigeonhole_collision(U_size, n, m):
    return U_size > n * m


if __name__ == "__main__":
    print("Collision guaranteed:",
          pigeonhole_collision(101, 10, 10))
