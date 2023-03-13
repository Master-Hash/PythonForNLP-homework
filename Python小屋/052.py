def main(lst: list[int]) -> list[int]:
    """
    returns the indexs of the maximum value in a list
    """
    max_value = max(lst)
    return [i for i, v in enumerate(lst) if v == max_value]
