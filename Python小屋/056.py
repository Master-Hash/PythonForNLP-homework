from typing import Literal, Any


def main(lst: list[Any]) -> Literal[0, 1, 2]:
    """
    if every item in lst is the same, return 0;
    if every item in lst is different, return 1;
    if part of items in lst is different, return 2.
    """

    if len(set(lst)) == 1:
        return 0
    elif len(set(lst)) == len(lst):
        return 1
    else:
        return 2
