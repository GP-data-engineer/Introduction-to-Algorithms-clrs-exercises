"""
Exercise 5.3-5
English: Prove that in PERMUTE-BY-SORTING, the probability that all priorities are distinct
is at least 1 - 1/n.
Polish: Udowodnij, że w PERMUTE-BY-SORTING prawdopodobieństwo, że wszystkie priorytety są różne,
wynosi co najmniej 1 - 1/n.
"""

# Polish description:
# W PERMUTE-BY-SORTING losujemy priorytety z dużego zakresu.
# Prawdopodobieństwo kolizji ≤ 1/n, więc prawdopodobieństwo unikalności ≥ 1 - 1/n.

def distinct_priorities_probability(n: int):
    return 1 - 1/n

if __name__ == "__main__":
    print("Exercise 5.5 Result:")
    print("Probability all priorities distinct (n=10):", distinct_priorities_probability(10))
