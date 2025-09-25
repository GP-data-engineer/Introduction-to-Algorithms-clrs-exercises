"""
Exercise 4.5-3
Solve recurrence T(n) = 2T(n/2) + n log n
Expected solution: T(n) = Θ(n log log n)
"""

# Polish description:
# Rozwiązanie rekurencji T(n) = 2T(n/2) + n log n przy użyciu metody uniwersalnej.
# Wynik to Θ(n log log n).

def recurrence_solution():
    return "Θ(n log log n)"

if __name__ == "__main__":
    print("Exercise 4.5-3 Result:")
    print(recurrence_solution())
