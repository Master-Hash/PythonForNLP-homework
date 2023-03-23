import re
from typing import List


def main(s: str) -> List[str]:
    """Get all 4-letter words in a string.

    :param s: A string.
    :return: A list of 4-letter words.
    """
    return re.findall(r"\b\w{4}\b", s)
