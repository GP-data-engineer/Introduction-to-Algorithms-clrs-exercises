"""
Exercise 5.4-5
English: Relation between k-show (k-permutation) and birthday paradox.
Polish: Związek między k-permutacją (k-show) a paradoksem urodzin.
"""

# Polish description:
# k-show to wybór k elementów bez powtórzeń.
# Związek: paradoks urodzin to przypadek k=2 (czy występuje powtórzenie).

def kshow_relation():
    return "Birthday paradox is a special case of k-show with k=2."

if __name__ == "__main__":
    print("Exercise 5.4-5 Result:")
    print(kshow_relation())
