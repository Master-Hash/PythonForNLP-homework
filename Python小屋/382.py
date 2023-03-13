from typing import Tuple
from doctest import testmod


def distinguish(text: str) -> bool:
    """
    if the four characters are all different, return True
    >>> distinguish("ABCD")
    True

    if the first two characters are the same and both the last two are different, return True
    >>> distinguish("AABC")
    True

    otherwise, return False
    >>> distinguish("ABCC")
    False
    """
    return (
        len(set(text)) == 4
        or len(set(text[:2])) == 1
        and len(set(text[2:])) == 2
        and text[0] != text[2]
    )


def main(text: str) -> Tuple[str, ...]:
    """
    returns the phrases with "AABC" and "ABCD" patterns

    >>> main('积极向上 爱党爱国 欣欣向荣 绘声绘色 念念不忘 头头是道')
    ('积极向上', '欣欣向荣', '念念不忘', '头头是道')

    >>> main('天下无双 春暖花开 亭亭玉立 面面相觑 欣欣向荣 窃窃私语 无声无色')
    ('天下无双', '春暖花开', '亭亭玉立', '面面相觑', '欣欣向荣', '窃窃私语')
    """
    return tuple(filter(distinguish, text.split()))


if __name__ == "__main__":
    ...
    # testmod()
