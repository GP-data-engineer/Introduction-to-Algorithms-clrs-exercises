"""
Explanation (in Polish):

Stwierdzenie „Czas działania algorytmu A wynosi co najmniej O(n²)” nie ma sensu,
ponieważ notacja O (Big-O) opisuje górne ograniczenie asymptotyczne funkcji,
a nie dolne. Oznacza to, że O(n²) to zbiór funkcji, które rosną nie szybciej
niż n² (z dokładnością do stałej i dla dużych n).

Jeżeli chcemy wyrazić dolne ograniczenie, powinniśmy użyć notacji Ω (Big-Omega),
która opisuje asymptotyczne ograniczenie od dołu.

Poprawne sformułowanie:
    „Czas działania algorytmu A wynosi co najmniej Ω(n²)”
"""

def explain_statement_meaning() -> str:
    """
    Returns an explanation why the statement
    'running time is at least O(n^2)' is meaningless.
    """
    return (
        "The statement 'running time is at least O(n^2)' is meaningless because "
        "Big-O notation describes an upper bound, not a lower bound. "
        "To express a lower bound, Big-Omega notation should be used."
    )

if __name__ == "__main__":
    # Demonstration
    print("Exercise 3.1.3 explanation:")
    print(explain_statement_meaning())
