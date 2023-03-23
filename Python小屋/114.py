def main(num: int) -> bool:
    """判断 `num` 是否为回文素数。"""
    return str(num) == str(num)[::-1] and all(num % i for i in range(2, num))
