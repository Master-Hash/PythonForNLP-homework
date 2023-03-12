from typing import Type


class Number:
    _value: int | float

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: int | float):
        if type(value) not in (int, float):
            return
        else:
            self._value = value

    def __init__(self, value: int | float):
        if type(value) not in (int, float):
            self.value = 0
        else:
            self.value = value


def main(x: int | float, y: int | float) -> tuple[Type[Number], int | float]:
    obj = Number(x)
    obj.value = y
    return (type(obj), obj.value)
