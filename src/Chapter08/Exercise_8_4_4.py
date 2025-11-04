"""
Zadanie 8.4.4 (PL): Sortuj n punktów rozmieszczonych jednostajnie w kole jednostkowym według ich odległości od środka. Algorytm powinien działać w czasie średnim Θ(n).

Exercise 8.4.4 (EN): Sort n points uniformly distributed in the unit circle by their distance from the origin. The algorithm should run in average-case time Θ(n).
"""

import math

def bucket_sort_points(points):
    """
    Sortuje punkty według ich odległości od środka układu współrzędnych.
    Zakłada jednostajny rozkład w kole jednostkowym.
    """
    n = len(points)
    buckets = [[] for _ in range(n)]

    for x, y in points:
        d = math.sqrt(x**2 + y**2)
        index = min(n - 1, int(d * n))  # Skalowanie do indeksu koszyka
        buckets[index].append((x, y))

    # Sortowanie lokalne w koszykach
    sorted_points = []
    for bucket in buckets:
        sorted_points.extend(sorted(bucket, key=lambda p: math.sqrt(p[0]**2 + p[1]**2)))

    return sorted_points

if __name__ == "__main__":
    import random
    random.seed(42)
    points = [(random.uniform(-1, 1), random.uniform(-1, 1)) for _ in range(20)]
    points = [p for p in points if 0 < p[0]**2 + p[1]**2 <= 1]
    sorted_pts = bucket_sort_points(points)
    print("Posortowane punkty według odległości od środka:")
    for pt in sorted_pts:
        print(f"{pt} -> d={math.sqrt(pt[0]**2 + pt[1]**2):.3f}")
