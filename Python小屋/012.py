def main(lst: list[str]) -> str:
    lst.sort(key=lambda x: len(x), reverse=True)
    return lst[0]
