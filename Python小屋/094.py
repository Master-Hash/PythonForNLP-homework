from typing import List


def main(data: List[int]) -> bool:
    """
    :return: whether the list is sorted
    """
    return data == sorted(data)
