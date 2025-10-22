# test_exercise_7_4_1.py
# Tests for Exercise_7_4_1.py

from src.Chapter06 import Exercise_7_4_1 as ex

def test_simulated_vs_lower_bound_grows_quadratically():
    # For increasing n, both lower bound and simulated T(n) should grow ~ n^2
    ns = [5, 10, 20]
    ratios = []
    for n in ns:
        sim = ex.simulate_recurrence(n, c=1.0, a=1.0, b=0.0)
        ratios.append(sim / (n * n))
    # ratios should not shrink to zero and should be roughly similar (Ω(n^2))
    assert ratios[0] > 0
    assert ratios[1] > 0
    assert ratios[2] > 0
    assert ratios[2] >= ratios[0] * 0.5  # rough sanity
