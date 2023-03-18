import re
from typing import Tuple


def main(s: str) -> Tuple[int, int]:
    """_summary_

    :return: the number of uppercase letters and lowercase letters
    """
    return len(re.findall(r"[A-Z]", s)), len(re.findall(r"[a-z]", s))
