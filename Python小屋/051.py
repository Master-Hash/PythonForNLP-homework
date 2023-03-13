from typing import Literal, TypeAlias

Chick: TypeAlias = int
Rabbit: TypeAlias = int
Head: TypeAlias = int
Foot: TypeAlias = int


def main(n: Head, m: Foot) -> tuple[Chick, Rabbit] | Literal["数据不对"]:
    """求鸡兔同笼问题"""
    if not isinstance(n, int) or not isinstance(m, int):
        return "数据不对"
    elif n * 2 > m:
        return "数据不对"
    else:
        for i in range(n + 1):
            j = n - i
            if i * 2 + j * 4 == m:
                return i, j
        return "数据不对"
