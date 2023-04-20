# see also #047

from doctest import testmod
from math import cos, radians, sqrt
from typing import Literal, Union


def main(s: str) -> Union[float, Literal["数据不合法。"]]:
    """
    :return: the length of the third side of a triangle

    >>> main("3 4 90")
    5.0
    """
    try:
        a, b, theta = map(float, s.split())
    except ValueError:
        return "数据不合法。"
    if (
        isinstance(a, (int, float))
        and isinstance(b, (int, float))
        and isinstance(theta, (int, float))
        and a > 0
        and b > 0
        and 0 < theta < 180
    ):
        return round(sqrt(a**2 + b**2 - 2 * a * b * cos(radians(theta))), 1)
    else:
        return "数据不合法。"
