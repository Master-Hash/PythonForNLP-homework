from itertools import combinations


def main(lst: list[int]) -> list[tuple[int, int, int]]:
    """
    returns tuples whose sum is 10.
    """
    return [i for i in combinations(lst, 3) if sum(i) == 10]
