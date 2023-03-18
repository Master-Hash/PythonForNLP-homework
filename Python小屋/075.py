from math import gcd
from functools import reduce
from typing import Literal, Union

# 参考 059.py


def main(*integers: int) -> Union[int, Literal["必须提供至少一个整数", "必须都是整数"]]:
    """
    implement gcd of multiple integers
    """
    if not integers:
        return "必须提供至少一个整数"
    if not all(isinstance(i, int) for i in integers):
        return "必须都是整数"
    return reduce(gcd, integers)
