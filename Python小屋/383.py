from typing import Dict


def main(text: str) -> Dict[str, int]:
    """
    >>> main('implicit')
    {'c': 1, 'i': 1, 'l': 1, 'm': 1, 'p': 1, 't': 1}

    键按 Unicode 码排序。
    """
    # return {char: text.count(char) for char in text}
    # rewrite with map()
    return dict(map(lambda char: (char, text.count(char)), sorted(text)))
