def main(lst: list[int | float]) -> list[int | float]:
    avg = sum(lst) / len(lst)
    return [i for i in lst if i >= avg]
