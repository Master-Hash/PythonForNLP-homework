import re


def main(s: str) -> str:
    """Trim, remove extra spaces and words."""
    t = re.sub(r"\s+", " ", s.strip())

    # Remove words which repeat consecutively
    while t != re.sub(r"(\b\w+)\s+\1\b", r"\1", t):
        t = re.sub(r"(\b\w+)\s+\1\b", r"\1", t)

    return t
