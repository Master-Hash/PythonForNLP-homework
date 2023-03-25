from itertools import islice
from typing import Generator, Literal, Union


def fib() -> Generator[int, None, None]:
    """生成斐波那契数列"""
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


def main(n: int) -> Union[int, Literal["无效参数"]]:
    if not isinstance(n, int):
        return "无效参数"
    elif n <= 0:
        return "无效参数"
    else:
        return next(islice(fib(), n - 1, n))
