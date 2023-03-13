from math import gcd
from functools import reduce


def main(lst: list[int]) -> int:
    """
    最大公约数
    Python 3.9 以后，`math.gcd` 支持任意多个参数
    """
    return reduce(gcd, lst)
