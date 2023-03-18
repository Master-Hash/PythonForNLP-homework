from functools import reduce
from typing import Tuple


def main(factors: Tuple[str, ...], x: int) -> int:
    """a0 * x^n + a1 * x^(n-1) + ... + an-1 * x + an
    :return: the result of the polynomial

    >>> main((3, 0, 1), 2)
    13

    >>> main((3, 0, 1), 3)
    28
    """
    return reduce(lambda a, b: a * x + b, factors)
