from operator import mul
from typing import List


def main(values: List[int], weights: List[int]) -> float:
    """
    :return: Weighted average of values
    """
    return round(sum(map(mul, values, weights)) / sum(weights), 3)
