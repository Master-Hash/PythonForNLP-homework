from typing import Callable


def main(func: Callable[[float], float], lst: list[float]) -> float:
    """调用函数并返回结果"""
    return max((func(i) for i in lst))
