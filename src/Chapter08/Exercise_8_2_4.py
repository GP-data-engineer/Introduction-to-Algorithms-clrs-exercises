# Exercise_8_2_4.py
# PL:
# Zadanie 8.2-4:
# Zaprojektuj algorytm, który dla danych n liczb z przedziału 0..k wykonuje
# wstępne obliczenia, a następnie pozwala w czasie O(1) określić,
# ile spośród tych n liczb leży w przedziale [a..b].
# Algorytm musi wykonać wszystkie obliczenia wstępne w Theta(n + k).
#
# EN:
# Exercise 8.2-4:
# Design an algorithm that preprocesses n numbers from 0..k in Theta(n + k)
# and then answers queries "how many numbers lie in [a..b]" in O(1).
#
# Implementacja:
# - CountingPreprocessor class:
#     * build(A, k) : Theta(n+k) preprocessing to build prefix counts P
#     * query(a, b)  : O(1) returns count of elements in [a..b]
# - W __main__ przykład użycia i proste testy.

from typing import List

class CountingPreprocessor:
    def __init__(self):
        self.P = None  # prefix sums array
        self.k = None

    def build(self, A: List[int], k: int) -> None:
        """
        Build prefix-sum array P such that P[x] = number of elements <= x.
        Complexity Theta(n + k).
        """
        n = len(A)
        counts = [0] * (k + 1)
        for v in A:
            if v < 0 or v > k:
                raise ValueError("All elements must be in 0..k")
            counts[v] += 1
        # build prefix sums
        P = [0] * (k + 1)
        running = 0
        for i in range(k + 1):
            running += counts[i]
            P[i] = running
        self.P = P
        self.k = k

    def query(self, a: int, b: int) -> int:
        """
        Return count of elements in [a..b] in O(1).
        Handles out-of-range a,b by clipping.
        """
        if self.P is None:
            raise RuntimeError("Preprocessor not built")
        if a > b:
            return 0
        # clip
        a_clip = max(0, a)
        b_clip = min(self.k, b)
        if b_clip < a_clip:
            return 0
        if a_clip == 0:
            return self.P[b_clip]
        return self.P[b_clip] - self.P[a_clip - 1]

if __name__ == "__main__":
    A = [2, 5, 3, 2, 0, 10, 7, 5, 3, 2]
    k = 10
    cp = CountingPreprocessor()
    cp.build(A, k)
    queries = [(0, 2), (2, 3), (4, 6), (0, 10), (8, 12)]
    print("A:", A)
    for a, b in queries:
        print(f"Count in [{a},{b}] = {cp.query(a, b)}")
