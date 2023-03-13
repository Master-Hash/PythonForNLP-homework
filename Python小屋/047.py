from math import cos, radians, sqrt


def main(a: float, b: float, theta: float) -> float | str:
    """
    return the length of the hypotenuse of a right triangle
    """
    if (
        isinstance(a, (int, float))
        and isinstance(b, (int, float))
        and isinstance(theta, (int, float))
        and a > 0
        and b > 0
        and 0 < theta < 180
    ):
        return round(sqrt(a**2 + b**2 - 2 * a * b * cos(radians(theta))), 1)
    else:
        return "数据不对"
