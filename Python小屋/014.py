def main(lst: list[int]) -> int:
    pair = zip(lst, map(abs, lst))
    return sorted(pair, key=lambda x: x[1], reverse=True)[0][0]
