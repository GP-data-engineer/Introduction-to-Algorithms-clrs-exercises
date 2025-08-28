"""
Exercise 2.2-4

Task:
How can we modify (almost) any algorithm to improve its running time
in the best-case scenario?
"""

def improve_best_case(algorithm_description: str) -> str:
    """
    Suggests a general modification to improve the best-case running time
    of an algorithm.

    Args:
        algorithm_description (str): Short description of the algorithm.

    Returns:
        str: Suggested modification.
    """
    return (
        f"For {algorithm_description}, you can add an early termination "
        "condition that checks if the desired result has been achieved "
        "before completing all steps. This can significantly improve "
        "the best-case running time."
    )
