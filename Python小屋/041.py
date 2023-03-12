def main(s1: str, *s2: str) -> bool:
    for i in s2:
        if i not in s1:
            return False
    else:
        return True
