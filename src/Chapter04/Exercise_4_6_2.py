"""
Exercise 4.6-2
Show that if f(n) = Θ(n^(log_b a) log^k n), with k ≥ 0,
then the recurrence has solution T(n) = Θ(n^(log_b a) log^(k+1) n).
"""

# Polish description:
# Zgodnie z twierdzeniem uniwersalnym, jeśli f(n) = Θ(n^(log_b a) log^k n),
# to rozwiązanie rekurencji to T(n) = Θ(n^(log_b a) log^(k+1) n).
# Funkcja zwraca tę postać jako string.

def recurrence_solution(k: int):
    return f"Θ(n^(log_b a) log^{k+1} n)"

if __name__ == "__main__":
    print("Exercise 4.6-2 Result:")
    print("For k=0:", recurrence_solution(0))
    print("For k=2:", recurrence_solution(2))
