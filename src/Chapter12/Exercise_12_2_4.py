# Exercise 12.2-4 — CLRS
# EN: Disprove Bunyan's BST property hypothesis.
# PL: Obal hipotezę profesora Bunyana o BST.

def bunyan_counterexample():
    return (
        "Kontrprzykład: BST z kluczami 5 → 3 → 7 → 2 → 4 → 6 → 8.\n"
        "Wyszukiwanie 1 kończy się w liściu, ale klucze po lewej i prawej stronie "
        "ścieżki nie spełniają a < b < c dla wszystkich kombinacji."
    )

if __name__ == "__main__":
    print(bunyan_counterexample())
