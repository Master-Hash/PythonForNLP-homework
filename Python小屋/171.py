from typing import Iterable, Literal, TypeVar, Union

T = TypeVar("T")


def main(
    iterable1: Iterable[T], iterable2: Iterable[T]
) -> Union[bool, Literal["参数必须为可迭代对象。"]]:
    """
    >>> main([1, 2, 3], [1, 2, 3])
    True
    >>> main([1, 2, 3], [1, 2, 4])
    False
    """
    if not isinstance(iterable1, Iterable) or not isinstance(iterable2, Iterable):
        return "参数必须为可迭代对象。"
    return all(i in iterable2 for i in iterable1)
