from typing import Literal
import re
from doctest import testmod


def main(pwd: str) -> Literal["weak", "below_middle", "above_middle", "strong"]:
    """_summary_

    :return: the strength of the password

    >>> main('a2Cd,')
    'weak'

    >>> main('a3B,4O0')
    'strong'

    >>> main('2amw8q3.9C')
    'strong'

    >>> main('董付国')
    'weak'

    >>> main('aBcDeFG')
    'below_middle'

    >>> main('aBcDe,FG')
    'above_middle'
    """
    strength = (
        # 1. contains at least one digit
        (1 if re.search(r"\d", pwd) else 0)
        # 2. contains at least one lowercase letter
        + (1 if re.search(r"[a-z]", pwd) else 0)
        # 3. contains at least one uppercase letter
        + (1 if re.search(r"[A-Z]", pwd) else 0)
        # 4. contains at least one special character
        + (1 if re.search(r"[\.\,]", pwd) else 0)
    )
    if len(pwd) < 6:
        return "weak"
    elif strength == 1:
        return "weak"
    elif strength == 2:
        return "below_middle"
    elif strength == 3:
        return "above_middle"
    elif strength == 4:
        return "strong"
    else:
        return "weak"


if __name__ == "__main__":
    testmod()
