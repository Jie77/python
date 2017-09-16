import turtle

def move(a, b, c):
    for i in range(a):
        turtle.right(b)
        turtle.forward(c)
def leaf(deg):
    turtle.pensize(1)
    turtle.color("green")
    turtle.begin_fill()
    turtle.left(deg)
    move(75,1,2)
    turtle.right(105)
    move(75,1,2)
    turtle.end_fill()
leaf(75)
leaf(0)
turtle.done()
