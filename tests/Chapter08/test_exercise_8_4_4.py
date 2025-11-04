"""
Testy do zadania 8.4.4 (PL): Sprawdzamy poprawność sortowania punktów według odległości od środka.

Tests for Exercise 8.4.4 (EN): Verifies correct sorting of points by distance from origin.
"""

import pytest
from src.Chapter08.Exercise_8_4_4 import bucket_sort_points
import math

def test_sorted_distances():
    points = [(0.1, 0.1), (0.5, 0.5), (0.9, 0.0)]
    sorted_pts = bucket_sort_points(points)
    distances = [math.sqrt(x**2 + y**2) for x, y in sorted_pts]
    assert distances == sorted(distances)

def test_preserves_all_points():
    points = [(0.3, 0.4), (0.6, 0.2), (0.1, 0.9)]
    sorted_pts = bucket_sort_points(points)
    assert set(sorted_pts) == set(points)
