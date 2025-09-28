"""
Exercise 5.2.1
English: Assuming candidates arrive in random order, what is the probability
that the HIRE-ASSISTANT procedure hires exactly one person? Exactly two people?
Polish: Zakładając losową kolejność kandydatów, jakie jest prawdopodobieństwo,
że procedura HIRE-ASSISTANT zatrudni dokładnie jedną osobę? Dokładnie dwie osoby?
"""

# Polish description:
# W procedurze HIRE-ASSISTANT zawsze zatrudniamy pierwszego kandydata.
# Dokładnie jedna osoba zostanie zatrudniona, jeśli najlepszy kandydat przyjdzie jako pierwszy.
# Dokładnie dwie osoby zostaną zatrudnione, jeśli najlepszy kandydat przyjdzie jako drugi.

def hire_probabilities(n: int):
    p_one = 1 / n
    p_two = 1 / n
    return p_one, p_two

if __name__ == "__main__":
    print("Exercise 5.2.1 Result:")
    print("Probabilities (exactly one, exactly two):", hire_probabilities(5))
