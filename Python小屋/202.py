def main(s: str) -> int:
    return len([i for i in s.split("，") if len(i) == 3])
