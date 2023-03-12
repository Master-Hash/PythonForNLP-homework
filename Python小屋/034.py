from __future__ import annotations


class Number:
    def __init__(self, value: int):
        self.value = value

    def __add__(self, other: Number) -> Number:
        return Number(self.value + other.value)

    def __str__(self) -> str:
        return f"{self.value}"


def main(x: int, y: int):
    return Number(x + y)
