from typing import Any, List


def main(lst: List[Any]) -> bool:
    """
    if all elements in lst are int or float, return True
    else return False
    """
    return all(isinstance(i, (int, float)) for i in lst)
