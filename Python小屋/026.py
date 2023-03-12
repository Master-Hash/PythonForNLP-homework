from math import sin, radians


def main(lst: list[float]) -> list[float]:
    """
    return the sum of the sine of all elements in lst
    """
    return list(map(lambda x: sin(radians(x)), lst))
