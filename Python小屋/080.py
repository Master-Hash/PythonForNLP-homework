from typing import List


def main(a: List[int], b: List[int]) -> int:
    """_summary_

    :param a: _description_
    :param b: _description_
    :return: sum of abs(a[i] - b[i])
    """
    return sum(map(lambda a, b: abs(a - b), a, b))
