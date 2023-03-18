def main(s: str) -> str:
    """
    :return: 将字符串中的元音字母转换为大写
    """
    d = {i: i.upper() for i in ["a", "e", "i", "o", "u"]}
    return "".join([d.get(i, i) for i in s])
