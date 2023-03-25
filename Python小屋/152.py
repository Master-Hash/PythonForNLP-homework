from typing import List


def main(lst: List[str]) -> List[str]:
    length = max(len(s) for s in lst)
    return [s.rjust(length, "0") for s in lst]
