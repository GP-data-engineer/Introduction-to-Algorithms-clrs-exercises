# Exercise 4.3-9
# Solves the recurrence T(n) = 4T(n/2) + n^3
# This recurrence grows cubically and results in Θ(n^3)

from functools import lru_cache

@lru_cache(maxsize=None)
def recurrence_4_3_9(n):
    # Base case: constant time for n <= 1
    if n <= 1:
        return 1
    # Recursive case: four subproblems of size n/2 plus cubic cost
    return 4 * recurrence_4_3_9(n // 2) + n ** 3

if __name__ == "__main__":
    # Example usage: compute T(16)
    result = recurrence_4_3_9(16)
    print(f"Result for T(16): {result}")

import matplotlib.pyplot as plt

# Apply clean style
plt.style.use('seaborn-v0_8')

# Define n values and corresponding T(n) values for each recurrence
n_values = [1, 2, 4, 8, 16]
T1 = [1, 3, 7, 15, 31]
T2 = [1, 2, 3, 4, 5]
T3 = [1, 4, 12, 32, 80]
T4 = [1, 6, 28, 120, 496]
T5 = [1, 8, 64, 320, 1280]
T6 = [1, 10, 82, 658, 5314]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(n_values, T1, marker='o', label='T1: T(n/2) + n (O(n))')
plt.plot(n_values, T2, marker='s', label='T2: T(n/2) + 1 (O(log n))')
plt.plot(n_values, T3, marker='^', label='T3: 2T(n/2) + n (O(n log n))')
plt.plot(n_values, T4, marker='D', label='T4: 4T(n/2) + n (O(n^2))')
plt.plot(n_values, T5, marker='v', label='T5: 4T(n/2) + n^2 (O(n^2 log n))')
plt.plot(n_values, T6, marker='X', label='T6: 4T(n/2) + n^3 (O(n^3))')

# Add labels and title
plt.xlabel('n values')
plt.ylabel('T(n) values')
plt.title('Growth Comparison of Recurrence Relations')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save the plot
output_path = 'recurrence_growth_comparison_exercise_4_3_9_plot.png'
plt.savefig(output_path)
plt.close()
