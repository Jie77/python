import turtle
import time
turtle.pensize(2)
turtle.bgcolor("black")
color = ["red","yellow","purple","blue"]
turtle.tracer(False)
for x in range(400):
    turtle.forward(2*x)
    turtle.color(color[x%4])
    turtle.left(91)
turtle.tracer(True)
time.sleep(3)
