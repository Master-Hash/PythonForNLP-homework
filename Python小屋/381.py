def main(start: int, end: int) -> int:
    return sum(map(lambda x: 1 if str(x).count("8") else 0, range(start, end + 1)))
