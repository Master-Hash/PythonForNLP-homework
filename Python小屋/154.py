from typing import Tuple


def main(tup: Tuple[int]) -> Tuple[int]:
    """Replace even index with 0"""
    return tuple(0 if i % 2 == 0 else x for i, x in enumerate(tup))
