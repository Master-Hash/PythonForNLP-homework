import turtle

t = turtle.Turtle()

# 参数设置
t.speed(10)  # 画图速度：0最快，如果是1到10之间的整数则越大越慢
t.pensize(1)  # 画笔宽度
r = 200  # 画圆弧的半径
colors = [  # 花瓣颜色
    "#ff0000",  # "#ff0000"，"red"，红色
    "#ff00ff",  # "#ff00ff"，"magenta"，洋红
    "#0000ff",  # "#0000ff"，"blue"，蓝色
    "#00ffff",  # "#00ffff"，"cyan"，青色
    "#00ff00",  # "#00ff00"，"lime"，闪亮绿
    "#ffff00",  # "#ffff00"，"yellow"，黄色
]

# 开始画图
# 六瓣花
t.left(30)
for i in range(6):
    t.color(colors[i])
    t.begin_fill()
    t.circle(r, 60)
    t.left(120)
    t.circle(r, 60)
    t.end_fill()
    t.left(180)
t.right(30)
t.clear()

# 四瓣花

colors = [
    "#ffff00",  # "#ffff00"，"yellow"，黄色
    "#ff0000",  # "#ff0000"，"red"，红色
    "#00ff00",  # "#00ff00"，"lime"，闪亮绿
    "#0000ff",  # "#0000ff"，"blue"，蓝色
]
t.right(45)
for i in range(4):
    t.color(colors[i])
    t.begin_fill()
    t.circle(r, 90)
    t.left(90)
    t.circle(r, 90)
    t.end_fill()
    t.left(180)

t.left(45)
t.clear()
# 三瓣花
colors = [
    "#ff0000",  # "#ff0000"，"red"，红色
    "#00ff00",  # "#00ff00"，"lime"，闪亮绿
    "#0000ff",  # "#0000ff"，"blue"，蓝色
]
t.left(60)
for i in range(3):
    t.color(colors[i])
    t.begin_fill()
    t.circle(r, 120)
    t.left(60)
    t.circle(r, 120)
    t.end_fill()
    t.left(180)


# 隐藏画笔
t.ht()

# 结束画图
turtle.done()
