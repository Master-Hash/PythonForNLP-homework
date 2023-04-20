from typing import List


def main(x: List[int], y: List[int]) -> int:
    return sum(abs(i - j) for i, j in zip(x, y))
