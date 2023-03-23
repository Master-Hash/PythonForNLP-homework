from typing import Tuple, Literal, Union
from functools import reduce


def main(
    *tups: Tuple[Union[int, float, complex], ...]
) -> Union[Tuple[Union[int, float, complex], ...], Literal["数据不符合要求"]]:
    if not all(isinstance(tup, tuple) for tup in tups):
        return "数据不符合要求"
    if reduce(lambda x, y: x if x == y else None, map(len, tups)) is None:
        return "数据不符合要求"
    if not all(isinstance(num, (int, float, complex)) for tup in tups for num in tup):
        return "数据不符合要求"
    return tuple(sum(x) for x in zip(*tups))
