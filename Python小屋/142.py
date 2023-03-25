import re


def main(s: str) -> str:
    return re.sub(r"\d+", "8", s)
