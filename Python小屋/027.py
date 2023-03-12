from datetime import date


def main(year1: int, month1: int, day1: int, year2: int, month2: int, day2: int):
    """计算两个日期之间的天数"""
    date1 = date(year1, month1, day1)
    date2 = date(year2, month2, day2)
    return abs((date2 - date1).days)
