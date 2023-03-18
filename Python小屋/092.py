def main(s: str) -> int:
    """
    :return: the count of spaces at the beginning of the string
    """
    return len(s) - len(s.lstrip(" "))
