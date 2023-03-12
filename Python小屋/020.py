def main(s: str) -> list[str]:
    c: dict[str, int] = {}
    for i in s:
        c[i] = c.get(i, 0) + 1
    return [i[0] for i in sorted(c.items(), reverse=True, key=lambda x: x[1])][:3]
