from typing import Any, Iterator


def main(obj: Any) -> bool:
    """Decide if the object is a iterator.

    :param obj: the object to be judged.
    :return: True if the object is a iterator, False otherwise.
    """
    return isinstance(obj, Iterator)
