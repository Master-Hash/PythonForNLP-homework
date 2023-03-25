import re
from doctest import testmod
from typing import Tuple


def main(s: str) -> Tuple[str, str]:
    """
    >>> main('<html><head>This is head.</head><body>This is body.</body></html>')
    ('This is head.', 'This is body.')
    """
    return re.search(r"<head>(.+?)</head>", s).group(1), re.search(
        r"<body>(.+?)</body>", s
    ).group(1)


if __name__ == "__main__":
    testmod()
