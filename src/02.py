# 导入
from sys import exit

# 输入正整数n
try:
    n = int(input())
except:
    n = -1
if n <= 0:
    print("ERROR")
    exit()


def bit_sorted(n: int, reverse: bool = False) -> int:
    """将n的各位数字按从小到大或从大到小排序"""
    ns = map(int, str(n))
    return int("".join(map(str, sorted(ns, reverse=reverse))))


# 能够按作业要求输出不大于n的所有黑洞数

black_hole = [
    i for i in range(495, n + 1) if i == abs(bit_sorted(i) - bit_sorted(i, True))
]

if black_hole:
    print("\n".join(map(str, black_hole)))
else:
    print("没找到")
