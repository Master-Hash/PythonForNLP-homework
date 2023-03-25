from operator import lt
from typing import List, Union


def main(data: List[Union[int, float]]) -> bool:
    """
    :return: True if data is sorted, False otherwise
    """
    return all(map(lt, data, data[1:]))
