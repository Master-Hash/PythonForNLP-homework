def b(n: int) -> str:
    """
    return a binary string of n
    """
    return bin(n)[2:]


def main(n: int) -> int:
    """
    returns how many "0"s at the tail of n.
    """
    t = b(n)
    return len(t) - len(t.rstrip("0"))
