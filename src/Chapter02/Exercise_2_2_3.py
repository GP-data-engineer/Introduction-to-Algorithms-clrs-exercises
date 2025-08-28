"""
Exercise 2.2-3

Task:
Consider the linear search algorithm (see Exercise 2.1-3).
How many elements of the input sequence are checked on average
when searching for a random element in the array?
What about in the worst case?
What are the running times of this algorithm, expressed in Θ-notation,
for the average and worst cases? Justify your answer.
"""

def linear_search_analysis(n: int) -> dict:
    """
    Analyzes the average and worst-case performance of linear search.

    Args:
        n (int): Number of elements in the array.

    Returns:
        dict: Dictionary containing:
            - average_checks: Expected number of elements checked on average.
            - worst_checks: Number of elements checked in the worst case.
            - average_case_time: Θ-notation for average case.
            - worst_case_time: Θ-notation for worst case.
    """
    average_checks = (n + 1) / 2
    worst_checks = n
    return {
        "average_checks": average_checks,
        "worst_checks": worst_checks,
        "average_case_time": "Θ(n)",
        "worst_case_time": "Θ(n)"
    }
