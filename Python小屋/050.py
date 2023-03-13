from typing import Generator


def fib(n: int) -> Generator[int, None, None]:
    """生成斐波那契数列"""
    a, b = 1, 1
    while b <= n:
        yield b
        a, b = b, a + b


def main(n: int) -> int:
    return list(fib(n))[-1]
