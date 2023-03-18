def main(s1: str, s2: str) -> str:
    """
    return s1 + s2, but without the common part of the tail of s1 and the head of s2.
    """
    for i in range(len(s1), 0, -1):
        if s1[-i:] == s2[:i]:
            return s1 + s2[i:]
    else:
        return s1 + s2
