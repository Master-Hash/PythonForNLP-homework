def main(s: str) -> tuple[bytes, bytes] | str:
    if type(s) != str:
        return "参数必须为字符串"
    else:
        return (s.encode("utf-8"), s.encode("gbk"))
