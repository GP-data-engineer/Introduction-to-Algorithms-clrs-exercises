# Exercise 4.3-1
# Solve T(n) = T(n/2) + n and show that the solution is O(n)

def recurrence_4_3_1(n):
    # Base case
    if n <= 1:
        return 1
    # Recursive case: T(n) = T(n/2) + n
    return recurrence_4_3_1(n // 2) + n

if __name__ == "__main__":
    # Demonstration for n = 16
    result = recurrence_4_3_1(16)
    print(f"Result for T(16): {result}")
