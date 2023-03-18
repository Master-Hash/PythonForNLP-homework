def main(s1: str, s2: str) -> int:
    return sum((1 for i, j in zip(s1, s2) if i == j))
