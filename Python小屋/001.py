def main(n: int) -> int:
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
