def main(s: str) -> str:
    if len(s) >= 20:
        return s
    else:
        n, m = divmod(20 - len(s), 2)
        return ("#" * n) + s + "#" * (n + m)
