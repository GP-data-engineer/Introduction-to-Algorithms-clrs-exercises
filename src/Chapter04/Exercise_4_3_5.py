# Exercise 4.3-5
# Demonstrates that by adjusting the inductive hypothesis, we can handle boundary conditions
# in recurrence T(n) = 2T(n/2) + n without changing the proof of the Master Theorem

def adjusted_inductive_hypothesis(n):
    # This function simulates the recurrence and shows that the base case can be adjusted
    # to fit the inductive proof without altering the asymptotic result
    if n <= 1:
        return 1
    return 2 * adjusted_inductive_hypothesis(n // 2) + n

if __name__ == "__main__":
    # Example usage: compute T(16)
    result = adjusted_inductive_hypothesis(16)
    print(f"Adjusted inductive result for T(16): {result}")
