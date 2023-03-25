import re
from typing import List


def main(s: str) -> List[str]:
    """
    :return: All words which repeat consecutively
    """
    return re.findall(r"(\b\w+)\s+\1\b", s)
