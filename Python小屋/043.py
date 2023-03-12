from itertools import permutations
from functools import reduce, partial
from typing import Callable, Any


def compose(*funcs: Callable[[Any], Any]) -> Callable[[Any], Any]:
    def _compose(
        f: Callable[[Any], Any], g: Callable[[Any], Any]
    ) -> Callable[[Any], Any]:
        return lambda x: f(g(x))

    return reduce(_compose, funcs)


def main(lst: list[int]) -> int:
    return compose(
        max,
        partial(map, int),
        partial(map, "".join),
        permutations,
        partial(map, str),
    )(lst)
