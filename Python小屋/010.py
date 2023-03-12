from functools import reduce
from operator import mul


def main(n: int) -> int:
    return reduce(mul, range(1, n + 1))


print(main(20), main(30), main(40), sep="\n")
