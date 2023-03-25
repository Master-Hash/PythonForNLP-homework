def main(text: str) -> str:
    """Unicode - 1"""
    return "".join((chr(ord(i) - 1) for i in text))
