import re
from typing import List


def main(s: str) -> List[str]:
    """
    :return: All words containing "t" in the middle of the word.
    """
    return re.findall(r"\b\w+t\w+\b", s)
