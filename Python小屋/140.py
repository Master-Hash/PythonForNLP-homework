import re
from typing import List


def main(text: str) -> List[str]:
    """
    :return: All int or float substring in text
    """
    return re.findall(r"[-+]?\d+(?:\.\d+)?", text)
