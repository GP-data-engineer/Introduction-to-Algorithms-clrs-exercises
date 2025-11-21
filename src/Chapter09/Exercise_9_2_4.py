# Exercise 9.2-4 (EN): Describe the worst-case partition sequence of RANDOMIZED-SELECT when finding the minimum.
# Exercise 9.2-4 (PL): Opisz pesymistyczny ciąg podziałów algorytmu RANDOMIZED-SELECT przy wyszukiwaniu minimum.

def worst_case_randomized_select_trace(A, i):
    # Symuluje pesymistyczny przebieg RANDOMIZED-SELECT dla minimum
    trace = []
    low = 0
    high = len(A) - 1
    while low <= high:
        pivot_index = high  # najgorszy przypadek: pivot to największy
        pivot = A[pivot_index]
        trace.append((A[low:high+1], pivot))
        # wszystkie elementy mniejsze trafiają na lewo
        high = pivot_index - 1
    return trace

if __name__ == "__main__":
    A = [3, 2, 9, 0, 7, 5, 4, 8, 6, 1]
    trace = worst_case_randomized_select_trace(A.copy(), 1)
    print("Pesymistyczny przebieg RANDOMIZED-SELECT dla minimum:")
    for step, pivot in trace:
        print(f"Podział: {step}, pivot: {pivot}")
