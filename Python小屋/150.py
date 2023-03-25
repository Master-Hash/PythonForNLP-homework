import re
from doctest import testmod
from typing import List


def main(s: str) -> List[str]:
    """
    :return: All words following the word "than".

    >>> main('I am taller than you.')
    ['you']
    """
    return re.findall(r"than\s+(\w+)", s)


if __name__ == "__main__":
    testmod()
