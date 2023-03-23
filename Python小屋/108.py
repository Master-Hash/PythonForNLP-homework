from typing import Literal


def main(num1: int, num2: int) -> Literal["符号相同", "符号不相同"]:
    """
    :param num1: the first number.
    :param num2: the second number.
    :return: the message of the sign.
    """
    return "符号相同" if num1 * num2 > 0 else "符号不相同"
