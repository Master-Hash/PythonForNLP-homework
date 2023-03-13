# rewrite main with for loop
def main(start: int, end: int) -> int:
    count = 0
    for i in range(start, end + 1):
        count += str(i).count("8")
    return count
