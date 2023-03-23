import turtle as t
from math import dist
from typing import Tuple

t.speed(0)

b = 133
c = dist((0, 0), (b, b)) / 2


def draw_square(colors: Tuple[str, str, str, str]):
    for color in colors:
        t.color(color)
        t.begin_fill()
        t.forward(b)
        t.right(135)
        t.forward(c)
        t.right(90)
        t.forward(c)
        t.end_fill()
        t.right(135)
        t.forward(b)
        t.right(90)


def move_down():
    t.up()
    t.right(90)
    t.forward(b)
    t.left(90)
    t.down()


def move_up():
    t.up()
    t.left(90)
    t.forward(2 * b)
    t.right(90)
    t.forward(b)
    t.down()


# Move to the start position
t.up()
t.left(180)
t.forward(199)
t.right(90)
t.forward(199)
t.right(90)
t.down()

for a in (
    ["red", "yellow", "blue", "green"],
    [
        "yellow",
        "blue",
        "green",
        "red",
    ],
    [
        "blue",
        "green",
        "red",
        "yellow",
    ],
):
    for _ in range(2):
        draw_square(tuple(a))
        move_down()
    else:
        draw_square(tuple(a))
        move_up()


t.hideturtle()
t.done()
