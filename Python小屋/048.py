def main(vector1: list[int | float], vector2: list[int | float]) -> int | float | str:
    if not isinstance(vector1, list) or not isinstance(vector2, list):
        return "数据不对"
    elif not all(isinstance(x, (int, float)) for x in vector1) or not all(
        isinstance(x, (int, float)) for x in vector2
    ):
        return "数据不对"
    elif len(vector1) != len(vector2):
        return "数据不对"
    else:
        return sum((abs(x - y) for x, y in zip(vector1, vector2)))
