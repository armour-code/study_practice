# author: fzb
# time: 2020/3/30
# function:  分形树
# method: 直接运行
# completion：100%
from turtle import *
Draw = Turtle()
MyDraw = Draw.getscreen()


def DrawTree(DrawPin, PinLine, Linesize):
    if PinLine > 5:
        if Linesize > 1:
            DrawPin.pensize(Linesize)
        DrawPin.pencolor("brown")
        if PinLine < 20:
            DrawPin.pencolor("green")
        DrawPin.forward(PinLine)
        DrawPin.left(30)
        DrawTree(DrawPin, PinLine-15, Linesize-1)
        DrawPin.right(60)
        DrawTree(DrawPin, PinLine-15, Linesize-1)
        DrawPin.left(30)
        DrawPin.pencolor("brown")
        if PinLine < 34:
            DrawPin.pencolor("green")
        DrawPin.backward(PinLine)


Draw.left(90)
Draw.sety(-50)
DrawTree(Draw, 100, 6)
MyDraw.exitonclick()
