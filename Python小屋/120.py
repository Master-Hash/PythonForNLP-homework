from datetime import datetime
from doctest import testmod


def main(year: int, month: int, day: int) -> str:
    """

    :return: 该日期从9:00到17:00所有整点日期时间字符串。

    >>> main(2020, 11, 6)
    '2020-11-06 09:00:00,2020-11-06 10:00:00,2020-11-06 11:00:00,2020-11-06 12:00:00,2020-11-06 13:00:00,2020-11-06 14:00:00,2020-11-06 15:00:00,2020-11-06 16:00:00,2020-11-06 17:00:00'
    """
    return ",".join(
        [str(datetime(year=year, month=month, day=day, hour=i)) for i in range(9, 18)]
    )


if __name__ == "__main__":
    testmod()
