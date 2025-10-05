"""
Exercise 5.4-7
English: Show that if k > sqrt(2n ln n), probability of birthday collision > 1/2,
and if k < sqrt(2n ln n), probability < 1/2.
Polish: Pokaż, że jeśli k > √(2n ln n), to prawdopodobieństwo kolizji urodzin > 1/2,
a jeśli k < √(2n ln n), to prawdopodobieństwo < 1/2.
"""

# Polish description:
# To klasyczny wynik analizy paradoksu urodzin.
# Funkcja zwraca warunek progowy.

import math

def birthday_threshold(n: int):
    return math.sqrt(2 * n * math.log(n))

if __name__ == "__main__":
    print("Exercise 5.4-7 Result:")
    print("Threshold k for n=365:", birthday_threshold(365))
