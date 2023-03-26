from itertools import product
from typing import List


def split_expr(expr: str) -> List[str]:
    """将算术表达式分割为数字和运算符的列表

    :param expr: 算术表达式，如"1+2*3-4/5"
    :return: 数字和运算符的列表，如['1', '+', '2', '*', '3', '-', '4', '/', '5']
    """
    r: List[str] = []
    n = ""
    for c in expr:
        if c in "0123456789":
            n += c
        else:
            r.append(n)
            r.append(c)
            n = ""
    r.append(n)
    return r


def make_bracket(exp: str) -> List[str]:
    """给定算术表达式，构造所有可能的加括号的算术表达式

    :param s: 算术表达式，如['1', '+', '2', '*', '3', '-', '4', '/', '5']
    :return: 所有可能的加括号的算术表达式
    """
    s = split_expr(exp)
    if len(s) == 1:
        return [s[0]]
    r: List[str] = []
    for i in range(1, len(s), 2):
        for x in make_bracket("".join(s[:i])):
            for y in make_bracket("".join(s[i + 1 :])):
                r.append(f"({x}{s[i]}{y})")
    return r


def make_n(nlist: List[int], n: int) -> List[str]:
    """123456789中间任意插入加减乘除符号和括号，构成算术表达式，使得结果等于n

    :param nlist: 构成算术表达式的数字列表，默认为[1, 2, 3, 4, 5, 6, 7, 8, 9]
    :param n: 欲求算术表达式的结果
    :return: 所有算术表达式的列表
    """
    r: List[str] = []
    slist = list(" ".join(map(str, nlist)))
    for opplist in product(("", "+", "-", "*", "/"), repeat=len(nlist) - 1):
        slist[1::2] = opplist
        for expr in make_bracket("".join(slist)):
            try:
                if eval(expr) == n:
                    r.append(f"{expr}={n}")
            except ZeroDivisionError:
                pass
    return r


# print(make_n([1, 2, 3, 4], 24))
if __name__ == "__main__":
    for n in range(1949, 2050):
        print(n)
        r = make_n(list(range(1, 10)), n)
        if r:
            print("\n".join(r) + "\n\n")
        else:
            print("没找到\n\n")


r"""
从本程序的运行结果可以看出：
1949到2049中有如下几个数字不能用本程序在123456789中插入加减乘除号来计算得到：
1949
1951
1960
1970
1980
2005
2006
2029
2037
2041
2043

在1949～2049之间的其它数字都能找到至少一个插入加减乘除号的表达式，例如：

2022
1234+5-6+789=2022
12*34*5+6-7-8-9=2022
1+2+3+4*567*8/9=2022
1+2+3/4*5*67*8+9=2022
1-2+345*6-7*8+9=2022
1*2*3+4*567*8/9=2022

2023
1+2*3+4*567*8/9=2023

2024
1234-5+6+789=2024
12*34*5-6+7-8-9=2024

我们希望引入括号机制，尽量（注意是尽量而不是一定）要让1949～2049中的每一个数字都能通过在123456789中插入合适的加减乘除号和括号来计算得到。
添加运算符和括号的注意事项：
（1）每两个数字之间至多插入一个运算符；
（2）如果某两个数字之间不插入运算符，我们认为这两个数字属于同一个整数；
（3）括号可以本着无重复原则任意添加，例如：
     (1*2)+3可以，但((1*2))+3就有重复添加的嫌疑
（4）添加括号后构造的四则运算表达式要能够用eval函数顺利求值而不出错。
请大家修改本示例程序中的函数make_n，完成本示例程序没能完成的任务。

修改注意事项：
1、函数make_n的名称和各参数含义不能变，
   调用函数make_n的那些代码不能变，
   函数make_n返回值的类型和含义不能变；
2、只修改函数内部的代码即可；
3、如果有必要，可以自定义函数，在函数make_n中调用；
4、如果有必要，可以导入标准库；
5、不许导入任何扩展库。

"""
