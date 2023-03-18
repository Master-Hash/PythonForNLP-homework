def filterPrime(n: list[int]) -> list[int]:
    return [n[0], *filterPrime([i for i in n[1:] if i % n[0] != 0])] if n else []


primes = filterPrime(list(range(2, 1000)))


def main(start: int, num: int) -> int:
    """
    return the num-th prime greater-than-or-equal-to start
    """
    return [i for i in primes if i >= start][num - 1]
