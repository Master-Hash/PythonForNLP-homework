from datetime import datetime


def main(s: str) -> str:
    """
    >>> main('2020-2-18 22:2:22')
    '2020-02-18 22:02:22'
    """
    return datetime.strptime(s, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
