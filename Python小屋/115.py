from typing import Literal, Union


def main(start: int, stop: int) -> Union[int, Literal["不存在"]]:

    """
    :return: 返回 [start, stop] 上能被17整除的最大正整数。
    """
    for i in range(stop, start - 1, -1):
        if i % 17 == 0:
            return i
    return "不存在"
