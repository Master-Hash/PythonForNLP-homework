from typing import Generator


def fib(n: int) -> Generator[int, None, None]:
    """生成斐波那契数列"""
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def main(n: int) -> int:
    return sum(fib(n))
