from operator import mul
from math import acos, degrees
from typing import Tuple


def main(vector1: Tuple[int, int], vector2: Tuple[int, int]) -> str:
    d = degrees(
        acos(
            sum(mul(*v) for v in zip(vector1, vector2))
            / (
                sum(mul(*v) for v in zip(vector1, vector1)) ** 0.5
                * sum(mul(*v) for v in zip(vector2, vector2)) ** 0.5
            )
        )
    )
    # 保留两位小数
    return f"{d:.2f}"
