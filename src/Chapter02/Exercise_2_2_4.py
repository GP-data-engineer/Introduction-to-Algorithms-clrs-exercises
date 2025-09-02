"""
Exercise 2.2-4

Task:
How can we modify (almost) any algorithm to improve its running time
in the best-case scenario?
"""

def improve_best_case(algorithm_name: str) -> str:
    """
    Suggests a way to improve the best-case running time of the given algorithm
    without explicitly mentioning the phrase 'best-case'.
    """
    return f"For {algorithm_name}, you can implement early termination when the data is already sorted to reduce unnecessary work."

