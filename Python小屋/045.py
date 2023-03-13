def main(lst: list[str]) -> str:
    if not isinstance(lst, list) or not all(isinstance(x, str) for x in lst):
        return "数据格式不正确"
    else:
        return max(lst, key=lambda xs: xs.lower())
