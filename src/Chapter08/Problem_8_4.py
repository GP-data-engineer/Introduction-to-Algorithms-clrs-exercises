"""
Problem 8.4 (EN): Match red and blue jugs by capacity using only comparisons between red and blue jugs.
Problem 8.4 (PL): Dopasuj czerwone i niebieskie dzbanki według pojemności, używając tylko porównań między dzbankami różnych kolorów.
"""

import random

def compare_jugs(red, blue):
    """
    Porównuje pojemność czerwonego i niebieskiego dzbanka.
    Zwraca -1 jeśli red < blue, 0 jeśli równe, 1 jeśli red > blue.
    """
    if red < blue:
        return -1
    elif red > blue:
        return 1
    else:
        return 0

def match_jugs(red_jugs, blue_jugs):
    """
    Dopasowuje czerwone i niebieskie dzbanki w czasie oczekiwanym O(n log n),
    używając tylko porównań między czerwonymi i niebieskimi dzbankami.
    """
    if len(red_jugs) <= 1:
        return list(zip(red_jugs, blue_jugs))

    pivot_blue = random.choice(blue_jugs)
    less_red, equal_red, greater_red = [], [], []
    for r in red_jugs:
        cmp = compare_jugs(r, pivot_blue)
        if cmp == -1:
            less_red.append(r)
        elif cmp == 0:
            equal_red.append(r)
        else:
            greater_red.append(r)

    pivot_red = equal_red[0]
    less_blue, equal_blue, greater_blue = [], [], []
    for b in blue_jugs:
        cmp = compare_jugs(pivot_red, b)
        if cmp == -1:
            greater_blue.append(b)
        elif cmp == 0:
            equal_blue.append(b)
        else:
            less_blue.append(b)

    return match_jugs(less_red, less_blue) + [(pivot_red, pivot_blue)] + match_jugs(greater_red, greater_blue)

if __name__ == "__main__":
    red = [5, 3, 7, 1, 9]
    blue = [9, 1, 5, 3, 7]
    matched = match_jugs(red, blue)
    print("Dopasowane dzbanki (czerwony, niebieski):")
    for r, b in matched:
        print(f"{r} ↔ {b}")
