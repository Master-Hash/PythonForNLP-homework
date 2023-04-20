from typing import Tuple


def main(integers: Tuple[int, ...], key: int) -> Tuple[int]:
    return tuple(i ^ key for i in integers)
