from re import findall
from typing import Literal


def main(s: str) -> str | Literal["没有数字"]:
    """
    returns the longest numberic substring
    """
    return max(findall(r"\d+", s), key=len, default="没有数字")
