from src.Chapter07.Exercise_7_3_2 import random_call_count

def test_random_call_count_linear_growth():
    n_values = [5, 10, 20]
    counts = [random_call_count(n) for n in n_values]
    # liczba wywołań powinna rosnąć liniowo
    assert counts[2] > counts[1] > counts[0]
    # liczba wywołań zbliżona do n
    for n, c in zip(n_values, counts):
        assert abs(c - n) <= n * 0.3  # tolerancja ±30%
