# Exercise 10.3-5 — CLRS
# EN: Implement COMPACTIFY-LIST to move list elements to positions 1..n and update free list.
# PL: Zaimplementuj COMPACTIFY-LIST, przesuwając elementy listy na pozycje 1..n i aktualizując listę wolnych pozycji.

def compactify_list(L, F, m):
    n = len(L["key"])
    for i in range(n):
        # Przesuwamy dane na pozycje 0..n-1
        L["key"][i] = L["key"][i]
        L["prev"][i] = i - 1 if i > 0 else None
        L["next"][i] = i + 1 if i < n - 1 else None

    # Aktualizujemy listę wolnych pozycji
    F["free"] = list(range(n, m))
    return L, F

if __name__ == "__main__":
    L = {"key": [10, 20, 30], "prev": [None, 0, 1], "next": [1, 2, None]}
    F = {"free": [3, 4, 5]}
    L, F = compactify_list(L, F, 6)
    print("Po kompaktyfikacji:", L, F)
