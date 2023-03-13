def main(num: int) -> str:
    """
    insert commas into a string representing a number
    """
    return (
        str(num) if num < 1000 else main(num // 1000) + "," + str(num % 1000).zfill(3)
    )
