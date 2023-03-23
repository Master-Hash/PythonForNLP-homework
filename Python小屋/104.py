import re
from typing import List
from doctest import testmod


def main(s: str) -> List[str]:
    """Get all AABB-pattern strings.

    :param s: the original string.
    :return: all AABB-pattern strings.

    >>> main('abcd aabb 兢兢业业 aaaa')
    ['aabb', '兢兢业业']
    """
    w = s.split()
    return [i for i in w if re.findall(r"(\S)\1(?!\1)(\S)\2", i)]


if __name__ == "__main__":
    testmod()
