def filterPrime(n: list[int]) -> list[int]:
    return [n[0], *filterPrime([i for i in n[1:] if i % n[0] != 0])] if n else []


def main(num: int) -> int:
    """_summary_

    :param num: _description_
    :return: max prime < num
    """
    return filterPrime(list(range(2, num)))[-1]
