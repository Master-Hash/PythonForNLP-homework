# identical to #144

import ipaddress


def main(s: str) -> bool:
    """
    Decide whether the string is a valid IP address.

    >>> main('0,0,0,0')
    True

    >>> main('119.189.876.0')
    False
    """
    try:
        ipaddress.ip_address(s)
    except ValueError:
        return False
    else:
        return True
