from typing import Literal, Tuple, Union


def main(color: Tuple[int, int, int]) -> Union[str, Literal["无效参数"]]:
    if not isinstance(color, tuple):
        return "无效参数"
    elif len(color) != 3:
        return "无效参数"
    elif not all(isinstance(x, int) for x in color):
        return "无效参数"
    elif not all(0 <= x <= 255 for x in color):
        return "无效参数"
    else:
        return f"#{color[0]:02X}{color[1]:02X}{color[2]:02X}"
