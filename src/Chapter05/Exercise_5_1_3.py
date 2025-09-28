"""
Exercise 5.1.3
English: Use BIASED-RANDOM (returns 1 with probability p, 0 with probability 1-p, p unknown)
to implement a fair coin (0 or 1 with probability 1/2).
Polish: Użyj BIASED-RANDOM (zwraca 1 z prawdopodobieństwem p, 0 z prawdopodobieństwem 1-p, p nieznane)
do implementacji uczciwego rzutu monetą (0 lub 1 z prawdopodobieństwem 1/2).
"""

# Polish description:
# Algorytm von Neumanna: wywołujemy BIASED-RANDOM dwa razy.
# Jeśli wyniki to (0,1) -> zwracamy 0, jeśli (1,0) -> zwracamy 1.
# W przeciwnym razie powtarzamy.

import random

def BIASED_RANDOM(p=0.7):
    return 1 if random.random() < p else 0

def FAIR_RANDOM(p=0.7):
    while True:
        a = BIASED_RANDOM(p)
        b = BIASED_RANDOM(p)
        if a == 0 and b == 1:
            return 0
        if a == 1 and b == 0:
            return 1

if __name__ == "__main__":
    print("Exercise 5.1.3 Result:")
    samples = [FAIR_RANDOM(0.7) for _ in range(20)]
    print("Fair random samples:", samples)
