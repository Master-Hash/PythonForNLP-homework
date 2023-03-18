from datetime import date


def main(year: int, month: int, day: int) -> int:
    """
    :return: n-th day of the year
    """
    return date(year, month, day).timetuple().tm_yday
