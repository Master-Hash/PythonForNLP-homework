import re


def main(s: str) -> int:
    """
    :return: Number of numeric characters in s
    """
    return len(re.findall(r"\d", s))
