def main(n: int) -> bool:
    """判断n是否为水仙花数"""
    return n == sum(map(lambda x: int(x) ** len(str(n)), str(n)))
