x = 3


def main(num: int) -> int:
    """makes x global, x = num and returns x

    :param num: _description_
    :return: _description_
    """
    global x
    x = num
    return globals()["x"]
