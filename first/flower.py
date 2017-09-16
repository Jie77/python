import turtle
t = turtle.Turtle()


def move(a, b, c):
    for i in range(a):
        t.right(b)
        t.forward(c)


def set_pos(x, y):
    t.up()
    t.goto(x, y)
    t.down()


def leaf(deg):
    t.pensize(1)
    t.color("green")
    t.begin_fill()
    t.left(deg)
    move(75, 1, 2)
    t.right(105)
    move(75, 1, 2)
    t.end_fill()


def gen(height):
    t.color("brown")
    t.pensize(10)
    t.forward(height)


t.color("red")
t.pensize(5)
set_pos(-100, 100)
t.speed(100)
for _ in range(5):
    t.left(72)
    move(144, 2, 2)
set_pos(-80, 90)
t.right(180)
t.circle(20, 360)
set_pos(-80, -15)
t.left(90)
gen(75)
t.left(90)
leaf(75)
t.left(90)
gen(50)
t.right(90)
leaf(0)
t.right(15)
gen(75)
turtle.done()
