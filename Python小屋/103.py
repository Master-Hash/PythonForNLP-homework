from hashlib import md5


def main(s: str) -> str:
    """Get the MD5 hash of the GBK-encoded string.

    :param s: the original string.
    :return: the MD5 hash of the GBK-encoded string.
    """
    return md5(s.encode("gbk")).hexdigest()
