from re import findall
from typing import List


def main(s: str) -> List[str]:
    """

    :return: All two-digit numbers.

    >>> main('99a11b22cc8c777c66')
    ['99', '11', '22', '66']
    """
    return findall(r"(?<!\d)\d\d(?!\d)", s)
