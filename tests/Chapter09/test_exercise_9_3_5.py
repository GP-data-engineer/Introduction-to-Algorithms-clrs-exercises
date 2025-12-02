# Test for Exercise 9.3-5 (EN): Verifies order statistic via black-box median.
# Test do Exercise 9.3-5 (PL): Sprawdza statystykę pozycyjną przez czarną skrzynkę mediany.

import pytest
from src.Chapter09.Exercise_9_3_5 import order_statistic_via_median_box

def test_statistic_correctness():
    A = [3, 2, 9, 0, 7, 5, 4, 8, 6, 1]
    assert order_statistic_via_median_box(A, 1) == 0
    assert order_statistic_via_median_box(A, 5) == 4
    assert order_statistic_via_median_box(A, 10) == 9
