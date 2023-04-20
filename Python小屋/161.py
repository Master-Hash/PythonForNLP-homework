def main(s: str) -> str:
    """String substitution.

    P -> !
    y -> @
    t -> #
    h -> $
    o -> %
    n -> ^
    a, b, c, d -> ''
    """

    d = {
        "P": "!",
        "y": "@",
        "t": "#",
        "h": "$",
        "o": "%",
        "n": "^",
        "a": "",
        "b": "",
        "c": "",
        "d": "",
    }

    return s.translate(str.maketrans(d))
