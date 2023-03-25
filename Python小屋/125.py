from doctest import testmod
from itertools import zip_longest
from typing import Iterable, List, Literal, Tuple, TypeVar, Union

T = TypeVar("T")
U = TypeVar("U")


def main(
    iterable1: Iterable[T], iterable2: Iterable[U]
) -> List[Tuple[Union[T, Literal[0]], Union[U, Literal[0]]]]:
    """
    >>> main([1, 2, 3, 4], '456')
    [(1, '4'), (2, '5'), (3, '6'), (4, 0)]

    >>> main('123', [5, 6, 7, 8])
    [('1', 5), ('2', 6), ('3', 7), (0, 8)]
    """
    return list(zip_longest(iterable1, iterable2, fillvalue=0))


if __name__ == "__main__":
    testmod()
