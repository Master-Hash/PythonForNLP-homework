from doctest import testmod
from typing import List


def bridge(a: List[int]) -> int:
    """求多个人同时过桥的最短时间。

    :param a: 每个旅行者过桥的时间
    :return: 最短时间

    >>> bridge([1, 2, 5, 10])
    17

    >>> bridge([1,2])
    2

    >>> bridge([1,2,5])
    8
    """
    a.sort()
    n = len(a)
    match n:
        case 1:
            return a[0]
        case 2:
            return a[1]
        case 3:
            return a[0] + a[1] + a[2]
        case int() as _n if _n >= 4:
            return min(2 * a[0] + a[-2] + a[-1], a[0] + 2 * a[1] + a[-1]) + bridge(
                a[:-2]
            )
        case _:
            raise ValueError("参数错误")


if __name__ == "__main__":
    testmod()
    s = "请输入几名旅行者的单独过桥时间，都是整数，用空格隔开："
    a = list(map(int, input(s).split()))
    print(a, bridge(a))
