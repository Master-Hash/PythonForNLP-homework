from typing import Callable, Literal, Union


def main(func: Callable[[int], Union[int, float]]) -> Literal["递减函数", "非递减函数"]:
    """测试函数在区间 [0, 5] 是否为递减函数。"""
    return (
        "递减函数" if func(0) > func(1) > func(2) > func(3) > func(4) > func(5) else "非递减函数"
    )
