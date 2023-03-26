"""广义回文"""

from doctest import testmod


def guangyi_huiwen(s: str) -> bool:
    """广义回文

    >>> guangyi_huiwen('')
    False

    >>> guangyi_huiwen('a')
    True

    >>> guangyi_huiwen('aa')
    True

    >>> guangyi_huiwen('aab')
    False

    >>> guangyi_huiwen('aab,aA')
    True

    >>> guangyi_huiwen('Able was I ere I saw elba')
    True

    >>> guangyi_huiwen("Madam, I'm Adam")
    True

    >>> guangyi_huiwen('上海自来水来自海上')
    True
    """
    s = s.lower()
    s = s.replace(" ", "")
    s = s.replace(",", "")
    s = s.replace(".", "")
    s = s.replace("!", "")
    s = s.replace("?", "")
    s = s.replace(";", "")
    s = s.replace(":", "")
    s = s.replace("'", "")
    s = s.replace('"', "")
    s = s.replace("(", "")
    s = s.replace(")", "")
    s = s.replace("[", "")
    s = s.replace("]", "")
    s = s.replace("{", "")
    s = s.replace("}", "")
    s = s.replace("-", "")
    s = s.replace("_", "")
    s = s.replace("/", "")
    s = s.replace("\\", "")
    s = s.replace("*", "")
    s = s.replace("&", "")
    s = s.replace("^", "")
    s = s.replace("%", "")
    s = s.replace("$", "")
    s = s.replace("#", "")
    s = s.replace("@", "")
    s = s.replace("`", "")
    s = s.replace("~", "")
    s = s.replace("+", "")
    s = s.replace("=", "")
    s = s.replace("<", "")
    s = s.replace(">", "")
    s = s.replace("0", "")
    s = s.replace("1", "")
    s = s.replace("2", "")
    s = s.replace("3", "")
    s = s.replace("4", "")
    s = s.replace("5", "")
    s = s.replace("6", "")
    s = s.replace("7", "")
    s = s.replace("8", "")
    s = s.replace("9", "")
    if s == "":
        return False
    return s == s[::-1]


if __name__ == "__main__":
    testmod()
    s = input()
    x = guangyi_huiwen(s)
    print(x)
