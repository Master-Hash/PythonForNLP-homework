from typing import Literal


def main(hour: int) -> Literal["现在是白天", "现在是晚上", "不是有效时间"]:
    """
    :param hour: the hour of the day.
    :return: the message of the day.

    >>> main(8)
    '现在是白天'
    >>> main(20)
    '现在是晚上'
    >>> main(24)
    '现在不是有效时间'
    """
    if 0 <= hour < 24:
        return "现在是白天" if 6 <= hour < 18 else "现在是晚上"
    return "不是有效时间"
