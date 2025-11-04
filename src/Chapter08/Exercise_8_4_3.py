# Exercise 8.4-3 (CLRS)
# English: Let X be the number of heads obtained in two flips of a fair coin. Find E[X^2] and (E[X])^2.
# Polish: Niech X będzie liczbą orłów uzyskanych w dwóch rzutach symetryczną monetą. Znajdź E[X^2] i (E[X])^2.

def expected_values():
    """Compute E[X], E[X^2], and (E[X])^2 for two fair coin tosses."""
    # Possible outcomes for X: 0, 1, 2
    outcomes = [0, 1, 2]
    probabilities = [1/4, 1/2, 1/4]

    E_X = sum(x * p for x, p in zip(outcomes, probabilities))
    E_X2 = sum((x**2) * p for x, p in zip(outcomes, probabilities))
    E_X_squared = E_X ** 2

    return E_X, E_X2, E_X_squared

if __name__ == "__main__":
    E_X, E_X2, E_X_squared = expected_values()
    print(f"E[X] = {E_X}")
    print(f"E[X^2] = {E_X2}")
    print(f"(E[X])^2 = {E_X_squared}")
