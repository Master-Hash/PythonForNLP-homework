from typing import Iterable, Literal, Tuple, Union


def main(
    iterable: Iterable[Union[int, float]],
    operator: Literal["+", "-", "*", "/", "//", "**"],
    num: Union[int, float],
) -> Union[
    Tuple[Union[int, float], ...],
    Literal["不识别的运算符。", "参数num必须是整数或实数。", "参数iterable必须是只包含整数或实数的可迭代对象。"],
]:
    """
    >>> main(range(5), '+', 3)
    (3, 4, 5, 6, 7)
    """
    if operator not in ("+", "-", "*", "/", "//", "**"):
        return "不识别的运算符。"
    if not isinstance(num, (int, float)):
        return "参数num必须是整数或实数。"
    if not all(isinstance(i, (int, float)) for i in iterable):
        return "参数iterable必须是只包含整数或实数的可迭代对象。"
    return tuple(eval(f"{i}{operator}{num}") for i in iterable)
