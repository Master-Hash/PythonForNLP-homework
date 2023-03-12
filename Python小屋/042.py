from math import pi


def area(r: int | float):
    if not isinstance(r, (int, float)) or r <= 0:
        return "参数必须是大于0的整数或实数"
    return round(pi * r * r, 2)


main = area
