def main(num: int) -> bool:
    """
    if the prime factors of num contains only 2, 3, 5, then returns True.
    """
    if num == 1:
        return False
    for i in [2, 3, 5]:
        while num % i == 0:
            num //= i
    return num == 1
