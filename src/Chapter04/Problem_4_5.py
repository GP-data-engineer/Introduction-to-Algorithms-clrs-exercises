"""
Simulation for Problem 4-5 (Testing Integrated Circuits)

We assume:
- Each circuit can be either "good" (always tells the truth) or "bad" (may lie arbitrarily).
- More than half of the circuits are good.
- Goal: find one good circuit, then identify all good circuits.

Algorithm:
1. Pair circuits and eliminate according to the rules:
   - If either says the other is bad -> discard both.
   - If both say the other is good -> keep one.
   This reduces the problem size by ~half.
2. Repeat until one candidate remains -> this candidate is guaranteed to be good.
3. Use this good circuit to test all others and identify the good ones.
"""

import random

class Circuit:
    def __init__(self, is_good: bool):
        self.is_good = is_good

    def test(self, other: "Circuit") -> bool:
        """
        Good circuit: always tells the truth.
        Bad circuit: may lie (here we simulate random lying).
        Returns True if 'other' is declared good, False if declared bad.
        """
        if self.is_good:
            return other.is_good
        else:
            # Bad circuit may lie randomly
            return random.choice([True, False])

def find_good_circuit(circuits):
    """
    Step 1: Pairing and elimination to find one good circuit.
    """
    candidates = circuits[:]
    while len(candidates) > 1:
        new_candidates = []
        for i in range(0, len(candidates) - 1, 2):
            A, B = candidates[i], candidates[i+1]
            if A.test(B) and B.test(A):
                # Both say "good" -> keep one
                new_candidates.append(A)
            # Otherwise discard both
        if len(candidates) % 2 == 1:
            # If odd number, carry last one forward
            new_candidates.append(candidates[-1])
        candidates = new_candidates
    return candidates[0]

def identify_all_good(circuits):
    """
    Step 2: Use the found good circuit to test all others.
    """
    good_circuit = find_good_circuit(circuits)
    good_list = [c for c in circuits if good_circuit.test(c)]
    return good_list

if __name__ == "__main__":
    # Example: 10 circuits, 7 good, 3 bad
    circuits = [Circuit(True) for _ in range(7)] + [Circuit(False) for _ in range(3)]
    random.shuffle(circuits)

    good_one = find_good_circuit(circuits)
    print("Found good circuit:", good_one.is_good)

    all_good = identify_all_good(circuits)
    print("Identified good circuits:", len(all_good), "out of", len(circuits))
