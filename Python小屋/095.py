from pypinyin import pinyin
import doctest


def main(s: str) -> str:
    """
    :return: the string sorted by pinyin

    >>> main('你好')
    '好你'
    """
    return "".join(sorted(s, key=lambda x: pinyin(x)[0][0]))


# doctest
if __name__ == "__main__":
    doctest.testmod()
