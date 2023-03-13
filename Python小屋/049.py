from typing import Literal

# 题目说 score 是实数，但是实际上是整数
def main(score: int) -> Literal["A", "B", "C", "D", "F", "数据不对"]:
    if not isinstance(score, int):
        return "数据不对"
    elif 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    elif 0 <= score < 60:
        return "F"
    else:
        return "数据不对"
