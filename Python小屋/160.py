def main(num: int) -> int:
    """角谷猜想

    :return: The number of steps required to reach 1.

    >>> main(3)
    7
    """
    i = 0
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
        i += 1
    return i
