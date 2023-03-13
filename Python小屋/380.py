def main(start: int, end: int) -> int:
    return sum(map(lambda x: str(x).count("8"), range(start, end + 1)))
