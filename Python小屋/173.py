from typing import Any, Dict, Literal, TypeVar, Union

K = TypeVar("K")
V = TypeVar("V")


def main(obj: Dict[K, V]) -> Union[K, Literal["字典的值必须是同一种类型。"]]:
    ...
