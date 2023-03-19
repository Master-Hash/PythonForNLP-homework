"""
寻找众数。
"""

from typing import List, Dict
from doctest import testmod

# 自定义函数：
def find_mode(a: List[int]) -> List[int]:
    """返回列表中的众数。

    :param a: 整数列表。
    :return: 众数列表，从小到大排列。如果没有众数，则返回空列表。

    >>> find_mode([5, 2, 4, 4, 2, 2])
    [2]

    >>> find_mode([5, 1, 4, 4, 2, 2])
    [2, 4]

    >>> find_mode([5, 4, 1, 6, 3, 2])
    []
    """
    # 用字典统计每个数出现的次数
    count: Dict[int, int] = {}
    for i in a:
        count[i] = count.get(i, 0) + 1

    # 找出最大值
    max_count = max(count.values())

    if max_count == 1:
        return []
    else:
        return sorted((i for i in count if count[i] == max_count))


# 我来教你怎么测试
if __name__ == "__main__":
    testmod()

# 写成单元测试也行，但你下面这样就不够意思了

# 测试代码
if __name__ == "__main__":
    s = input("请从键盘输入若干个整数，这些整数用空格隔开：")
    try:
        x = list(map(int, s.split()))
        result = find_mode(x)
        print(result)
    except:
        print("你没有按要求输入若干个整数。")
