"""
Exercise 7.3-1 (CLRS, 4th Edition)
----------------------------------
Pytanie:
Dlaczego analizujemy *oczekiwany czas działania* algorytmu randomizowanego,
a nie jego *pesymistyczny czas działania*?

Odpowiedź:
Pesymistyczny (najgorszy) przypadek dla algorytmu randomizowanego
zazwyczaj ma znikome prawdopodobieństwo wystąpienia.
Analizujemy więc *oczekiwany czas działania*, który odzwierciedla
średni koszt obliczeń dla wszystkich możliwych wyników losowań.

Przykład:
W algorytmie RANDOMIZED-QUICKSORT najgorszy przypadek (T(n)=Θ(n²))
występuje, gdy za każdym razem wybierany jest skrajny element jako pivot.
Jednak oczekiwany czas działania to Θ(n log n),
ponieważ losowy wybór pivotu równomiernie rozkłada podziały tablicy.
"""

def explanation() -> str:
    return (
        "Analizujemy oczekiwany czas działania, ponieważ pesymistyczny "
        "czas ma bardzo małe prawdopodobieństwo wystąpienia. "
        "Oczekiwany czas Θ(n log n) dobrze opisuje praktyczną wydajność "
        "RANDOMIZED-QUICKSORT, podczas gdy pesymistyczny Θ(n²) jest mało realistyczny."
    )


if __name__ == "__main__":
    print(explanation())
