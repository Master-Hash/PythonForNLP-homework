def main(lst: list[int]) -> list[int]:
    return sorted(lst, key=lambda x: sum(map(int, str(x))))
