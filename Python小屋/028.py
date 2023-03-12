from typing import Literal


def main(year: int) -> Literal["yes", "no"]:
    """判断是否为闰年"""
    return "yes" if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else "no"
