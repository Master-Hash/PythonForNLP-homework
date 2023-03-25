from typing import Literal, Tuple, Union


def main(color: str) -> Union[Tuple[int, int, int], Literal["无效参数"]]:
    if not isinstance(color, str):
        return "无效参数"
    elif not color.startswith("#"):
        return "无效参数"
    elif len(color) != 7:
        return "无效参数"
    elif not all(x in "0123456789ABCDEFabcdef" for x in color[1:]):
        return "无效参数"
    else:
        return (int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16))
