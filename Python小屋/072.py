from typing import Literal, List, Union


def main(lst: List[int]) -> Union[List[int], Literal["数据不符合要求"]]:
    if not isinstance(lst, list) or not all(isinstance(i, int) for i in lst):
        return "数据不符合要求"
    return [i for i in lst if i % 2 == 0 if i > 8]
