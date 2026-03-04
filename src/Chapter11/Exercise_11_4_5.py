# Exercise 11.4-5 — CLRS
# EN: Find load factors α for which expected probes remain constant.
# PL: Znajdź współczynniki zapełnienia α, dla których liczba sprawdzeń jest stała.

def good_alpha():
    # Z twierdzeń 11.6 i 11.8:
    # sukces: ≤ (1/α) ln(1/(1-α))
    # porażka: ≤ 1/(1-α)
    # Stałe wartości → α < 0.5
    return [0.25, 0.33, 0.4, 0.45]

if __name__ == "__main__":
    print("Dobre wartości α:", good_alpha())
