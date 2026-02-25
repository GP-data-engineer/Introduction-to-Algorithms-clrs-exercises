# Exercise 11.3-5 (CLRS)
# PL:
# Dla ε-uniwersalnej rodziny funkcji haszujących:
# ε ≥ 1/|B| - 1/|U|
#
# EN:
# For ε-universal hash family:
# ε ≥ 1/|B| - 1/|U|

def epsilon_lower_bound(U_size: int, B_size: int) -> float:
    return 1 / B_size - 1 / U_size


if __name__ == "__main__":
    print("Lower bound:", epsilon_lower_bound(100, 10))