# Exercise 4.3-2
# This function solves the recurrence relation T(n) = T(n/2) + 1
# It demonstrates that the time complexity is O(log n)

def recurrence_4_3_2(n):
    # Base case: constant time for n <= 1
    if n <= 1:
        return 1
    # Recursive case: divide problem size by 2 and add constant cost
    return recurrence_4_3_2(n // 2) + 1

if __name__ == "__main__":
    # Example usage: compute T(16)
    result = recurrence_4_3_2(16)
    print(f"Result for T(16): {result}")
