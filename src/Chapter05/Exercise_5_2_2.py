"""
Exercise 5.2.2
English: Probability of hiring exactly two people in HIRE-ASSISTANT with random order.
Polish: Prawdopodobieństwo zatrudnienia dokładnie dwóch osób w HIRE-ASSISTANT przy losowej kolejności.
"""

def hire_two_probability(n: int):
    return 1 / n

if __name__ == "__main__":
    print("Exercise 5.2.2 Result:")
    print("Probability of hiring exactly two people (n=5):", hire_two_probability(5))
