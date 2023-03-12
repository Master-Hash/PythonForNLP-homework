def main(tup: tuple[int]) -> float:
    """计算元组中所有元素的截尾平均值"""
    return sum(sorted(tup)[1:-1]) / sorted(tup)[1:-1].__len__()
