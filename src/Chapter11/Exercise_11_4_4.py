# Exercise 11.4-4 — CLRS
# EN: Show that if d = gcd(m, h2(k)) ≥ 1, unsuccessful search checks only m/d slots.
# PL: Pokaż, że jeśli d = NWD(m, h2(k)) ≥ 1, to wyszukiwanie kończące się porażką
#     sprawdza tylko m/d pozycji.

import math

def positions_checked(m, h2):
    d = math.gcd(m, h2)
    return m // d

if __name__ == "__main__":
    print("m=12, h2=4 → sprawdzonych pozycji:", positions_checked(12, 4))
