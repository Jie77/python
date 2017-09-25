from turtle import Turtle,mainloop
from time import clock
import random

def ran(num):
    arr=[]
    i=0
    while i<num:
        arr.append(random.randint(-250,200))
        i += 1
    return arr


def tree(plist, l, a, f):

    if l>13:
        lst = []
        for p in plist:
            p.pensize(8)
            p.color("brown")
            p.forward(l)
            q = p.clone()
            p.left(a)
            q.right(a)
            lst.append(q)
            lst.append(p)
        for x in tree(lst, l*f, a, f):
            yield None
    elif l > 3:
        lst = []
        for p in plist:
            p.pensize(13)
            p.color("green")
            p.forward(l)
            q = p.clone()
            p.left(a)
            q.right(a)
            lst.append(q)
            lst.append(p)
        for x in tree(lst, l*f, a, f):
            yield None


def maketree(x,y):
    p = Turtle()
    p.color('green')
    p.setundobuffer(None)
    p.hideturtle()
    p.speed(0)
    p.getscreen().tracer(30,0)
    p.left(90)
    p.penup()
    p.goto(x,y)
    p.pendown()
    t = tree([p], 100, 65, 0.6)
    for x in t:
        pass
    print(len(p.getscreen().turtles()))

def make(num):
    num = num*2
    arr = ran(num)
    for i in range(0,len(arr),2):
        maketree(arr[i],arr[i+1])
def main():
    a = clock()
    print("请输入树的数量：")
    num = int(input())
    make(num)
    b = clock()
    return "done:%.2f sec." % (b-a)


if __name__ == "__main__":
    msg = main()
    print(msg)
    mainloop()





