from math import factorial


def main(n: int, i: int) -> int:
    """
    Returns:
    int: how many ways to choose i from n
    """
    return factorial(n) // (factorial(i) * factorial(n - i))
