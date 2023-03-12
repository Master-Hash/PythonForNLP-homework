from typing import TypeVar

T = TypeVar("T")


def main(lst: list[set[T]]) -> set[T]:
    """
    Returns:
    set: the intersection of all sets in lst
    """
    x, *xs = lst
    return x.union(*xs)
