from typing import Iterable, Tuple, TypeVar

T = TypeVar("T")


def main(iterable: Iterable[T]) -> Tuple[Tuple[int, T]]:
    """
    >>> main([1, 2, 3, 4, 5])
    ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))
    """
    return tuple(enumerate(iterable, 1))
