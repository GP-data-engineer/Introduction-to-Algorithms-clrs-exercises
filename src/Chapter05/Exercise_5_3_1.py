"""
Exercise 5.3-1
English: Modify RANDOMIZE-IN-PLACE so that the loop invariant is valid before the first iteration,
and adapt the proof of Lemma 5.5 accordingly.
Polish: Zmień RANDOMIZE-IN-PLACE tak, aby niezmiennik pętli był prawdziwy przed pierwszą iteracją
i zmodyfikuj dowód lematu 5.5.
"""

# Polish description:
# Standardowy RANDOMIZE-IN-PLACE zaczyna od pustej podtablicy.
# Modyfikacja: zaczynamy od i=0 i zamieniamy element z losowym z całej tablicy,
# dzięki czemu niezmiennik (podtablica jest permutacją) jest spełniony od początku.

import random

def randomize_in_place(A):
    n = len(A)
    for i in range(n):
        j = random.randint(i, n-1)
        A[i], A[j] = A[j], A[i]
    return A

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print("Exercise 5.3-1 Result:")
    print("Randomized array:", randomize_in_place(arr))
