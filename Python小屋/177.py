def main(num: int) -> int:
    octo = oct(num)
    return str(octo).count("6")
