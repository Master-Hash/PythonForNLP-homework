# 参考 070.py


def main(lst: list[int]) -> tuple[int, int]:
    o = e = 0
    for i, j in enumerate(lst):
        if i % 2 == 0:
            o += j
        else:
            e += j
    return o, e
