def main(s: str) -> str:
    """
    return the chars in s that only appear once
    """
    return "".join(i for i in s if s.count(i) == 1)
