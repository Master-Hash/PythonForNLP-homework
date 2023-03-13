from os.path import splitext


def main(s: str) -> str:
    """
    returns the file name with _new suffix
    """
    name, ext = splitext(s)
    return name + "_new" + ext
