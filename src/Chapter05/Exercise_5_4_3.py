"""
Exercise 5.4-3
English: For birthdays to be independent, do we need mutual independence or just pairwise independence?
Polish: Czy dla urodzin wystarczy niezależność parami, czy potrzebna jest pełna niezależność?
"""

# Polish description:
# Wystarczy pełna niezależność, bo para-niezależność nie gwarantuje poprawnych wyników
# w problemie urodzin. Odpowiedź: potrzebna jest niezależność wzajemna.

def independence_requirement():
    return "Mutual independence is required, pairwise independence is not enough."

if __name__ == "__main__":
    print("Exercise 5.4-3 Result:")
    print(independence_requirement())
