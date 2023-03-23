from doctest import testmod
from datetime import datetime


def main(year: int, month: int, day: int) -> int:
    """
    :return: the day of the week.

    >>> main(2023, 3, 22)
    3
    """
    return datetime(year, month, day).weekday() + 1


if __name__ == "__main__":
    testmod()
