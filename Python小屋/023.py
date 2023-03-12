def main(n: int, a: int) -> int:
    """
    return a + aa + aaa + ... + n times a
    """
    # return sum(int(str(a) * i) for i in range(1, n + 1))
    # rewrite with map() instead of list comprehension
    return sum(map(lambda i: int(str(a) * i), range(1, n + 1)))
