from doctest import testmod
from typing import Any, Iterable, List


def main(*iterables: Iterable[Any]) -> List[Any]:
    """
    >>> main([1, 2, 3], '456', (7, 8, 9))
    [2, '5', 8]
    """
    return [list(i) for i in zip(*iterables)][1]


if __name__ == "__main__":
    testmod()
