# Exercise_8_3_5.py
# PL:
# Zadanie 8.3-5:
# Ile faz potrzeba w najgorszym przypadku do posortowania d-cyfrowych liczb
# dziesiętnych, jeśli zastosujemy pierwszy z opisanych w tym podrozdziale
# algorytmów sortujących karty? Ile może się w tym czasie pojawić tymczasowych plików kart?
#
# EN:
# Exercise 8.3-5:
# How many passes (phases) are needed in worst case to sort d-digit decimal numbers
# using the "first described" card-sorting algorithm in the section (i.e., LSD radix by digits)?
# How many temporary piles/files of cards may appear?
#
# Odpowiedź (intuicyjna):
# - Liczba faz = d (one pass per digit, from least significant to most).
# - Liczba tymczasowych plików = base = 10 (one pile per digit value 0..9).
#
# Implementacja:
# - functions that compute these values and simulate piles usage.

def phases_and_piles_for_decimal(d: int) -> tuple:
    """
    Return (phases, piles) for digit count d in decimal system.
    """
    if d < 0:
        raise ValueError("d must be non-negative")
    phases = d
    piles = 10  # decimal digits 0..9
    return phases, piles

def simulate_radix_piles_decimal(numbers: list, d: int):
    """
    Simulate LSD passes showing piles counts at each pass (only to illustrate).
    """
    piles_history = []
    base = 10
    A = list(numbers)
    for pos in range(d):
        piles = [[] for _ in range(base)]
        for x in A:
            digit = (x // (10 ** pos)) % 10
            piles[digit].append(x)
        piles_history.append([len(p) for p in piles])
        # collect back
        A = [x for bucket in piles for x in bucket]
    return piles_history

if __name__ == "__main__":
    d = 4
    phases, piles = phases_and_piles_for_decimal(d)
    print(f"d={d} -> phases={phases}, piles={piles}")
    # simulate
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    print("simulation piles history:", simulate_radix_piles_decimal(arr, 3))
