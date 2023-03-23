from string import ascii_lowercase, ascii_uppercase
from doctest import testmod


def main(s: str, k: int) -> str:
    """凯撒密码。
    :param s: 明文。
    :param k: 移动位数。
    :return: 密文。

    非字母字符不变。大写字母加密后仍为大写字母，小写字母加密后仍为小写字母。

    >>> main('aBc', 1)
    'bCd'
    """
    # 生成移位后的字母表
    lower = ascii_lowercase
    upper = ascii_uppercase
    lower_shift = lower[k:] + lower[:k]
    upper_shift = upper[k:] + upper[:k]
    # 生成映射表
    table = str.maketrans(lower + upper, lower_shift + upper_shift)
    return s.translate(table)


if __name__ == "__main__":
    testmod()
