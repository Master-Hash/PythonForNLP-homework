def main(text: str, characters: str) -> int:
    """
    >>> main('abcdeaaab', 'aae')
    6
    """
    return sum(text.count(i) for i in set(characters))
