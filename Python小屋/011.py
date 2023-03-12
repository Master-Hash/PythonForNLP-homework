from operator import mul


def main(vector1: list[int], vector2: list[int]) -> int:
    return sum(map(mul, vector1, vector2))
