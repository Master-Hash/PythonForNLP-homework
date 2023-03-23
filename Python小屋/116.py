from typing import Tuple


def main(data: Tuple[int, ...]) -> Tuple[int, ...]:
    return tuple(d for i, d in enumerate(data) if (i + 1) % 4)
