s = sum


def main(start: int, end: int) -> int:
    return s(map(lambda x: str(x).count("8"), range(start, end + 1)))
