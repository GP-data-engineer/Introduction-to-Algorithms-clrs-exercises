"""
Exercise 5.4-2
English: Balls are thrown into b bins uniformly at random. What is the expected number of throws
until some bin contains two balls?
Polish: Kule są wrzucane do b urn. Jaka jest oczekiwana liczba rzutów,
zanim w którejś urnie znajdą się dwie kule?
"""

# Polish description:
# To klasyczny problem "birthday paradox".
# Oczekiwana liczba rzutów ≈ √(πb/2).

import math

def expected_throws_until_collision(b: int):
    return math.sqrt(math.pi * b / 2)

if __name__ == "__main__":
    print("Exercise 5.4-2 Result:")
    print("Expected throws until collision (b=365):", expected_throws_until_collision(365))
