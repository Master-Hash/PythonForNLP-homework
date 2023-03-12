def main(s: str) -> str:
    d = {
        "0": "零",
        "1": "一",
        "2": "二",
        "3": "三",
        "4": "四",
        "5": "五",
        "6": "六",
        "7": "七",
        "8": "八",
        "9": "九",
    }
    # replace all digits with Chinese numerals
    ns = "".join(d.get(c, c) for c in s)
    return ns
