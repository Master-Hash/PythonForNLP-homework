from re import sub


def main(s: str) -> str:
    return sub(r"\b\w(?=\w*\b)", lambda i: i.group().upper(), s)
