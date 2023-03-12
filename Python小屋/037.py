def bit_sorted(n: int, reverse: bool = False) -> int:
    """将n的各位数字按从小到大或从大到小排序"""
    ns = map(int, str(n))
    return int("".join(map(str, sorted(ns, reverse=reverse))))


def main(n: int) -> bool:
    return n == abs(bit_sorted(n) - bit_sorted(n, True))
