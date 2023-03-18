def main(n: int) -> int:
    """Caculate how many ways to get n by 1, 2, 3
    >>> main(4)
    7
    >>> main(5)
    13
    """
    # if n <= 2:
    #     return n
    # elif n == 3:
    #     return 4
    # else:
    #     return main(n - 1) + main(n - 2) + main(n - 3)

    # rewrite with for
    if n <= 2:
        return n
    elif n == 3:
        return 4
    else:
        a, b, c = 1, 2, 4
        for _ in range(4, n + 1):
            a, b, c = b, c, a + b + c
        return c
