def main(s1: str, s2: str) -> int:
    """_summary_

    :param s1: _description_
    :param s2: _description_
    :return: sum of times each unique char in s2 appears in s1
    """
    return sum(map(lambda c: s1.count(c), set(s2)))
