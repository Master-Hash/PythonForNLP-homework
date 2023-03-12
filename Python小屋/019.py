import re


def main(s: str) -> bool:
    # delete all non-alphabet characters
    s = re.sub(r"[^a-zA-Z]", "", s)
    return True if s == s[::-1] else False
