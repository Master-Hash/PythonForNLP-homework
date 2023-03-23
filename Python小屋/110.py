def filterPrime(n: list[int]) -> list[int]:
    return [n[0], *filterPrime([i for i in n[1:] if i % n[0] != 0])] if n else []


primes = filterPrime(list(range(2, 100)))[::-1]


def main(k: int) -> int:
    return primes[k - 1]
