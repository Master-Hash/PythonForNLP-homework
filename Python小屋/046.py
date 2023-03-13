def main(lst: list[int | float]) -> int | float:
    """
    return the number appears the most times in the list
    """
    return max(lst, key=lambda x: (lst.count(x), x))
