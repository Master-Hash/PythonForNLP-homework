from typing import List


def main(data: List[int]) -> int:
    return sum(i for i in data if i < 30 or i > 70)
