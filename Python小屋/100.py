def main() -> int:
    with open("data100.txt", "r") as f:
        lines = f.readlines()
    return max(map(len, lines))


print(main())
