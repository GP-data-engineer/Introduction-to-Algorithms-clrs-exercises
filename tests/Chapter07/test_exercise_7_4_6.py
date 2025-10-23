# test_exercise_7_4_6.py
# Tests for Exercise_7_4_6.py

from src.Chapter06 import Exercise_7_4_6 as ex

def test_theoretical_and_simulation_agree():
    n = 101
    for alpha in [0.05, 0.1, 0.2]:
        theo = ex.theoretical_probability_bad_split(n, alpha)
        sim = ex.simulate_median_of_three(n, alpha, trials=5000)
        # Allow some sampling error
        assert abs(theo - sim) < 0.05

def test_probability_decreases_with_alpha():
    n = 101
    p1 = ex.theoretical_probability_bad_split(n, 0.05)
    p2 = ex.theoretical_probability_bad_split(n, 0.10)
    # As alpha grows, the "bad region" grows so probability of being in bad region should not decrease.
    assert p2 >= p1
