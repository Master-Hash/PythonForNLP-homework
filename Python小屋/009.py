def main(lst: list[str]) -> list[str]:
    return sorted(lst, reverse=True, key=lambda x: len(x))
