# Test for Exercise 10.3-3 — CLRS
# EN: Verify that ALLOCATE-OBJECT and FREE-OBJECT do not modify the prev field.
# PL: Sprawdź, że ALLOCATE-OBJECT i FREE-OBJECT nie modyfikują pola prev.

import pytest
from src.Chapter10.Exercise_10_3_3 import MemoryManager

def test_prev_field_unchanged():
    mm = MemoryManager(4)
    initial_prev = mm.prev.copy()

    # Alokujemy dwa obiekty
    i1 = mm.allocate_object("A")
    i2 = mm.allocate_object("B")

    # Zwalniamy jeden obiekt
    mm.free_object(i1)

    # Alokujemy ponownie
    i3 = mm.allocate_object("C")

    # Pole prev nie powinno się zmienić
    assert mm.prev == initial_prev, "Pole prev zostało zmodyfikowane, co nie powinno mieć miejsca"

def test_allocation_and_free_logic():
    mm = MemoryManager(3)
    i1 = mm.allocate_object("X")
    i2 = mm.allocate_object("Y")
    mm.free_object(i1)
    i3 = mm.allocate_object("Z")
    assert i3 == i1, "Zwolniona pozycja nie została ponownie użyta"
    assert mm.key[i3] == "Z"
