"""
Exercise 5.4-4
English: How many people are needed so that probability > 1/2 that at least two share a birthday?
Polish: Ile osób potrzeba, aby prawdopodobieństwo > 1/2, że dwie osoby mają te same urodziny?
"""

# Polish description:
# Klasyczny paradoks urodzin: minimalna liczba osób = 23.

def min_people_birthday_paradox():
    return 23

if __name__ == "__main__":
    print("Exercise 5.4-4 Result:")
    print("Minimum people needed:", min_people_birthday_paradox())
