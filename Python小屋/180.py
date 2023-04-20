from html import escape


def main(s: str) -> str:
    """Return a string with special characters escaped.

    >>> main('<every good>')
    '&lt;every good&gt;'
    """
    return escape(s)
