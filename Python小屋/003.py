from typing import TypeVar

T = TypeVar("T")


def main(lst: list[T], item: T) -> int | str:
    return lst.index(item) if item in lst else "不存在"
