from itertools import product
from typing import Iterable, List, Tuple, TypeVar

T = TypeVar("T")
U = TypeVar("U")


def main(iterable1: Iterable[T], iterable2: Iterable[U]) -> List[Tuple[T, U]]:
    """
    :return: Descartes product of iterable1 and iterable2
    """
    return list(product(iterable1, iterable2))
