from typing import Literal


def main(s: str) -> int | Literal["数据错误"]:
    """
    >>> main('1,234')
    1234

    >>> main('1,234,567')
    1234567

    >>> main('1s3')
    '数据错误'

    >>> main('12,34')
    '数据错误'

    comma can only appear before thousand, million, billion, ...
    Copilot is not smart enough to understand this
    """
    if not s.replace(",", "").isdigit():
        return "数据错误"
    elif s.startswith(","):
        return "数据错误"
    elif s.endswith(","):
        return "数据错误"
    else:
        a = s.split(",")
        if not all(len(i) == 3 for i in a[1:]) or len(a[0]) > 3:
            return "数据错误"
        else:
            return int("".join(a))
