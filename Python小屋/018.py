from typing import Literal


def main(lst: list[int]) -> Literal[0, 1, 2]:
    """
    if every number in lst is the same, return 0;
    if every number in lst is different, return 1;
    if part of numbers in lst is different, return 2.
    """

    if len(set(lst)) == 1:
        return 0
    elif len(set(lst)) == len(lst):
        return 1
    else:
        return 2
