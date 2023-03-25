import re


def main(pwd: str) -> bool:
    """Decide whether the password is valid

    :return: True if the password contains only letters, numbers, unterscores, commas and dots, otherwise False.

    >>> main('gsoigh4ih0w_,.f04f')
    True

    >>> main('gsoigh4i#h0w_,.f04f')
    False

    >>> main('gsoigh4ih你好0w_,.f04f')
    False
    """
    return bool(re.fullmatch(r"^[0-9A-Za-z\.,_]+&", pwd))
