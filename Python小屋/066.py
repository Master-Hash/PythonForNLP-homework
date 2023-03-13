from typing import Literal


def main(num: int) -> str | Literal["数据错误"]:
    """
    >>> main(1234)
    '1,2,3,4'
    """
    if not isinstance(num, int):
        return "数据错误"
    return ",".join(str(num))
