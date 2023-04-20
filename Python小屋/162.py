from collections import UserList
from typing import Any, Iterable, Optional, TypeVar

T = TypeVar("T")

# 你又出 naïve 的题，继承 list 要不得
# Python 3.8 不支持 UserList[T]
# Python 3.9 开始支持，详见 PEP 585
class MyList(UserList[T]):
    def __getitem__(self, index: int) -> Optional[T]:
        try:
            return super().__getitem__(index)
        except IndexError:
            return None


def main(data: Iterable[Any], index: int):
    my_list = MyList(data)
    return my_list[index]


# if __name__ == "__main__":
#     print(main([1, 2, 3], 0))
#     print(main([1, 2, 3], 1))
#     print(main([1, 2, 3], 2))
#     print(main([1, 2, 3], 3))
#     print(main([1, 2, 3], 4))
#     print(main([1, 2, 3], 5))
