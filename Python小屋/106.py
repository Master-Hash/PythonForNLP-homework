from datetime import datetime


def main(seconds: int) -> str:
    """
    :param seconds: the timestamp in seconds.
    :return: the formatted time string.

    >>> main(1601901810)
    '2020-10-05_20:43:30'
    """
    return datetime.fromtimestamp(seconds).strftime("%Y-%m-%d_%H:%M:%S")
