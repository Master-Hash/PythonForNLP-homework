from operator import mul
from typing import List
from functools import reduce


def main(lst: List[int]) -> int:
    """
    :return: prod of all numbers in lst
    """
    return reduce(mul, lst)
