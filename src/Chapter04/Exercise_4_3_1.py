# Exercise 4.3-1
# This function solves the recurrence relation T(n) = T(n/2) + n
# It demonstrates that the time complexity is O(n)

def recurrence_4_3_1(n):
    # Base case: for n <= 1, return constant time
    if n <= 1:
        return 1
    # Recursive case: divide the problem size by 2 and add linear cost
    return recurrence_4_3_1(n // 2) + n

if __name__ == "__main__":
    # Example usage: compute T(16)
    result = recurrence_4_3_1(16)
    print(f"Result for T(16): {result}")

