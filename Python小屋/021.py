from collections import deque
from doctest import testmod
from itertools import count, takewhile
from typing import Generator, Iterator, TypeVar

T = TypeVar("T")


def filter_prime(ns: Iterator[int]) -> Generator[int, None, None]:
    yield (n := next(ns))
    yield from filter_prime(i for i in ns if i % n != 0)


# https://docs.python.org/3/library/itertools.html#itertools-recipes
def tail(n: int, iterable: Iterator[T]) -> Iterator[T]:
    "Return an iterator over the last n items"
    return iter(deque(iterable, maxlen=n))


primes = filter_prime(count(2))


def main(n: int) -> int:
    """Get the greatest prime number less than or equal to n.

    :param n: the upper bound
    :return: the greatest prime number less than or equal to n

    >>> main(2)
    2

    >>> main(37)
    37

    main(100)
    97

    >>> main(200)
    199
    """

    # `itertools.tee()` is awkward to use
    primes = filter_prime(count(2))

    return next(tail(1, takewhile(lambda x: x <= n, primes)))


if __name__ == "__main__":
    # Each mod is test independently, so global `primes` is not exhausted.
    testmod()
