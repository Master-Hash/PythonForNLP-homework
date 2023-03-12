def filterPrime(n: list[int]) -> list[int]:
    return [n[0], *filterPrime([i for i in n[1:] if i % n[0] != 0])] if n else []


primes = filterPrime(list(range(2, 1000)))


def isPrime(n: int) -> bool:
    return n in primes


def main(n: int) -> int:
    return filterPrime(list(range(2, n + 1)))[-1]
