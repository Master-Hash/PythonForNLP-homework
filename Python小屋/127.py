from functools import partial
from math import isclose
from typing import Iterable, Union

_isclose = partial(isclose, abs_tol=1)


def main(
    iterable1: Iterable[Union[int, float]], iterable2: Iterable[Union[int, float]]
) -> bool:
    return all(_isclose(x, y) for x, y in zip(iterable1, iterable2))
