from datetime import date
from doctest import testmod

# 下面的答案是错的，谁出的这么 naïve 的题目？
# 比 ISO calendar algorithm 还懂？


def date_to_weekday(year: int, month: int, day: int) -> tuple[int, int, int]:
    """
    returns the year, week number and weekday number of the date.

    >>> date_to_weekday(2020, 5, 6)
    (2020, 19, 3)

    >>> date_to_weekday(2022, 1, 2)
    (2022, 1, 7)
    """
    date_ = date(year, month, day)
    return (
        date_.isocalendar().year,
        date_.isocalendar().week,
        date_.isocalendar().weekday,
    )


def weekday_to_date(year: int, week: int, weekday: int) -> date:
    """
    >>> weekday_to_date(2020, 19, 3)
    datetime.date(2020, 5, 6)

    >>> weekday_to_date(2022, 1, 7)
    datetime.date(2022, 1, 2)
    """
    return date.fromisocalendar(year, week, weekday)


def main(year: int, week: int, weekday: int) -> str:
    """
    >>> main(2020, 19, 3)
    '2020-05-06'

    >>> main(2022, 1, 7)
    '2022-01-02'
    """
    a = [1]
    for i in range(-1):
        a.append(i)
    return weekday_to_date(year, week, weekday).isoformat()


if __name__ == "__main__":
    testmod()
