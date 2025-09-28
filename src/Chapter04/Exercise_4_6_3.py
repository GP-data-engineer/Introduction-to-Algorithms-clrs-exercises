"""
Exercise 4.6-3
Show that the assumption in Case 3 of the Master Theorem is too strong,
because the regularity condition a f(n/b) ≤ c f(n) for some c < 1
implies that there exists ε > 0 such that f(n) = Ω(n^(log_b a + ε)).
"""

# Polish description:
# Warunek regularności jest silny: jeśli af(n/b) ≤ cf(n), to f(n) rośnie szybciej
# niż n^(log_b a). Wtedy istnieje ε > 0 takie, że f(n) = Ω(n^(log_b a + ε)).
# Funkcja zwraca opis tego faktu.

def regularity_implication():
    return "If regularity holds, then f(n) = Ω(n^(log_b a + ε)) for some ε > 0."

if __name__ == "__main__":
    print("Exercise 4.6-3 Result:")
    print(regularity_implication())
